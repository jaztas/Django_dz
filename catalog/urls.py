from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import home, contacts, products_list, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contacts, name='contacts'),
    path('catalog/', products_list, name='products_list'),
    path('catalog/<int:pk>/', product, name='product'),
]