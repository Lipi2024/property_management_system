from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rent_management.models import *


def manage_payments(request):
    if request.method == 'POST':
        receipt_no = request.POST.get('receipt_number')
        house_number = request.POST.get('house_number')
        amount_paid = request.POST.get('monthly_amount')

        house_number_instance = House.objects.filter(id=house_number).first()
        add_payment_detail = Payment.objects.create(receipt_no=receipt_no, house_details=house_number_instance,
                                                    paid_amount=amount_paid)
        add_payment_detail.save()
        return redirect('/manage_payments')

    house_list = House.objects.all()
    payment_list = Payment.objects.all()
    context = {
        'houses': house_list,
        'payments': payment_list,
    }
    return render(request, "rent/payments/manage_payments.html", context)


def delete_payments(request, pk):
    payment_remove = Payment.objects.filter(id=pk)
    payment_remove.delete()
    return redirect('/manage_payments')
