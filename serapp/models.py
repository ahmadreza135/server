from django.db import models

# Create your models here.


class emailv(models.Model):
    email = models.CharField(max_length=200)

class arz_roo_boors(models.Model):
    name = models.CharField(max_length=200)
    timeclosed = models.DateTimeField()
    market_cap = models.IntegerField()
    price = models.IntegerField()