from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class newuser(models.Model):
    user=User
    Nom= models.CharField(max_length=120)
    Prénom=models.CharField(max_length=120)
    Date_de_naissance=models.DateField()
    Num_tel=models.PositiveBigIntegerField(unique=True)
    email=models.EmailField(max_length=254,unique=True)



