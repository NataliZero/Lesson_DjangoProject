from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data, name='data'),  # Маршрут для /data/
    path('test/', views.test, name='test'),  # Маршрут для /test/
    path('', views.data, name='home'),  # Корневой маршрут
]
