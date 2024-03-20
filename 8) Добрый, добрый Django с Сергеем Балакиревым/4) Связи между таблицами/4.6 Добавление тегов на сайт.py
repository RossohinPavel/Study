""" Упражнение
Подвиг 5 (на повторение). Объявите класс модели с именем Subject (предмет) для описания таблицы следующей структуры:

id: primary key (в модели явно не прописывается);
slug: поле для хранения слагов (slug); максимальная длина 150, уникальное, обязательное;
name: текстовая строка; максимальная длина 100 символов, обязательное;
descr: тестовое поле (многострочное), необязательное;
is_active: булево поле (True - предмет активен / False - неактивен), по умолчанию True;
time_create: время создания записи (DateTimeField); формируется автоматически в момент первого добавления записи в таблицу.
"""
from django.db import models

# здесь объявляйте класс модели
class Subject(models.Model):
    slug = models.SlugField(max_length=150, unique=True)
    name = models.CharField(max_length=100)
    descr = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
