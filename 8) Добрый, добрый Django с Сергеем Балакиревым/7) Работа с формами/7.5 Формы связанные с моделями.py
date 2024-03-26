""" Упражнение 1
Подвиг 1. Пусть в программе объявлена следующая модель:

# ---------------- models.py -------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


# ---------------- forms.py -------------------------
from django import forms
# from .models import Post

# здесь продолжайте программу
Объявите класс формы PostForm, связанной с моделью Post, с отображением следующих полей:

title, slug, is_published, content

Порядок отображения полей в форме должен быть именно таким.

P.S. На экран ничего выводить не нужно.
"""
# ---------------- models.py -------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


# ---------------- forms.py -------------------------
from django import forms
# from .models import Post

# здесь продолжайте программу
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'is_published', 'content')


""" Упражнение 2
Подвиг 2. Пусть в программе объявлена следующая модель:

# ---------------- models.py -------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


# ---------------- forms.py -------------------------
from django import forms
# from .models import Person

# здесь продолжайте программу
Объявите класс формы PersonForm, связанной с моделью Person и следующими свойствами, прописанными во вложенном классе Meta:

отображаемые поля (с сохранением порядка): full_name, salary, job;
поля full_name и job должны иметь CSS-стили attrs={'class': 'form-input'};
названия полей в HTML-форме: full_name -> "Полное имя"; salary -> "Зарплата"; job -> "Профессия".
P.S. На экран ничего выводить не нужно.
"""
# ---------------- models.py -------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


# ---------------- forms.py -------------------------
from django import forms
# from .models import Person

# здесь продолжайте программу
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('full_name', 'salary', 'job')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'job': forms.TextInput(attrs={'class': 'form-input'})
        }
        labels = {'full_name': "Полное имя", 'salary': "Зарплата", 'job': "Профессия"}


""" Упражнение 3
Подвиг 3. Пусть в программе объявлены следующие модели:

# ---------------- models.py -------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    descr = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')

# ---------------- forms.py -------------------------
from django import forms
# from .models import Subject, Category

# здесь продолжайте программу
Объявите класс формы SubjectForm, связанной с моделью Subject и следующими свойствами:

отображаемые поля (с сохранением порядка): title, slug, descr, cat; прописывается во вложенном классе Meta;
поля title и slug должны иметь CSS-стили attrs={'class': 'form-input'}; прописывается во вложенном классе Meta;
поле descr должно иметь CSS-стили attrs={'cols': 50, 'rows': 5} и быть необязательным; прописывается в форме SubjectForm, как объект класса соответствующего поля;
поле cat должно наполняться всеми записями из модели Category; не выбранный пункт должен называться "Выберите категорию"; прописывается в форме SubjectForm, как объект класса соответствующего поля.
P.S. На экран ничего выводить не нужно.
"""
# ---------------- models.py -------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    descr = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')

# ---------------- forms.py -------------------------
from django import forms
# from .models import Subject, Category

# здесь продолжайте программу
class SubjectForm(forms.ModelForm):
    descr = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    cat = forms.ModelChoiceField(queryset=Category.objects, empty_label='Выберите категорию')

    class Meta:
        model = Subject
        fields = ('title', 'slug', 'descr', 'cat')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
        }


""" Упражнение 4
Подвиг 4. Пусть в программе объявлена модель и форма для нее:

# ---------------- models.py -------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

# ---------------- forms.py -------------------------
from django import forms
# from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

# ---------------- views.py -------------------------
# from django.shortcuts import render
# from .models import Category
# from .forms import CategoryForm

# здесь продолжайте программу
Объявите в программе функцию представления с именем add_category и пропишите в ней следующий функционал:

для метода передачи данных GET представление должно создавать пустую форму CategoryForm и с помощью функции render формируется HTML-документ по шаблону 'subject/addcategory.html' с передачей в него объекта формы CategoryForm через переменную (ключ) form;
при получении POST-запроса создать заполненную форму CategoryForm (из принятых данных), проверить корректность заполнения формы стандартным методом формы и для корректных данных выполнить сохранение данных формы в БД (с помощью соответствующего метода формы); после сохранения данных возвратить объект формы.
P.S. На экран ничего выводить не нужно.
"""
# ---------------- models.py -------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

# ---------------- forms.py -------------------------
from django import forms
# from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

# ---------------- views.py -------------------------
# from django.shortcuts import render
# from .models import Category
# from .forms import CategoryForm

# здесь продолжайте программу
def add_category(request):
    if request.method == 'GET':
        return render(request, 'subject/addcategory.html', {'form': CategoryForm()})
                      
    if request.method == 'POST': 
        f = CategoryForm(request.POST)
        if f.is_valid():
            f.save()
            return f

            
""" Упражнение 5
Подвиг 5. Пусть в программе объявлена следующая модель:

# ---------------- models.py -------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    salary = models.PositiveIntegerField(default=0, verbose_name="Зарплата")
    age = models.PositiveIntegerField(default=0, verbose_name="Возраст")
    job = models.CharField(max_length=255, verbose_name="Профессия")
    is_active = models.BooleanField(default=True, verbose_name="Статус")

# ---------------- forms.py -------------------------
from django import forms
# from .models import Person

# здесь продолжайте программу
Объявите класс формы AddPersonForm, связанной с моделью Person со следующими свойствами, прописанными во вложенном классе Meta:

отображаемые поля (с сохранением порядка): full_name, age, job;
поля full_name, age и job должны иметь CSS-стили attrs={'class': 'form-input'}.
Добавить в класс AddPersonForm метод с именем:

clean_<проверяемое поле>

для проверки, что введенный возраст age меньше 65. Если проверка не проходит, то генерировать исключение:

raise ValidationError("Слишком большой возраст.")
Иначе, метод должен возвращать значение age.

P.S. На экран ничего выводить не нужно.
"""
# ---------------- models.py -------------------------
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    salary = models.PositiveIntegerField(default=0, verbose_name="Зарплата")
    age = models.PositiveIntegerField(default=0, verbose_name="Возраст")
    job = models.CharField(max_length=255, verbose_name="Профессия")
    is_active = models.BooleanField(default=True, verbose_name="Статус")

# ---------------- forms.py -------------------------
from django import forms
from django.core.exceptions import ValidationError
# from .models import Person

# здесь продолжайте программу
class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('full_name', 'age', 'job')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'age': forms.TextInput(attrs={'class': 'form-input'}),
            'job': forms.TextInput(attrs={'class': 'form-input'}),
        }
    
    def clean_age(self):
        age = self.cleaned_data['age']
        if age >= 65:
            raise ValidationError("Слишком большой возраст.")
        
        return age
