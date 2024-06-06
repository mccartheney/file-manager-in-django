from django.db import models

# import user model to connect folder to user
from django.contrib.auth.models import User

# root folder of user
class master_folder (models.Model) :
    # parent user of the root folder (first folder, created when account is created and every folder and file will be inside of it)
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name="parent_user")
    # id and name of folder
    folder_id = models.IntegerField()
    folder_name = models.TextField(max_length=100)

    # how the model will be showed
    def __str__(self) -> str:
        return f'{self.folder_name} < {self.User} >'

# normal folder 
class folder (models.Model) :
    # the creator of that folder
    User = models.OneToOneField(User, on_delete = models.CASCADE,related_name="parent_of_folder")

    # id and name of that folder
    folder_id = models.IntegerField
    folder_name = models.TextField(max_length=100)

    # parent folder of that folder (witch folder that folder is inside)
    parent_folder = models.ForeignKey(master_folder, on_delete=models.CASCADE, related_name="children_folder")

    # how the model will be showed
    def __str__(self) -> str:
        return f'{self.folder_name} < {self.User} >'

class file (models.Model) :
    pass