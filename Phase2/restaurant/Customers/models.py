from django.db import models


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(unique=True, max_length=11)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Customer'