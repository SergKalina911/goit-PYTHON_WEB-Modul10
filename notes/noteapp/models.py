""" Модуль models.py для приложения noteapp, который содержит модели данных для заметок и тегов."""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    """ Модель для тегов, которые можно присваивать заметкам."""
    # Поле name для названия тега, которое не может быть пустым, должно быть уникальным и имеет
    # максимальную длину 25 символов.
    name = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        """ Класс Meta для модели Tag, который содержит метаданные модели. Здесь мы определяем
        уникальное ограничение для полей user и name, чтобы один пользователь не мог создавать
        теги с одинаковыми именами. Это гарантирует, что каждый тег будет уникальным для каждого
        пользователя. """
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        """ Метод для отображения тега в виде строки, который возвращает имя тега."""
        return f"{self.name}"


class Note(models.Model):
    """ Модель для заметок."""
    # Поле name для названия заметки, которое не может быть пустым и имеет максимальную длину 50
    # символов.
    name = models.CharField(max_length=50, null=False)
    # Поле description для описания заметки, которое не может быть пустым и имеет максимальную
    # длину 150 символов.
    description = models.CharField(max_length=150, null=False)
    # Поле done для отметки о выполнении заметки, которое по умолчанию равно False.
    done = models.BooleanField(default=False)
    # Поле created для хранения даты и времени создания заметки.
    created = models.DateTimeField(auto_now_add=True)
    # Поле tags для связи заметки с тегами. Здесь используется ManyToManyField, что означает, что
    # одна заметка может иметь несколько тегов, а один тег может быть присвоен нескольким заметкам.
    tags = models.ManyToManyField(Tag)
    # Поле user для связи заметки с пользователем, который ее создал. Здесь используется ForeignKey
    # что означает, что одна заметка принадлежит одному пользователю, а один пользователь может
    # иметь несколько заметок. При удалении пользователя все его заметки также будут удалены
    # (on_delete=models.CASCADE). По умолчанию, если не указано иное, заметка будет принадлежать
    # пользователю с id 1 (default=1).
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """ Метод для отображения заметки в виде строки, который возвращает имя заметки."""
        return f"{self.name}"
