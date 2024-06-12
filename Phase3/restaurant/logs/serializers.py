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

from rest_framework import serializers
from .models import DailyInsertLog, DailyDeleteLog, DailyUpdateLog, LogEmployee, LogChef, LogManager, LogWaiter, LogCustomer, LogIngredient, LogShipper, LogRecipe, LogItem, LogOrder

class DailyInsertLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyInsertLog
        fields = '__all__'

class DailyDeleteLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyDeleteLog
        fields = '__all__'

class DailyUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyUpdateLog
        fields = '__all__'

class LogEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEmployee
        fields = '__all__'

class LogChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogChef
        fields = '__all__'

class LogManagerSerializer(serializers.ModelSerializer):    
    class Meta:
        model = LogManager
        fields = '__all__'

class LogWaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogWaiter
        fields = '__all__'  

class LogCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogCustomer
        fields = '__all__'  

class LogIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogIngredient
        fields = '__all__'

class LogShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogShipper
        fields = '__all__'

class LogRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogRecipe
        fields = '__all__'

class LogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogItem
        fields = '__all__'

class LogOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogOrder
        fields = '__all__'
