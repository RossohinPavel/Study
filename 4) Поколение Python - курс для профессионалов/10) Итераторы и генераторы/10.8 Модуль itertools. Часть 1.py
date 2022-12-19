""" Упражнение 1
Реализуйте функцию tabulate(), которая принимает один аргумент:
func — произвольная функция
Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых значений функции
func сначала с аргументом 1, затем 2, затем 3, и так далее.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию tabulate(), но не код,
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    func = lambda x: x
    values = tabulate(func)
    print(next(values))
    print(next(values))
Sample Output 1:
    1
    2
Sample Input 2:
    func = lambda x: x + 10
    values = tabulate(func)

    print(next(values))
    print(next(values))
    print(next(values))
Sample Output 2:
    11
    12
    13
"""
import itertools as it

def tabulate(func):
    yield from map(func, it.count(1))


""" Упражнение 2
Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является факториалом 
очередного натурального числа.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию factorials(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = factorials(6)
    
    print(*numbers)
Sample Output 1:
    1 2 6 24 120 720
Sample Input 2:
    numbers = factorials(2)
    
    print(next(numbers))
    print(next(numbers))
Sample Output 2:
    1
    2
"""
import itertools as it

def factorials(n):
    yield from it.accumulate(range(1, n+1), lambda x, y: x*y)


""" Упражнение 3
Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.
Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных 
латинских букв:
1, A, 2, B, 3, C, .., X, 25, Y, 26, Z
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию alnum_sequence(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    alnum = alnum_sequence()
    
    print(*(next(alnum) for _ in range(55)))
Sample Output 1:
    1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 
    26 Z 1 A 2
Sample Input 2:
    alnum = alnum_sequence()
    
    print(*(next(alnum) for _ in range(100)))
Sample Output 2:
    1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 
    26 Z 1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X
"""
import itertools as it
from string import ascii_uppercase

def alnum_sequence():
    def seq():
        for i, v in enumerate(ascii_uppercase, 1):
            yield i
            yield v
    yield from it.cycle(x for x in seq())


""" Упражнение 4
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, каждый из которых 
является итерируемым объектом.
Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых объектов: 
сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее; 
после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.
Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию roundrobin(), но не код, 
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(*roundrobin('abc', 'd', 'ef'))
Sample Output 1:
    a d e b f c
Sample Input 2:
    numbers = [1, 2, 3]
    letters = iter('beegeek')
    
    print(*roundrobin(numbers, letters))
Sample Output 2:
    1 b 2 e 3 e g e e k
Sample Input 3:
    print(list(roundrobin()))
Sample Output 3:
    []
"""
def roundrobin(*args):
    args = [iter(x) for x in args]
    c = len(args)
    while c > 0:
        c = len(args)
        for i in range(len(args)):
            try:
                yield next(args[i])
            except:
                c -= 1
