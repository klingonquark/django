"""
EVENTS API URLs
"""
from django.urls import path 
from .views import CategoryListCreateView, CategoryRetrieveView

urlpatterns = [
    # api/events/category
    path("category", CategoryListCreateView.as_view(), name="api-category-list"),
    path("category/<int:pk>", CategoryRetrieveView.as_view(), name="api-create-delete"),
]