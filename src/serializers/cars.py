from enum import Enum

from rest_framework import serializers


class CarsViewConsts:
    class StatusEnum(str, Enum):
        OK = "ok"
        ERROR = "error"

    class DetailEnum(str, Enum):
        NOT_FOUND = "not_found"
        UNSUCCESSFUL_API_RESPONSE = "unsuccessful_api_response"
        MAKE_HAS_NO_MODELS = "make_has_no_models"
        CREATED = "created"
        ALREADY_EXISTS = "already_exists"
        FAILED_TO_CREATE = "failed_to_create"
        DELETED = "deleted"

    status = StatusEnum
    detail = DetailEnum


class CarsBodySerializer(serializers.Serializer):
    model = serializers.CharField(max_length=255)
    make = serializers.CharField(max_length=255)


class CarsModelSerializer(serializers.Serializer):
    make = serializers.CharField(max_length=255, required=True)
    model = serializers.CharField(max_length=255, required=True)


class CarsReponseSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=CarsViewConsts.status, required=True)
    detail = serializers.ChoiceField(choices=CarsViewConsts.detail, required=True)
    data = CarsModelSerializer(many=False, required=False)
