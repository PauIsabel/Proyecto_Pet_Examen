# Generated by Django 3.1.2 on 2022-07-11 20:57

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20220711_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscripcion',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='suscripcion',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]