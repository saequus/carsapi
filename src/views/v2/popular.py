import json

import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from src.defs.cars import CarWithRatingsCountDef
from src.models import Car
from src.serializers.cars import (
    CarsBodySerializer,
    CarsReponseSerializer,
    CarsViewConsts,
)


class PopularCarsView(APIView):
    status = CarsViewConsts.status
    detail = CarsViewConsts.detail

    def get(self, request):
        data = {"status": "ok", "cars": []}
        cars = list()
        cars_query = Car.objects.all().prefetch_related("rate_set")

        for car in cars_query:
            car_dict = CarWithRatingsCountDef(
                id=car.id,
                make=car.make,
                model=car.model,
                rates_number=car.rate_set.count(),
            )
            cars.append(car_dict)

        sorted(data["cars"], key=lambda x: x.rates_number, reverse=True)
        data["cars"] = [car.dict() for car in cars]
        return JsonResponse(
            data=data,
            status=200,
        )
