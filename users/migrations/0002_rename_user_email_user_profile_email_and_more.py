# Generated by Django 5.0.6 on 2024-06-04 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='user_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='user_password',
            new_name='password',
        ),
    ]
