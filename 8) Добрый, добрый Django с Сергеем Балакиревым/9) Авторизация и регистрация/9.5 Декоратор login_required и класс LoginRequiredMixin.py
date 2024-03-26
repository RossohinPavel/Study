""" Упражнение 1
Подвиг 2. Пусть имеется следующая функция представления:

# from django.contrib.auth.decorators import login_required

def show_post(request, post_slug):
    post = {'title': "Статья", 'slug': post_slug, 'content': "Содержимое статьи"} # заглушка для get_object_or_404(Subject, slug=post_slug)

    data = {
        'title': post['title'],
        'post': post,
    }

    return render(request, 'subject/post_detail.html', context=data)
Примените к ней декоратор login_required, чтобы запретить просмотр неавторизованным пользователям.
"""
from django.contrib.auth.decorators import login_required

@login_required
def show_post(request, post_slug):
    post = {'title': "Статья", 'slug': post_slug, 'content': "Содержимое статьи"} # заглушка для get_object_or_404(Subject, slug=post_slug)

    data = {
        'title': post['title'],
        'post': post,
    }

    return render(request, 'subject/post_detail.html', context=data)


""" Упражнение 2
Подвиг 3. Пусть имеется следующая функция представления:

from django.contrib.auth.decorators import login_required

def support(request):
    data = {
        'title': 'Поддержка клиентов',
    }

    return render(request, 'users/support.html', context=data)
Примените к ней декоратор login_required, чтобы запретить просмотр неавторизованным пользователям. При попытке получить доступ неавторизованным пользователем автоматически перенаправлять по URL-адресу с именем 'login'.
"""
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def support(request):
    data = {
        'title': 'Поддержка клиентов',
    }

    return render(request, 'users/support.html', context=data)


""" Упражнение 3
Подвиг 4. Пусть имеется следующий класс представления:

from django.contrib.auth.mixins import LoginRequiredMixin

class ListPost(ListView):
    template_name = 'post/list.html'
    model = Post
    context_object_name = 'posts'
    extra_context = {
        'title': 'Список опубликованных статей',
    }
Примените к нему класс LoginRequiredMixin, чтобы ограничить доступ неавторизованным пользователям.
"""
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class ListPost(LoginRequiredMixin, ListView):
    template_name = 'post/list.html'
    model = Post
    context_object_name = 'posts'
    extra_context = {
        'title': 'Список опубликованных статей',
    }

    
""" Упражнение 4
Подвиг 5. Пусть имеется следующий класс представления:

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class AddPerson(CreateView):
    form_class = PersonForm
    template_name = 'person/person_create.html'
    success_url = reverse_lazy('list-person')
    extra_context = {'title': 'Новая персона'}
Примените к нему класс LoginRequiredMixin, чтобы ограничить доступ неавторизованным пользователям. При попытке получить доступ неавторизованным пользователем автоматически перенаправлять по URL-адресу '/home/'.
"""
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class AddPerson(LoginRequiredMixin, CreateView):
    form_class = PersonForm
    template_name = 'person/person_create.html'
    success_url = reverse_lazy('list-person')
    extra_context = {'title': 'Новая персона'}
    login_url = '/home/'
