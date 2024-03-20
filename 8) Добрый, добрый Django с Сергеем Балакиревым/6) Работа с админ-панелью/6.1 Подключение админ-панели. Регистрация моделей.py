""" Упражнение 1
Подвиг 3. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Women

# здесь пишите команду
Используя декоратор admin.site.register, зарегистрируйте модель Women в админ-панели фреймворка Django.

P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Women

# здесь пишите команду
admin.site.register(Women)


""" Упражнение 2
Подвиг 4. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

    # здесь продолжайте программу


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
Объявите в модели Subject вложенный класс Meta, в котором определите названия для единственного и множественного числа модели Subject в виде следующих строк:

"Предмет" - ед. ч.;
"Предметы" - мн. ч.

С помощью декоратора admin.site.register зарегистрируйте модель Subject для админ-панели. 

P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

    # здесь продолжайте программу
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
admin.site.register(Subject)


""" Упражнение 3 
Подвиг 6 (на повторение). Объявите класс модели с именем User для работы с таблицей следующей структуры:

id: primary key (в модели не прописывается);
slug: слаг; максимальная длина 255 символов, уникальное поле, обязательное поле;
username: CharField - текстовое поле, максимальная длина 100 символов, уникальное поле, обязательное поле;
password: CharField - текстовое поле, максимальная длина 100 символов, не уникальное поле, обязательное поле;
email: E-mail (поле для адреса электронной почты), необязательное поле;
is_staff: булево поле, начальное значение False.
"""
from django.db import models

# здесь объявляйте класс модели
class User(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    username =  models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
