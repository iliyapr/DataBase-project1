from django.db import models

from Customers.models import Customer
from Inventory.models import Recipe


class Item(models.Model):
    title = models.CharField(max_length=255)
    cateorgy = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    cooking = models.BooleanField()
    price = models.IntegerField()
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "Item"


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    shipper_ssn = models.ForeignKey(
        "Employees.Shipper", models.DO_NOTHING, db_column="shipper_ssn", null=True
    )
    waiter_ssn = models.ForeignKey(
        "Employees.Waiter", models.DO_NOTHING, db_column="waiter_ssn", null=True
    )
    table_number = models.ForeignKey(
        "Orders.Table", models.DO_NOTHING, db_column="table_number", null=True
    )
    ordered_at = models.DateField()
    discount = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    payment = models.IntegerField()
    order_type = models.IntegerField()

    class Meta:
        db_table = "Order"


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, models.CASCADE)
    item = models.ForeignKey(Item, models.CASCADE)
    amount = models.IntegerField()
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "Order_Item"
        unique_together = (("order", "item"),)


class Table(models.Model):
    number = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        db_table = "Table"


class ItemRecipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(Item, models.CASCADE)
    recipe = models.ForeignKey(Recipe, models.CASCADE)

    class Meta:
        db_table = "Item_Recipe"
        unique_together = (("item", "recipe"),)
