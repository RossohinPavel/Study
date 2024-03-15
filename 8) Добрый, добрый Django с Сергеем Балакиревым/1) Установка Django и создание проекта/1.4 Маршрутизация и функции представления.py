""" Упражнение 1
Подвиг 3. Запишите функцию представления с именем about, которая бы возвращала клиенту HTTP-ответ со строкой "О сайте".
P. S. Функцию вызывать не нужно, только объявить.
"""
from django.http import HttpResponse, HttpRequest

# здесь объявляйте функцию
def about(r):
    return HttpResponse('О сайте')



""" Упражнение 2
Подвиг 5. Пусть имеется функция представления с именем catalog. Необходимо ее связать с маршрутом так, чтобы она срабатывала на URL-адрес:
http://127.0.0.1:8000/women/cat/
Используйте для этого функцию path() фреймворка Django. Полагается, что коллекция urlpatterns определяется в пакете конфигурации проекта сайта.
"""
from django.urls import path
from django.http import HttpResponse

def catalog(request):
    return HttpResponse("catalog")


urlpatterns = [
    # здесь с помощью функции path() прописывайте новый маршрут
    path('women/cat/', catalog)
]
