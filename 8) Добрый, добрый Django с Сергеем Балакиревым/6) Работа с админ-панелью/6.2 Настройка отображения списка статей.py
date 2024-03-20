""" Упражнение 1
Подвиг 2. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
С помощью декоратора admin.register зарегистрируйте модель Subject для админ-панели и примените его к новому классу SubjectAdmin. В этом классе определите порядок сортировки отображаемых в админ-панели записей по убыванию поля volume.

P.S. Не забудьте унаследовать класс SubjectAdmin от класса admin.ModelAdmin. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ordering = ('-volume', )


""" Упражнение 2
Подвиг 3. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
Необходимо дополнить модель Subject так, чтобы поля slug, name, volume в админ-панели отображались с соответствующими именами:

Слаг; Название; Объем

Затем, зарегистрируйте эту модель в админ-панели с помощью декоратора admin.site.register.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    name = models.CharField(max_length=255, verbose_name='Название')
    volume = models.PositiveIntegerField(default=0, verbose_name='Объем')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Subject

# здесь продолжайте программу
admin.site.register(Subject)


""" Упражнение 3
Подвиг 4. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Person

# здесь продолжайте программу
С помощью декоратора admin.register зарегистрируйте модель Person для админ-панели и примените его к новому классу PersonAdmin, унаследованного от базового класса admin.ModelAdmin. В классе PersonAdmin определите:

отображаемые поля: full_name, salary, job;
редактируемые поля: salary;
кликабельные поля: full_name.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
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
    list_display = ('full_name', 'salary', 'job')
    list_display_links = ('full_name', )
    list_editable = ('salary', )


""" Упражнение 4
Подвиг 5. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Person

# здесь продолжайте программу
С помощью декоратора admin.register зарегистрируйте модель Person для админ-панели и примените его к новому классу PersonAdmin, унаследованного от базового класса admin.ModelAdmin. В классе PersonAdmin определите:

отображаемые поля: full_name, job, age;
кликабельные поля: full_name, job;
порядок сортировки записей по убыванию поля salary;
максимальное число отображаемых записей на странице 10.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
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
    list_display = ('full_name', 'job', 'age')
    list_display_links = ('full_name', 'job')
    ordering = ('-salary', )
    list_per_page = 10

    
""" Упражнение 5
Подвиг 6. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Person

# здесь продолжайте программу
С помощью декоратора admin.register зарегистрируйте модель Person для админ-панели и примените его к новому классу PersonAdmin, унаследованного от базового класса admin.ModelAdmin. В классе PersonAdmin определите:

отображаемые поля: full_name, salary, is_active;
редактируемые поля: salary, is_active;
порядок сортировки записей по возрастанию поля salary и убыванию поля age.
Дополните модель Person так, чтобы поля full_name, salary, is_active в админ-панели отображались с соответствующими именами:

Имя сотрудника; Зарплата; Работающий

P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя сотрудника')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    age = models.PositiveIntegerField(default=0, )
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, verbose_name='Работающий')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Person

# здесь продолжайте программу
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'salary', 'is_active')
    list_editable = ('salary', 'is_active')
    ordering = ('salary', '-age')
