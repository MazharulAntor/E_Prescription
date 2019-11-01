# Generated by Django 2.2.6 on 2019-10-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('licence', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineName', models.CharField(max_length=25)),
                ('singleUnitQuantity', models.CharField(max_length=50)),
                ('formName', models.CharField(choices=[("MA'S", "MA'S"), ('CTS', 'CTS')], max_length=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Company')),
            ],
        ),
    ]