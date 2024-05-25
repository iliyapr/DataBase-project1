from django.db import models
from Employees.models import Manager, Chef


class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "Ingredient"


class Storehouse(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    manager_ssn = models.ForeignKey(
        Manager, models.DO_NOTHING, db_column="manager_ssn", blank=True, null=True
    )

    class Meta:
        db_table = "Storehouse"


class StorehouseIngredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    storehouse = models.OneToOneField(Storehouse, models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "Storehouse_Ingredient"
        unique_together = (("storehouse", "ingredient"),)


class Recipe(models.Model):
    instructions = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.

    class Meta:
        db_table = "Recipe"


class RecipeIngredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    recipe = models.OneToOneField(Recipe, models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "Recipe_Ingredient"
        unique_together = (("recipe", "ingredient"),)


class ChefRecipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    chef_ssn = models.OneToOneField(Chef, models.DO_NOTHING, db_column="chef_ssn")
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)

    class Meta:
        db_table = "chef_Recipe"
        unique_together = (("chef_ssn", "recipe"),)
