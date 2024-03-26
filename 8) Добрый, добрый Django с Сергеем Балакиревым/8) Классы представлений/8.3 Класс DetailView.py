""" Упражнение 1
Подвиг 4. Пусть имеется следующая функция представления:

def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    data = {
        'title': "Содержание поста",
        'post': post,
        'cat_selected': 0,
    }

    return render(request, 'post/detail_post.html', data)
Замените эту функцию классом представления с именем PostDetail, унаследованным от базового класса DetailView, со следующим функционалом:

через атрибуты класса:

используемый шаблон: 'post/detail_post.html';
модель: Post;
имя переменной для шаблона с объектом записи: post;
извлечение записи по переменной post_slug;
дополнительные переменные для шаблона: {'title': "Содержание поста", 'cat_selected': 0}.
P.S. На экран ничего выводить не нужно.
"""
from django.views.generic import DetailView
# from .models import Post

# здесь объявляйте класс представления
class PostDetail(DetailView):
    template_name = 'post/detail_post.html'
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    extra_context =  {'title': "Содержание поста", 'cat_selected': 0}


""" Упражнение 2
Подвиг 5. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

# --------- views.py ------------------------
# from django.shortcuts import get_object_or_404
# from .models import Post

def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, is_published=1)

    data = {
        'title': post.title,
        'post': post,
    }

    return render(request, 'post/detail_post.html', data)
Замените эту функцию классом представления с именем PostDetail, унаследованным от базового класса DetailView, со следующим функционалом:

через атрибуты класса:

используемый шаблон: 'post/detail_post.html';
имя переменной для шаблона с объектом записи: post;
через методы класса:

get_object: извлечение записи по критерию: slug = post_slug и is_published = 1; для получения записи использовать функцию get_object_or_404();
get_context_data: сформировать следующие переменные для шаблона: {'title': "Заголовок поста", 'cat_selected': 0}.
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
    is_published = models.BooleanField(default=False)

# --------- views.py ------------------------
from django.views.generic import DetailView
# from django.shortcuts import get_object_or_404
# from .models import Post

# здесь объявляйте класс представления
class PostDetail(DetailView):
    model = Post
    template_name = 'post/detail_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs[self.slug_url_kwarg], is_published=1)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs) | {'title': "Заголовок поста", 'cat_selected': 0}
    