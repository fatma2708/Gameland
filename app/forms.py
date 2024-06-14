from django import forms
from .models import Agence
import re 
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Agence
        fields = ['Name_user', 'Lastname_user', 'Name_agence','Dateofbirth','phone_number','email_user','user_cin','nb_bus','nb_guides']

    def valid_cin(self):
        user_cin = self.cleaned_data['cin_number']
        if len(str(user_cin)) != 8:
            raise forms.ValidationError("Le CIN doit etre composé de 8 chiffres.")
        return user_cin
    
    def valid_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        
        phone_regex = r'^\+?1?\d{9,15}$'
        if not re.match(phone_regex, phone_number):
            raise forms.ValidationError("Le numero de téléphone est invalide .")
        
        return phone_number





