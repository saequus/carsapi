from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from src.defs.rate import RateDef
from src.models import Car, Rate
from src.serializers.rate import (
    RateBodySerializer,
    RateReponseSerializer,
    RateViewConsts,
)


class RateView(APIView):
    status = RateViewConsts.status
    detail = RateViewConsts.detail

    @swagger_auto_schema(
        query_serializer=RateBodySerializer,
        responses={"200": RateReponseSerializer},
    )
    def post(self, request):
        serializer = RateBodySerializer(data=request.data)
        serializer.is_valid()

        car_id = request.data.get("car_id", None)
        rating = request.data.get("rating", None)

        rate_def = RateDef(car_id=car_id, rating=rating)

        if not 1 <= rate_def.rating <= 5:
            return JsonResponse(
                {
                    "status": self.status.ERROR,
                    "detail": self.detail.INVALID_RATING_VALUE,
                },
                status=400,
            )

        try:
            car = Car.objects.get(id=rate_def.car_id)
        except (ObjectDoesNotExist,):
            return JsonResponse(
                {"status": self.status.ERROR, "detail": self.detail.CAR_NOT_FOUND},
                status=404,
            )

        try:
            Rate.objects.create(rating=rate_def.rating, car=car)
        except (Exception,):
            return JsonResponse(
                {"status": self.status.ERROR, "detail": self.detail.FAILED_TO_CREATE},
                status=400,
            )

        return JsonResponse(
            data={
                "status": self.status.OK,
                "detail": self.detail.CREATED,
                "rate": rate_def.dict(exclude_none=True),
            },
            status=201,
        )
