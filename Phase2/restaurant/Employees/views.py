from django.shortcuts import get_object_or_404, render

from rest_framework import generics

from .models import Chef, Employee, Manager, Shipper, Waiter

from .serializers import ChefSerializer, EmployeeSerializer, ManagerSerializer, ShipperSerializer, WaiterSerializer

class EmployeeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get_object(self):
        ssn = self.kwargs['ssnPK']
        return get_object_or_404(Employee, ssn=ssn)

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ChefRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    
    def get_object(self):
        ssn = self.kwargs['ssnPK']
        employee = get_object_or_404(Employee, ssn=ssn)
        return get_object_or_404(Chef, ssn=employee)

class ChefListCreate(generics.ListCreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer

class WaiterRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    
    def get_object(self):
        ssn = self.kwargs['ssnPK']
        employee = get_object_or_404(Employee, ssn=ssn)
        return get_object_or_404(Waiter, ssn=employee)

class WaiterListCreate(generics.ListCreateAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer

class ManagerRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
    def get_object(self):
        ssn = self.kwargs['ssnPK']
        employee = get_object_or_404(Employee, ssn=ssn)
        return get_object_or_404(Manager, ssn=employee)

class ManagerListCreate(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
class ShipperRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
    
    def get_object(self):
        ssn = self.kwargs['ssnPK']
        employee = get_object_or_404(Employee, ssn=ssn)
        return get_object_or_404(Shipper, ssn=employee)

class ShipperListCreate(generics.ListCreateAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer