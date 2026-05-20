""" Модуль admin.py для приложения noteapp, который регистрирует модели данных для заметок и тегов
в административной панели Django. Здесь мы импортируем модели Tag и Note из файла models.py и
регистрируем их с помощью функции admin.site.register(), чтобы они были доступны для управления
через административный интерфейс Django."""
from django.contrib import admin

from .models import Tag, Note

# Register your models here.
admin.site.register(Tag)
admin.site.register(Note)
