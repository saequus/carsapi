import ast
import json
import os
import sys

from django.conf import settings

from src.models import Driver, TripData


def load_data_to_new_trip_data(json_obj, driver_name):
    states = json.loads(json_obj)
    driver = Driver.objects.get(user__username=driver_name)
    TripData.objects.create(states=states, driver=driver)


if __name__ == "__main__":
    settings.configure()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    path = sys.argv[1]
    driver_name = sys.argv[2]
    with open(path, "r") as json_obj:
        json_obj = ast.literal_eval(json_obj.read())
        trip_data = load_data_to_new_trip_data(
            json_obj=json_obj, driver_name=driver_name
        )
