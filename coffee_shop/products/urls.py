from django.contrib import admin
from django.urls import path
from .views import ProductFormView, ProductsListView
urlpatterns = [
    path('', ProductsListView.as_view(), name='list_product'),
    path('add/', ProductFormView.as_view(), name='add_product')
]
