""" Упражнение
Подвиг 2. Пусть в программе объявлены следующие модели:

from django.db import models

class PersonData(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    passport = models.CharField(max_length=100, db_index=True, unique=True)


class Person(models.Model):
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data = # здесь опишите связь one-to-one с моделью PersonData
Завершите определение модели Person, добавив для атрибута data связь one-to-one с моделью PersonData, как необязательную, с допустимым значением NULL, и установкой значения NULL в поле data в случае удаления записи из связанной таблицы.

Важно: модель PersonData в связи one-to-one указывайте в виде строки.
"""
from django.db import models

class PersonData(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    passport = models.CharField(max_length=100, db_index=True, unique=True)


class Person(models.Model):
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data = models.OneToOneField('PersonData', blank=True, null=True, on_delete=models.SET_NULL)
