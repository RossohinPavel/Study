""" Упражнение 1
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
    chainmap — объект типа ChainMap, элементами которого являются словари
    key — произвольный объект
Функция должна возвращать множество, элементами которого являются все значения по ключу key из всех словарей в chainmap.
Если ключ key отсутствует в chainmap, функция должна вернуть пустое множество.
Примечание 1. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит словари с хешируемыми значениями.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_values(),
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    result = get_all_values(chainmap, 'name')

    print(*sorted(result))
Sample Output 1:
    Arthur Timur
Sample Input 2:
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    result = get_all_values(chainmap, 'age')

    print(result)
Sample Output 2:
    set()
"""
from collections import ChainMap
def get_all_values(chainmap, key):
    return set([x.get(key) for x in chainmap.maps if key in x])


""" Упражнение 2
Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:
    chainmap — объект типа ChainMap, элементами которого являются словари
    key — хешируемый объект
    value — произвольный объект
Функция должна изменять все значения по ключу key во всех словарях в chainmap на value. Если ключ key отсутствует в 
chainmap, функция должна добавить пару key: value в первый словарь.
Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать значение None.
Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит хотя бы один словарь.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию deep_update(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
    deep_update(chainmap, 'name', 'Dima')
    
    print(chainmap)
Sample Output 1:
    ChainMap({'city': 'Moscow'}, {'name': 'Dima'}, {'name': 'Dima'})
Sample Input 2:
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    deep_update(chainmap, 'age', 20)
    
    print(chainmap)
Sample Output 2:
    ChainMap({'name': 'Arthur', 'age': 20}, {'name': 'Timur'})
"""
from collections import ChainMap
def deep_update(chainmap, key, value):
    if key in chainmap.keys():
        for d in chainmap.maps:
            if key in d:
                d[key] = value
    else:
        chainmap[key] = value


""" Упражнение 3
Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:
    chainmap — объект типа ChainMap, элементами которого являются словари
    key — произвольный объект
    from_left — булево значение, по умолчанию равное True
Функция должна возвращать значение по ключу key из chainmap, причем:
если from_left имеет значение True, поиск ключа в chainmap должен происходить от первого словаря к последнему
если from_left имеет значение False, поиск ключа в chainmap должен происходить от последнего словаря к первому
Если ключ key отсутствует в chainmap, функция должна вернуть значение None.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_value(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    
    print(get_value(chainmap, 'name'))
Sample Output 1:
    Arthur
Sample Input 2:
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    
    print(get_value(chainmap, 'name', False))
Sample Output 2:
    Timur
Sample Input 3:
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
    
    print(get_value(chainmap, 'age'))
Sample Output 3:
    None
"""
from collections import ChainMap
def get_value(chainmap, key, from_left=True):
    if from_left is False:
        chainmap.maps.reverse()
    return chainmap.get(key, None)
