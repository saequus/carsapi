from django.urls import re_path

from src.views.v1 import cars, index, popular, rate

urlpatterns = [
    re_path(r"^$", index.view, name="index"),
    re_path(r"^cars/$", cars.CarsView.as_view(), name="create_car"),
    re_path(r"^cars/$", cars.CarsView.as_view(), name="create_car"),
    re_path(r"^cars/(?P<car_id>[0-9]+)/$", cars.CarsView.as_view(), name="delete_car"),
    re_path(r"^rate/$", rate.RateView.as_view(), name="create_rate"),
    re_path(r"^popular/$", popular.PopularCarsView.as_view(), name="get_popular_cars"),
]
