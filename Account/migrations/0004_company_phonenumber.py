# Generated by Django 2.2.6 on 2019-10-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20191028_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='phoneNumber',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
