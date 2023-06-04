""" Упражнение 1
Будем считать, что игровое поле для игры в дартс представляет собой квадратную матрицу, заполненную натуральными
числами, расположенными в порядке возрастания от краев к центру. Стороной игрового поля будем называть сторону
квадратной матрицы, которую представляет это поле.
Напишите программу, которая создает поле для игры в дартс определенного размера.
Формат входных данных
На вход программе подается единственное натуральное число — сторона игрового поля.
Формат выходных данных
Программа должна создать и вывести игровое поле с заданной стороной.
Примечание 1. Гарантируется, что сторона игрового поля не превышает 18.
Sample Input 1: 1
Sample Output 1:
1
Sample Input 2: 2
Sample Output 2:
1 1
1 1
Sample Input 3: 3
Sample Output 3:
1 1 1
1 2 1
1 1 1
Sample Input 4: 4
Sample Output 4:
1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1
Sample Input 5: 5
Sample Output 5:
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
"""
def create_matrix(value: int) -> list:
    matrix = [[1 for _ in range(value)] for _ in range(value)]
    for x in range(value):
        for i in range(value):
            for j in range(value):
                if 0 + x < i < value - x - 1 and 0 + x < j < value - x - 1:
                    matrix[i][j] += 1
    return matrix

for row in create_matrix(int(input())):
    print(*row)


""" Упражнение 2
Назовем скобочной последовательностью строку, состоящую из символов ( и ). Будем считать скобочную последовательность 
правильной, если:
    для каждой открывающей скобки есть закрывающая скобка
    скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая 
находится левее
Напишите программу, которая определяет, является ли скобочная последовательность правильной.
Формат входных данных
На вход программе подается строка, представляющая собой скобочную последовательность.
Формат выходных данных
Программа должна вывести True, если введенная скобочная последовательность является правильной, или False в противном 
случае.
Sample Input 1: ()()()
Sample Output 1: True
Sample Input 2: (())
Sample Output 2: True
Sample Input 3: ()()()(
Sample Output 3: False
Sample Input 4: )(
Sample Output 4: False
Sample Input 5: (()))
Sample Output 5: False
"""
def is_correct_bracket(text):
    c = 0
    for i in text:
        if c < 0:
            return False
        if i == '(':
            c += 1
        if i == ')':
            c -= 1
    return c == 0
# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


""" Упражнение 3
Дана последовательность чисел [a1, a2,..., an]. Назовем пару (ai, aj) инверсией, если i<j, а ai > aj. Например, 
последовательность 3,1,4,2 имеет три инверсии (3,1),(3,2),(4,2). Каждая инверсия — это пара элементов, нарушающих 
порядок.
Реализуйте функцию inversions(), которая принимает один аргумент:
    sequence — последовательность, элементами которой являются числа
Функция должна возвращать единственное число — количество инверсий в последовательности sequence.
Примечание 1. Последовательностью будем считать объект, имеющий длину и поддерживающий индексацию. Например, объекты 
типа list или range являются последовательностями.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию inversions(), но не код, 
вызывающий ее.
Sample Input 1:
sequence = [3, 1, 4, 2]

print(inversions(sequence))
Sample Output 1: 3
Sample Input 2:
sequence = [1, 2, 3, 4, 5]

print(inversions(sequence))
Sample Output 2:0
Sample Input 3:
sequence = [4, 3, 2, 1]

print(inversions(sequence))
Sample Output 3:6
Sample Input 4:
sequence = [1, 1, 1, 1, 1, 1]

print(inversions(sequence))
Sample Output 4: 0
"""
def inversions(seq):
    count = 0
    for i in range(len(seq)):
        for j in range(len(seq)):
            if i < j and seq[i] > seq[j]:
                count += 1
    return count


""" Упражнение 4
Артур владеет небольшой коллекцией карточек с покемонами, среди которых встречаются дубликаты. Он хочет оставить 
по одной карточке каждого типа, а остальные продать.
Напишите программу, которая определяет, сколько дубликатов из своей коллекции Артур может продать.
Формат входных данных
На вход программе подается произвольное количество строк, которые представляют коллекцию карточек с покемонами. 
В каждой строке указывается имя покемона с карточки.
Формат выходных данных
Программа должна вывести единственное число — количество карточек, которые из данной коллекции можно продать, чтобы 
оставить по одной карточке каждого типа.
Примечание 1. Рассмотрим первый тест. Чтобы оставить по одной карточке каждого типа, достаточно продать две карточки 
Pichu и одну карточку Tyrogue.
Sample Input 1:
    Pichu
    Pichu
    Tyrogue
    Pichu
    Combee
    Marill
    Tyrogue
Sample Output 1: 3
Sample Input 2:
    Tyrogue
    Pichu
    Combee
Sample Output 2: 0
"""
import sys

lst = [x.strip('\n') for x in sys.stdin]
print(len(lst) - len(set(lst)))


""" Упражнение 5
Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @jsonify, но не код, 
вызывающий его.
Sample Input 1:
    @jsonify
    def make_user(id, live, options):
        return {'id': id, 'live': live, 'options': options}
        
    print(make_user(4, False, None))
Sample Output 1:
    {"id": 4, "live": false, "options": null}
Sample Input 2:
    @jsonify
    def make_list(n):
        return list(range(1, n + 1))
        
    print(make_list(10))
Sample Output 2:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sample Input 3:
    @jsonify
    def make_str(s1, s2):
        return (s1 + s2) * 5
        
    print(make_str('bee', 'geek'))
Sample Output 3:
    "beegeekbeegeekbeegeekbeegeekbeegeek"
"""
import json


def jsonify(func):
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


""" Упражнение 6
Географические координаты представляют собой пару чисел (x,y), где x — широта, y — долгота, причем −90°≤x≤90°, 
−180°≤y≤180°.
Напишите программу, которая принимает произвольное количество строк и определяет, какие из них представляют собой 
корректные географические координаты.
Формат входных данных
На вход программе подается произвольное количество строк, каждая из которых представляет собой пару чисел в следующем 
формате:
    (<координата x>, <координата y>)
Формат выходных данных
Программа должна для каждой строки вывести True, если она представляет собой корректные географические координаты, 
или False в противном случае.
Sample Input 1:
    (75, 180)
    (90, -147.45)
    (77.111, 149.9999)
    (90, 180)
    (55.1, 249.9)
    (120, 150)
Sample Output 1:
    True
    True
    True
    True
    False
    False
Sample Input 2:
    (-90, -180)
    (-90.0, -180.0)
    (-90, 180)
    (90, -180)
    (90.0, 180.0)
Sample Output 2:
    True
    True
    True
    True
    True
Sample Input 3:
    (-90.1, 1)
    (-90.2, 45)
    (10, 180.01)
    (1, 180.0004)
Sample Output 3:
    False
    False
    False
    False
"""
import sys


for line in sys.stdin:
    x, y = map(float, line.strip('\n')[1:-1].split(', '))
    print(-90 <= x <= 90 and -180 <= y <= 180)


""" Упражнение 7
Реализуйте функцию quantify(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
predicate — функция-предикат, то есть функция, возвращающая True или False. Если имеет значение None, то работает 
аналогично функции bool()
Функция quantify() должна считать, для скольких элементов итерируемого объекта iterable функция-предикат predicate 
вернула значение True, и возвращать полученный результат.
Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 10, 
в качестве функции-предиката — функция, возвращающая True, если аргумент больше единицы, или False в противном случае. 
Переданный список чисел содержит ровно 9 чисел, больших единицы.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию quantify(), но не код, 
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылкам:
Sample Input 1:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(quantify(numbers, lambda x: x > 1))
Sample Output 1: 9
Sample Input 2:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(quantify(numbers, lambda x: x % 2 == 0))
Sample Output 2: 5
Sample Input 3:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(quantify(numbers, lambda x: x < 0))
Sample Output 3: 0
"""
def quantify(iterable, predicate):
    if predicate is None:
        predicate = bool
    return sum(1 for x in iterable if predicate(x))


""" Упражнение 8
Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.
Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.
Формат входных данных
На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.
Формат выходных данных
Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат 
в формате DD.MM.YYYY.
Примечание 1. Гарантируется, что подаваемые год и месяц всегда корректны.
Sample Input 1:
    2012
    3
Sample Output 1: 22.03.2012
Sample Input 2:
    2015
    2
Sample Output 2: 26.02.2015
Sample Input 3:
    2018
    6
Sample Output 3: 28.06.2018
"""
import calendar

year, month = int(input()), int(input())
month_matrix = calendar.monthcalendar(year, month)
date = month_matrix[3][3]
if month_matrix[0][3] == 0:
    date = month_matrix[4][3]
print(f'{date}.{str(month).rjust(2, "0")}.{year}')


""" Упражнение 9
Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного 
символа дефиса -.
Реализуйте функцию is_integer(), которая принимает один аргумент:
    string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_integer(), но не код, 
вызывающий ее.
Sample Input 1: print(is_integer('199'))
Sample Output 1: True
Sample Input 2: print(is_integer('-43'))
Sample Output 2: True
Sample Input 3: print(is_integer('5f'))
Sample Output 3: False
Sample Input 4: print(is_integer('5.0'))
Sample Output 4: False
Sample Input 5: print(is_integer('1.1'))
Sample Output 5: False
"""
import re


def is_integer(string):
    return bool(re.fullmatch(r'-?\d+', string))


""" Упражнение 10
Будем считать вещественным числом последовательность из одной или более цифр, которая может начинаться с 
необязательного символа дефиса -, а также содержать на любой позиции одну десятичную точку ., кроме случая, когда точка 
стоит перед символом дефиса.
Реализуйте функцию is_decimal(), которая принимает один аргумент:
    string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False 
в противном случае.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_decimal(), но не код, 
вызывающий ее.
Sample Input 1: print(is_decimal('100'))
Sample Output 1: True
Sample Input 2: print(is_decimal('199.1'))
Sample Output 2: True
Sample Input 3: print(is_decimal('-0.2'))
Sample Output 3:True
Sample Input 4: print(is_decimal('.-95'))
Sample Output 4: False
Sample Input 5: print(is_decimal('-.95'))
Sample Output 5: True
Sample Input 6: print(is_decimal('.10'))
Sample Output 6: True
"""
import re


def is_decimal(string):
    return bool(re.fullmatch(r'-?(?:\d+\.?(\d+)?|(\d+)?\.?\d+)', string))


""" Упражнение 11

"""

""" Упражнение 12

"""

""" Упражнение 13 

"""

""" Упражнение 14

"""

""" Упражнение 15

"""

