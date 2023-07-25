from django.http import HttpResponse
from django.shortcuts import render
from rent_management.models import *


def manage_tenants(request):
    tenants_list = User.objects.filter(user_type=3)
    context = {
        'tenants_lists': tenants_list,
    }
    return render(request, "rent/tenants/manage_tenants.html", context)


def tenants(request):
    tenants_list = User.objects.filter(user_type=3)
    house_rented_list = Tenants.objects.all()
    context = {
        'tenants_list': tenants_list,
        'house_rent_list': house_rented_list,
    }
    return render(request, "rent/tenants/tenants.html", context)
