from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, StorehouseViewSet, StorehouseIngredientViewSet, RecipeViewSet, RecipeIngredientViewSet, ChefRecipeViewSet

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'storehouses', StorehouseViewSet)
router.register(r'storehouse-ingredients', StorehouseIngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'recipe-ingredients', RecipeIngredientViewSet)
router.register(r'chef-recipes', ChefRecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
