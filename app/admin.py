from django.contrib import admin
from .models import Agence
# Register your models here.
@admin.register(Agence)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('Name_user', 'Lastname_user', 'Name_agence','Dateofbirth','phone_number','email_user','user_cin','nb_bus','nb_guides')
    search_fields = ('Name_user', 'user_cin', 'phone_number')