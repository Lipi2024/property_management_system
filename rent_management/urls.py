from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("house-type/", views.house_type, name="house_type"),
    path("house-type/edit/<int:pk>", views.edit_house_type, name="edit_house_type"),

    path("houses/", views.houses, name="houses"),
    path("houses/edit/<int:pk>", views.edit_houses, name="edit_houses"),
    path("houses_allocation/", views.house_allocation, name="house_allocation"),
    path("houses_allocation/delete/<int:pk>", views.delete_house_allocation, name="delete_house_allocation"),


    # MANAGE USERS
    path("user/", views.users, name="user"),

    # manage tenants
    path("manage_tenants/", views.manage_tenants, name="menge_tenants"),
]
