from rest_framework import serializers

from .models import Chef, Employee, Manager, Shipper, Waiter

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'
        
class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
        
class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = '__all__'