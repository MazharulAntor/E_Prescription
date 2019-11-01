# Generated by Django 2.2.6 on 2019-10-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('licence', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
