import json

import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from src.defs.cars import CarDef, CarWithAvgRatingDef
from src.models import Car
from src.serializers.cars import (
    CarsBodySerializer,
    CarsReponseSerializer,
    CarsViewConsts,
)


class CarsView(APIView):
    status = CarsViewConsts.status
    detail = CarsViewConsts.detail

    def get(self, request):
        data = list()
        cars_query = Car.objects.all().prefetch_related("rate_set")

        for car in cars_query:
            avg_rating = 0
            if car.rate_set.exists():
                avg_rating = round(
                    car.rate_set.aggregate(Avg("rating"))["rating__avg"], 4
                )
            car_dict = CarWithAvgRatingDef(
                id=car.id,
                make=car.make,
                model=car.model,
                avg_rating=avg_rating,
            ).dict(exclude_none=True)
            data.append(car_dict)

        return JsonResponse(data=data, status=200, safe=False)

    @swagger_auto_schema(
        query_serializer=CarsBodySerializer,
        responses={"200": CarsReponseSerializer},
    )
    def post(self, request):
        serializer = CarsBodySerializer(data=request.data)
        serializer.is_valid()

        make = request.data.get("make", None)
        model = request.data.get("model", None)
        if not make or not model:
            return JsonResponse(
                {
                    "status": self.status.ERROR,
                    "detail": self.detail.MODEL_OR_MAKE_NOT_PROVIDED,
                },
                status=401,
            )

        url = f"{settings.DOT_GOV_URL}{settings.MODELS_FOR_MAKE_API_URL}{make}?{settings.JSON_FORMAT}"
        response = requests.get(url)
        content = json.loads(response.content)

        if any(
            [
                "Message" not in content,
                content["Message"] != settings.RESPONSE_RETURNED_SUCCESSFULLY,
                "Results" not in content,
            ]
        ):
            return JsonResponse(
                {
                    "status": self.status.ERROR,
                    "detail": self.detail.UNSUCCESSFUL_API_RESPONSE,
                },
                status=400,
            )

        if len(content["Results"]) < 1:
            return JsonResponse(
                {"status": self.status.ERROR, "detail": self.detail.MAKE_HAS_NO_MODELS},
                status=401,
            )

        car_def, just_created = None, False
        for item in content["Results"]:
            if "Model_Name" in item and item["Model_Name"] == model:
                car_def = CarDef(
                    make=item["Make_Name"],
                    model=item["Model_Name"],
                )

        if car_def:
            try:
                car_model, just_created = Car.objects.get_or_create(
                    model=car_def.model,
                    make=car_def.make,
                )
            except (Exception,):
                return JsonResponse(
                    data={
                        "status": self.status.ERROR,
                        "detail": self.detail.FAILED_TO_CREATE,
                    },
                    status=401,
                )

        if car_def and just_created:
            return JsonResponse(
                data=car_def.dict(),
                status=201,
            )

        if car_def and not just_created:
            return JsonResponse(
                data=car_def.dict(),
                status=200,
            )

        return JsonResponse(
            {"status": self.status.ERROR, "detail": self.detail.NOT_FOUND}, status=404
        )

    def delete(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
        except (ObjectDoesNotExist,):
            return JsonResponse(
                {"status": self.status.ERROR, "detail": self.detail.NOT_FOUND},
                status=404,
            )

        else:
            car_def = CarDef(
                make=car.make,
                model=car.model,
            )
            car.delete()
            return JsonResponse(
                {"status": self.status.OK, "car": car_def.dict()},
                status=204,
            )
