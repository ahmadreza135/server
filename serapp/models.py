from django.db import models

# Create your models here.


class emailv(models.Model):
    email = models.CharField(max_length=200)

class public_arz(models.Model):
    name = models.CharField(max_length=200)
    timeopened = models.DateTimeField()
    timeclosing = models.DateTimeField()
    market_cap = models.FloatField()
    price = models.FloatField()