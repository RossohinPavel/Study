""" Упражнение 1
Подвиг 2. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, вычислите количество записей для каждой профессии (job). Число записей должно храниться в поле с именем total. Агрегирующая функция Count() должна применяться к полю id.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = Person.objects.values('job').annotate(total=Count('id'))


""" Упражнение 2
Подвиг 3. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, вычислите количество записей для каждой профессии (job) при условии, что зарплата salary >= 50000. Число записей должно храниться в поле с именем total.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = Person.objects.values('job').filter(salary__gte=50000).annotate(total=Count('id'))


""" Упражнение 3
 Подвиг 4. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, вычислите среднюю зарплату (salary) для каждой профессии (job). Значение средней зарплаты должно храниться в поле с именем salary_avg.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = Person.objects.values('job').annotate(salary_avg=Avg('salary'))


""" Упражнение 4
Подвиг 5. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = # здесь прописывайте команду
Используя стандартный менеджер записей (objects) модели Person, вычислите максимальную и минимальную зарплату (salary) для каждой профессии (job) при условии, что возраст сотрудника (age) больше 30. Значения максимальной и минимальной зарплаты должно храниться в полях с именами salary_max и salary_min.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    salary = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


result = Person.objects.values('job').filter(age__gt=30).annotate(salary_max=Max('salary'), salary_min=Min('salary'))


""" Упражнение 5
Подвиг 6. Пусть в программе объявлена следующая модель:

from django.db import models
from django.db.models.functions import Length

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
Используя стандартный менеджер записей (objects) модели Post, методы annotate(), filter() и count(), определите число записей с размером заголовка (title) больше 50 символов. Размер заголовка должен определяться полем length.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models.functions import Length

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


result = Post.objects.annotate(length=Length('title')).filter(length__gt=50).count()


""" Упражнение 6
Подвиг 7. Пусть имеются две следующие модели:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True, related_name='subs')
Используя стандартный менеджер записей (objects) модели Subject, методы annotate() и filter(), выберите все записи (предметы), у которых имеется хотя бы один лектор. Общее число лекторов по каждому предмету хранить в вычисляемом поле с именем total.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True, related_name='subs')


result = Subject.objects.annotate(total=Count('subs')).filter(total__gt=0)


""" Упражнение 7
 Подвиг 8. Пусть имеются две следующие модели:

from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True, related_name='subs')
Используя стандартный менеджер записей (objects) модели Lector, выполните группировку по предметам (subjects) с определением общего числа лекторов и при условии, что предмет volume >= 16. Новое вычисляемое поле с числом лекторов назвать total. Агрегирующая функция Count() должна применяться к полю id.

P.S. На экран ничего выводить не нужно.
"""
from django.db import models
from django.db.models import Count, Sum, Avg, Max, Min

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)


class Lector(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    fio = models.CharField(max_length=255)
    subjects = models.ManyToManyField('Subject', blank=True, related_name='subs')


result = Lector.objects.values('subjects').filter(subjects__volume__gte=16).annotate(total=Count('id'))
