""" Упражнение 1
Подвиг 3. С помощью стандартной функции send_mail() фреймворка Django:

from django.core.mail import send_mail
выполните отправку следующего сообщения:

E-mail отправителя: balakirev@sitewomen.ru;
список E-mail получателей: sergey@supermail.com
тема письма: "Django 4";
текст письма: "Спасибо Django, что ты есть!";
В программе нужно только вызвать функцию send_mail() для отправки указанного письма, больше ничего.
"""
from django.core.mail import send_mail

# здесь вызывайте функцию send_mail()
send_mail(
    "Django 4",
    "Спасибо Django, что ты есть!",
    'balakirev@sitewomen.ru',
    ['sergey@supermail.com']
)


""" Упражнение 2
Подвиг 5 (на повторение). Пусть имеется следующий фрагмент программы:

# --------- views.py ------------------------
from django.views import View
# from django.shortcuts import render

class PostView(View):
    def get(self, request):
        return render(request, 'post/post_detail.html', {'title': 'Добавление статьи'})


# --------- urls.py ------------------------
from django.urls import path
# from .views import PostView

urlpatterns = [
    # здесь прописывайте маршрут
]
Необходимо в коллекции urlpatterns с помощью функции path прописать маршрут связи URL-адреса:

http://127.0.0.1:8000/main/

с классом представления PostView. Имя маршрута определить строкой 'mainpage'.

P.S. На экран ничего выводить не нужно.
"""
# --------- views.py ------------------------
from django.views import View
# from django.shortcuts import render

class PostView(View):
    def get(self, request):
        return render(request, 'post/post_detail.html', {'title': 'Добавление статьи'})


# --------- urls.py ------------------------
from django.urls import path
# from .views import PostView

urlpatterns = [
    # здесь прописывайте маршрут
    path('main/', PostView.as_view(), name='mainpage')
]
