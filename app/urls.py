from django.urls import path
from .views import index, success

urlpatterns = [
    path('', index, name='index'),
    path('success/', success, name='success'),
]
