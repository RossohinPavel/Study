""" Упражнение 1
Реализуйте функцию power(), которая принимает один аргумент:
degree — целое число
Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x и возвращает значение x
в степени degree.
Примечание 1. Рассмотрим пример из первого теста. Вызов power(2) возвращает функцию, которая принимает в качестве
аргумента число и возводит его во вторую степень. Функция присваивается переменной square. Далее полученная функция
вызывается с аргументом 55 и возвращает значение 5^2 = 25
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию power(), но не код,
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    square = power(2)
    print(square(5))
Sample Output 1:
    25
Sample Input 2:
    print(power(3)(3))
Sample Output 2:
    27
Sample Input 3:
    result = power(4)(2)
    print(result)
Sample Output 3:
    16
"""
def power(degree):
    def func(x):
        return x**degree
    return func


""" Упражнение 2
Рассмотрим семейство функций — квадратных трехчленов. Все эти функции имеют один и тот же вид:
f(x) = ax^2 + bx + c
Реализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:
    a — вещественное число, коэффициент aa
    b — вещественное число, коэффициент bb
    c — вещественное число, коэффициент cc
Функция generator_square_polynom() должна возвращать функцию, которая принимает в качестве аргумента вещественное число 
x и возвращает значение выражения ax^2 + bx + c
Примечание 1. Рассмотрим пример из первого теста. Вызов generator_square_polynom(1, 2, 1) возвращает функцию, 
соответствующую квадратному трехчлену x^2 + 2x + 1.  Функция присваивается переменной f. Далее полученная функция 
вызывается с аргументом 5 и возвращает значение 5^2 + 5 * 2 + 1 = 36 
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию generator_square_polynom(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    f = generator_square_polynom(1, 2, 1)
    print(f(5))
Sample Output 1:
    36
Sample Input 2:
    print(generator_square_polynom(9, 52, 64)(8))
Sample Output 2:
    1056
Sample Input 3:
    f = generator_square_polynom(26, 83, 22)
    print(f(55))
Sample Output 3:
    83237
"""
def generator_square_polynom(a, b, c):
    def func(x):
        return a*x**2 + b*x + c
    return func


""" Упражнение 3
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного 
знака и идет до конца адреса. Например:
    https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
    https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green 
Реализуйте функцию sourcetemplate(), которая принимает один аргумент:
    url — URL адрес
Функция sourcetemplate() должна возвращать функцию, которая принимает произвольное количество именованных аргументов 
и возвращает url адрес, объединенный со строкой запроса, сформированной из переданных аргументов. При вызове без 
аргументов она должна возвращать исходный url адрес без изменений.
Примечание 1. Параметры в строке запроса должны располагаться в лексикографическом порядке ключей.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию sourcetemplate(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    url = 'https://beegeek.ru'
    load = sourcetemplate(url)
    print(load(name='timur'))
Sample Output 1:
    https://beegeek.ru?name=timur
Sample Input 2:
    url = 'https://stepik.org/lesson/651459/step/14'
    load = sourcetemplate(url)
    print(load(thread='solutions', unit=648165))
Sample Output 2:
    https://stepik.org/lesson/651459/step/14?thread=solutions&unit=648165
Sample Input 3:
    url = 'https://beegeek.ru'
    load = sourcetemplate(url)
    print(load())
Sample Output 3:
    https://beegeek.ru
"""
def sourcetemplate(url):
    def func(**kwargs):
        qs = '?' + '&'.join([f'{k}={v}' for k, v in sorted(kwargs.items())]) if kwargs else ''
        return url + qs
    return func


""" Упражнение 4
Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
код страны	формат даты
    ru	DD.MM.YYYY
    us	MM-DD-YYYY
    ca	YYYY-MM-DD
    br	DD/MM/YYYY
    fr	DD.MM.YYYY
    pt	DD-MM-YYYY
Реализуйте функцию date_formatter(), которая принимает один аргумент:
    country_code — код страны
Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date) и возвращает 
строку с данной датой в формате страны с кодом country_code.
Примечание 1. Гарантируется, что в функцию date_formatter() передаются только те коды стран, что перечислены в 
приведенной выше таблице.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию date_formatter(), но не код, 
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    date_ru = date_formatter('ru')
    today = date(2022, 1, 25)
    print(date_ru(today))
Sample Output 1:
    25.01.2022
Sample Input 2:
    date_ru = date_formatter('us')
    today = date(2025, 1, 5)
    print(date_ru(today))
Sample Output 2:
    01-05-2025
Sample Input 3:
    date_ru = date_formatter('ca')
    today = date(2015, 12, 7)
    print(date_ru(today))
Sample Output 3:
    2015-12-07
"""
from datetime import date
def date_formatter(country):
    def func(dtf):
        pattern = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d', 'br': '%d/%m/%Y',
                   'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
        return dtf.strftime(pattern[country])
    return func


""" Упражнение 5
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
    values — список чисел
    group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, 
которая должна следовать первой.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию sort_priority(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {5, 7, 2, 3}
    sort_priority(numbers, group)
    
    print(numbers)
Sample Output 1:
    [2, 3, 5, 7, 1, 4, 6, 8]
Sample Input 2:
    numbers = [150, 200, 300, 1000, 50, 20000]
    sort_priority(numbers, [300, 100, 200])
    
    print(numbers)
Sample Output 2:
    [200, 300, 50, 150, 1000, 20000]
Sample Input 3:
    numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort_priority(numbers, (300, 100, 200))
    
    print(numbers)
Sample Output 3:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

