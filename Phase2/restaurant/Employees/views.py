from django.shortcuts import get_object_or_404, render

from rest_framework import generics

from .models import Chef, Employee

from .serializers import ChefSerializer, EmployeeSerializer

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
