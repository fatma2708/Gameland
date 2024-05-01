from django.contrib import admin
from app2.models import newuser
# Register your models here.
@admin.register(newuser)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Prénom', 'Num_tel','Date_de_naissance','email')
