""" Упражнение 1
Подвиг 4. Объявите класс модели с именем Post следующей структуры:

id: primary key (в модели явно не прописывается);
slug: SlugField - slug поста, максимум 255 символов; уникальное, обязательное поле;
title: CharField - строка, максимум 200 символов; обязательное поле;
content: TextField - текст статьи; необязательное поле;
time_create: DateTimeField - время создания записи (заполняется автоматически);
time_update: DateTimeField - время последнего изменения записи (заполняется автоматически);
is_published: BooleanField - флаг отображения поста (True - отображается; False - не отображается); по умолчанию False.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models

# здесь объявляйте класс модели
class Post(models.Model):
    slug = models.SlugField(unique=True, max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


""" Упражнение 2
Подвиг 6. Пусть имеется следующий класс модели:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
И функция представления для отображения текущей записи по слагу:

def post_show_by_slug(request, ps_slug):
    post = # здесь прописывайте функцию get_object_or_404()
    return render(request, 'post/post.html', {'post': post})
Допишите функцию post_show_by_slug для выбора текущей записи поста модели Post по слагу ps_slug с помощью функции get_object_or_404(). Импортировать функции get_object_or_404() и render() не нужно!
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


def post_show_by_slug(request, ps_slug):
    post = get_object_or_404(Post, slug=ps_slug)
    return render(request, 'post/post.html', {'post': post})


""" Упражнение 3
Подвиг 7. Пусть имеется следующий класс модели:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
И функция представления для отображения текущей записи по идентификатору и слагу:

def post_show_by_slug(request, ps_pk, ps_slug):
    post = # здесь прописывайте функцию get_object_or_404()
    return render(request, 'post/post.html', {'post': post})
Допишите функцию post_show_by_slug для выбора текущей записи поста модели Post по идентификатору ps_pk и слагу ps_slug с помощью функции get_object_or_404(). Импортировать функции get_object_or_404() и render() не нужно!
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


def post_show_by_slug(request, ps_pk, ps_slug):
    post = get_object_or_404(Post, pk=ps_pk, slug=ps_slug)
    return render(request, 'post/post.html', {'post': post})
