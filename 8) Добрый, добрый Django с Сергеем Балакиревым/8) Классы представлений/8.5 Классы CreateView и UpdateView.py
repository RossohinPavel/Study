""" Упражнение 1
Подвиг 5. Пусть имеется следующая модель:

# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------- views.py ------------------------
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from .models import Lector

# здесь продолжайте программу
Необходимо в разделе views.py объявить класс представления с именем CreateLector, унаследованный от базового класса CreateView, со следующим функционалом:

через атрибуты класса:

используемая модель: Lector;
поля для заполнения в форме: fio, slug, is_work;
шаблон: 'mgtu/lector_create.html';
перенаправление при успешном добавлении: reverse_lazy('lector-list');
через методы класса:

form_valid: назначить полю salary создаваемой записи значение 11000;
Подсказка: ранее в подвиге был пример реализации метода form_valid, который здесь вам поможет:

def form_valid(self, form):
    p = form.save(commit=False)  # формирование объекта записи, без сохранения ее в БД (commit=False)
    p.job = 'djano'              # изменение поля job на значение 'django'
    return super().form_valid(form)  # запись сохраняется в БД через вызов метода form_valid базового класса
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------- views.py ------------------------
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from .models import Lector

# здесь продолжайте программу
class CreateLector(CreateView):
    model = Lector
    fields = ('fio', 'slug', 'is_work')
    template_name = 'mgtu/lector_create.html'
    success_url = reverse_lazy('lector-list')
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.salary = 11000
        return super().form_valid(form)


""" Упражнение 2
Подвиг 6. Пусть имеется следующая модель:

# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------- views.py ------------------------
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
# from .models import Lector

# здесь продолжайте программу
Необходимо в разделе views.py объявить класс представления с именем UpdateLector, унаследованный от базового класса UpdateView, со следующим функционалом:

через атрибуты класса:

используемая модель: Lector;
поля для редактирования в форме: fio, slug, salary, is_work;
шаблон: 'mgu/lector_create.html';
перенаправление при успешном добавлении: reverse_lazy('lector-list');
дополнительные переменные для шаблона: {'title': 'Добавление лектора'}. 
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------- views.py ------------------------
# from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
# from .models import Lector

# здесь продолжайте программу
class UpdateLector(UpdateView):
    model = Lector
    fields = ('fio', 'slug', 'salary', 'is_work')
    template_name = 'mgu/lector_create.html'
    success_url = reverse_lazy('lector-list')
    extra_context = {'title': 'Добавление лектора'}

    
""" Упражнение 3
Подвиг 7. Пусть имеется следующий фрагмент программы:

# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------- mgu/lector_delete.html-----------
<form method="post">
    {% csrf_token %}
    <p>Удаляемая запись: "{{ object }}"</p>
    {{ form.as_p }}
    <input type="submit" value="Удалить">
</form>

# --------- views.py ------------------------
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
# from .models import Lector

# здесь продолжайте программу
Необходимо в разделе views.py объявить класс представления с именем DeleteLector, унаследованный от базового класса DeleteView, со следующим функционалом:

через атрибуты класса:

используемая модель: Lector;
шаблон: 'mgu/lector_delete.html';
перенаправление при успешном добавлении: reverse_lazy('lector-list').
"""
# --------- models.py ------------------------
from django.db import models

class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    salary = models.PositiveIntegerField(default=0, verbose_name='Зарплата')
    is_work = models.BooleanField(default=False, verbose_name='Статус')

# --------- mgu/lector_delete.html-----------
# <form method="post">
#     {% csrf_token %}
#     <p>Удаляемая запись: "{{ object }}"</p>
#     {{ form.as_p }}
#     <input type="submit" value="Удалить">
# </form>

# --------- views.py ------------------------
# from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
# from .models import Lector

# здесь продолжайте программу
class DeleteLector(DeleteView):
    model = Lector
    template_name = 'mgu/lector_delete.html'
    success_url = reverse_lazy('lector-list')
