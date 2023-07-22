from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rent_management.models import *


def house_type(request):
    if request.method == 'POST':
        house = request.POST.get('house_type')
        add_house_type = HouseType.objects.create(type=house)
        add_house_type.save()
        return redirect('/house-type')

    # Filter All Hose Type
    houses_type = HouseType.objects.all().order_by('-id')
    context = {
        'house_type': houses_type,
    }
    return render(request, "rent/house_type/house_type.html", context)


def edit_house_type(request, pk):
    obj = get_object_or_404(HouseType, pk=pk)
    if request.method == 'POST':
        obj.type = request.POST['edit_house_type_name']
        obj.save()
        return redirect('/house-type')
