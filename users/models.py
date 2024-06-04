from django.db import models

# import User model to associate it to user_profile model
from django.contrib.auth.models import User

# user_profile mode;
class user_profile (models.Model) :
    # connection from that model to User model, on delete that User that user profile will be deleted too
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # email, name and password fields 
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # the name of the model
    def __str__(self) -> str:
        return f'{self.name} <{self.email}>'