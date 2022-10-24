""" Упражнение 1
Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку через
разделитель (sep). Если разделитель не задан, им служит пробел.
Примечание 1. Обратите внимание, что функция concat() должна принимать не список, а именно переменное количество
аргументов.
Примечание 2. Приведенный ниже код, при условии, что функция concat() написана правильно
    print(concat('hello', 'python', 'and', 'stepik'))
    print(concat('hello', 'python', 'and', 'stepik', sep='*'))
    print(concat('hello', 'python', sep='()()()'))
    print(concat('hello', sep='()'))
    print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
должен выводить:
    hello python and stepik
    hello*python*and*stepik
    hello()()()python
    hello
    1$$2$$3$$4$$5$$6$$7$$8$$9
Примечание 3. Вызывать функцию concat() не нужно, требуется только реализовать.
"""
def concat(*args, sep=' '):
    return sep.join(map(str, args)) if len(args) > 1 else args[0]


""" Упражнение 2
Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().
def product_of_odds(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result
Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование встроенных функций filter() и reduce(), 
однако лучше сделать это задание честно 😃.
Примечание 2. Вызывать функцию product_of_odds() не нужно, требуется только реализовать ее в функциональном стиле.
"""
from functools import reduce
from operator import mul
def product_of_odds(data):
    return reduce(mul, filter(lambda x: x % 2 == 1 ,data), 1)


""" Упражнение 3
Дан список слов words. Допишите код после оператора распаковки (*), который оборачивает в двойные кавычки все элементы 
списка words, а затем печатает результат на одной строке через пробел.
Примечание. Вспомните про встроенную функцию map() и анонимные функции lambda.
"""
words = 'the world is mine take a look what you have started'.split()
print(*map(lambda x: f'\"{x}\"', words))


""" Упражнение 4
Дан список целых чисел numbers. Допишите код после оператора распаковки (*), для удаления из списка всех 
чисел-палиндромов и печати результата на одной строке через пробел.
Примечание. Вспомните про встроенную функцию filter() и анонимные функции lambda.
"""
numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x) != str(x)[::-1], numbers))


""" Упражнение 5
Дан список numbers, состоящий из кортежей. Допишите пропущенную часть программы, чтобы список sorted_numbers был 
упорядочен по убыванию среднего арифметического элементов кортежей списка numbers.
Примечание. Вспомните про анонимные функции lambda.
"""
numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12),
           (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
sorted_numbers = sorted(numbers, reverse=True, key=lambda x: sum(x) / len(x))
print(sorted_numbers)


""" Упражнение 6
Напишите функцию call(), которая принимает произвольную функцию и аргументы для неё и делает вызов переданной функции, 
возвращая ее значение.
Примечание 1. Приведенный ниже код, при условии, что функция call() написана правильно
def mul7(x):
    return x * 7
def add2(x, y):
    return x + y
def add3(x, y, z):
    return x + y + z
print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))
должен выводить:
    70
    9
    80
    False
Примечание 2. Вызывать функцию call() не нужно, требуется только реализовать ее.
"""
def call(func, *args):
    return func(*args)


""" Упражнение 7
Напишите функцию compose(), которая принимает на вход две других одноаргументных функции f и g и возвращает новую 
функцию. Эта новая функция также должна принимать один аргумент x и применять к нему исходные функции в нужном 
порядке: для функций f и g порядок применения должен выглядеть, как f(g(x)).
Примечание 1. Приведенный ниже код, при условии, что функция compose() написана правильно
def add3(x):
    return x + 3
def mul7(x):
    return x * 7
print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))
должен выводить:
    28
    17
    3333333
    35
Примечание 2. Вызывать функцию compose() не нужно, требуется только реализовать ее.
Примечание 3. С точки зрения математики, композиция функций f и g — это новая функция h(x) = f(g(x)), при этом порядок 
применения функций f и g важен! 
"""
def compose(f, g):
    return lambda x: f(g(x))


""" Упражнение 8
Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций (+, -, *, /) 
и возвращает функцию двух аргументов для соответствующей операции.
Примечание 1. Приведенный ниже код, при условии, что функция arithmetic_operation() написана правильно
    add = arithmetic_operation('+')
    div = arithmetic_operation('/')
    print(add(10, 20))
    print(div(20, 5))
должен выводить:
    30
    4.0
Примечание 2. Вызывать функцию arithmetic_operation() не нужно, требуется только реализовать ее.
Примечание 3. Модуль operator может быть полезен при решении этой задачи (функции модуля тут). 
"""
from operator import *
def arithmetic_operation(operation):
    d = {'+': add, '-': sub, '*': mul, '/': truediv}
    return d[operation]


""" Упражнение 9
Дана строка из разделенных пробелами слов в разных регистрах. Напишите программу, которая отсортирует слова независимо 
от регистра, а затем выведет их. Отсортированные слова должны выводиться на печать в исходном регистре, в каком 
переданы программе на вход.
Формат входных данных
На вход программе подается строка из разделенных пробелами слов в разных регистрах.
Формат выходных данных
Программа должна вывести строку разделенных пробелом отсортированных слов в прежних регистрах.
Примечание 1. Решите задачу в одну строку кода 😎.
Примечание 2. Встроенная функция sorted() сортирует строки в лексикографическом порядке, но учитывает регистр буквы. 
Любая буква в верхнем регистре считается идущей раньше, чем буква в нижнем регистре.
Sample Input:
    cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo
Sample Output:
    bee cat CatAlo cate CATERS Cats cATwalk dolphin Frog FROGs mOus mouse
"""
print(*sorted(input().split(), key=lambda x: x.lower()))


""" Упражнение 10
Гематрией слова называется сумма числовых значений входящих в него букв.
Для вычисления гематрии слова в этой задаче:
переведём слово в верхний регистр;
числовое значение буквы вычислим как код(буквы) - код(буквы A).
На вход программе подается натуральное число nn, а затем nn строк английских слов в разных регистрах.
Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке) в порядке возрастания 
их гематрии. Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке.
Формат входных данных
На вход программе подается натуральное число nn, а затем nn строк английских слов в разных регистрах.
Формат выходных данных
Программа должна отсортировать слова в соответствии с условием задачи.
Примечание 1. Для получения кода символа воспользуйтесь встроенной функцией ord().
Примечание 2. Слова во входных данных могут повторяться.
Примечание 3. Пусть требуется вычислить гематрию слова BaSis. Переводим его в верхний регистр BASIS. 
Для каждого символа в слове находим его код с помощью встроенной функции ord():
    ord('B') = 66
    ord('A') = 65
    ord('S') = 83
    ord('I') = 73
    ord('S') = 83
В соответствии с условием задачи вычисляем числовое значение буквы как код(буквы) - код(буквы A). Вычитаем из кода 
каждой буквы значение ord('A') = 65:
    ord('B') - ord('A') = 66 - 65 = 1
    ord('A') - ord('A') = 65 - 65 = 0
    ord('S') - ord('A') = 83 - 65 = 18
    ord('I') - ord('A') = 73 - 65 = 8
    ord('S') - ord('A') = 83 - 65 = 18
Гематрия слова BaSis равна 1+0+18+8+18=45. 
Sample Input 1:
    4
    basis
    after
    chief
    agenda
Sample Output 1:
    agenda
    chief
    after
    basis
Sample Input 2:
    4
    Basis
    afTEr
    CHief
    agenda
Sample Output 2:
    CHief
    agenda
    Basis
    afTEr
"""
l = [input() for _ in range(int(input()))]
l.sort()
l.sort(key=lambda w: sum(map(lambda x: ord(x) - 65, w.upper())))
print(*l, sep='\n')


""" Упражнение 11
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.
В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел (октетов) 
со значением от 00 до 255255, разделённых точками, например, 192.168.1.2
Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в соответствии с десятичным 
представлением.
Формат входных данных
На вход программе подается число n (n≥1) – количество IP-адресов. Затем nn строк с корректными IP-адресами.
Формат выходных данных
Программа должна вывести IP-адреса в порядке возрастания в соответствии с десятичным представлением.
Примечание 1. Чтобы перевести IP-адрес 192.168.1.2 в десятичное число мы используем формулу:
192*256^3 + 168*256^2 + 1*256^1 + 2*256^0 = 3232235778
Примечание 2. Используйте необязательный аргумент key.
Sample Input:
    9
    128.199.44.24
    128.199.201.245
    143.198.168.95
    172.67.181.62
    172.67.222.111
    172.67.10.90
    45.8.106.59
    203.13.32.156
    172.67.181.194
Sample Output:
    45.8.106.59
    128.199.44.24
    128.199.201.245
    143.198.168.95
    172.67.10.90
    172.67.181.62
    172.67.181.194
    172.67.222.111
    203.13.32.156
"""
def ss(st):
    st = list(map(int, st.split('.')))
    return sum(map(lambda x, y: x*256**y, st, range(len(st)-1, -1, -1)))
l = [input() for _ in range(int(input()))]
l.sort(key=ss)
print(*l, sep='\n')
