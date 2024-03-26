""" Упражнение 1
Подвиг 2. Пусть имеется следующая модель:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

# здесь продолжайте программу
Объявите класс представления ListPost, унаследованного от класса ListView, со следующим функционалом:
через атрибуты класса:

шаблон для отображения статей: 'post/list.html';
модель для получения списка всех записей: Post;
переменная со списком выбранных записей из модели Post (для передачи в шаблон): posts;
дополнительные переменные для шаблона: {'title': "Список опубликованных статей"};
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

# здесь продолжайте программу
class ListPost(ListView):
    template_name = 'post/list.html'
    model = Post
    context_object_name = 'posts'
    extra_context = {'title': "Список опубликованных статей"}


""" Упражнение 2
Подвиг 3 (усложнение подвига 2). Пусть имеется следующая модель:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

# здесь продолжайте программу
Объявите класс представления ListPost, унаследованного от класса ListView, со следующим функционалом:

через атрибуты класса:

шаблон для отображения статей: 'post/list.html';
переменная со списком выбранных записей из модели Post (для передачи в шаблон): posts;
дополнительные переменные для шаблона: {'title': "Список опубликованных статей"};
через методы класса:

метод для выборки записей из модели Post, у которых значение поля is_published равно 1 (через стандартный менеджер записей).
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

# здесь продолжайте программу
class ListPost(ListView):
    template_name = 'post/list.html'
    context_object_name = 'posts'
    extra_context = {'title': "Список опубликованных статей"}
    
    def get_queryset(self):
        return Post.objects.filter(is_published=1)


""" Упражнение 3
Подвиг 4. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Имя')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст')
    job = models.CharField(max_length=255, verbose_name='Профессия')
    is_active = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Person

# здесь объявляйте класс PersonList
Объявите класс представления PersonList в разделе views.py, унаследованного от класса ListView, со следующим функционалом:
через атрибуты класса:

шаблон для отображения статей: 'person/list.html';
переменная со списком выбранных записей из модели Person (для передачи в шаблон): persons;
запрет на отображение страницы без записей (должно генерироваться исключение 404);
через методы класса:

метод формирования (для шаблона) переменной title со значением "Список персон";
метод для выборки записей: с помощью стандартного менеджера записей модели Person и метода filter выбрать все записи, у которых поле salary в пределах [11000; 32000] (включительно).
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

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Person

# здесь объявляйте класс PersonList
class PersonList(ListView):
    template_name = 'person/list.html'
    context_object_name = 'persons'
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs) | {'title': "Список персон"}
    
    def get_queryset(self):
        return Person.objects.filter(salary__gte=11000, salary__lte=32000)

        
""" Упражнение 4
Подвиг 5. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')


# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

# здесь объявляйте класс PostListCategory


# --------- urls.py ------------------------

from django.urls import path
# from .views import PostListCategory

urlpatterns = [
    path('category/<slug:cat_slug>/', PostListCategory.as_view(), name='category'),
]
Объявите класс представления PostListCategory в разделе views.py, унаследованного от класса ListView, со следующим функционалом:

через атрибуты класса:

шаблон для отображения статей: 'post/list.html';
переменная со списком выбранных записей из модели Post (для передачи в шаблон): cat_posts;
запрет на отображение страницы без записей (должно генерироваться исключение 404);
через методы класса:

метод формирования (для шаблона) переменной title со значением "Список постов по рубрике";
метод для выборки записей: с помощью стандартного менеджера записей модели Post и метода filter выбрать все посты, у которых поле slug модели Category равно параметру cat_slug URL-маршрута.
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')


# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

# здесь объявляйте класс PostListCategory
class PostListCategory(ListView):
    template_name = 'post/list.html'
    context_object_name = 'cat_posts'
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs) | {'title': 'Список постов по рубрике'}
    
    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'])
    
# --------- urls.py ------------------------

from django.urls import path
# from .views import PostListCategory

urlpatterns = [
    path('category/<slug:cat_slug>/', PostListCategory.as_view(), name='category'),
]
