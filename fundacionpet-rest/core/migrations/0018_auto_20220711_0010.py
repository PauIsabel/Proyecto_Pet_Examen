# Generated by Django 3.1.2 on 2022-07-11 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_suscripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suscripcion',
            old_name='FK_sus_us',
            new_name='id_usuario',
        ),
    ]