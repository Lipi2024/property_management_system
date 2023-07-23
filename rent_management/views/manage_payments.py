from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rent_management.models import *


def manage_payments(request):
    return render(request, "rent/payments/manage_payments.html")