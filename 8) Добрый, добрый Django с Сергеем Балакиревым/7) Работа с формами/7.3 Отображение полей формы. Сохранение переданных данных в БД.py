""" Упражнение 1
Подвиг 4. Объявите класс формы с именем OsagoForm, не связанной с моделью, со следующими полями:

fio: текстовое поле; максимальная длина 200 символов, обязательное, название "Владелец";
email: поле ввода адреса электронной почты; обязательное, название "E-mail";
vin: текстовое поле; максимальная длина 20 символов, обязательное, название "VIN";
model: текстовое поле; максимальная длина 100 символов, обязательное, название "Модель";
stag: числовое поле; необязательное, название "Стаж".

Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: fio, email, vin  и т.д.

P.S. На экран ничего выводить не нужно.
"""
from django import forms

# здесь продолжайте программу
class OsagoForm(forms.Form):
    fio = forms.CharField(max_length=200, label='Владелец')
    email = forms.EmailField(label='E-mail')
    vin = forms.CharField(max_length=20, label='VIN')
    model = forms.CharField(max_length=100, label='Модель')
    stag = forms.IntegerField(label='Стаж', required=False)


""" Упражнение 2
Подвиг 5. Пусть имеется следующий класс модели:

# --------------- models.py -------------------------
class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

# --------------- forms.py -------------------------
# from .models import Subject

# здесь продолжайте программу
Объявите класс формы с именем LectorForm, не связанной с моделью, со следующими полями:

first_name: текстовое поле; максимальная длина 100 символов, обязательное, название "Имя";
last_name: текстовое поле; максимальная длина 100 символов, обязательное, название "Фамилия";
email: поле ввода адреса электронной почты; обязательное, название "E-mail";
salary: числовое поле; необязательное, название "Зарплата";
subject: поле выбора из модели Subject; обязательное, название "Предмет", название не выбранного пункта "Выберите предмет".

Атрибуты класса должны иметь те же названия и порядок, что и в описании.

P.S. На экран ничего выводить не нужно.
"""
# --------------- models.py -------------------------
from django.db import models

class Subject(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField(default=0)

# --------------- forms.py -------------------------
# from .models import Subject

# здесь продолжайте программу
class LectorForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    email = forms.EmailField(label='E-mail')
    salary = forms.IntegerField(required=False, label='Зарплата')
    subject = forms.ModelChoiceField(label='Предмет', queryset=Subject.objects.all(), empty_label='Выберите предмет')


""" Упражнение 3
Подвиг 6. Пусть имеется следующий класс формы:

class ContactForm(forms.Form):
    fio = forms.CharField(max_length=200)
    email = forms.EmailField()
    city = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=12, required=False)
    agree = forms.BooleanField(initial=False, required=False)
    content = forms.CharField(widget=forms.Textarea())
Дополните его следующей информацией:

заголовки полей: fio - "ФИО"; email - "E-mail"; city - "Город"; phone - "Телефон"; agree - "Согласие на обработку"; content - "Сообщение";
полям fio, email, city, phone назначить стиль оформления attrs={'class': 'form-input'};
поле content установить шириной (cols) 30 единиц, высотой (rows) 7 единиц.
"""
from django import forms

class ContactForm(forms.Form):
    fio = forms.CharField(max_length=200, label='ФИО', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    city = forms.CharField(max_length=100, required=False, label='Город', widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(max_length=12, required=False, label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input'}))
    agree = forms.BooleanField(initial=False, required=False, label='Согласие на обработку')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 7}), label='Сообщение')

    
""" Упражнение 4
Подвиг 7 (на повторение). Пусть имеется следующий класс формы:

# --------------- forms.py -------------------------
from django import forms

class LectorForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="Имя")
    last_name = forms.CharField(max_length=100, label="Фамилия")
    email = forms.EmailField(label="E-mail")
    salary = forms.IntegerField(required=False, label="Зарплата")

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import LectorForm

# здесь продолжайте программу
Объявите функцию представления с именем lector_add, в которой:

при POST-запросе формируется заполненная форма LectorForm; выполняется проверка корректности данных формы; если данные корректны, то возвращается объект формы;
при GET-запросе создается пустая форма LectorForm; с помощью функции render формируется HTML-документ по шаблону 'lector/addlector.html' с передачей в него объекта формы LectorForm через переменную (ключ) form.
P.S. На экран ничего выводить не нужно.
"""
# --------------- forms.py -------------------------
from django import forms

class LectorForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="Имя")
    last_name = forms.CharField(max_length=100, label="Фамилия")
    email = forms.EmailField(label="E-mail")
    salary = forms.IntegerField(required=False, label="Зарплата")

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import LectorForm

# здесь продолжайте программу
def lector_add(request):
    if request.POST:
        return LectorForm(request.POST)
    
    return render(request, 'lector/addlector.html', {'form': LectorForm()})
