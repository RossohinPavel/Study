""" Упражнение 1
Подвиг 3. Пусть имеется следующий класс представления:

# from .models import Person
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

class PersonList(ListView):
    model = Person
    template_name = 'person/list.html'
    context_object_name = 'persons'
    allow_empty = False
    paginate_by = 3
Отредактируйте этот класс, разрешив просмотр списка только пользователям с разрешением вида 'users.view_person'.
"""
# from .models import Person
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

class PersonList(PermissionRequiredMixin, ListView):
    model = Person
    template_name = 'person/list.html'
    context_object_name = 'persons'
    allow_empty = False
    paginate_by = 3
    permission_required = 'users.view_person'


""" Упражнение 2
Подвиг 4. Пусть имеется следующая функция представления:

# from django.contrib.auth.decorators import login_required, permission_required
# from .forms import AddPostForm

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            return True
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'title': 'Добавление статьи', 'form': form})
Примените к ней декоратор permission_required так, чтобы доступ имели только пользователи с разрешением вида 'women.add_post'. Для всех других пользователей должно генерироваться исключение с кодом 403 - доступ запрещен.
"""
from django.contrib.auth.decorators import permission_required
# from .forms import AddPostForm

@permission_required(perm='women.add_post', raise_exception=True)
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            return True
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'title': 'Добавление статьи', 'form': form})
