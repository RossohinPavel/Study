""" Упражнение 1
Подвиг 1. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import F

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
Используя стандартный менеджер записей (objects) модели Person и класс F, нужно увеличить зарплату (salary) всех сотрудников на 1000.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import F

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


Person.objects.update(salary=F('salary')+1000)


""" Упражнение 2
  Подвиг 2. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import F, Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
Используя стандартный менеджер записей (objects) модели Person, классы F и Q, нужно увеличить зарплату (salary) в 2 раза всех сотрудников у которых поле job равно 'django' или возраст (age) больше 30.

P.S. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import F, Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


Person.objects.filter(Q(job='django') | Q(age__gt=30)).update(salary=F('salary')*2)


""" Упражнение 3
Подвиг 4. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import F, Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

records = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person и класс F, сформировать выборку с дополнительным вычисляемым полем tax (налог), значение которого должно вычисляться на основе поля salary следующим образом: tax = salary*0.13

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import F, Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.annotate(tax=F('salary')*0.13)


""" Упражнение 4
Подвиг 5. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import F, Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

records = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, классы F и Q, сформировать выборку из сотрудников, у которых возраст (age) больше 40 или зарплата (salary) больше 20000. Для этой выборки дополнительно сформировать вычисляемое поле tax (налог) на основе поля salary по следующей формуле: tax = salary*0.13

P.S. Порядок параметров в критерии не менять. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import F, Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.filter(Q(age__gt=40) | Q(salary__gt=20000)).annotate(tax=F('salary')*0.13)


""" Упражнение 5
 Подвиг 6. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import F, Q, Value

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

records = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, классы F и Value, сформировать выборку из сотрудников с двумя дополнительными вычисляемыми полями:

поле tax = salary * 0.13
поле is_paid = False
То есть, первое поле tax вычисляется на основе поля salary с умножением на 0.13, а второе поле is_paid всюду равно False (булевому значению).

P.S. Порядок полей не менять, сначала tax, затем is_paid. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import F, Q, Value

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.annotate(tax=F('salary')*0.13, is_paid=Value(False))


""" Упражнение 6
Подвиг 7. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import F, Q, Value

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

records = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, классы F, Q и Value, сформировать выборку из сотрудников, возраст (age) которых меньше 35 или зарплата (salary) меньше 40000 с двумя дополнительными вычисляемыми полями:

поле tax = salary * 0.13
поле is_paid = False
То есть, первое поле tax вычисляется на основе поля salary с умножением на 0.13, а второе поле is_paid всюду равно False (булевому значению).

P.S. Порядок параметров в критерии и порядок полей не менять, сначала tax, затем is_paid. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import F, Q, Value

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.filter(Q(age__lt=35) | Q(salary__lt=40000)).annotate(tax=F('salary')*0.13, is_paid=Value(False))
