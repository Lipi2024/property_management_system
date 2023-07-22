from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rent_management.models import *


def house_allocation(request):
    if request.method == 'POST':
        tenants_name = request.POST.get('tenants_name')
        members = request.POST.get('member_input')
        rented_house = request.POST.get('rented_house')

        # creating House type instance
        user_name_instance = User.objects.filter(id=tenants_name).first()
        rented_house_instance = House.objects.filter(id=rented_house).first()

        # user_name_instance = User.objects.get(id=tenants_name)
        # rented_house_instance = User.objects.get(id=rented_house)

        allocate = Tenants.objects.create(name=user_name_instance, member=members, rented_house=rented_house_instance)
        allocate.save()
        return redirect('/houses_allocation')

    tenants_list = User.objects.filter(user_type=3)
    houses_list = House.objects.all()
    allocated_houses_list = Tenants.objects.all().order_by('-id')
    context = {
        'tenants_lists': tenants_list,
        'houses_lists': houses_list,
        'allocated_list': allocated_houses_list,
    }
    return render(request, "rent/house_type/house_allocation.html", context)


def delete_house_allocation(request, pk):
    allocation_remove = Tenants.objects.filter(id=pk)
    allocation_remove.delete()
    return redirect('/houses_allocation')

