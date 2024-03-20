""" Упражнение 1
Подвиг 2. Пусть в программе объявлена следующая модель:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Post, путем вызова одного из методов first/last (подумайте какого), выберите запись с наименьшим (самым ранним) временем создания (поле time_create).

P.S. На экран ничего выводить не нужно.
"""
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = Post.objects.last()


""" Упражнение 2
Подвиг 3. Пусть в программе объявлена следующая модель:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Post, путем вызова методов order_by() и first() выберите запись с наибольшим временем изменения (поле time_update).

P.S. На экран ничего выводить не нужно.
"""
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = Post.objects.order_by('-time_update').first()


""" Упражнение 3
Подвиг 4. Пусть в программе объявлена следующая модель:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Post, путем вызова одного из методов latest/earliest выберите запись с наибольшим временем создания (поле time_create).

P.S. На экран ничего выводить не нужно.
"""
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = Post.objects.latest('time_create')


""" Упражнение 4
Подвиг 5. Пусть в программе объявлена следующая модель:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Post, сформируйте сначала выборку всех записей с упорядочиванием по возрастанию поля slug (с помощью метода order_by), а затем, из полученного списка выберите запись с наименьшим временем изменения (поле time_update) с помощью одного из методов latest/earliest.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']


record = Post.objects.order_by('slug').earliest('time_update')


""" Упражнение 5
Подвиг 6. Пусть в программе объявлена следующая модель:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Post, выберите из таблицы записи по критерию: is_published = 0. Определите наличие хотя бы одной записи в полученной выборке. На выходе нужно получить значение True, если записи есть, и False в противном случае.

P.S. Все нужно записать в виде одной команды (строчки). На экран ничего выводить не нужно.
"""
from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = Post.objects.filter(is_published=0).exists()


""" Упражнение 6
Подвиг 7. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Q

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Post, метод filter() и класс Q, выберите из таблицы записи по критерию: slug содержит фрагмент 'django' или фрагмент 'python' (без учета регистра). Определите число записей в полученной выборке.

P.S. Все нужно записать в виде одной команды (строчки). Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = Post.objects.filter(Q(slug__icontains='django') | Q(slug__icontains='python')).count()


""" Упражнение 7
 Подвиг 8. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Q

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = # здесь продолжайте команду
Используя стандартный менеджер записей (objects) модели Post, метод filter() и класс Q, выберите из таблицы записи по критерию: slug содержит фрагмент 'django' и title содержит фрагмент 'django' (оба без учета регистра). Определите наличие хотя бы одной записи в полученной выборке. На выходе нужно получить значение True, если записи есть, и False в противном случае.

P.S. Все нужно записать в виде одной команды (строчки). Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


result = Post.objects.filter(Q(slug__icontains='django') & Q(title__icontains='django')).exists()
