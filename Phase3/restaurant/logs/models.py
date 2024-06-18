from django.db import models

class InsertLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=255)
    changed_data = models.TextField()
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'InsertLog'
        managed = False

class DeleteLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=255)
    changed_data = models.TextField()
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'DeleteLog'
        managed = False

class UpdateLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=255)
    previous_data = models.TextField()
    changed_data = models.TextField()
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'UpdateLog'
        managed = False

from django.db import models

class DailyInsertLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    changed_data = models.TextField()
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_DailyInsertLog'


class DailyDeleteLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    changed_data = models.TextField()
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_DailyDeleteLog'


class DailyUpdateLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    previous_data = models.TextField()
    changed_data = models.TextField()
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_DailyUpdateLog'


class LogEmployee(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Employee'

class LogChef(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Chef'

class LogWaiter(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Waiter'

class LogShipper(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Shipper'

class LogManager(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Manager'

class LogCustomer(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Customer'

class LogOrder(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Order'

class LogItem(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Item'

class LogRecipe(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Recipe'

class LogIngredient(models.Model):
    change_type = models.CharField(max_length=10)
    log_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=255)
    data = models.TextField()
    previous_data = models.TextField(null=True)
    changed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vw_Log_Ingredient'