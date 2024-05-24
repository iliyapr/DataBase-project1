from rest_framework import viewsets
from .models import Ingredient, Storehouse, StorehouseIngredient, Recipe, RecipeIngredient, ChefRecipe
from .serializers import IngredientSerializer, StorehouseSerializer, StorehouseIngredientSerializer, RecipeSerializer, RecipeIngredientSerializer, ChefRecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class StorehouseViewSet(viewsets.ModelViewSet):
    queryset = Storehouse.objects.all()
    serializer_class = StorehouseSerializer

class StorehouseIngredientViewSet(viewsets.ModelViewSet):
    queryset = StorehouseIngredient.objects.all()
    serializer_class = StorehouseIngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeIngredientViewSet(viewsets.ModelViewSet):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

class ChefRecipeViewSet(viewsets.ModelViewSet):
    queryset = ChefRecipe.objects.all()
    serializer_class = ChefRecipeSerializer
