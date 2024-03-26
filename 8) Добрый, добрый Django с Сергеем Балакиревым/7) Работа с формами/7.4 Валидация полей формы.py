""" Упражнение 1
Подвиг 2. Объявите класс формы с именем CardForm, не связанной с моделью, со следующими полями:

fio: текстовое поле; максимальная длина 200 символов, минимальная длина 10 символов, обязательное, название "Владелец";
email: поле ввода адреса электронной почты; минимальная длина 5 символов, обязательное, название "E-mail";
city: текстовое поле; минимальная длина 2 символа, обязательное, название "Город";
is_rf: булево поле (checkbox); по умолчанию True, обязательное, название "Гражданство РФ".

Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: fio, email, city и т.д.

Для поля fio дополнительно пропишите вывод сообщений об ошибках для валидаторов:

превышения числа символов: "Слишком длинная строка";
недостаточного числа символов: "Слишком короткая строка".
Для поля email через параметр widget укажите стили оформления: attrs={'class': 'form-input'} 

P.S. На экран ничего выводить не нужно.
"""
from django import forms

# здесь продолжайте программу
class CardForm(forms.Form):
    fio = forms.CharField(min_length=10, max_length=200, label='Владелец', error_messages={'min_length': 'Слишком короткая строка', 'max_length': 'Слишком длинная строка'})
    email = forms.EmailField(min_length=5, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'} ))
    city = forms.CharField(min_length=2, label='Город')
    is_rf = forms.BooleanField(initial=True, label='Гражданство РФ')


""" Упражнение 2
Подвиг 3. В программе импортированы следующие два валидатора:

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

# здесь продолжайте программу
Определите целочисленное поле формы с ограничениями по диапазону вводимых данных от -100 до 20 включительно (через параметры min_value и max_value). Эти ограничения должны действовать и на уровне формы в браузере и на уровне сервера при ее обработке. Также добавьте валидаторы MinValueValidator и MaxValueValidator. В каждом из них определите следующие сообщения об ошибках:

MinValueValidator: "Минимальное значение -100";
MaxValueValidator: "Максимальное значение 20".
На объект созданного целочисленного поля должна ссылаться переменная с именем field.

P.S. Класс формы объявлять не нужно, только переменную с именем field. На экран ничего выводить не нужно.
"""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

# здесь продолжайте программу
field = forms.IntegerField(
    min_value=-100, 
    max_value=20,
    validators=(
        MinValueValidator(-100, message='Минимальное значение -100'),
        MaxValueValidator(20, message='Максимальное значение 20')
    )
)


""" Упражнение 3
Подвиг 4. Объявите класс формы с именем LoginForm, не связанной с моделью, со следующими полями:

username: текстовое поле; максимальная длина 50 символов, минимальная длина 5 символов, обязательное, название "Логин";
password: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Пароль".

Атрибуты класса должны иметь те же названия и порядок, что и в описании.

Для полей формы через параметр widget укажите стили оформления: attrs={'class': 'form-login-input'}

Для проверки корректности поля password объявите в классе LoginForm метод с именем:

clean_<название поля>

В этом методе реализовать проверку значения поля password по следующим критериям:

допустимые символы: буквы латинского алфавита (малые и большие), цифры и символы "-?!$#@_";
минимальная длина пароля 6 символов.
Если эти проверки не проходят, то генерировать исключение:

raise ValidationError("Некорректно введенный пароль.")
Иначе метод должен возвращать введенный пароль (в виде строки).

P.S. На экран ничего выводить не нужно.
"""
from django import forms
from django.core.exceptions import ValidationError
from string import ascii_letters, digits

CHARS = set(f'{ascii_letters}{digits}-?!$#@_')

# здесь продолжайте программу
class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=50, label='Логин', widget=forms.TextInput(attrs={'class': 'form-login-input'}))
    password = forms.CharField(min_length=6, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-login-input'}))
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6 or set(password) - CHARS:
            raise ValidationError("Некорректно введенный пароль.")
        return password


""" Упражнение 4
Подвиг 5. Объявите класс формы с именем RegisterForm, не связанной с моделью, со следующими полями:

username: текстовое поле; максимальная длина 50 символов, минимальная длина 5 символов, обязательное, название "Логин";
email: поле ввода адреса электронной почты; минимальная длина 5 символов, необязательное, название "E-mail";
first_name: текстовое поле; максимальная длина 50 символов, необязательное, название "Имя";
last_name: текстовое поле; максимальная длина 50 символов, необязательное, название "Фамилия";
password1: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Пароль";
password2: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Повтор пароля".

Атрибуты класса должны иметь те же названия и порядок, что и в описании.

Для полей формы через параметр widget укажите стили оформления: attrs={'class': 'form-register-input'}

Для проверки корректности полей password1 и password2 объявите в классе RegisterForm метод clean следующим образом:

def clean(self):
    cleaned_data = super().clean()
    # продолжение метода
В этом методе реализуйте проверку значений полей password1 и password2 по следующим критериям:

а) допустимые символы: буквы латинского алфавита (малые и большие), цифры и символы "-?!$#@_";
б) минимальная длина пароля 6 символов;
в) пароли password1 и password2 должны совпадать.

Если эти проверки не проходят, то генерировать исключения:

а) raise ValidationError("Некорректно введенный пароль.")
б) raise ValidationError("Слишком короткий пароль.")
в) raise ValidationError("Пароли не совпадают.")

P.S. На экран ничего выводить не нужно.
"""
from django import forms
from django.core.exceptions import ValidationError
from string import ascii_letters, digits

CHARS = set(f'{ascii_letters}{digits}-?!$#@_')


# здесь продолжайте программу
class RegisterForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=50, label='Логин', widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    email = forms.EmailField(min_length=5, required=False, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    first_name = forms.CharField(max_length=50, required=False, label='Имя', widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    last_name = forms.CharField(max_length=50, required=False, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    password1 = forms.CharField(min_length=6, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-register-input'}))
    password2 =  forms.CharField(min_length=6, label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-register-input'}))

    def clean(self):
        cleaned_data = super().clean()
        p1, p2 = cleaned_data['password1'], cleaned_data['password2']
        if set((*p1, *p2)) - CHARS:
            raise ValidationError("Некорректно введенный пароль.")
        if len(p1) < 6 or len(p2) < 6:
            raise ValidationError("Слишком короткий пароль.")
        if p1 != p2:
            raise ValidationError("Пароли не совпадают.")
