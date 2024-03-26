""" Упражнение 1
Подвиг 3. Объявите класс формы с именем ContactForm, не связанной с моделью, со следующими полями:
fio: текстовое поле; максимальная длина 200 символов, обязательное;
email: поле ввода адреса электронной почты; обязательное;
city: текстовое поле; максимальная длина 100 символов, необязательное;
phone: текстовое поле; максимальная длина 12 символов, необязательное;
agree: поле BooleanField; необязательное;
content: поле ввода полноценного многострочного текста; обязательное.
Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: fio, email, city и т.д.
P.S. На экран ничего выводить не нужно.
"""
from django import forms

# здесь продолжайте программу
class ContactForm(forms.Form):
    fio = forms.CharField(max_length=200)
    email = forms.EmailField()
    city = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=12, required=False)
    agree = forms.BooleanField(required=False)
    content = forms.CharField(widget=forms.Textarea())


""" Упражнение 2
Подвиг 4. Пусть имеется следующий класс формы:
# --------------- forms.py -------------------------
from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import AddPostForm
# здесь продолжайте программу
Объявите функцию представления с именем post_new, в которой:
создается пустая форма AddPostForm;
с помощью функции render формируется HTML-документ по шаблону 'women/addpage.html' с передачей в него объекта формы AddPostForm через переменную (ключ) form.
P.S. На экран ничего выводить не нужно.
"""
# --------------- forms.py -------------------------
from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import AddPostForm

# здесь продолжайте программу
def post_new(request):
    return render(request, 'women/addpage.html', {'form': AddPostForm ()})


""" Упражнение 3
Подвиг 5. Пусть имеется следующий класс формы:
# --------------- forms.py -------------------------
from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import AddPostForm
# здесь продолжайте программу
Объявите функцию представления с именем post_new, в которой:
при POST-запросе формируется заполненная форма AddPostForm; выполняется проверка корректности данных формы; если данные корректны, то возвращается объект формы;
при GET-запросе создается пустая форма AddPostForm; с помощью функции render формируется HTML-документ по шаблону 'women/addpage.html' с передачей в него объекта формы AddPostForm через переменную (ключ) form.
P.S. На экран ничего выводить не нужно.
"""
# --------------- forms.py -------------------------
from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import AddPostForm

# здесь продолжайте программу
def post_new(request):
    if request.POST:
        return AddPostForm(request.POST)
    
    return render(request, 'women/addpage.html', {'form': AddPostForm()})


""" Упражнение 4
Подвиг 6. Объявите класс формы с именем CommentForm, не связанной с моделью, со следующими полями:
username: текстовое поле; максимальная длина 100 символов, обязательное;
email: поле ввода адреса электронной почты; обязательное;
agree: поле типа CheckBox; обязательное;
content: поле ввода полноценного многострочного текста; обязательное.

Атрибуты класса должны иметь те же названия и порядок, что и в описании. То есть: username, email, agree и т.д.

# --------------- forms.py -------------------------
from django import forms

# здесь объявляйте класс формы

# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import CommentForm

# здесь объявляйте функцию представления
Объявите функцию представления с именем comment_add, в которой:

при POST-запросе формируется заполненная форма CommentForm; выполняется проверка корректности данных формы; если данные корректны, то возвращается объект формы;
при GET-запросе создается пустая форма CommentForm; с помощью функции render формируется HTML-документ по шаблону 'user/comment_add.html' с передачей в него объекта формы CommentForm через переменную (ключ) form.
P.S. На экран ничего выводить не нужно.
"""
# --------------- forms.py -------------------------
from django import forms

# здесь объявляйте класс формы
class CommentForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    agree = forms.BooleanField()
    content = forms.CharField(widget=forms.Textarea())
    
    
# --------------- views.py -------------------------
# from django.shortcuts import render
# from .forms import CommentForm
def comment_add(request):
    if request.POST:
        return CommentForm(request.POST)
    
    return render(request, 'user/comment_add.html', {'form': CommentForm()})

# здесь объявляйте функцию представления
