""" Упражнение 1
Подвиг 6. Заполните следующий класс модели Category:
class Category(models.Model):
    # здесь прописывайте атрибуты класса
для работы с таблицей БД следующей структуры:
id: идентификатор записи (Primary Key); формируется автоматически (описывать в классе не нужно);
name: название категории (models.CharField) с максимальной длиной 50 символов;
time_create: время создания категории (models.DateTimeField); должно заполняться автоматически в момент создания записи
Названия атрибутов должны совпадать с названиями полей.
P.S. В программе требуется только объявить класс, создавать его объекты не нужно.
"""
from django.db import models

class Category(models.Model):
    # здесь прописывайте атрибуты класса
    name = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)


""" Упражнение 2
Подвиг 7. Объявите класс модели с именем Post, унаследованный от базового класса models.Model, 
для работы с таблицей БД следующей структуры:

id: идентификатор записи (Primary Key); формируется автоматически (описывать в классе не нужно);
title: название поста (models.CharField) с максимальной длиной 150 символов;
content: содержание поста (models.TextField) с указанием необязательности заполнения при создании записи;
time_create: время создания категории (models.DateTimeField); должно заполняться автоматически в момент создания записи
time_update: время последнего изменения записи (models.DateTimeField); должно заполняться/обновляться автоматически в момент каждого изменения записи
is_published: флаг публикации записи (models.BooleanField) со значением по умолчанию True;
Названия атрибутов должны совпадать с названиями полей.
P.S. В программе требуется только объявить класс, создавать его объекты не нужно.
"""
from django.db import models

# здесь объявляйте класс модели
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
