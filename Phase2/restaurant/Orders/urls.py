from django.urls import path
from .views import (
    ItemListCreateAPIView,
    ItemDetailAPIView,
    OrderListCreateAPIView,
    OrderDetailAPIView,
    TableListCreateAPIView,
    TableDetailAPIView,
)


urlpatterns = [
    path("items/", ItemListCreateAPIView.as_view(), name="item-list-create"),
    path("items/<int:pk>/", ItemDetailAPIView.as_view(), name="item-detail"),
    path("orders/", OrderListCreateAPIView.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
    path("tables/", TableListCreateAPIView.as_view(), name="table-list-create"),
    path("tables/<int:pk>/", TableDetailAPIView.as_view(), name="table-detail"),
]
