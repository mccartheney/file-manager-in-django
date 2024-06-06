from django.contrib import admin

# import models to give access to folders to admin (only on development)
from .models import master_folder, folder

# give admin access to models imported above
admin.site.register(master_folder)
admin.site.register(folder)