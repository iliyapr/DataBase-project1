# Generated by Django 5.0.6 on 2024-06-17 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('ssn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=16, null=True)),
                ('started_at', models.DateField()),
                ('role', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('ssn', models.OneToOneField(db_column='ssn', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Employees.employee')),
                ('style', models.CharField(blank=True, max_length=50, null=True)),
                ('uniform_size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Chef',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('ssn', models.OneToOneField(db_column='ssn', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Employees.employee')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('responsibitiy', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Manager',
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('ssn', models.OneToOneField(db_column='ssn', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Employees.employee')),
                ('vehicle_plate_number', models.CharField(max_length=8)),
                ('vehicle_model', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Shipper',
            },
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('ssn', models.OneToOneField(db_column='ssn', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Employees.employee')),
                ('uniform_size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Waiter',
            },
        ),
    ]