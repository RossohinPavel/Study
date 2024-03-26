""" Упражнение 1
Подвиг 2. Объявите класс формы LectorRegisterForm для регистрации преподавателей. Форма LectorRegisterForm должна быть связана с моделью User, доступ к которой следует выполнить с помощью функции get_user_model(). Сама же форма должна иметь следующие элементы:

через атрибуты класса:

username: текстовое поле, максимальная длина 50 символов, название "Логин";
password: поле ввода пароля, максимальная длина 30 символов, название "Пароль";
password2: поле ввода пароля, максимальная длина 30 символов, название "Повтор пароля";
через атрибуты вложенного класса Meta:

модель: определяется вызовом функции get_user_model();
отображаемые в форме поля: username, email, password, password2;
дополнительные метки (названия) полей: email -> "E-mail".
P.S. На экран ничего выводить не нужно.
"""
from django import forms
# from django.contrib.auth import get_user_model

# здесь объявляйте класс формы
class LectorRegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(max_length=30, label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, label='Повтор пароля', widget=forms.PasswordInput())
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'password2')
        labels = {'email': "E-mail"}

        
""" Упражнение 2
Подвиг 3. Объявите класс формы CompanyRegisterForm для регистрации коммерческой компании. Форма CompanyRegisterForm должна быть связана с моделью User, доступ к которой следует выполнить с помощью функции get_user_model(). Сама же форма должна иметь следующие элементы:

через атрибуты класса:

username: текстовое поле, максимальная длина 50 символов, название "Логин";
password: поле ввода пароля, максимальная длина 30 символов, название "Пароль";
password2: поле ввода пароля, максимальная длина 30 символов, название "Повтор пароля";
через атрибуты вложенного класса Meta:

модель: определяется вызовом функции get_user_model();
отображаемые в форме поля: username, first_name, email, password, password2;
дополнительные метки (названия) полей: first_name -> "Название компании", email -> "E-mail".
через методы класса:

метод clean_password2: выполнить проверку совпадения содержимого полей password и password2; для доступа к полям используйте словарь self.cleaned_data; если пароли совпадают, то вернуть пароль, иначе сгенерировать исключение:
raise ValidationError("Пароли не совпадают!")
P.S. На экран ничего выводить не нужно.
"""
from django import forms
from django.core.exceptions import ValidationError

# здесь объявляйте класс формы
class CompanyRegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Логин")
    password = forms.CharField(max_length=30, label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, label="Повтор пароля", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email', 'password', 'password2')
        labels = {'first_name': "Название компании", 'email': "E-mail"}
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError("Пароли не совпадают!")
        return cd['password']
