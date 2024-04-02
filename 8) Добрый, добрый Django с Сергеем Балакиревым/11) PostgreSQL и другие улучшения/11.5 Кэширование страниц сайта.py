""" Упражнение 1
Подвиг 6. С помощью объекта cache:

from django.core.cache import cache
сохраните в кэше данные с ключом 'https://proproprogs.ru' и значением 'Главная страница'. Время хранения кэша выберите самостоятельно, но не менее одной минуты.
"""
from django.core.cache import cache

# здесь продолжайте программу
cache.set('https://proproprogs.ru', 'Главная страница', 69)


""" Упражнение 2
Подвиг 7. Пусть в кэш через объект cache были сохранены данные с ключом 'https://sitewomen.ru'. Прочитайте данные по этому ключу и выведите их в консоль.
"""
from django.core.cache import cache

# здесь продолжайте программу
print(cache.get('https://sitewomen.ru'))
