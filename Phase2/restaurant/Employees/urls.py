from django.urls import path
from .views import EmployeeView, ChefView, WaiterView, ManagerView, ShipperView

urlpatterns = [
    path("employees/", EmployeeView.as_view(), name="employee-list-create"),
    path("employees/<str:pk>/", EmployeeView.as_view(), name="employee-detail"),
    path("chefs/", ChefView.as_view(), name="chef-list-create"),
    path("chefs/<str:pk>/", ChefView.as_view(), name="chef-detail"),
    path("waiters/", WaiterView.as_view(), name="waiter-list-create"),
    path("waiters/<str:pk>/", WaiterView.as_view(), name="waiter-detail"),
    path("managers/", ManagerView.as_view(), name="manager-list-create"),
    path("managers/<str:pk>/", ManagerView.as_view(), name="manager-detail"),
    path("shippers/", ShipperView.as_view(), name="shipper-list-create"),
    path("shippers/<str:pk>/", ShipperView.as_view(), name="shipper-detail"),
]
