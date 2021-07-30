from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    re_path("", include("api.url.v1")),
    re_path("v2/", include("api.url.v2")),
]
