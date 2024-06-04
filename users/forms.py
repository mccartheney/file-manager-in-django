from django import forms
from .models import user_profile

class user_profile_form_register (forms.ModelForm) : 
    class Meta :
        model = user_profile
        fields = ["name", "email", "password"]

        widgets = {
            "password" : forms.PasswordInput()
        }