# Generated by Django 3.1.7 on 2021-04-02 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='comic',
        ),
    ]
