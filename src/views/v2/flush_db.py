from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from src.defs.cars import CarWithRatingsCountDef
from src.models import Car, Rate
from src.serializers.cars import CarsViewConsts


class FlushView(APIView):
    status = CarsViewConsts.status
    detail = CarsViewConsts.detail

    def get(self, request):
        rates_query = Rate.objects.all()
        for rate in rates_query:
            rate.delete()
        cars_query = Car.objects.all()
        for car in cars_query:
            car.delete()
        return JsonResponse(data={"status": "flushed"})
