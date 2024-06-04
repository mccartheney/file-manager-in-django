from django.db import models
from django.contrib.auth.models import User

class user_profile (models.Model) :
    # user main data
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name} <{self.email}>'