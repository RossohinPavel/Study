""" Упражнение 1
Подвиг 2. Пусть в файле users/authentication.py приложения users объявлен следующий класс аутентификации через ВКонтакте:

# -------------- authentication.py -----------------------
from django.contrib.auth.backends import BaseBackend

class VKAuthBackend(BaseBackend):
    "Бэкенд авторизации через ВК"

# -------------- settings.py -----------------------

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
Добавьте в список AUTHENTICATION_BACKENDS бэкенд VKAuthBackend так, чтобы он использовался в первую очередь.
"""
# -------------- authentication.py -----------------------
# from django.contrib.auth.backends import BaseBackend

class VKAuthBackend(BaseBackend):
    "Бэкенд авторизации через ВК"

# -------------- settings.py -----------------------

AUTHENTICATION_BACKENDS = [
    'users.authentication.VKAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]
