from django.urls import path

from .views import ChefRetrieveUpdateDelete, EmployeeListCreate, EmployeeRetrieveUpdateDelete, ChefListCreate, ManagerListCreate, ManagerRetrieveUpdateDelete, ShipperListCreate, ShipperRetrieveUpdateDelete, WaiterListCreate, WaiterRetrieveUpdateDelete

urlpatterns = [
    path('employee/RetrieveUpdateDelete/<str:ssnPK>', EmployeeRetrieveUpdateDelete.as_view()),    
    path('employee/ListCreate/', EmployeeListCreate.as_view()),
    
    path('chef/RetrieveUpdateDelete/<str:ssnPK>', ChefRetrieveUpdateDelete.as_view()),    
    path('chef/ListCreate/', ChefListCreate.as_view()),
    
    path('waiter/RetrieveUpdateDelete/<str:ssnPK>', WaiterRetrieveUpdateDelete.as_view()),    
    path('waiter/ListCreate/', WaiterListCreate.as_view()),
    
    path('manager/RetrieveUpdateDelete/<str:ssnPK>', ManagerRetrieveUpdateDelete.as_view()),    
    path('manager/ListCreate/', ManagerListCreate.as_view()),
    
    path('shipper/RetrieveUpdateDelete/<str:ssnPK>', ShipperRetrieveUpdateDelete.as_view()),    
    path('shipper/ListCreate/', ShipperListCreate.as_view()),
]
