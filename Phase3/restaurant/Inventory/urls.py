from django.urls import path
from .views import IngredientView, StorehouseView, RecipeView

urlpatterns = [
    path("ingredients/", IngredientView.as_view(), name="ingredient-list-create"),
    path("ingredients/<int:pk>/", IngredientView.as_view(), name="ingredient-detail"),
    path("storehouses/", StorehouseView.as_view(), name="storehouse-list-create"),
    path("storehouses/<int:pk>/", StorehouseView.as_view(), name="storehouse-detail"),
    path("recipes/", RecipeView.as_view(), name="recipe-list-create"),
    path("recipes/<int:pk>/", RecipeView.as_view(), name="recipe-detail"),
]
