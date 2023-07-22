from django.db import models


# Create your models here.
class HouseType(models.Model):
    objects = None
    type = models.CharField(max_length=255)
    add_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class House(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20, default='')
    type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    address = models.TextField(default='')
    rent = models.CharField(max_length=20, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class UserType(models.Model):
    type = models.CharField(max_length=50, default='')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class User(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=20, choices=GENDER, default='M')
    aadhaar_number = models.CharField(max_length=50, default='')
    mobile_number = models.CharField(max_length=13, default='Not Given', null=True)
    email_id = models.CharField(max_length=100, default='')
    alternative_number = models.CharField(max_length=15, default='')
    address = models.TextField(default='')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tenants(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.IntegerField(default=1)
    rented_house = models.ForeignKey(House, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.name


class Payment(models.Model):
    receipt_no = models.CharField(max_length=20, default='')
    tenants_details = models.ForeignKey(Tenants, on_delete=models.CASCADE)
    paid_amount = models.IntegerField(default=0)
    paid_date = models.DateTimeField(auto_now_add=True)
    outstanding = models.IntegerField(default=0)

    def __str__(self):
        return self.receipt_no
