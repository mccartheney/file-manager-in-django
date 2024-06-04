from django.contrib import admin

# import user models to give acess to admin see, create and delete
from .models import user_profile

# give admin acess to user_profile
admin.site.register(user_profile)