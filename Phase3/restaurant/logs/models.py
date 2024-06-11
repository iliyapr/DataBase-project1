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
