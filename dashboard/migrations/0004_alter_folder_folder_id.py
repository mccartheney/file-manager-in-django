# Generated by Django 5.0.6 on 2024-06-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_folder_folder_id_alter_master_folder_folder_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='folder_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
