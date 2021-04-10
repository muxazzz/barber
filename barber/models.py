from django.db import models
from django import forms

# Create your models here.

class Order(models.Model):  
    client_name = models.CharField(max_length=100, default=None)
    client_comments = models.TextField(max_length=200, blank=True)
    client_tel = models.CharField(max_length=100, blank=True)
    client_email = models.EmailField(blank=True)
    FRESHMAN = 'Стрижка'
    SOPHOMORE = 'Маникюр'
    JUNIOR = 'Педикюр'
    SENIOR = 'Брови'
    GRADUATE = 'Депиляция'
    client_order_choices = [
        (FRESHMAN, 'Стрижка'),
        (SOPHOMORE, 'Маникюр'),
        (JUNIOR, 'Педикюр'),
        (SENIOR, 'Брови'),
        (GRADUATE, 'Депиляция'),
    ]
    client_order = models.CharField(
        max_length=10,
        choices=client_order_choices,
        default=FRESHMAN,
    )
    private_data = models.BooleanField(blank=False, default=None)


