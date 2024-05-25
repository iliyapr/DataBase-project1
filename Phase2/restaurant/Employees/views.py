# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Chef, Waiter, Manager, Shipper
from .serializers import (
    EmployeeSerializer,
    ChefSerializer,
    WaiterSerializer,
    ManagerSerializer,
    ShipperSerializer,
)


class EmployeeView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                employee = Employee.objects.get(pk=pk)
                serializer = EmployeeSerializer(employee)
            except Employee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChefView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                chef = Chef.objects.get(pk=pk)
                serializer = ChefSerializer(chef)
            except Chef.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            chefs = Chef.objects.all()
            serializer = ChefSerializer(chefs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChefSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            chef = Chef.objects.get(pk=pk)
        except Chef.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ChefSerializer(chef, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            chef = Chef.objects.get(pk=pk)
        except Chef.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        chef.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WaiterView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                waiter = Waiter.objects.get(pk=pk)
                serializer = WaiterSerializer(waiter)
            except Waiter.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            waiters = Waiter.objects.all()
            serializer = WaiterSerializer(waiters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WaiterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            waiter = Waiter.objects.get(pk=pk)
        except Waiter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WaiterSerializer(waiter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            waiter = Waiter.objects.get(pk=pk)
        except Waiter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        waiter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagerView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                manager = Manager.objects.get(pk=pk)
                serializer = ManagerSerializer(manager)
            except Manager.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            managers = Manager.objects.all()
            serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            manager = Manager.objects.get(pk=pk)
        except Manager.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ManagerSerializer(manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            manager = Manager.objects.get(pk=pk)
        except Manager.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShipperView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                shipper = Shipper.objects.get(pk=pk)
                serializer = ShipperSerializer(shipper)
            except Shipper.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            shippers = Shipper.objects.all()
            serializer = ShipperSerializer(shippers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShipperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            shipper = Shipper.objects.get(pk=pk)
        except Shipper.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShipperSerializer(shipper, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            shipper = Shipper.objects.get(pk=pk)
        except Shipper.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        shipper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
