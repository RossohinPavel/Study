""" Упражнение 1
Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum, которая бы возвращала текущую
сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. Например:
- для первого числа 1 сумма равна 1;
- для второго числа 2 сумма равна 1+2 = 3
....
- для N-го числа сумма равна 1+2+...+(N-1)+N
Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить.
Sample Input: 5
Sample Output: 1 3 6 10 15
"""
N = int(input())
def get_sum(n):
    for i in range(1, n+1):
        s = 0
        for m in range(0, i+1):
            s += m
        yield s


""" Упражнение 2
Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, которая строится по правилу: каждое 
последующее число равно сумме двух предыдущих. Для разнообразия давайте будем генерировать каждое последующее как сумму 
трех предыдущих чисел. При этом первые три числа равны 1 и имеем такую последовательность: 
1, 1, 1, 3, 5, 9, 17, 31, 57, ...
Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева. 
Итак, на вход программы поступает натуральное число N (N > 5) и необходимо определить функцию-генератор, которая бы 
возвращала N первых чисел последовательности Балакирева (включая первые три единицы).
Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.). Вызовите ее N раз для получения 
N чисел и выведите полученные числа на экран в одну строчку через пробел.
Sample Input: 7
Sample Output: 1 1 1 3 5 9 17
"""
N = int(input())
def get_bal(n):
    a, b, c, d = 0, 0, 0, 0
    for i in range(1, n+1):
        if i > 3:
            d = a + b + c
        else:
            d = 1
        a, b, c = b, c, d
        yield c
for i in get_bal(N):
    print(i, end=' ')


""" Упражнение 3
Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль длиной N 
символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых символов для 
генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе 
которых формируется общий список:
    from string import ascii_lowercase, ascii_uppercase
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и 
делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx в 
диапазоне [a; b] для символа можно с помощью функции randint модуля random:
    import random
    random.seed(1)
    indx = random.randint(a, b)
Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).
Sample Input:
    10
Sample Output:
    riGp?58WAm
    !dX3a5IDnO
    dcdbWB2d*C
    4?DSDC6Lc1
    mxLpQ@2@yM
"""
import random
from string import ascii_lowercase, ascii_uppercase
random.seed(1)
def pas_gen(n):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        s = ''
        for i in range(n):
            indx = random.randint(0, len(chars))
            s = s + chars[indx]
        yield s
a = int(input())
n = 0
while n < 5:
    print(next(pas_gen(a)))
    n += 1


""" Упражнение 4
Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
    from string import ascii_lowercase, ascii_uppercase
    chars = ascii_lowercase + ascii_uppercase
задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и 
длиной в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru
Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
    import random
    random.seed(1)
    indx = random.randint(0, len(chars)-1)
Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно. Выведите первые 
пять сгенерированных email и выведите их в столбик (каждый с новой строки).
Sample Input: 8
Sample Output:
    iKZWeqhF@mail.ru
    WCEPyYng@mail.ru
    FbyBMWXa@mail.ru
    SCrUZoLg@mail.ru
    ubbbPIay@mail.ru
"""
import random
from string import ascii_lowercase, ascii_uppercase
random.seed(1)
def pas_gen(n):
    chars = ascii_lowercase + ascii_uppercase
    while True:
        s = ''
        for i in range(n):
            indx = random.randint(0, len(chars) - 1)
            s = s + chars[indx]
        yield f'{s}@mail.ru'
a = int(input())
n = 0
while n < 5:
    print(next(pas_gen(a)))
    n += 1


""" Упражнение 5
Определите функцию-генератор, которая бы возвращала простые числа. (Простое число - это натуральное число, которое 
делится только на себя и на 1). Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку 
через пробел.
"""
def prost_gen():
    n = 2
    while True:
        flag = True
        for x in range(2, n+1):
            if n % x == 0 and x != n:
                flag = False
        if flag:
            yield n
        n += 1
gen = prost_gen()
x = 0
while x < 20:
    print(next(gen), end=' ')
    x += 1
