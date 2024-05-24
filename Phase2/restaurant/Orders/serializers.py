from rest_framework import serializers
from .models import Item, Order, OrderItem, Table, ItemRecipe
from Customers.serializers import CustomerSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    customer = CustomerSerializer()
    table = TableSerializer()

    class Meta:
        model = Order
        fields = ("id", "ordered_at", "discount", "status", "payment", "order_type")


class ItemRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRecipe
        fields = "__all__"
