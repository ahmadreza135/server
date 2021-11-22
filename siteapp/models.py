from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField
# Create your models here.

class dashboard(AbstractUser):
    sarafi = models.CharField(max_length=50,default="null")
    verified_trades = models.IntegerField(default=0,null=False)
    invited_peaple = models.IntegerField(default=0,null=False)
    sum_of_trades = models.IntegerField(default=0,null=False)
    ranking = models.IntegerField(default=0,null=False)
