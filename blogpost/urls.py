from django.urls import path

from blogpost.apps import BlogPostConfig
from blogpost.views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, \
    BlogPostDeleteView

app_name = BlogPostConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('view/', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view'),
    path('update/<int:pk>/', BlogPostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]