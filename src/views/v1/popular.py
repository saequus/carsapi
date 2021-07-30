from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from src.defs.cars import CarWithRatingsCountDef
from src.models import Car
from src.serializers.cars import CarsViewConsts


class PopularCarsView(APIView):
    status = CarsViewConsts.status
    detail = CarsViewConsts.detail

    def get(self, request):
        data, cars = list(), list()
        cars_query = Car.objects.all().prefetch_related("rate_set")

        for car in cars_query:
            car_dict = CarWithRatingsCountDef(
                id=car.id,
                make=car.make,
                model=car.model,
                rates_number=car.rate_set.count(),
            )
            cars.append(car_dict)

        sorted(cars, key=lambda x: x.rates_number, reverse=True)
        data = [car.dict() for car in cars]
        return JsonResponse(
            data=data,
            status=200,
            safe=False,
        )
