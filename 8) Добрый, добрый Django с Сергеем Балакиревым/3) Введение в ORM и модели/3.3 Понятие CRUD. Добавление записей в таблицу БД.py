""" Упражнение 1
Подвиг 3. Объявите класс модели с именем Profile для работы с таблицей следующей структуры:
id: primary key (в модели не прописывается)
first_name: CharField - строка с максимальной длиной 100 символов; не обязательное поле;
last_name: CharField - строка с максимальной длиной 150 символов; не обязательное поле;
birth_day: DateTimeField - дата рождения; не обязательное поле;
is_banned: BooleanField - флаг бана профайла (True - забанен; False - активен); по умолчанию False.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

# здесь объявляйте класс модели
class Profile(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    birth_day = models.DateTimeField(blank=True)
    is_banned = models.BooleanField(default=False)


""" Упражнение 2
Подвиг 4. Пусть имеется следующий класс модели:
from django.db import models

class ShopItem(models.Model):
    name = models.CharField(max_length=255)
    descr = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_exists = models.BooleanField(default=True)
Добавьте с помощью этого класса в таблицу новую запись товара с параметрами:

name="Добрый, добрый Django 4"
descr="Лучший курс по Django 4"

путем создания экземпляра класса ShopItem с последующим вызовом нужного метода.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class ShopItem(models.Model):
    name = models.CharField(max_length=255)
    descr = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_exists = models.BooleanField(default=True)

# здесь продолжайте программу
new_item = ShopItem(name="Добрый, добрый Django 4", descr="Лучший курс по Django 4")
new_item.save()
