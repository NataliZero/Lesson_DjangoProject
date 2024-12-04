from django.contrib import admin
from django.urls import path, include  # Подключаем include

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для админки
    path('', include('myapp.urls')),  # Подключаем маршруты из myapp для корневого и других путей
]
