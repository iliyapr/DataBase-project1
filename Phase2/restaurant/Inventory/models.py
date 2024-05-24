from django.db import models
from Employees.models import Manager, Chef

class Ingredient(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    type = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    unit = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ingredient'
        
class Storehouse(models.Model):
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    manager_ssn = models.ForeignKey(Manager, models.DO_NOTHING, db_column='manager_ssn', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Storehouse'


class StorehouseIngredient(models.Model):
    storehouse = models.OneToOneField(Storehouse, models.DO_NOTHING, primary_key=True)  # The composite primary key (storehouse_id, ingredient_id) found, that is not supported. The first column is selected.
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Storehouse_Ingredient'
        unique_together = (('storehouse', 'ingredient'),)



class Recipe(models.Model):
    instructions = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Recipe'


class RecipeIngredient(models.Model):
    recipe = models.OneToOneField(Recipe, models.DO_NOTHING, primary_key=True)  # The composite primary key (recipe_id, ingredient_id) found, that is not supported. The first column is selected.
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Recipe_Ingredient'
        unique_together = (('recipe', 'ingredient'),)

class ChefRecipe(models.Model):
    chef_ssn = models.OneToOneField(Chef, models.DO_NOTHING, db_column='chef_ssn', primary_key=True)  # The composite primary key (chef_ssn, recipe_id) found, that is not supported. The first column is selected.
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chef_Recipe'
        unique_together = (('chef_ssn', 'recipe'),)