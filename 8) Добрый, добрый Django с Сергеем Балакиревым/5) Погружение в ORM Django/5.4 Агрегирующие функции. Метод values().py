""" Упражнение 1
Подвиг 2. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Subject и метод aggregate(), вычислите среднее значение цены (price) предметов. На выходе должен формироваться словарь с ключом 'subject_avg' и соответствующим значением.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.aggregate(subject_avg=Avg('price'))


""" Упражнение 2
 Подвиг 3. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Subject и метод aggregate(), вычислите среднее значение часов (volume) предметов, а также минимальную и максимальную цену (price). На выходе должен формироваться словарь с ключами: 'vol_avg', 'pr_min', 'pr_max' и соответствующими значениями.

P.S. Порядок вызова агрегирующих функций, как указано в описании. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.aggregate(vol_avg=Avg('volume'), pr_min=Min('price'), pr_max=Max('price'))


""" Упражнение 3
 Подвиг 4. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Subject, методы filter() и aggregate(), выберите записи с price > 4000, вычислите их общее количество, а также разность между максимальной и средней ценой. На выходе должен формироваться словарь с ключами: 'total', 'price_diff' и соответствующими значениями. Агрегирующая функция Count() должна применяться к полю id.
P.S. Порядок вызова агрегирующих функций, как указано в описании. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.filter(price__gt=4000).aggregate(total=Count('id'), price_diff=Max('price') - Avg('price'))


""" Упражнение 4
Подвиг 5. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min, Q

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Subject, методы filter() и aggregate(), выберите записи с price >= 2000 или volume > 16, вычислите их общее количество, а также разность между максимальным и минимальным объемами (volume). На выходе должен формироваться словарь с ключами: 'total', 'volume_diff' и соответствующими значениями. Агрегирующая функция Count() должна применяться к полю id.

P.S. Порядок критериев выбора записей и вызова агрегирующих функций, как указано в описании. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min, Q

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)


result = Subject.objects.filter(Q(price__gte=2000) | Q(volume__gt=16)).aggregate(total=Count('id'), volume_diff=Max('volume') - Min('volume'))


""" Упражнение 5
Подвиг 6. Пусть в программе объявлена следующая модель:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

records = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, выберите все записи так, чтобы в выборке фигурировали только поля full_name и salary.

P.S. Порядок полей должен быть, как указано в описании. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.values('full_name', 'salary')


""" Упражнение 6
 Подвиг 7. Пусть в программе объявлена следующая модель:

from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

records = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, методы filter() и values(), выберите все записи с полем job = 'python' и так, чтобы в выборке фигурировали только поля full_name, salary и age.

P.S. Порядок полей должен быть, как указано в описании. На экран ничего выводить не нужно.
"""
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


records = Person.objects.filter(job='python').values('full_name', 'salary', 'age')


""" Упражнение 7
Подвиг 8 (на повторение). Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

Используя стандартный менеджер записей (objects) модели Person, измените значение поля is_active на False (булево значение) у записей с salary < 10000 или age > 65.

P.S. Порядок следования критериев отбора записей, как в описании. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Q

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


Person.objects.filter(Q(salary__lt=10000) | Q(age__gt=65)).update(is_active=False)
