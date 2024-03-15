""" Упражнение 1
Подвиг 5. На вход подается строка с заголовком страницы:
title_page = input()
Необходимо преобразовать этот заголовок в слаг (slug), используя стандартный фильтр slugify 
фреймворка Django. Результирующую строку вывести в консоль.

Sample Input: Sergey Balakirev
Sample Output: sergey-balakirev
"""
from django.template.defaultfilters import slugify

title_page = input()

# здесь продолжайте программу
print(slugify(title_page))


""" Упражнение 2
Подвиг 6. На вход подается строка с заголовком страницы:
title_page = input()
Необходимо удалить из строки title_page все символы двоеточий, используя стандартный 
фильтр фреймворка Django (подумайте какой). Результирующую строку вывести в консоль.
Sample Input: username: Sergey, password: 1234
Sample Output: username Sergey, password 1234
"""
# здесь импортируйте фильтр (из ветки django.template.defaultfilters)
from django.template.defaultfilters import cut

title_page = input()
# здесь продолжайте программу
print(cut(title_page, ':'))


""" Упражнение 3
Подвиг 7. На вход подается строка из пунктов меню, записанных через точку с запятой:
menu = list(map(str.strip, input().split(";")))
С помощью стандартных фильтров фреймворка Django необходимо выбрать первый и последний 
элементы списка menu и вывести их в консоль в виде одной строки в формате:
<первый элемент> <последний элемент>
Sample Input: main; addpage; contact; about
Sample Output: main about
"""
# здесь импортируйте необходимые фильтры (из ветки django.template.defaultfilters)
from django.template.defaultfilters import first, last

menu = list(map(str.strip, input().split(";")))

# здесь продолжайте программу
print(first(menu), last(menu))
