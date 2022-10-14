from email.policy import default
from enum import unique
from hashlib import blake2b
from pyexpat import model
from django.db import models


# Create your models here.


class ServiceModel(models.Model):
    serv_name = models.CharField(max_length=25 )
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.serv_name


class CustomersModel(models.Model):
    def servChoices(servs):
        lst = [x.serv_name for x in servs]
        ch =()
        for a in lst:
            ch += (a,a),
        return ch

    customer_name = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=12)
    email = models.EmailField()
    website_URL = models.URLField(max_length=200, null=True, blank=True)
    service_insterested = models.OneToOneField(ServiceModel, on_delete = models.CASCADE)
    tell_us_about_your_business = models.TextField(max_length = 2000)

    def __str__(self):
        return self.customer_name if self.customer_name!= None else 'Consult'+f'{self.id}'


class PackageModel(models.Model):
    service = models.OneToOneField(ServiceModel, on_delete=models.CASCADE, unique=True)
    pack1 = models.CharField(max_length = 200)
    price1 = models.CharField(max_length = 200)
    pack2 = models.CharField(max_length = 200)
    price2 = models.CharField(max_length = 200)
    pack3 = models.CharField(max_length = 200)
    price3 = models.CharField(max_length = 200)

    def __str__(self):
        return self.service.serv_name



