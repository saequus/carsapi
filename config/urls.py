from django.conf import settings
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path("api/", include("api.urls")),
]


if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view
    from rest_framework import permissions

    schema_view = get_schema_view(
        openapi.Info(
            title="API",
            default_version="v1",
            description="ETG Django Template DRF API documentation",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
