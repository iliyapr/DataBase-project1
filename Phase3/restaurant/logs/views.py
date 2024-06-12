from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InsertLog, DeleteLog, UpdateLog
from .serializers import InsertLogSerializer, DeleteLogSerializer, UpdateLogSerializer

class InsertLogView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = InsertLog.objects.get(pk=pk)
                serializer = InsertLogSerializer(log)
            except InsertLog.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = InsertLog.objects.all()
            serializer = InsertLogSerializer(logs, many=True)
        return Response(serializer.data)

class DeleteLogView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = DeleteLog.objects.get(pk=pk)
                serializer = DeleteLogSerializer(log)
            except DeleteLog.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = DeleteLog.objects.all()
            serializer = DeleteLogSerializer(logs, many=True)
        return Response(serializer.data)

class UpdateLogView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = UpdateLog.objects.get(pk=pk)
                serializer = UpdateLogSerializer(log)
            except UpdateLog.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = UpdateLog.objects.all()
            serializer = UpdateLogSerializer(logs, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DailyInsertLog, DailyDeleteLog, DailyUpdateLog, DailyInsertLog, DailyDeleteLog, DailyUpdateLog, LogEmployee, LogChef, LogManager, LogWaiter, LogCustomer, LogIngredient, LogShipper, LogRecipe, LogItem, LogOrder
from .serializers import DailyInsertLogSerializer, DailyDeleteLogSerializer, DailyUpdateLogSerializer, LogEmployeeSerializer, LogChefSerializer, LogManagerSerializer, LogWaiterSerializer, LogCustomerSerializer, LogIngredientSerializer, LogShipperSerializer, LogRecipeSerializer, LogItemSerializer, LogOrderSerializer

class DailyInsertLogView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = DailyInsertLog.objects.get(pk=pk)
                serializer = DailyInsertLogSerializer(log)
            except DailyInsertLog.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = DailyInsertLog.objects.all()
            serializer = DailyInsertLogSerializer(logs, many=True)
        return Response(serializer.data)

class DailyDeleteLogView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = DailyDeleteLog.objects.get(pk=pk)
                serializer = DailyDeleteLogSerializer(log)
            except DailyDeleteLog.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = DailyDeleteLog.objects.all()
            serializer = DailyDeleteLogSerializer(logs, many=True)
        return Response(serializer.data)

class DailyUpdateLogView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = DailyUpdateLog.objects.get(pk=pk)
                serializer = DailyUpdateLogSerializer(log)
            except DailyUpdateLog.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = DailyUpdateLog.objects.all()
            serializer = DailyUpdateLogSerializer(logs, many=True)
        return Response(serializer.data)

class LogEmployeeView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogEmployee.objects.get(pk=pk)
                serializer = LogEmployeeSerializer(log)
            except LogEmployee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogEmployee.objects.all()
            serializer = LogEmployeeSerializer(logs, many=True)
        return Response(serializer.data)

class LogChefView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogChef.objects.get(pk=pk)
                serializer = LogChefSerializer(log)
            except LogChef.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogChef.objects.all()
            serializer = LogChefSerializer(logs, many=True)
        return Response(serializer.data)
    
class LogWaiterView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogWaiter.objects.get(pk=pk)
                serializer = LogWaiterSerializer(log)
            except LogWaiter.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogWaiter.objects.all()
            serializer = LogWaiterSerializer(logs, many=True)
        return Response(serializer.data)
    
class LogShipperView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogShipper.objects.get(pk=pk)
                serializer = LogShipperSerializer(log)
            except LogShipper.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogShipper.objects.all()
            serializer = LogShipperSerializer(logs, many=True)
        return Response(serializer.data)
    
class LogManagerView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogManager.objects.get(pk=pk)
                serializer = LogManagerSerializer(log)
            except LogManager.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogManager.objects.all()
            serializer = LogManagerSerializer(logs, many=True)
        return Response(serializer.data)

class LogCustomerView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogCustomer.objects.get(pk=pk)
                serializer = LogCustomerSerializer(log)
            except LogCustomer.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogCustomer.objects.all()
            serializer = LogCustomerSerializer(logs, many=True)
        return Response(serializer.data)
    
class LogIngredientView(APIView):   
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogIngredient.objects.get(pk=pk)
                serializer = LogIngredientSerializer(log)
            except LogIngredient.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogIngredient.objects.all()
            serializer = LogIngredientSerializer(logs, many=True)
        return Response(serializer.data)
    
class LogRecipeView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogRecipe.objects.get(pk=pk)
                serializer = LogRecipeSerializer(log)
            except LogRecipe.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogRecipe.objects.all()
            serializer = LogRecipeSerializer(logs, many=True)
        return Response(serializer.data)

class LogItemView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogItem.objects.get(pk=pk)
                serializer = LogItemSerializer(log)
            except LogItem.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogItem.objects.all()
            serializer = LogItemSerializer(logs, many=True)
        return Response(serializer.data)
    
class LogOrderView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                log = LogOrder.objects.get(pk=pk)
                serializer = LogOrderSerializer(log)
            except LogOrder.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            logs = LogOrder.objects.all()
            serializer = LogOrderSerializer(logs, many=True)
        return Response(serializer.data)
    
