""" Упражнение 1
Подвиг 2. Объявите в программе класс формы UploadDocumentForm, не связанной с моделью, содержащей одно поле:
doc_upload: загрузка произвольных файлов (FileField), обязательное, название "Выберите документ".
"""
from django import forms

# здесь продолжайте программу
class UploadDocumentForm(forms.Form):
    doc_upload = forms.FileField(label='Выберите документ')


""" Упражнение 2
Подвиг 3. Пусть имеется следующий шаблон для загрузки файлов на сервер и фрагмент программы:

# --------------- templates/studio/upload_file.html --------------

<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <p><button type="submit">Загрузить документ</button></p>
</form>

# --------------- forms.py ---------------------------------------

from django import forms

# здесь определяйте класс формы

# --------------- views.py ---------------------------------------
# from django.shortcuts import render
# from .forms import UploadCustomFile

def handle_uploaded_file(upload):
    Функция-заглушка для тестирования загрузки файла
    return upload


# здесь определяйте функцию представления
Необходимо в файле (разделе) forms.py объявить класс формы UploadCustomFile, не связанной с моделью для выбора файлов. Этот класс должен содержать одно поле:

upload_file: класс FileField, обязательное, название "Выберите файл".

Затем, в файле (разделе) views.py объявить функцию представления upload_custom_file со следующим функционалом:

при GET-запросе должна создаваться пустая форма UploadCustomFile и с помощью функции render формироваться HTML-документ по шаблону 'studio/upload_file.html' с передачей в него объекта формы UploadCustomFile через переменную (ключ) form;
при POST-запросе должна формироваться заполненная форма UploadCustomFile, затем, выполняться проверка корректности переданных данных методом is_valid и при успешной проверке сохраняться файл путем вызова метода handle_uploaded_file(form.cleaned_data['upload_file']);
функция upload_custom_file и для GET и для POST запросов должна с помощью функции render возвращать HTML-документ по шаблону 'studio/upload_file.html' с передачей в него сформированного объекта формы UploadCustomFile через переменную (ключ) form.
P.S. На экран ничего выводить не нужно.
"""
# --------------- templates/studio/upload_file.html --------------

# <form action="" method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <p><button type="submit">Загрузить документ</button></p>
# </form>

# --------------- forms.py ---------------------------------------

from django import forms

# здесь определяйте класс формы
class UploadCustomFile(forms.Form):
    upload_file = forms.FileField(label='Выберите файл')
    
# --------------- views.py ---------------------------------------
# from django.shortcuts import render
# from .forms import UploadCustomFile

def handle_uploaded_file(upload):
    """Функция-заглушка для тестирования загрузки файла"""
    return upload


# здесь определяйте функцию представления
def upload_custom_file(request):
    if request.method == 'POST':
        f = UploadCustomFile(request.POST, request.FILES)
        if f.is_valid():
            handle_uploaded_file(f.cleaned_data['upload_file'])
    else:
        f = UploadCustomFile()
    return render(request, 'studio/upload_file.html', {'form': f})


""" Упражнение 3
Подвиг 4. Пусть имеется следующий шаблон для загрузки файлов на сервер и фрагмент программы:

# --------------- templates/studio/upload_file.html --------------

<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <p><button type="submit">Загрузить изображение</button></p>
</form>

# --------------- forms.py ---------------------------------------

from django import forms

# здесь определяйте класс формы

# --------------- views.py ---------------------------------------
# from django.shortcuts import render
# from .forms import UploadImageFile

def handle_uploaded_image(upload):
    ""Функция-заглушка для тестирования загрузки файла""
    return upload


# здесь определяйте функцию представления
Необходимо в файле (разделе) forms.py объявить класс формы UploadImageFile, не связанной с моделью для выбора файлов. Этот класс должен содержать одно поле:

upload_image: класс ImageField, обязательное, название "Выберите изображение".

Затем, в файле (разделе) views.py объявить функцию представления upload_image_file со следующим функционалом:

при GET-запросе должна создаваться пустая форма UploadImageFile и с помощью функции render формироваться HTML-документ по шаблону 'studio/upload_file.html' с передачей в него объекта формы UploadImageFile через переменную (ключ) form;
при POST-запросе должна формироваться заполненная форма UploadImageFile, затем, выполняться проверка корректности переданных данных методом is_valid и при успешной проверке сохраняться файл путем вызова метода handle_uploaded_image(form.cleaned_data['upload_image']);
функция upload_image_file и для GET и для POST запросов должна с помощью функции render возвращать HTML-документ по шаблону 'studio/upload_file.html' с передачей в него сформированного объекта формы UploadImageFile через переменную (ключ) form.
P.S. На экран ничего выводить не нужно.
"""
# --------------- templates/studio/upload_file.html --------------

# <form action="" method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <p><button type="submit">Загрузить изображение</button></p>
# </form>

# --------------- forms.py ---------------------------------------

from django import forms

# здесь определяйте класс формы
class UploadImageFile(forms.Form):
    upload_image = forms.ImageField(label='Выберите изображение')

    
# --------------- views.py ---------------------------------------
# from django.shortcuts import render
# from .forms import UploadImageFile

def handle_uploaded_image(upload):
    """Функция-заглушка для тестирования загрузки файла"""
    return upload


# здесь определяйте функцию представления
def upload_image_file(r):
    if r.method == 'GET':
        f = UploadImageFile()
    if r.method == 'POST':
        f = UploadImageFile(r.POST, r.FILES)
        if f.is_valid():
            handle_uploaded_image(f.cleaned_data['upload_image'])
    
    return render(r, 'studio/upload_file.html', {'form': f})
