from django.db import models
from django.contrib.auth.models import User

class user_profile (models.Model) :
    # user main data
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user_email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.user_name} <{self.user_email}>'