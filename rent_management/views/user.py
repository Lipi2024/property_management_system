from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rent_management.models import *


def users(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name_input')
        user_age = request.POST.get('usr_age_input')
        user_sex = request.POST.get('usr_sex_input')
        user_aadhaar_number = request.POST.get('usr_aadhaar_input')
        user_mobile_number = request.POST.get('usr_mobile_input')
        user_email_id = request.POST.get('usr_alternative_input')
        user_alternative_number = request.POST.get('usr_email_input')
        user_address = request.POST.get('usr_address_input')
        user_user_type = request.POST.get('usr_type_input')

        # creating User type instance
        user_type_instance = UserType.objects.filter(id=user_user_type).first()
        add_user_details = User.objects.create(name=user_name, age=user_age, sex=user_sex,
                                               aadhaar_number=user_aadhaar_number, mobile_number=user_mobile_number,
                                               email_id=user_email_id, alternative_number=user_alternative_number,
                                               address=user_address, user_type=user_type_instance)
        add_user_details.save()
        return redirect('/user')

    user_list = User.objects.all().order_by('-id')
    user_type_list = UserType.objects.all()
    context = {
        'users': user_list,
        'select_gender': User.GENDER,
        'user_type_context': user_type_list,
    }
    return render(request, 'rent/user/user.html', context)
