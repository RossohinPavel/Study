""" Упражнение 1
Подвиг 1. Пусть в файле settings.py параметр TEMPLATES определен следующим образом:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'profile.context_processors.default_data',
            ],
        },
    },
]
Необходимо в файле profile/context_processors.py определить контекстный процессор default_data для передачи в шаблоны следующих переменных:

default_avatar: 'profile/default_avatar.jpg';
default_auth: 'username/password'.
P.S. На экран ничего выводить не нужно.
"""
# ------------------- settings.py ---------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'profile.context_processors.default_data',
            ],
        },
    },
]

# ------------------- profile/context_processors.py ---------------------
# from django.shortcuts import render

# здесь объявляйте функцию
def default_data(request):
    return {'default_avatar': 'profile/default_avatar.jpg', 'default_auth': 'username/password'}


""" Упражнение 2
Подвиг 3 (на повторение). Необходимо продолжить программу для объявления простого шаблонного тега (simple tag) в виде функции get_default_title(), которая не имеет никаких параметров и возвращает строку "Заголовок по умолчанию".
P.S. В программе нужно только создать простой тег. Вызывать его не нужно.
"""
from django import template

register = template.Library()

# здесь продолжайте программу
@register.simple_tag
def get_default_title():
    return "Заголовок по умолчанию"


""" Упражнение 3
Подвиг 4 (на повторение). Необходимо продолжить программу для объявления включающего шаблонного тега (inclusion tag), использующего шаблон 'women/mainmenu.html', и реализованного в виде функции show_list(), которая не имеет никаких параметров и передающая в указанный шаблон данные в виде словаря:
{'items': ['about', 'contact', 'docs']}
P.S. В программе нужно только создать включающий тег. Вызывать его не нужно.
"""
from django import template

register = template.Library()

# здесь продолжайте программу
@register.inclusion_tag('women/mainmenu.html')
def show_list():
    return {'items': ['about', 'contact', 'docs']}
