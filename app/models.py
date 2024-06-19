from django.db import models
from datetime import datetime,timezone


class Users(models.Model):
    FIO = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    token = models.CharField(max_length=60,default='')
    exp_date = models.DateTimeField()

class Clients(models.Model):
    account_number = models.CharField(max_length=20)
    familiya = models.CharField(max_length=30)
    imya = models.CharField(max_length=30)
    otchestvo = models.CharField(max_length=30)
    birthday = models.DateField()
    INN = models.CharField(max_length=12)
    FIO_representative = models.CharField(max_length=100)
    status = models.CharField(max_length=20,default='Не в работе')


