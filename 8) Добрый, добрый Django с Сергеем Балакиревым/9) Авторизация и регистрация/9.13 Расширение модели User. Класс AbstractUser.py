""" Упражнение 1
Подвиг 3. Объявите новую модель пользователя с именем Lector с базовым классом AbstractUser и следующими дополнительными полями:

avatar: поле изображения (ImageField); путь для загрузки "avatars/<текущий год>/<текущий месяц>/", необязательное, по умолчанию "avatars/default.jpg", название "Изображение";
status: текстовое поле; максимальная длина 200 символов, необязательное, название "Должность";
salary: целочисленное поле (IntegerField); необязательное, по умолчанию значение 0, название "Зарплата".
Объявите переменную AUTH_USER_MODEL и присвойте ей значение новой модели пользователя Lector приложения users.

P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.models import AbstractUser
from django.db import models

# здесь продолжайте программу
class Lector(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/", blank=True, default="avatars/default.jpg", verbose_name='Изображение')
    status = models.CharField(max_length=200, blank=True, verbose_name='Должность')
    salary = models.IntegerField(blank=True, default=0, verbose_name='Зарплата')


AUTH_USER_MODEL = 'users.Lector'


""" Упражнение 2
Подвиг 4. Объявите новую модель пользователя с именем Student с базовым классом AbstractUser и следующими дополнительными полями:

photo: поле изображения (ImageField); путь для загрузки "avatars/<текущий год>/<текущий день>/", обязательное, по умолчанию "avatars/default.jpg", название "Фотография";
group: текстовое поле; максимальная длина 100 символов, необязательное, название "Группа";
stipend: целочисленное поле (PositiveIntegerField); необязательное, по умолчанию значение 0, название "Стипендия".
Объявите переменную AUTH_USER_MODEL и присвойте ей значение новой модели пользователя Student приложения students.

Зарегистрируйте модель Student в админ-панели, используя стандартный класс UserAdmin и декоратор admin.site.register.
"""
# from django.contrib.auth.models import AbstractUser
from django.db import models

# здесь объявляйте модель Student
class Student(AbstractUser):
    photo = models.ImageField(upload_to='avatars/%Y/%d/', default="avatars/default.jpg", verbose_name='Фотография')
    group = models.CharField(max_length=100, blank=True, verbose_name='Группа')
    stipend = models.PositiveIntegerField(blank=True, default=0, verbose_name='Стипендия')

    
AUTH_USER_MODEL = 'students.Student'

from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Student

# здесь регистрируйте модель в админ-панели
admin.site.register(Student, UserAdmin)


""" Упражнение 3
Подвиг 5. Выполните расширение стандартной модели User с использованием связи one-to-one. Для этого объявите класс модели с именем Profile со следующими атрибутами:

user: связь one-to-one со стандартной моделью User (пропишите класс User в кавычках в виде строки); удаление связанных записей по алгоритму CASCADE;
photo: поле изображения (ImageField); путь для загрузки "users/<текущий год>/<текущий месяц>/", необязательное, по умолчанию "users/default.jpg", название "Изображение";
date_birth: поле с датой (DateField); необязательное, допустимо значение NULL, название "Дата рождения".
Зарегистрируйте через декоратор для админ-панели модель Profile. Во вспомогательном классе ProfileAdmin (унаследованный от admin.ModelAdmin) определите следующие атрибуты:

отображаемые поля: user, photo, date_birth;
редактируемые поля: date_birth;
поля при редактировании записи: user, photo, date_birth.
P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.models import User
from django.db import models

# здесь объявляйте модель Profile
class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="users/%Y/%m/", blank=True, default='users/default.jpg', verbose_name='Изображение')
    date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

from django.contrib import admin

# здесь регистрируйте модель в админ-панели
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'date_birth')
    list_editable = ('date_birth', )
    fields = ('user', 'photo', 'date_birth')

    
""" Упражнение 4
Подвиг 6. Пусть имеется следующая расширенная модель пользователя:

# from django.contrib.auth.models import AbstractUser
from django.db import models

class Lector(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/", blank=True, verbose_name="Изображение")
    status = models.CharField(max_length=200, blank=True, verbose_name="Должность")
    salary = models.IntegerField(blank=True, default=0, verbose_name="Зарплата")
Объявите класс формы ProfileForm для редактирования профиля пользователя (форма связанная с моделью) со следующими элементами:

через атрибуты класса:

username: текстовое поле, закрытое для редактирования (disabled=True), название "Логин";
email: поле ввода E-mail, закрытое для редактирования (disabled=True), название "E-mail";
status: текстовое поле, закрытое для редактирования (disabled=True), название "Должность";
через атрибуты вложенного класса Meta:

модель: получить через вызов функции get_user_model();
отображаемые поля в форме (порядок важен): avatar, username, email, first_name, last_name, status, salary;
дополнительные названия полей: first_name -> "Имя", last_name -> "Фамилия".
P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class Lector(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/", blank=True, verbose_name="Изображение")
    status = models.CharField(max_length=200, blank=True, verbose_name="Должность")
    salary = models.IntegerField(blank=True, default=0, verbose_name="Зарплата")


# здесь продолжайте программу
class ProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    email = forms.EmailField(disabled=True, label='E-mail')
    status = forms.CharField(disabled=True, label='Должность')
    
    class Meta:
        model = get_user_model()
        fields = ('avatar', 'username', 'email', 'first_name', 'last_name', 'status', 'salary')
        labels = {'first_name': "Имя", 'last_name': "Фамилия"}
