from rest_framework import serializers
from .models import InsertLog, DeleteLog, UpdateLog

class InsertLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsertLog
        fields = '__all__'

class DeleteLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeleteLog
        fields = '__all__'

class UpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateLog
        fields = '__all__'
