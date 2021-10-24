from django.db import models

# Create your models here.


class emailv(models.Model):
    email = models.CharField(max_length=200)

class room(models.Model):
    name = models.CharField(max_length=32)
    number_of_memebers = models.IntegerField()
    
