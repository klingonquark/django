""" 
Event URLS
"""
from django.urls import path
from .views import (hello_world, 
                    category_list, 
                    category_detail, 
                    EventListView, 
                    EventCreateView,
                    EventUpdateView, 
                    EventDeleteView,
                    send_mail,
         
                    )

app_name = "events"  # link: app_name:path_name (zb. events:category_detail)


urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
    path("create", EventCreateView.as_view(), name="event_create"),
    path("update/<int:pk>", EventUpdateView.as_view(), name="event_update"),
    path("delete/<int:pk>", EventDeleteView.as_view(), name="event_delete"),
    path("hello", hello_world, name="hello"),
    path("categories", category_list, name="category_list"),
    path("category/<int:pk>", category_detail, name="category_detail"),
    path("email", send_mail, name="email")
]