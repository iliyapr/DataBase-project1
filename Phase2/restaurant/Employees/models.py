from django.db import models

class Employee(models.Model):
    ssn = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    gender = models.IntegerField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)  # This field type is a guess.
    bank_account_number = models.CharField(max_length=16, blank=True, null=True)
    started_at = models.DateField()
    role = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        db_table = 'Employee'
    
    
class Chef(models.Model):
    ssn = models.OneToOneField('Employee', models.DO_NOTHING, db_column='ssn', primary_key=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    uniform_size = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Chef'

class Manager(models.Model):
    ssn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ssn', primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    responsibitiy = models.CharField(max_length=255)

    class Meta:
        db_table = 'Manager'

class Shipper(models.Model):
    ssn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ssn', primary_key=True)
    vehicle_plate_number = models.CharField(max_length=8)
    vehicle_model = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Shipper'

class Waiter(models.Model):
    ssn = models.OneToOneField(Employee, models.DO_NOTHING, db_column='ssn', primary_key=True)
    uniform_size = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Waiter'
