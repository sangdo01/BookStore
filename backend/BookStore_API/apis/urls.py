from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.ListUsers.as_view(), name='test'),
]