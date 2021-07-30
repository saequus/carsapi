import json

import mock
from django.http.response import JsonResponse
from django.test import TestCase
from django.urls import reverse

from src.models import Car, Rate


class TestCarView(TestCase):
    @property
    def url(self):
        return "/api/cars/"

    @property
    def url_v2(self):
        return "/api/v2/cars/"

    @property
    def gov_dot_mercedes(self):
        data = {
            "Count": 54,
            "Message": "Response returned successfully",
            "SearchCriteria": "Make:mercedes-benz",
            "Results": [
                {
                    "Make_ID": 449,
                    "Make_Name": "MERCEDES-BENZ",
                    "Model_ID": 1703,
                    "Model_Name": "Sprinter",
                },
                {
                    "Make_ID": 449,
                    "Make_Name": "MERCEDES-BENZ",
                    "Model_ID": 2079,
                    "Model_Name": "SL-Class",
                },
            ],
        }
        return JsonResponse(data=data, safe=False)

    @staticmethod
    def create_cars():
        bmw, _ = Car.objects.get_or_create(make="BMW", model="128i")
        honda, _ = Car.objects.get_or_create(make="HONDA", model="Odyssey")
        mercedes, _ = Car.objects.get_or_create(make="MERCEDES-BENZ", model="AMG GT")
        return bmw, honda, mercedes

    @staticmethod
    def create_rate(car, rating):
        rate, _ = Rate.objects.get_or_create(car=car, rating=rating)
        return rate

    @staticmethod
    def create_car():
        car, _ = Car.objects.get_or_create(make="BMW", model="128i")
        return car

    def test_url_not_unintentionally_changed(self):
        self.assertEqual(self.url, reverse("create_car"))

    def test_url_not_unintentionally_changed_v2(self):
        self.assertEqual(self.url_v2, reverse("create_car_v2"))

    def test_get_response_ok(self):
        bmw, honda, mercedes = self.create_cars()
        self.create_rate(bmw, 1)
        self.create_rate(bmw, 2)
        self.create_rate(bmw, 4)

        self.create_rate(honda, 4)
        self.create_rate(honda, 5)

        self.create_rate(mercedes, 3)

        cars = [
            {"id": bmw.id, "make": "BMW", "model": "128i", "avg_rating": 2.3333},
            {"id": honda.id, "make": "HONDA", "model": "Odyssey", "avg_rating": 4.5},
            {
                "id": mercedes.id,
                "make": "MERCEDES-BENZ",
                "model": "AMG GT",
                "avg_rating": 3.0,
            },
        ]

        response = self.client.get(self.url)
        self.assertEqual(json.loads(response.content), cars)

    def test_post_response_ok(self):
        data = {"model": "Sprinter", "make": "MERCEDES-BENZ"}
        with mock.patch("requests.api.request") as request_to_gov_dot:
            request_to_gov_dot.return_value = self.gov_dot_mercedes
            response = self.client.post(self.url, data)
            self.assertEqual(
                json.loads(response.content),
                {"make": "MERCEDES-BENZ", "model": "Sprinter"},
            )
