from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class dashboard(User):
    sarafi = models.CharField(max_length=50)
    verified_trades = models.IntegerField()
