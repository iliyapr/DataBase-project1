from rest_framework import serializers
from .models import Ingredient, Storehouse, Recipe, StorehouseIngredient, RecipeIngredient, ChefRecipe

class StorehouseIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorehouseIngredient
        fields = '__all__'

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class ChefRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefRecipe
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    storehouse_id = serializers.IntegerField(write_only=True, required=False)
    recipe_id = serializers.IntegerField(write_only=True, required=False)
    amount_in_storehouse = serializers.IntegerField(write_only=True, required=False)
    amount_in_recipe = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Ingredient
        fields = '__all__'

class StorehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storehouse
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    chef_ssn = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Recipe
        fields = '__all__'
