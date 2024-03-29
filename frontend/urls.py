from django.urls import path
from .views import index\

urlpatterns = [
    path('', index),
    path('BookRoom', index),
    path('BrowseBooks', index)
]
