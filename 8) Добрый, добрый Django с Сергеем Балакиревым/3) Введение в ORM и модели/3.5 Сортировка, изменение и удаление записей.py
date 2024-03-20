""" Упражнение 1
Подвиг 2. Пусть имеется следующий класс модели:

from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
С помощью последовательного вызова методов filter() и order_by() менеджера записей класса CourseItem выберите записи с флагом is_published=True и отсортируйте их в порядке возрастания поля title.
P. S. На экран ничего выводить не нужно.
"""
from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# здесь продолжайте программу
CourseItem.objects.filter(is_published=True).order_by('title')


""" Упражнение 2
Подвиг 3. Пусть имеется следующий класс модели:

from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
С помощью стандартного менеджера записей класса CourseItem выберите все записи и отсортируйте их в порядке убывания поля title.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# здесь продолжайте программу
CourseItem.objects.all().order_by('-title')


""" Упражнение 3
Подвиг 4. Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
Добавьте в него вложенный класс с именем Meta и пропишите автоматическую сортировку выбираемых записей по возрастанию зарплаты salary.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)

    # здесь прописывайте класс Meta
    class Meta:
        ordering = ['salary']


""" Упражнение 4
Подвиг 5. Пусть имеется следующий класс модели:

from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
Необходимо с помощью метода get() стандартного менеджера записей класса CourseItem извлечь запись с pk равным 2 и сохранить объект в переменной item. Затем, изменить в объекте item следующие поля:

title="Python ООП"
content="Обучающий курс по Python ООП"

После этого изменить в таблице БД запись объекта item.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# здесь продолжайте программу
item = CourseItem.objects.get(pk=2)
item.title="Python ООП"
item.content="Обучающий курс по Python ООП"
item.save()


""" Упражнение 5
Подвиг 6. Пусть имеется следующий класс модели:

from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
С помощью методов filter() и update() стандартного менеджера записей класса CourseItem у записей со значением is_published=False изменить поле content на пустую строку.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class CourseItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


# здесь продолжайте программу
CourseItem.objects.filter(is_published=False).update(content='')


""" Упражнение 6
Подвиг 7. Пусть имеется следующий класс модели:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
С помощью методов filter() и delete() выполнить выборку и удаление из таблицы БД всех сотрудников с зарплатами (salary) ниже 13000.
P.S. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)


# здесь продолжайте программу
Person.objects.filter(salary__lt=13000).delete()
