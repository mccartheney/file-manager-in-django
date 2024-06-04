# import django.forms to create forms
from django import forms

# import user_profile model to create forms for that model
from .models import user_profile

# form for register
class user_profile_form_register (forms.ModelForm) : 
    class Meta :
        # form parent model
        model = user_profile

        # fields with will apear on html (that fields are the same from model)
        fields = ["name", "email", "password"]

        widgets = {
            # set appearence of password imput as password
            "password" : forms.PasswordInput()
        }

# form for login
class user_profile_form_login (forms.ModelForm) :
    class Meta :
        # form parent model
        model = user_profile

        # fields with will apear on html (that fields are the same from model)
        fields = ["email", "password"]

        widgets = {
            # set appearence of password imput as password
            "password" : forms.PasswordInput()
        }