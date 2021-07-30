import json

from django.test import TestCase
from django.urls import reverse

from src.models import Car, Rate


class TestCarView(TestCase):
    @property
    def url(self):
        return "/api/popular/"

    @property
    def url_v2(self):
        return "/api/v2/popular/"

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

    def test_url_not_unintentionally_changed(self):
        self.assertEqual(self.url, reverse("get_popular_cars"))

    def test_url_not_unintentionally_changed_v2(self):
        self.assertEqual(self.url_v2, reverse("get_popular_cars_v2"))

    def test_response_ok(self):
        bmw, honda, mercedes = self.create_cars()
        self.create_rate(bmw, 1)
        self.create_rate(bmw, 2)
        self.create_rate(bmw, 4)

        self.create_rate(honda, 4)
        self.create_rate(honda, 5)

        self.create_rate(mercedes, 3)

        popular = [
            {"id": bmw.id, "make": "BMW", "model": "128i", "rates_number": 3},
            {"id": honda.id, "make": "HONDA", "model": "Odyssey", "rates_number": 2},
            {
                "id": mercedes.id,
                "make": "MERCEDES-BENZ",
                "model": "AMG GT",
                "rates_number": 1,
            },
        ]

        response = self.client.get(self.url)
        self.assertEqual(json.loads(response.content), popular)
