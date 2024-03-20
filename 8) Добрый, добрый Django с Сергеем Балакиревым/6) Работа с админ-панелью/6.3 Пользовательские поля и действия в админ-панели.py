""" Упражнение 1
Подвиг 2. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Post

# здесь продолжайте программу
Необходимо зарегистрировать для админ-панели модель Post и во вспомогательном классе PostAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: title, slug, is_published, + поля методов;
кликабельные поля: title.
Затем, добавить пользовательское вычисляемое поле путем объявления в классе PostAdmin метода:

def info_post(self, post: Post): ...
Который должен возвращать число слов в заголовке title в виде фразы:

"Заголовок содержит <число> слов"

(Полагается, что слова разделяются пробелом.)

Добавьте поле созданного метода info_post для отображения в админ-панели. Декорируйте метод info_post, чтобы в админ-панели это поле имело название "О заголовке".

P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Post

# здесь продолжайте программу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'info_post')
    list_display_links = ('title', )
    
    @admin.display(description='О заголовке')
    def info_post(self, post: Post):
        return f'Заголовок содержит {post.title.count(" ") + 1} слов'


""" Упражнение 2
Подвиг 3. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_update']


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Post

# здесь продолжайте программу
Необходимо зарегистрировать для админ-панели модель Post и во вспомогательном классе PostAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: title, slug, time_update, is_published, + поля методов;
кликабельные поля: slug;
максимальное число записей на страницу: 10;
сортировка: по возрастанию поля time_create.
Затем, добавить два новых пользовательских поля путем объявления в класс PostAdmin следующих методов:

def info_slug(self, post: Post): ...
def info_post(self, post: Post): ...
Эти методы должны возвращать соответствующие строки:

info_slug: "Слаг содержит <число> символов";
info_post: "Пост содержит <число> символов";
(Здесь вместо фрагмента <число> следует подставлять соответствующие вычисленные значения длин строк из полей slug и content.)

Добавьте эти новые пользовательские поля для отображения в админ-панель. Декорируйте их так, чтобы в админ-панели они имели соответственно названия:

info_slug: "О слаге";
info_post: "О посте".
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_update']


# --------- admin.py ------------------------
from django.contrib import admin
# импорт from .models import Post

# здесь продолжайте программу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'time_update', 'is_published', 'info_slug', 'info_post')
    list_display_links = ('slug', )
    list_per_page = 10
    ordering = ('time_create', )
    
    @admin.display(description='О слаге')
    def info_slug(self, post: Post):
        return f'Слаг содержит {len(post.slug)} символов'
    
    @admin.display(description='О посте')
    def info_post(self, post: Post):
        return f'Пост содержит {len(post.content)} символов'


""" Упражнение 3
Подвиг 4. Пусть имеется следующий фрагмент программы:

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

отображаемые поля: fio, salary, is_work, + поля методов;
кликабельные поля: fio;
редактируемые поля: is_work;
максимальное число записей на страницу: 15.
Дополнительно в классе LectorAdmin определить пользовательское поле со следующими характеристиками:

название метода: info_salary;
возвращаемое значение (в виде строки):
"низкая", если salary < 25000;
"средняя", если 25000 <= salary < 55000;
"высокая", если salary >= 55000;
название поля при отображении: "Величина зарплаты";
сортировка поля: по убыванию поля salary.
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
    list_display = ('fio', 'salary', 'is_work', 'info_salary')
    list_display_links = ('fio', )
    list_editable = ('is_work', )
    list_per_page = 15
    
    @admin.display(description='Величина зарплаты', ordering='-salary')
    def info_salary(self, lector: Lector):
        if lector.salary >= 55000:
            return 'высокая'
        elif lector.salary < 25000:
            return 'низкая'
        else:
            return 'средняя'


""" Упражнение 4
Подвиг 5. Пусть имеется следующий фрагмент программы:

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

отображаемые поля: fio, salary, is_work.
Дополнительно в классе LectorAdmin определить пользовательское действие в виде следующего метода:

def default_salary(self, request, queryset): ...
Данный метод должен всем записям выборки queryset устанавливать значение поля salary равным 0.

С помощью декоратора admin.action назначьте действию default_salary название:

"Сброс зарплаты"

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
    list_display = ('fio', 'salary', 'is_work')
    actions = ['default_salary']
    
    @admin.action(description='Сброс зарплаты')
    def default_salary(self, request, queryset):
        queryset.update(salary=0)

        
""" Упражнение 5
Подвиг 6. Пусть имеется следующий фрагмент программы:

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

отображаемые поля: fio, salary, is_work;
сортировка: по убыванию поля salary.
Дополнительно в классе LectorAdmin определить пользовательское действие в виде следующего метода:

def set_work(self, request, queryset): ...
Данный метод должен записям выборки queryset, у которых salary больше 0, устанавливать значение поля is_work равным True (булево значение).

С помощью декоратора admin.action назначьте действию set_work название:

"Установить работающими"

После выполнения данного действия должно отображаться стандартное сообщение в админ-панели в виде строки:

"Было изменено <число> записей."

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
    list_display = ('fio', 'salary', 'is_work')
    ordering = ('-salary', )
    actions = ['set_work']
    
    @admin.action(description='Установить работающими')
    def set_work(self, request, queryset):
        c = queryset.filter(salary__gt=0).update(is_work=True)
        self.message_user(request, f'Было изменено {c} записей.')
