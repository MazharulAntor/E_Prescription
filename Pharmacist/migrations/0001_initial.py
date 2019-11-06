# Generated by Django 2.2.6 on 2019-11-06 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('pharmacistId', models.AutoField(primary_key=True, serialize=False)),
                ('pharmacistStoreName', models.CharField(max_length=33)),
                ('pharmacistDrugeLicence', models.CharField(max_length=33)),
                ('pharmacistPhoneNummber', models.BigIntegerField(max_length=18)),
                ('pharmacistStoreAddress', models.CharField(max_length=33)),
                ('pharmacistPassword', models.CharField(max_length=33)),
            ],
        ),
    ]
