from django.urls import path
from .views import ItemView, OrderView, TableView

urlpatterns = [
    path("items/", ItemView.as_view(), name="item-list-create"),
    path("items/<int:pk>/", ItemView.as_view(), name="item-detail"),
    path("tables/", TableView.as_view(), name="table-list-create"),
    path("tables/<int:pk>/", TableView.as_view(), name="table-detail"),
    path("orders/", OrderView.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", OrderView.as_view(), name="order-detail"),
]
