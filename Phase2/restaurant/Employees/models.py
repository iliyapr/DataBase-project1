from django.db import models

class Employee(models.Model):
    ssn = models.CharField(primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone_number = models.CharField(max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS')
    gender = models.IntegerField(blank=True, null=True)
    resume = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.
    bank_account_number = models.CharField(max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    started_at = models.DateField()
    role = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Employee'
    
    
class Chef(models.Model):
    ssn = models.OneToOneField('Employee', models.DO_NOTHING, db_column='ssn', primary_key=True)
    style = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    uniform_size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Chef'

class Manager(models.Model):
    ssn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ssn', primary_key=True)
    username = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    responsibitiy = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'Manager'

class Shipper(models.Model):
    ssn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ssn', primary_key=True)
    vehicle_plate_number = models.CharField(max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')
    vehicle_model = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Shipper'

class Waiter(models.Model):
    ssn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ssn', primary_key=True)
    uniform_size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Waiter'
