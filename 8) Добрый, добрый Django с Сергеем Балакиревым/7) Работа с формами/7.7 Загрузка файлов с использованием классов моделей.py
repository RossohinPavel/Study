""" Упражнение 1
Подвиг 2. Объявите класс модели Profile со следующими атрибутами:

full_name: текстовое поле, максимальное число символов 200, обязательное, название "Имя";
email: поле хранения E-mail-адреса, необязательное, название "E-mail";
photo: поле хранения загружаемого изображения, необязательное, подкаталог загрузки "profile", название "Аватар".

P.S. На экран ничего выводить не нужно.
"""
from django.db import models

# здесь объявляйте класс модели
class Profile(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    photo = models.ImageField(blank=True, verbose_name='Аватар', upload_to="profile/")


""" Упражнение 2
Подвиг 3. Пусть в программе объявлена следующая модель:

# --------------- models.py ---------------------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name="Изображение")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

# --------------- forms.py ---------------------------------------
from django import forms
#from .models import Post

# здесь продолжайте программу
Необходимо объявить класс формы PostForm, связанной с моделью Post, со следующими свойствами, прописанными во вложенном классе Meta:

отображаемые поля: title, slug, photo, content;
CSS-стили attrs={'class': 'form-input'} для полей title, slug;
CSS-стили attrs={'cols': 50, 'rows': 5} для поля content.
P.S. На экран ничего выводить не нужно.
"""
# --------------- models.py ---------------------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name="Изображение")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

# --------------- forms.py ---------------------------------------
from django import forms
#from .models import Post

# здесь продолжайте программу
class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'photo', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

        
""" Упражнение 3
Подвиг 4. Пусть имеется следующий фрагмент программы:

# --------------- models.py ---------------------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name='Изображение')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------------- forms.py ---------------------------------------
from django import forms
#from .models import Lector

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['fio', 'slug', 'photo', 'salary']

# --------------- views.py ---------------------------------------
# from django.shortcuts import render, redirect
# from .forms import LectorForm

# здесь определяйте функцию представления
Необходимо объявить функцию представления add_lector со следующим функционалом:

при GET-запросе должна создаваться пустая форма LectorForm и с помощью функции render формироваться HTML-документ по шаблону 'profile/add_lector.html' с передачей в него объекта формы LectorForm через переменную (ключ) form;
при POST-запросе должна формироваться заполненная форма LectorForm, затем, выполняться проверка корректности переданных данных методом is_valid, при успешной проверке данные формы сохраняются в БД и выполняется редирект на главную страницу с помощью команды:
return redirect('/')
P.S. На экран ничего выводить не нужно.
"""
# --------------- models.py ---------------------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name='Изображение')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------------- forms.py ---------------------------------------
from django import forms
#from .models import Lector

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['fio', 'slug', 'photo', 'salary']

# --------------- views.py ---------------------------------------
# from django.shortcuts import render, redirect
# from .forms import LectorForm

# здесь определяйте функцию представления
def add_lector(r):
    if r.method == 'GET':
        return render(r, 'profile/add_lector.html', {'form': LectorForm()})
    if r.method == 'POST':
        f = LectorForm(r.POST, r.FILES)
        if f.is_valid():
            f.save()
            return redirect('/')
