from rest_framework import serializers
from .models import (
    Ingredient,
    Storehouse,
    Recipe,
    StorehouseIngredient,
    RecipeIngredient,
)


class IngredientSerializer(serializers.ModelSerializer):
    storehouses = serializers.PrimaryKeyRelatedField(
        queryset=Storehouse.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Ingredient
        fields = "__all__"

    def create(self, validated_data):
        storehouses = validated_data.pop("storehouses", [])
        ingredient = Ingredient.objects.create(**validated_data)
        for storehouse in storehouses:
            StorehouseIngredient.objects.create(
                ingredient=ingredient, storehouse=storehouse
            )
        return ingredient

    def update(self, instance, validated_data):
        storehouses = validated_data.pop("storehouses", [])
        instance = super().update(instance, validated_data)
        StorehouseIngredient.objects.filter(ingredient=instance).delete()
        for storehouse in storehouses:
            StorehouseIngredient.objects.create(
                ingredient=instance, storehouse=storehouse
            )
        return instance


class StorehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storehouse
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Recipe
        fields = "__all__"

    def create(self, validated_data):
        ingredients = validated_data.pop("ingredients", [])
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients:
            RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)
        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.pop("ingredients", [])
        instance = super().update(instance, validated_data)
        RecipeIngredient.objects.filter(recipe=instance).delete()
        for ingredient in ingredients:
            RecipeIngredient.objects.create(recipe=instance, ingredient=ingredient)
        return instance
