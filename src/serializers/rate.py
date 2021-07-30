from enum import Enum

from rest_framework import serializers


class RateViewConsts:
    class StatusEnum(str, Enum):
        OK = "ok"
        ERROR = "error"

    class DetailEnum(str, Enum):
        NOT_FOUND = "not_found"
        CAR_NOT_FOUND = "car_not_found"
        INVALID_RATING_VALUE = "invalid_rating_value"
        CREATED = "created"
        FAILED_TO_CREATE = "failed_to_create"
        DELETED = "deleted"

    status = StatusEnum
    detail = DetailEnum


class RateBodySerializer(serializers.Serializer):
    car_id = serializers.IntegerField(required=True)
    rating = serializers.IntegerField(required=True)


class RateSerializer(serializers.Serializer):
    car_id = serializers.IntegerField(required=True)
    rating = serializers.IntegerField(required=True)


class RateReponseSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=RateViewConsts.status, required=True)
    detail = serializers.ChoiceField(choices=RateViewConsts.detail, required=True)
    data = RateSerializer(many=False, required=False)
