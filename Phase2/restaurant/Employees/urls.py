from django.urls import path

from .views import ChefRetrieveUpdateDelete, EmployeeListCreate, EmployeeRetrieveUpdateDelete, ChefListCreate

urlpatterns = [
    path('employee/RetrieveUpdateDelete/<str:ssnPK>', EmployeeRetrieveUpdateDelete.as_view()),    
    path('employee/ListCreate/', EmployeeListCreate.as_view()),
    
    path('chef/RetrieveUpdateDelete/<str:ssnPK>', ChefRetrieveUpdateDelete.as_view()),    
    path('chef/ListCreate/', ChefListCreate.as_view()),
]
