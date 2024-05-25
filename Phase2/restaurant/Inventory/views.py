from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ingredient, Storehouse, Recipe
from .serializers import IngredientSerializer, StorehouseSerializer, RecipeSerializer


class IngredientView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                ingredient = Ingredient.objects.get(pk=pk)
                serializer = IngredientSerializer(ingredient)
            except Ingredient.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            ingredients = Ingredient.objects.all()
            serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            ingredient = Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            ingredient = Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StorehouseView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                storehouse = Storehouse.objects.get(pk=pk)
                serializer = StorehouseSerializer(storehouse)
            except Storehouse.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            storehouses = Storehouse.objects.all()
            serializer = StorehouseSerializer(storehouses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StorehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            storehouse = Storehouse.objects.get(pk=pk)
        except Storehouse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StorehouseSerializer(storehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            storehouse = Storehouse.objects.get(pk=pk)
        except Storehouse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        storehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                recipe = Recipe.objects.get(pk=pk)
                serializer = RecipeSerializer(recipe)
            except Recipe.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
