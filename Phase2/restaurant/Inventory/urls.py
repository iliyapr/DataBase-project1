from django.urls import path
from .views import (
    IngredientCreateAPIView,
    IngredientUpdateAPIView,
    IngredientDeleteAPIView,
    StorehouseCreateAPIView,
    StorehouseUpdateAPIView,
    StorehouseDeleteAPIView,
    RecipeCreateAPIView,
    RecipeUpdateAPIView,
    RecipeDeleteAPIView
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

    # Recipe URLs
    path('recipes/create/', RecipeCreateAPIView.as_view(), name='recipe-create'),
    path('recipes/update/<int:pk>/', RecipeUpdateAPIView.as_view(), name='recipe-update'),
    path('recipes/delete/<int:pk>/', RecipeDeleteAPIView.as_view(), name='recipe-delete'),
]
