""" Упражнение
Подвиг 1. Пусть имеются две следующие модели:

from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = # здесь прописывайте связь типа many-to-many с моделью Subject
Необходимо в модели Lector прописать связь типа many-to-many с моделью Subject. При этом поле subjects должно быть необязательным к заполнению.

P.S. При определении связи первичную модель Subject указать в виде строки "Subject".
"""
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True)
