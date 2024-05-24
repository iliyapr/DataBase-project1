from django.db import models


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(unique=True, max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    last_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer'