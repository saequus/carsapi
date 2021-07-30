import json

from django.test import TestCase
from django.urls import reverse

from src.models import Car, Rate


class TestCarView(TestCase):
    @property
    def url(self):
        return "/api/rate/"

    @property
    def url_v2(self):
        return "/api/v2/rate/"

    @staticmethod
    def create_car():
        car, _ = Car.objects.get_or_create(make="BMW", model="128i")
        return car

    def test_url_not_unintentionally_changed(self):
        self.assertEqual(self.url, reverse("create_rate"))

    def test_url_not_unintentionally_changed_v2(self):
        self.assertEqual(self.url_v2, reverse("create_rate_v2"))

    def test_response_ok(self):
        car = self.create_car()
        data = {"rating": 2, "car_id": car.id}
        response = self.client.post(self.url, data)
        self.assertEqual(
            json.loads(response.content),
            {
                "rating": 2,
                "car_id": car.id,
            },
        )
        data = {"rating": 5, "car_id": car.id}
        response = self.client.post(
            self.url, data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(
            json.loads(response.content),
            {
                "rating": 5,
                "car_id": car.id,
            },
        )
        rates = Rate.objects.all()
        self.assertEqual(rates.count(), 2)
        self.assertEqual([rate.rating for rate in rates], [2, 5])

    def test_invalid_rating_value(self):
        error = {"status": "error", "detail": "invalid_rating_value"}
        car = self.create_car()
        data = {"rating": 7, "car_id": car.id}
        response = self.client.post(
            self.url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(json.loads(response.content), error)
        response = self.client.post(
            self.url_v2, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(json.loads(response.content), error)
