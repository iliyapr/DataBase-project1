from rest_framework import serializers
from .models import Item, Order, Table, OrderItem, ItemRecipe, Recipe


class ItemRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecipe
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Item
        fields = "__all__"

    def create(self, validated_data):
        recipes = validated_data.pop("recipes", [])
        item = Item.objects.create(**validated_data)
        for recipe in recipes:
            ItemRecipe.objects.create(item=item, recipe=recipe)
        return item

    def update(self, instance, validated_data):
        recipes = validated_data.pop("recipes", [])
        instance = super().update(instance, validated_data)
        ItemRecipe.objects.filter(item=instance).delete()
        for recipe in recipes:
            ItemRecipe.objects.create(item=instance, recipe=recipe)
        return instance


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["item", "amount", "rate"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", [])
        instance = super().update(instance, validated_data)
        OrderItem.objects.filter(order=instance).delete()
        for item_data in items_data:
            OrderItem.objects.create(order=instance, **item_data)
        return instance
