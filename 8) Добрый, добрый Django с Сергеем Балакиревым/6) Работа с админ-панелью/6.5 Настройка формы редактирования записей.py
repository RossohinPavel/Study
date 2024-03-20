""" Упражнение 1
Подвиг 2. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст')
    job = models.CharField(max_length=255, verbose_name='Профессия')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Person

# здесь продолжайте программу
Необходимо зарегистрировать для админ-панели модель Person и во вспомогательном классе PersonAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: full_name, salary, age, job;
редактируемые поля: salary, job;
кликабельные поля: full_name;
поля при редактировании записи: full_name, salary, age, job, is_active;
поля "только для просмотра" при редактировании записи: full_name.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст')
    job = models.CharField(max_length=255, verbose_name='Профессия')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Person

# здесь продолжайте программу
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'salary', 'age', 'job')
    list_editable = ('salary', 'job')
    list_display_links = ('full_name', )
    fields = ('full_name', 'salary', 'age', 'job', 'is_active')
    readonly_fields = ('full_name', )


""" Упражнение 2
Подвиг 3. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Lector

# здесь продолжайте программу
Необходимо зарегистрировать для админ-панели модель Lector и во вспомогательном классе LectorAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: fio, slug, salary;
редактируемые поля: salary;
кликабельные поля: fio, slug;
поля исключенные при редактировании записи: fio;
поля "только для просмотра" при редактировании записи: slug, salary.
поиск (через панель поиска админки): по полю salary и с начала поля slug.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Lector

# здесь продолжайте программу
@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ('fio', 'slug', 'salary')
    list_editable = ('salary', )
    list_display_links = ('fio', 'slug')
    exclude = ('fio', )
    readonly_fields = ('slug', 'salary')
    search_fields = ('salary', 'slug__startswith')


""" Упражнение 3
Подвиг 4. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    name = models.CharField(max_length=255, verbose_name='Название')
    volume_lect = models.PositiveIntegerField(default=0, verbose_name='Объем лекций')
    volume_lab = models.PositiveIntegerField(default=0, verbose_name='Объем лабораторных')


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
Необходимо прописать в модели Subject вложенный класс Meta с атрибутами для формирования названия модели в админ-панели в единственном и множественном числах со следующими строками:

ед. ч.: "Предмет";
мн. ч.: "Предметы".
После этого зарегистрировать для админ-панели модель Subject и во вспомогательном классе SubjectAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: name, slug, volume_lect, volume_lab;
поля при редактировании записи: name, slug, volume_lect, volume_lab;
используя атрибут prepopulated_fields, настроить автозаполнение поля slug по полю name.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    name = models.CharField(max_length=255, verbose_name='Название')
    volume_lect = models.PositiveIntegerField(default=0, verbose_name='Объем лекций')
    volume_lab = models.PositiveIntegerField(default=0, verbose_name='Объем лабораторных')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        
        
# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'volume_lect', 'volume_lab')
    fields = ('name', 'slug', 'volume_lect', 'volume_lab')
    prepopulated_fields = {'slug': ('name', )}


""" Упражнение 4
Подвиг 5. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')
    grad = models.CharField(max_length=255, verbose_name='Должность')

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Lector

# здесь продолжайте программу
Необходимо зарегистрировать для админ-панели модель Lector и во вспомогательном классе LectorAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: fio, slug, salary, grad;
редактируемые поля: salary, grad;
поля исключенные при редактировании записи: is_work;
поля "только для просмотра" при редактировании записи: grad;
используя атрибут prepopulated_fields, настроить автозаполнение поля slug по полю fio;
поиск (через панель поиска админки): с конца поля fio и с начала поля slug;
фильтрация записей: по полям is_work и grad.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')
    grad = models.CharField(max_length=255, verbose_name='Должность')

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Lector

# здесь продолжайте программу
@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ('fio', 'slug', 'salary', 'grad')
    list_editable = ('salary', 'grad')
    exclude = ('is_work', )
    readonly_fields = ('grad', )
    prepopulated_fields = {'slug': ('fio', )}
    search_fields = ('fio__endswith', 'slug__startswith')
    list_filter = ('is_work', 'grad')

    
""" Упражнение 5
Подвиг 6 (на повторение). Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Subject и метод aggregate(), вычислите среднее значение цены (price) предметов. На выходе должен формироваться словарь с ключом 'subject_avg' и соответствующим значением.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.aggregate(subject_avg=Avg('price'))
