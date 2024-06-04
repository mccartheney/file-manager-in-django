from django import forms
from .models import user_profile

class user_profile_form_register (forms.ModelForm) : 
    class Meta :
        model = user_profile
        fields = ["user_email", "user_name", "user_password"]

        widgets = {
            "user_password" : forms.PasswordInput()
        }