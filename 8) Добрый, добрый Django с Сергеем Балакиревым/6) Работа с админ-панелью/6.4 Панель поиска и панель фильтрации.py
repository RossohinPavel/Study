""" Упражнение 1
Подвиг 2. Пусть имеется следующий фрагмент программы:

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

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'volume_lect', 'volume_lab']
    # здесь продолжайте программу
Добавьте в класс SubjectAdmin атрибуты для следующих настроек в админ-панели:

редактируемые поля: volume_lect, volume_lab;
кликабельные поля: name;
упорядочивание: по убыванию поля volume_lect;
поиск (через панель поиска админки): по полю name.
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

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'volume_lect', 'volume_lab']
    # здесь продолжайте программу
    list_editable = ('volume_lect', 'volume_lab')
    list_display_links = ('name', )
    ordering = ('-volume_lect', )
    search_fields = ['name']


""" Упражнение 2
Подвиг 3. Пусть имеется следующий фрагмент программы:

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

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'volume_lect', 'volume_lab']
    # здесь продолжайте программу
Добавьте в класс SubjectAdmin атрибуты для следующих настроек в админ-панели:

кликабельные поля: name, slug;
упорядочивание: по возрастанию поля volume_lab;
регистрозависимый поиск (через панель поиска админки): по окончанию поля name и по началу поля slug.
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

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'volume_lect', 'volume_lab']
    # здесь продолжайте программу
    list_display_links = ('name', 'slug')
    ordering = ('volume_lab', )
    search_fields = ['name__endswith', 'slug__startswith']


""" Упражнение 3
Подвиг 4. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Category, Post

# здесь продолжайте программу
Необходимо зарегистрировать для админ-панели модель Post и во вспомогательном классе PostAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: title, slug, cat;
кликабельные поля: title;
поиск (через панель поиска админки): по полю title и по полю name связанной модели Category;
фильтрация записей: по полям is_published и name связанной модели Category.
Дополнительно в модели Post для полей title, slug, cat прописать отображаемые в админ-панели соответствующие названия:

"Заголовок", "Слаг", "Категория"

P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Category, Post

# здесь продолжайте программу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'cat')
    list_display_links = ('title', )
    search_fields = ('title', 'cat__name')
    list_filter = ('is_published', 'cat__name')


""" Упражнение 4
Подвиг 5. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Post


class ContentFilter(admin.SimpleListFilter):
    # здесь прописывайте атрибуты title и parameter_name

    def lookups(self, request, model_admin):
        # здесь продолжайте метод lookups

    def queryset(self, request, queryset):
        # здесь продолжайте метод queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published']
    list_display_links = ['title']
    list_filter = ['is_published', ContentFilter]
Необходимо дописать класс ContentFilter, который бы определял фильтрацию постов по объему их контента (поле content) в соответствии со следующими критериями (для отбора записей используйте метод annotate для формирования вычисляемого поля с именем length и последующим вызовом метода filter):

Короткие статьи: content < 1000 символов;
Средние статьи: 1000 <= content < 5000 символов;
Большие статьи: content >= 5000 символов.
Названия пунктов в фильтре: "Короткие статьи", "Средние статьи", "Большие статьи". Названия параметров соответственно:

short, middle, long.

Атрибуты title и parameter_name класса ContentFilter определить следующими:

title = "Сортировка по статьям"
parameter_name = 'status'
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
from django.db.models.functions import Length
# импорт from .models import Post


class ContentFilter(admin.SimpleListFilter):
    # здесь прописывайте атрибуты title и parameter_name
    title = "Сортировка по статьям"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        # здесь продолжайте метод lookups
        return [('short', 'Короткие статьи'), ('middle', 'Средние статьи'), ('long', 'Большие статьи')]

    def queryset(self, request, queryset):
        # здесь продолжайте метод queryset
        queryset = queryset.annotate(length=Length('content'))
        
        kwarg = {}
        match self.value():
            case 'short': kwarg['length__lt'] = 1000
            case 'long': kwarg['length__gte'] = 5000
            case 'middle': kwarg.update({'length__gte': 1000, 'length__lt': 5000})
        
        return queryset.filter(**kwarg)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published']
    list_display_links = ['title']
    list_filter = ['is_published', ContentFilter]

    
""" Упражнение 5
Подвиг 6 (на повторение). Пусть в программе объявлена следующая модель:

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


result = # здесь продолжайте команду
