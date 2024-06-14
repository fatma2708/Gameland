from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import newuser
from django.contrib.auth.models import User

class CombinedRegistrationForm(UserCreationForm):
    Nom = forms.CharField(max_length=120)
    Prénom = forms.CharField(max_length=120)
    Date_de_naissance = forms.DateField()
    Num_tel = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'Nom', 'Prénom', 'Date_de_naissance', 'Num_tel', 'email']

def save(self, commit=True):
    user = super(CombinedRegistrationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    
    if commit:
        user.save()

        new_user = newuser.objects.create(
            user=user,
            Nom=self.cleaned_data['Nom'],
            Prénom=self.cleaned_data['Prénom'],
            Date_de_naissance=self.cleaned_data['Date_de_naissance'],
            Num_tel=self.cleaned_data['Num_tel'],
            email=self.cleaned_data['email'],
        )
    return user