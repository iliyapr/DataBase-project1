from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ingredient, Storehouse, Recipe, StorehouseIngredient, RecipeIngredient, ChefRecipe
from .serializers import IngredientSerializer, StorehouseSerializer, RecipeSerializer, StorehouseIngredientSerializer, RecipeIngredientSerializer, ChefRecipeSerializer

# Ingredient Views
class IngredientCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            ingredient = serializer.save()

            # Update StorehouseIngredient if storehouse_id is provided
            storehouse_id = serializer.validated_data.get('storehouse_id')
            amount_in_storehouse = serializer.validated_data.get('amount_in_storehouse')
            if storehouse_id and amount_in_storehouse:
                StorehouseIngredient.objects.create(storehouse_id=storehouse_id, ingredient=ingredient, amount=amount_in_storehouse)

            # Update RecipeIngredient if recipe_id is provided
            recipe_id = serializer.validated_data.get('recipe_id')
            amount_in_recipe = serializer.validated_data.get('amount_in_recipe')
            if recipe_id and amount_in_recipe:
                RecipeIngredient.objects.create(recipe_id=recipe_id, ingredient=ingredient, amount=amount_in_recipe)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientUpdateAPIView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            ingredient = Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            ingredient = serializer.save()

            # Update StorehouseIngredient if storehouse_id is provided
            storehouse_id = serializer.validated_data.get('storehouse_id')
            amount_in_storehouse = serializer.validated_data.get('amount_in_storehouse')
            if storehouse_id and amount_in_storehouse:
                storehouse_ingredient, created = StorehouseIngredient.objects.update_or_create(
                    storehouse_id=storehouse_id, ingredient=ingredient,
                    defaults={'amount': amount_in_storehouse}
                )

            # Update RecipeIngredient if recipe_id is provided
            recipe_id = serializer.validated_data.get('recipe_id')
            amount_in_recipe = serializer.validated_data.get('amount_in_recipe')
            if recipe_id and amount_in_recipe:
                recipe_ingredient, created = RecipeIngredient.objects.update_or_create(
                    recipe_id=recipe_id, ingredient=ingredient,
                    defaults={'amount': amount_in_recipe}
                )

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientDeleteAPIView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            ingredient = Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Storehouse Views
class StorehouseCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StorehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StorehouseUpdateAPIView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            storehouse = Storehouse.objects.get(pk=pk)
        except Storehouse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StorehouseSerializer(storehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StorehouseDeleteAPIView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            storehouse = Storehouse.objects.get(pk=pk)
        except Storehouse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        storehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Recipe Views
class RecipeCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RecipeSerializer(data=request.data)
        # if serializer.is_valid():
        #     recipe = serializer.save()

            # # Update ChefRecipe if chef_ssn is provided
            # chef_ssn = serializer.validated_data.get('chef_ssn')
            # if chef_ssn:
            #     ChefRecipe.objects.create(chef_ssn=chef_ssn, recipe=recipe)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeUpdateAPIView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe, data=request.data)
        # if serializer.is_valid():
        #     recipe = serializer.save()

            # # Update ChefRecipe if chef_ssn is provided
            # chef_ssn = serializer.validated_data.get('chef_ssn')
            # if chef_ssn:
            #     chef_recipe, created = ChefRecipe.objects.update_or_create(
            #         chef_ssn=chef_ssn, recipe=recipe
            #     )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDeleteAPIView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
