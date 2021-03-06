# Generated by Django 3.1.7 on 2021-04-01 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_auto_20210401_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reading',
            name='read',
            field=models.CharField(choices=[('Y', 'Yeah'), ('N', 'Nah')], default='Y', max_length=1),
        ),
    ]
