from django.db import models

# Create your models here.


class emailv(models.Model):
    email = models.CharField(max_length=200)
