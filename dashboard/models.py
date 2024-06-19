from django.db import models

# import user model to connect folder to user
from users.models import user_profile

# root folder of user
class master_folder (models.Model) :
    # parent user of the root folder (first folder, created when account is created and every folder and file will be inside of it)
    User = models.OneToOneField(user_profile, on_delete=models.CASCADE, related_name="root_folder")
    # id and name of folder
    folder_id = models.TextField()
    folder_name = models.TextField(max_length=100)

    # how the model will be showed
    def __str__(self) -> str:
        return f'{self.folder_name} < {self.User} >'

# normal folder 
class folder (models.Model) :
    # the creator of that folder
    User = models.ForeignKey(user_profile, on_delete = models.CASCADE,related_name="folders")

    # id and name of that folder
    folder_id = models.TextField()
    folder_name = models.TextField(max_length=100)

    # parent folder of that folder (witch folder that folder is inside)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children_folder", null=True, blank=True)

    # how the model will be showed
    def __str__(self) -> str:
        return f'{self.folder_name} - {self.User} -'

class file (models.Model) :
    User = models.ForeignKey(user_profile, on_delete=models.CASCADE, related_name="files")

    file = models.FileField (upload_to='uploads/')
    file_id = models.TextField()
    file_visible_name = models.TextField(max_length=100)
    file_name = models.TextField(max_length=100)

    parent_folder = models.ForeignKey(folder, on_delete=models.CASCADE, related_name="children_files")

    def __str__(self) -> str:
        return f'{self.file_name} <{self.parent_folder} [{self.file_id}]>'