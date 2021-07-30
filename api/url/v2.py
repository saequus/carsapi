from django.urls import re_path

from src.views.v2 import cars, flush_db, popular, rate

urlpatterns = [
    re_path(r"^cars/$", cars.CarsView.as_view(), name="create_car_v2"),
    re_path(
        r"^cars/(?P<model_id>[0-9]+)/$", cars.CarsView.as_view(), name="delete_car_v2"
    ),
    re_path(r"^rate/$", rate.RateView.as_view(), name="create_rate_v2"),
    re_path(
        r"^popular/$", popular.PopularCarsView.as_view(), name="get_popular_cars_v2"
    ),
    re_path(r"^flush-db/$", flush_db.FlushView.as_view(), name="flush_db_v2"),
]
