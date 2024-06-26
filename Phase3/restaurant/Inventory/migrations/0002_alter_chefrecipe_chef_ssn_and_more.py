# Generated by Django 5.0.6 on 2024-06-17 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefrecipe',
            name='chef_ssn',
            field=models.ForeignKey(db_column='chef_ssn', on_delete=django.db.models.deletion.DO_NOTHING, to='Employees.chef'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Inventory.recipe'),
        ),
        migrations.AlterField(
            model_name='storehouseingredient',
            name='storehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Inventory.storehouse'),
        ),
    ]
