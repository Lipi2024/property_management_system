# Generated by Django 4.2.3 on 2023-07-24 15:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rent_management', '0009_remove_payment_outstanding_alter_user_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='tenants_details',
        ),
        migrations.AddField(
            model_name='payment',
            name='house_details',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rent_management.house'),
            preserve_default=False,
        ),
    ]