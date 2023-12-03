from django.urls import path
from .views import index, success, result
urlpatterns = [
    path('', index, name='index'),
    path('success/', success, name='success'),
    path('result/', result, name='result'),
]
