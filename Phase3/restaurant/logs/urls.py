from django.urls import path
from .views import InsertLogView, DeleteLogView, UpdateLogView

urlpatterns = [
    path("insertlog/", InsertLogView.as_view(), name="insertlog-list"),
    path("insertlog/<str:pk>/", InsertLogView.as_view(), name="insertlog-detail"),
    path("deletelog/", DeleteLogView.as_view(), name="deletelog-list"),
    path("deletelog/<str:pk>/", DeleteLogView.as_view(), name="deletelog-detail"),
    path("updatelog/", UpdateLogView.as_view(), name="updatelog-list"),
    path("updatelog/<str:pk>/", UpdateLogView.as_view(), name="updatelog-detail"),
]
