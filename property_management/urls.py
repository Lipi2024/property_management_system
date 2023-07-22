from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("rent_management.urls")),
    path("admin/", admin.site.urls),
]