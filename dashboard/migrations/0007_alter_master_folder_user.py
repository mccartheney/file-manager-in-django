# Generated by Django 5.0.6 on 2024-06-07 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_folder_user_alter_master_folder_user'),
        ('users', '0003_alter_user_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_folder',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='root_folder', to='users.user_profile'),
        ),
    ]
