# Generated by Django 4.1 on 2022-09-03 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pichangasApp', '0002_equipo_app_pichanga_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios_app',
            name='equipo',
            field=models.CharField(default='', max_length=128),
        ),
    ]
