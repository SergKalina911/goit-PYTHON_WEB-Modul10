""" Модуль urls.py для приложения noteapp, который определяет маршруты URL для приложения. Здесь мы
импортируем функцию path из django.urls и представления из текущего приложения. Затем мы создаем
список urlpatterns, который содержит маршруты URL и соответствующие им представления. В данном
случае, мы определяем маршрут для главной страницы приложения, который будет обрабатывать запросы
по корневому URL ('') и вызывать функцию main из views.py. Мы также указываем имя маршрута 'main'
для удобства использования в шаблонах и других местах приложения."""

from django.urls import path
from . import views

app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('note/', views.note, name='note'),
    path('detail/<int:note_id>', views.detail, name='detail'),
    path('done/<int:note_id>', views.set_done, name='set_done'),
    path('delete/<int:note_id>', views.delete_note, name='delete'),
]
