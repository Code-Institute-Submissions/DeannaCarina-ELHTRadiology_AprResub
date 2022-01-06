# Generated by Django 3.2 on 2022-01-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_angioappointment_exam_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='DexaAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=10)),
                ('hospital_number', models.CharField(max_length=8)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('date_of_exam', models.DateField()),
                ('time_of_exam', models.TimeField()),
                ('preg_status', models.CharField(max_length=20)),
                ('weight_status', models.CharField(max_length=100)),
                ('surgery_status', models.CharField(max_length=100)),
                ('comms_problems', models.TextField(max_length=1000)),
                ('contact_number', models.IntegerField()),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]
