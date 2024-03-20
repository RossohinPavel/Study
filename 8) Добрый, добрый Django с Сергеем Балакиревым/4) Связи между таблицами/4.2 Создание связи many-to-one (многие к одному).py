""" Упражнение 1
Подвиг 2. Пусть дан класс первичной модели Category:

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)
и вторичной модели Post:

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cat = # здесь определяйте связь many-to-one с моделью Category
Пропишите в модели Post для атрибута cat связь типа Many To One с моделью Category так, чтобы из Category нельзя было удалять записи, используемые в модели Post.

P.S. Первичную модель Category при определении атрибута cat укажите в виде строки "Category".
"""
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)


""" Упражнение 2
Подвиг 3. Пусть дан класс первичной модели Category:

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)
и вторичной модели Post:

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cat = # здесь определяйте связь many-to-one с моделью Category
Пропишите в модели Post для атрибута cat связь типа Many To One с моделью Category так, чтобы при удалении записи из Category удалялись все связанные записи из Post.
P.S. Первичную модель Category при определении атрибута cat укажите в виде строки "Category".
"""
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
