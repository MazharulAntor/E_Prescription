# Generated by Django 3.0 on 2019-12-14 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pharmacist', '0001_initial'),
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuspiciousSoldMedicineReport',
            fields=[
                ('suspiciousSoldMedicineReportId', models.AutoField(primary_key=True, serialize=False)),
                ('reportComent', models.TextField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Patient')),
                ('pharmacist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacist.Pharmacist')),
                ('soldMedicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacist.SoldMedicine')),
            ],
        ),
    ]
