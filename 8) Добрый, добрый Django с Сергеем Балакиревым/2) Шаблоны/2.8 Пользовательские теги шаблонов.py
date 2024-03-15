""" Упражнение 1
Подвиг 2. Необходимо продолжить программу для объявления простого шаблонного тега (simple tag) в виде функции get_default_title(), которая не имеет никаких параметров и возвращает строку "Заголовок по умолчанию".
P.S. В программе нужно только создать простой тег. Вызывать его не нужно.
"""
from django import template

register = template.Library()

# здесь продолжайте программу
@register.simple_tag()
def get_default_title():
    return "Заголовок по умолчанию"


""" Упражнение 2
Подвиг 3. Необходимо усовершенствовать предыдущую программу и объявить простой шаблонный тег 
(simple tag) в виде функции:
def get_default_title(title="Без заголовка"): ...
которая принимает один параметр title с начальным значением "Без заголовка" и возвращает его в виде строки.
P.S. В программе нужно только создать простой тег. Вызывать его не нужно.
"""
from django import template

register = template.Library()

# здесь продолжайте программу
@register.simple_tag()
def get_default_title(title="Без заголовка"):
    return title


""" Упражнение 3
Подвиг 6. Необходимо продолжить программу для объявления включающего шаблонного тега 
(inclusion tag), использующего шаблон 'women/mainmenu.html', и реализованного в виде функции show_list(), 
которая не имеет никаких параметров и передающая в указанный шаблон данные в виде словаря:
{'items': ['about', 'contact', 'docs']}
P.S. В программе нужно только создать включающий тег. Вызывать его не нужно.
"""
from django import template

register = template.Library()

# здесь продолжайте программу
@register.inclusion_tag('women/mainmenu.html')
def show_list():
    return {'items': ['about', 'contact', 'docs']}


""" Упражнение 4
Подвиг 7. Необходимо продолжить программу для объявления включающего шаблонного тега (inclusion tag), 
использующего шаблон 'women/mainmenu.html', и реализованного в виде функции:
def show_list(items=None): ...
с одним параметром items и передачей в указанный шаблон данные в виде следующего словаря:
{'items': items}
P.S. В программе нужно только создать включающий тег. Вызывать его не нужно.
"""
from django import template

register = template.Library()

# здесь продолжайте программу
@register.inclusion_tag('women/mainmenu.html')
def show_list(items=None):
    return {'items': items}
