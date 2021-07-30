from django.contrib import admin

from src.models import Car, Rate


class CarAdmin(admin.ModelAdmin):
    list_display_links = ("__str__",)
    list_filter = ("model", "make")
    list_display = ("__str__", "id", "model", "make")


class RateAdmin(admin.ModelAdmin):
    list_display_links = ("__str__",)
    list_filter = ("rating",)
    list_display = ("__str__", "rating", "car")


admin.site.register(Car, CarAdmin)
admin.site.register(Rate, RateAdmin)
