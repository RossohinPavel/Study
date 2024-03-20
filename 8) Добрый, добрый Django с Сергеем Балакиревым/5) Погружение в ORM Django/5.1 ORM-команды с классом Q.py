""" Упражнение 1 
Подвиг 3. Пусть имеется следующий класс модели:

from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() и класса Q выберите все записи по критерию: is_active = 0 или salary < 10000.

P.S. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(Q(is_active=0) | Q(salary__lt=10000))


""" Упражнение 2
Подвиг 4. Пусть имеется следующий класс модели:

from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() выберите все записи по критерию: is_active = 1 и salary > 12000.

P.S. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(Q(is_active=1) & Q(salary__gt=12000))


""" Упражнение 3
Подвиг 5. Пусть имеется следующий класс модели:

from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() и класса Q выберите все записи по критерию: is_active = 1 или salary >= 10000 и salary <= 20000.

P.S. Помните о приоритетах операций. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(Q(is_active=1) | Q(salary__gte=10000) & Q(salary__lte=20000))


""" Упражнение 4
Подвиг 6. Пусть имеется следующий класс модели:

from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() и класса Q выберите все записи по критерию: job != 'junior' или salary >= 40000.

P.S. Помните о приоритетах операций. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(~Q(job='junior') | Q(salary__gte=40000))


""" Упражнение 5
Подвиг 7. Пусть имеется следующий класс модели:

from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Person, с помощью метода filter() и класса Q выберите все записи по критерию: job содержит фрагмент 'ra' (без учета регистра) или идентификатор записи pk не принадлежит значениям 3, 7, 11.

P.S. Помните о приоритетах операций. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


p_lst = Person.objects.filter(Q(job__icontains='ra') | ~Q(pk__in=[3, 7, 11]))
