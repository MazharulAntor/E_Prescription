# Generated by Django 2.2.6 on 2019-11-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacist', '0010_remove_order_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=20),
        ),
    ]