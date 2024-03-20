""" Упражнение 1
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


""" Упражнение 2
 Подвиг 5 (на повторение). Пусть имеется следующий класс модели:

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
