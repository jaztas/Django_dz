from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import HomeListView, ProductListView, ProductDetailView, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contact/', contacts, name='contacts'),
    path('catalog/', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product'),
]