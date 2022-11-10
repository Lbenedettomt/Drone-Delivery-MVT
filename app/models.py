from django.db import models

# Create your models here.
class Register(models.Model):
    drone = models.CharField(max_length= 130)
    product = models.CharField(max_length=130)