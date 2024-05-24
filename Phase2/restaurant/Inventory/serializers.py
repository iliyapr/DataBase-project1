from rest_framework import serializers
from .models import Ingredient, Storehouse, StorehouseIngredient, Recipe, RecipeIngredient, ChefRecipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class StorehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storehouse
        fields = '__all__'

class StorehouseIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorehouseIngredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class ChefRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefRecipe
        fields = '__all__'
