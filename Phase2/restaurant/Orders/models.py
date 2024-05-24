from django.db import models

from Customers.models import Customer

class Item(models.Model):
    title = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cateorgy = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    description = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.
    cooking = models.BooleanField()
    price = models.IntegerField()
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Item'

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    shipper_ssn = models.ForeignKey('Shipper', models.DO_NOTHING, db_column='shipper_ssn', blank=True, null=True)
    waiter_ssn = models.ForeignKey('Waiter', models.DO_NOTHING, db_column='waiter_ssn', blank=True, null=True)
    table_number = models.ForeignKey('Table', models.DO_NOTHING, db_column='table_number', blank=True, null=True)
    ordered_at = models.DateField()
    discount = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    payment = models.IntegerField()
    order_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Order'

class OrderItem(models.Model):
    order = models.OneToOneField(Order, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, item_id) found, that is not supported. The first column is selected.
    item = models.ForeignKey(Item, models.DO_NOTHING)
    amount = models.IntegerField()
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Order_Item'
        unique_together = (('order', 'item'),)

class Table(models.Model):
    number = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Table'

class ItemRecipe(models.Model):
    item = models.OneToOneField(Item, models.DO_NOTHING, primary_key=True)  # The composite primary key (item_id, recipe_id) found, that is not supported. The first column is selected.
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Item_Recipe'
        unique_together = (('item', 'recipe'),)