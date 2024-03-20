""" Упражнение 1
Подвиг 2. Пусть имеется следующая модель:

from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    model_manager = ModelManager()
Объявите в программе пользовательский класс менеджера ModelManager, который бы возвращал все статьи со значением is_published равным 1 и заголовком (title), начинающимся с фрагмента "ли" (регистронезависимый).
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

# здесь объявляйте класс менеджера
class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1, title__istartswith='ли')


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    model_manager = ModelManager()


""" Упражнение 2
Подвиг 4. Используя базовый класс TextChoices:

from django.db.models import TextChoices
объявите класс перечисления с именем Currencies для следующих валют (порядок следования важен):

Атрибут класса; значение; метка
RUB; 'rub'; 'Рубли'
EUR; 'eur'; 'Евро'
USD; 'usd'; 'Доллар'

P.S. На экран ничего выводить не нужно.
"""
from django.db.models import TextChoices

# здесь продолжайте программу
class Currencies(TextChoices):
    RUB = 'rub', 'Рубли'
    EUR = 'eur', 'Евро'
    USD = 'usd', 'Доллар'


""" Упражнение 3
Подвиг 5. Пусть имеется следующая модель:

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'drf', 'Черновик'
        PUBLISHED = 'pub', 'Опубликовано'

    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = # здесь определяйте поле CharField с перечислением Status
Вам необходимо дописать атрибут is_published, который должен определять текстовое поле максимальной длины 3, использовать перечисление Status и по умолчанию принимать значение атрибута PUBLISHED класса Status.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import TextChoices

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'drf', 'Черновик'
        PUBLISHED = 'pub', 'Опубликовано'

    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.CharField(max_length=3, choices=Status.choices, default=Status.PUBLISHED)
