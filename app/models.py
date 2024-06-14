from django.db import models
# Create your models here.
class Agence(models.Model):
    Name_user= models.CharField(max_length=120)
    Lastname_user=models.CharField(max_length=120)
    Name_agence=models.CharField(max_length=120)
    Dateofbirth=models.DateField()
    phone_number=models.PositiveBigIntegerField(unique=True)
    email_user=models.EmailField(max_length=254,unique=True)
    user_cin = models.PositiveIntegerField(unique=True)
    nb_bus=models.PositiveIntegerField()
    nb_guides=models.PositiveIntegerField()
    



        
