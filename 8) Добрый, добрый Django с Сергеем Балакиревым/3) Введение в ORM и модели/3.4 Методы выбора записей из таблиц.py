""" Упражнение 1
Подвиг 1. Пусть имеется следующий класс модели:

	from django.db import models

	class Person(models.Model):
	    full_name = models.CharField(max_length=255)
	    salary = models.PositiveIntegerField(default=0)
	    job = models.CharField(max_length=255)

Добавьте с помощью этого класса в таблицу новую запись с параметрами:

	full_name="Сергей Балакирев"
	salary=4321
	job="Создатель"

Сделать это следует с помощью вызова метода create менеджера записей класса Person.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


# здесь продолжайте программу
Person.objects.create(full_name="Сергей Балакирев", salary=4321, job="Создатель")


""" Упражнение 2
Подвиг 2. Пусть имеется следующий класс модели:

from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
Добавьте с помощью этого класса в таблицу две записи с параметрами:

title="Курс по Django 4"
content="Полный базовый курс по Django 4"
и
title="Добрый, добрый Django 4"
content="Курс по Django 4 на Stepik"
Сделать это следует с помощью вызова метода create менеджера записей класса CourseItem.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# здесь продолжайте программу
for record in (
    {'title': "Курс по Django 4", 'content': "Полный базовый курс по Django 4"},
    {'title': "Добрый, добрый Django 4", 'content': "Курс по Django 4 на Stepik"}
):
    CourseItem.objects.create(**record)


""" Упражнение 3
Подвиг 3. Объявите класс модели с именем ShopItem для работы с таблицей следующей структуры:

id: primary key (в модели не прописывается)
name: CharField - строка с максимальной длиной 100 символов; обязательное поле;
weight: IntegerField - вес товара с начальным значением 0; не обязательное поле;
price: IntegerField - цена товара с начальным значением 0; обязательное поле;
is_exists: BooleanField - наличие товара (True - присутствует; False - отсутствует); по умолчанию True.

Используя метод all() стандартного менеджера записей класса ShopItem, выберите все записи из соответствующей таблицы БД и сохраните их в переменной records.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

# здесь продолжайте программу
class ShopItem(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(blank=True, default=0)
    price = models.IntegerField(default=0)
    is_exists = models.BooleanField(default=True)


records = ShopItem.objects.all()


""" Упражнение 4
Подвиг 4. Объявите класс модели с именем Auto для работы с таблицей следующей структуры:

id: primary key (в модели не прописывается)
name: CharField - строка с максимальной длиной 100 символов; обязательное поле;
model: CharField - марка машины; обязательное поле;
price: IntegerField - цена машины с начальным значением 0; необязательное поле;
is_exists: BooleanField - наличие товара (True - присутствует; False - отсутствует); по умолчанию True.

С помощью класса Auto добавьте в БД следующие машины в порядке их перечисления:

name="BMW X6"; model="BMW"; price=6000111;
name="Toyota Corolla"; model="Toyota";
name="Haval 7"; model="Haval"; price=3500222;

Используя метод all() стандартного менеджера записей класса Auto выберите первую запись из соответствующей таблицы БД. Результат сохраните в переменной autos.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

# здесь продолжайте программу
class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField()
    price = models.IntegerField(blank=True, default=0)
    is_exists = models.BooleanField(default=True)


tpl = (
    'name="BMW X6", model="BMW", price=6000111',
    'name="Toyota Corolla", model="Toyota"',
    'name="Haval 7", model="Haval", price=3500222'
)
for line in tpl:
    eval(f'Auto({line})')

autos = Auto.objects.all()[0]


""" Упражнение 5
Подвиг 5. Объявите класс модели с именем Auto для работы с таблицей следующей структуры:

id: primary key (в модели не прописывается)
name: CharField - строка с максимальной длиной 100 символов; обязательное поле;
model: CharField - марка машины; обязательное поле;
price: IntegerField - цена машины с начальным значением 0; необязательное поле;
distance: IntegerField - пробег машины с начальным значением 0; необязательное поле;
is_exists: BooleanField - наличие товара (True - присутствует; False - отсутствует); по умолчанию True.

С помощью класса Auto добавьте в БД следующие машины в порядке их перечисления:

name="BMW X6"; model="BMW"; price=6000111;
name="Toyota Corolla"; model="Toyota"; distance=72000;
name="Haval 7"; model="Haval"; price=3500222;

Используя метод all() стандартного менеджера записей класса Auto выберите первые две записи из соответствующей таблицы БД. Результат сохраните в переменной autos.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

# здесь продолжайте программу
class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField()
    price = models.IntegerField(blank=True, default=0)
    distance = models.IntegerField(blank=True, default=0)
    is_exists = models.BooleanField(default=True)


tpl = (
    'name="BMW X6", model="BMW", price=6000111',
    'name="Toyota Corolla", model="Toyota", distance=72000',
    'name="Haval 7", model="Haval", price=3500222'
)
for m in tpl:
    eval(f'Auto({m})')

autos = Auto.objects.all()[:2]


""" Упражнение 6
Подвиг 6. Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
Используя метод filter() стандартного менеджера записей класса Person, выберите все записи с параметром job равным "Программист".
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


# здесь продолжайте программу
Person.objects.filter(job='Программист')


""" Упражнение 7
Подвиг 7. Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
Используя метод filter() стандартного менеджера записей класса Person, выберите все записи с параметром salary строго меньше 20000.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


# здесь продолжайте программу
Person.objects.filter(salary__lt=20000)


""" Упражнение 8
Подвиг 8. Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
Используя метод filter() стандартного менеджера записей класса Person, выберите все записи с параметром salary лежащем в диапазоне [12000; 15000].
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


# здесь продолжайте программу
Person.objects.filter(salary__gte=12000, salary__lte=15000)


""" Упражнение 9
Подвиг 9. Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
Используя метод filter() стандартного менеджера записей класса Person, выберите все записи с параметром pk равным 5.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


# здесь продолжайте программу
Person.objects.filter(pk=5)


""" Упражнение 10
Подвиг 10. Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
Используя метод get() стандартного менеджера записей класса Person, выберите запись с параметром pk равным 3.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


# здесь продолжайте программу
Person.objects.get(pk=3)
