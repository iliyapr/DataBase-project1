from django.urls import path
from .views import (
    IngredientCreateAPIView, IngredientUpdateAPIView, IngredientDeleteAPIView,
    StorehouseCreateAPIView, StorehouseUpdateAPIView, StorehouseDeleteAPIView,
    StorehouseIngredientCreateAPIView, StorehouseIngredientUpdateAPIView, StorehouseIngredientDeleteAPIView,
    RecipeCreateAPIView, RecipeUpdateAPIView, RecipeDeleteAPIView,
    RecipeIngredientCreateAPIView, RecipeIngredientUpdateAPIView, RecipeIngredientDeleteAPIView,
    ChefRecipeCreateAPIView, ChefRecipeUpdateAPIView, ChefRecipeDeleteAPIView
)

urlpatterns = [
    # Ingredient URLs
    path('ingredients/create/', IngredientCreateAPIView.as_view(), name='ingredient-create'),
    path('ingredients/update/<int:pk>/', IngredientUpdateAPIView.as_view(), name='ingredient-update'),
    path('ingredients/delete/<int:pk>/', IngredientDeleteAPIView.as_view(), name='ingredient-delete'),

    # Storehouse URLs
    path('storehouses/create/', StorehouseCreateAPIView.as_view(), name='storehouse-create'),
    path('storehouses/update/<int:pk>/', StorehouseUpdateAPIView.as_view(), name='storehouse-update'),
    path('storehouses/delete/<int:pk>/', StorehouseDeleteAPIView.as_view(), name='storehouse-delete'),

    # StorehouseIngredient URLs
    path('storehouse-ingredients/create/', StorehouseIngredientCreateAPIView.as_view(), name='storehouse-ingredient-create'),
    path('storehouse-ingredients/update/<int:pk>/', StorehouseIngredientUpdateAPIView.as_view(), name='storehouse-ingredient-update'),
    path('storehouse-ingredients/delete/<int:pk>/', StorehouseIngredientDeleteAPIView.as_view(), name='storehouse-ingredient-delete'),

    # Recipe URLs
    path('recipes/create/', RecipeCreateAPIView.as_view(), name='recipe-create'),
    path('recipes/update/<int:pk>/', RecipeUpdateAPIView.as_view(), name='recipe-update'),
    path('recipes/delete/<int:pk>/', RecipeDeleteAPIView.as_view(), name='recipe-delete'),

    # RecipeIngredient URLs
    path('recipe-ingredients/create/', RecipeIngredientCreateAPIView.as_view(), name='recipe-ingredient-create'),
    path('recipe-ingredients/update/<int:pk>/', RecipeIngredientUpdateAPIView.as_view(), name='recipe-ingredient-update'),
    path('recipe-ingredients/delete/<int:pk>/', RecipeIngredientDeleteAPIView.as_view(), name='recipe-ingredient-delete'),

    # ChefRecipe URLs
    path('chef-recipes/create/', ChefRecipeCreateAPIView.as_view(), name='chef-recipe-create'),
    path('chef-recipes/update/<int:pk>/', ChefRecipeUpdateAPIView.as_view(), name='chef-recipe-update'),
    path('chef-recipes/delete/<int:pk>/', ChefRecipeDeleteAPIView.as_view(), name='chef-recipe-delete'),
]
