""" Упражнение 1
Подвиг 1. Пусть имеется следующий фрагмент программы:

# --------- views.py ------------------------
from django.views import View
# from django.shortcuts import render

class PostView(View):
    def get(self, request):
        return render(request, 'post/post_detail.html', {'title': 'Добавление статьи'})


# --------- urls.py ------------------------
from django.urls import path
# from .views import PostView

urlpatterns = [
    # здесь прописывайте маршрут
]
Необходимо в коллекции urlpatterns с помощью функции path прописать маршрут связи URL-адреса:

http://127.0.0.1:8000/main/

с классом представления PostView. Имя маршрута определить строкой 'mainpage'.

P.S. На экран ничего выводить не нужно.
"""
# --------- views.py ------------------------
from django.views import View
# from django.shortcuts import render

class PostView(View):
    def get(self, request):
        return render(request, 'post/post_detail.html', {'title': 'Добавление статьи'})


# --------- urls.py ------------------------
from django.urls import path
# from .views import PostView

urlpatterns = [
    # здесь прописывайте маршрут
    path('main/', PostView.as_view(), name='mainpage')
]


""" Упражнение 2
Подвиг 2. Пусть имеется следующая функция представления:

def index(request):
    data = {
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'subject/index.html', context=data)
Замените эту функцию аналогичным классом представления с именем MainPage, унаследованным от базового класса TemplateView.

В описании класса используйте только нужные атрибуты. Методы объявлять не нужно.

P.S. На экран ничего выводить не нужно.
"""
from django.views.generic import TemplateView

# здесь объявляйте класс представления
class MainPage(TemplateView):
    template_name = 'subject/index.html'
    extra_context = {
        'title': 'Главная страница',
        'cat_selected': 0,
    }


""" Упражнение 3
Подвиг 3. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

# --------- forms.py ------------------------
from django import forms
# from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']

# --------- views.py ------------------------
# from django.shortcuts import render, redirect
# from .forms import AddPostForm

def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddPostForm()

    return render(request, 'post/addpost.html', {'title': 'Добавление статьи', 'form': form})
Замените функцию add_post аналогичным классом представления с именем AddPost, унаследованным от базового класса View.

В классе AddPost должны быть объявлены только два метода get и post с соответствующим содержимым.

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

# --------- forms.py ------------------------
from django import forms
# from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']

# --------- views.py ------------------------
from django.views import View
# from django.shortcuts import render, redirect
# from .forms import AddPostForm

# здесь объявляйте класс представления
class AddPost(View):
    def get(self, request):
        form = AddPostForm()
        return render(request, 'post/addpost.html', {'title': 'Добавление статьи', 'form': form})
 
    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
 
        return render(request, 'post/addpost.html', {'title': 'Добавление статьи', 'form': form})


""" Упражнение 4
Подвиг 4. Пусть имеется следующая функция представления:

def show_post(request, post_slug):
    # заглушка вместо вызова get_object_or_404(Women, slug=post_slug)
    post = {'title': 'Заголовок', 'slug': post-slug, 'content': 'Супер пост'} 

    data = {
        'title': post['title'],
        'post': post,
        'cat_selected': 0,
    }

    return render(request, 'post/post_detail.html', context=data)
Замените эту функцию аналогичным классом представления с именем PostDetail, унаследованным от базового класса TemplateView. Класс должен иметь следующее содержимое:

атрибут для использования шаблона 'post/post_detail.html';
метод get_context_data для передачи в шаблон данных из словаря data.
Вместо функции get_object_or_404() используйте словарь:

post = {'title': 'Заголовок', 'slug': 'post-slug', 'content': 'Супер пост'} 
P.S. На экран ничего выводить не нужно.
"""
from django.views.generic import TemplateView

POST = {'title': 'Заголовок', 'slug': 'post-slug', 'content': 'Супер пост'} 

# здесь объявляйте класс представления
class PostDetail(TemplateView):
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context | {'title': POST['title'], 'post': POST, 'cat_selected': 0}
