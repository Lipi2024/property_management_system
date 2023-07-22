# Generated by Django 4.2.3 on 2023-07-20 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent_management', '0004_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=20)),
                ('aadhaar_number', models.CharField(default='', max_length=15)),
                ('mobile_number', models.CharField(default='', max_length=13)),
                ('alternative_number', models.CharField(default='', max_length=15)),
                ('address', models.TextField(default='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_management.usertype')),
            ],
        ),
    ]
