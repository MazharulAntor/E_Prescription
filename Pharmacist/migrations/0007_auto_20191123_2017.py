# Generated by Django 2.2.6 on 2019-11-23 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacist', '0006_auto_20191123_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pharmacist',
            old_name='phoneNummber',
            new_name='phoneNumber',
        ),
    ]
