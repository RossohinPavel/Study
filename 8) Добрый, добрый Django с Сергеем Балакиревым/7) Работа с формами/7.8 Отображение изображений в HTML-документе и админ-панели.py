""" Упражнение 1
Подвиг 3. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name='Изображение')
    content = models.TextField(blank=True, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
from django.utils.safestring import mark_safe

# импорт from .models import Post

# здесь продолжайте программу
Необходимо зарегистрировать для админ-панели модель Post и во вспомогательном классе PostAdmin (унаследованный от admin.ModelAdmin) определить:

отображаемые поля: title, slug, is_published;
кликабельные поля: title;
поля при редактировании записи: title, slug, content, photo, is_published;
показать верхнюю панель редактирования записи.
Затем, добавить пользовательское вычисляемое поле путем объявления в классе PostAdmin метода:

def post_photo(self, post: Post): ...
который должен возвращать HTML-строку с тегом img в следующем формате:

"<img src='<URL-адрес изображения photo>' width=50>"

(Не забудьте использовать функцию mark_safe для отмены экранирования HTML-тегов.)

Добавьте это новое поле для отображения в админ-панели. Декорируйте метод post_photo, чтобы в админ-панели это поле имело название "Изображение".

P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(upload_to="post/%Y/%m/", blank=True, verbose_name='Изображение')
    content = models.TextField(blank=True, verbose_name='Контент')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# --------- admin.py ------------------------
from django.contrib import admin
from django.utils.safestring import mark_safe

# импорт from .models import Post

# здесь продолжайте программу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'post_photo')
    list_display_links = ('title', )
    fields = ('title', 'slug', 'content', 'photo', 'is_published')
    save_on_top = True
    
    @admin.display(description='Изображение')
    def post_photo(self, post: Post):
        return mark_safe(f"<img src='{post.photo.url}' width=50>")
        
