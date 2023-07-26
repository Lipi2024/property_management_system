from django.http import HttpResponse
from django.shortcuts import render
from rent_management.models import *
from django.db.models import Sum


def index(request):
    collection = Payment.objects.aggregate(Sum('paid_amount'))
    context = {
        'collection_list':collection,
    }
    return render(request, "rent/index.html", context)