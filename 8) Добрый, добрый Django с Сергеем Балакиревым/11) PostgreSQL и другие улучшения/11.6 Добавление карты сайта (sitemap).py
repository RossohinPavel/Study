""" Упражнение 1
Подвиг 3. Пусть имеется следующая модель:

# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    name = models.CharField(max_length=255, verbose_name="Название")
    volume = models.PositiveIntegerField(default=16, verbose_name="Объем часов")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_active = models.BooleanField(default=False, verbose_name='Доступно')

    def get_absolute_url(self):
        return reverse('subject', kwargs={'sub_slug': self.slug})

# --------- sitemaps.py ------------------------
from django.contrib.sitemaps import Sitemap
# from .models import Subject

# здесь продолжайте программу
Объявите класс SubjectSitemap, унаследованный от класса Sitemap, со следующим функционалом:

через атрибуты класса:

частота обновления страниц: ежедневно;
приоритет: 0,85;
через методы класса:

items: выборка через стандартный менеджер записей (objects) модели Subject всех записей с is_active = 1 и volume > 0;
lastmod: возврат время последнего редактирования страницы (значения поля time_update).
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    name = models.CharField(max_length=255, verbose_name="Название")
    volume = models.PositiveIntegerField(default=16, verbose_name="Объем часов")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_active = models.BooleanField(default=False, verbose_name='Доступно')

    def get_absolute_url(self):
        return reverse('subject', kwargs={'sub_slug': self.slug})

# --------- sitemaps.py ------------------------
from django.contrib.sitemaps import Sitemap
# from .models import Subject

# здесь продолжайте программу
class SubjectSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.85

    def items(self):
        return Subject.objects.filter(is_active=1, volume__gt=0)

    def lastmod(self, obj):
        return obj.time_update
  