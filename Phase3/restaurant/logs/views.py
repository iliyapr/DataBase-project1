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
