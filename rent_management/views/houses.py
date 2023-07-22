from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rent_management.models import *


def houses(request):
    if request.method == 'POST':
        house_number = request.POST.get('house_number')
        house_name = request.POST.get('house_name')
        house_type = request.POST.get('house_type')
        house_rent = request.POST.get('monthly_amount')
        house_address = request.POST.get('address')

        # creating House type instance
        house_type_instance = HouseType.objects.filter(id=house_type).first()

        add_house_details = House.objects.create(number=house_number, name=house_name, type=house_type_instance,
                                                 address=house_address, rent=house_rent)
        add_house_details.save()
        return redirect('/houses')

    houses_type = HouseType.objects.all()
    houses_list = House.objects.all().order_by('-id')
    context = {
        'house_type': houses_type,
        'houses': houses_list,
    }
    return render(request, "rent/house_type/houses.html", context)


def edit_houses(request, pk):
    obj = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        obj.number = request.POST['house_number']
        obj.name = request.POST['house_name']
        house_types = request.POST['house_type']

        obj.address = request.POST['address']
        obj.rent = request.POST['monthly_amount']

        # CREATE HOUSE TYPE INSTANCE
        house_type = HouseType.objects.get(pk=house_types)

        obj.type = house_type
        obj.save()
        return redirect('/houses')
