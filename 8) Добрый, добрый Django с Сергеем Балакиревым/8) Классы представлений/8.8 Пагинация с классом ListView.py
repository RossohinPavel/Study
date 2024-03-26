""" Упражнение 1
Подвиг 3. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.urls import reverse
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.urls import reverse_lazy
from django.views.generic import ListView
# from .models import Person

def show_persons(request):
    data = {
        'title': 'Список персон',
        'p_list': Person.objects.all(),
    }

    return render(request, 'users/persons.html', context=data)
Замените функцию show_persons эквивалентным классом представления ShowPersons, унаследованным от базового класса ListView, со следующим функционалом (через атрибуты класса):

шаблон: 'users/persons.html';
модель: Person;
переменная со списком записей (в шаблоне): p_list;
дополнительные переменные: {'title': 'Список персон'};
пагинация: разбиение по 3 записи на страницу.
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

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Person

# здесь объявляйте класс представления
class ShowPersons(ListView):
    template_name = 'users/persons.html'
    model = Person
    context_object_name = 'p_list'
    extra_context = {'title': 'Список персон'}
    paginate_by = 3

 
""" Упражнение 2
Подвиг 4. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

def post_list(request):
    data = {
        'title': 'Список статей',
        'p_list': Post.objects.filter(is_published=1),
    }

    return render(request, 'post/listpost.html', context=data)
Замените функцию post_list эквивалентным классом представления PostList, унаследованным от базового класса ListView, со следующим функционалом:

через атрибуты класса:

шаблон: 'post/listpost.html';
переменная со списком записей (в шаблоне): p_list;
дополнительные переменные: {'title': 'Список статей'};
пагинация: разбиение по 3 записи на страницу;
через методы класса:

get_queryset: выборка записей через модель Post с полем is_published=1 (используя стандартный менеджер записей модели).
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

# --------- views.py ------------------------
from django.views.generic import ListView
# from .models import Post

# здесь объявляйте класс представления
class PostList(ListView):
    template_name = 'post/listpost.html'
    context_object_name = 'p_list'
    extra_context = {'title': 'Список статей'}
    paginate_by = 3
    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter( is_published=1)
