# Generated by Django 2.2.6 on 2019-11-30 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20191130_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescribedmedicine',
            old_name='prescribedMedicinePrescriptioin',
            new_name='prescribedMedicinePrescription',
        ),
    ]