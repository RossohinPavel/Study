""" Упражнение 1
Реализуйте функцию drop_while_negative(), которая принимает один аргумент:
iterable — итерируемый объект, элементами которого являются целые числа
Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable, начиная с первого
неотрицательного числа.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию drop_while_negative(),
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [-3, -2, -1, 0, 1, 2, 3]

    print(*drop_while_negative(numbers))
Sample Output 1:
    0 1 2 3
Sample Input 2:
    iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])

    print(*drop_while_negative(iterator))
Sample Output 2:
    0 1 2 3 -4 -5 -6
Sample Input 3:
    iterator = iter([-3, -2, -1, -4, -5, -6])

    print(list(drop_while_negative(iterator)))
Sample Output 3:
    []
"""
import itertools as it

drop_while_negative = lambda n: it.dropwhile(lambda x: x < 0, n)


""" Упражнение 2
Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:
    iterable — итерируемый объект
    obj — произвольный объект
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, 
начиная с элемента, не равного obj.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию drop_this(), но не код, 
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [0, 0, 0, 1, 2, 3]
    
    print(*drop_this(numbers, 0))
Sample Output 1:
    1 2 3
Sample Input 2:
    iterator = iter('bbbbeebee')
    
    print(*drop_this(iterator, 'b'))
Sample Output 2:
    e e b e e
Sample Input 3:
    iterator = iter('ssssssssssssssssssssssss')
    
    print(list(drop_this(iterator, 's')))
Sample Output 3:
    []
"""
import itertools as it

drop_this = lambda iterable, obj: it.dropwhile(lambda x: x == obj, iterable)


""" Упражнение 3
Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция 
predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.
Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве 
аргумента значения.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_true(), но не код,
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [1, 1, 1, 1, 2, 4, 5, 6]
    
    print(first_true(numbers, lambda num: num % 2 == 0))
Sample Output 1:
    2
Sample Input 2:
    numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
    
    print(first_true(numbers, lambda num: num > 10))
Sample Output 2:
    100
Sample Input 3:
    numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
    
    print(first_true(numbers, None))
Sample Output 3:
    69
"""
import itertools as it

def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    try:
        return next(filter(predicate, iterable))
    except:
        return None

# У оператора next есть 2й необязательный параметр, который возвращает свое значение при возникновении StopIterations
from itertools import dropwhile

def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    return next(dropwhile(lambda elem: not predicate(elem), iterable), None)


""" Упражнение 4
Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:
    iterable — итерируемый объект
    n — натуральное число
Функция должна возвращать итератор, генерирующей последовательность из первых n элементов итерируемого объекта iterable.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию take(), но не код,
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(*take(range(10), 5))
Sample Output 1:
    0 1 2 3 4
Sample Input 2:
    iterator = iter('beegeek')
    
    print(*take(iterator, 22))
Sample Output 2:
    b e e g e e k
Sample Input 3:
    iterator = iter('beegeek')
    
    print(*take(iterator, 1))
Sample Output 3:
    b
"""
import itertools as it

take = lambda iterable, n: it.islice(iterable, n)


""" Упражнение 5
Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
n — натуральное число
Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. Если итерируемый объект iterable содержит 
менее n элементов, функция должна вернуть значение None.
Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию take_nth(), но не код, 
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [11, 22, 33, 44, 55]
    
    print(take_nth(numbers, 3))
Sample Output 1:
    33
Sample Input 2:
    iterator = iter('beegeek')
    
    print(take_nth(iterator, 4))
Sample Output 2:
    g
Sample Input 3:
    iterator = iter('beegeek')
    
    print(take_nth(iterator, 10))
Sample Output 3:
    None
"""
import itertools as it

take_nth = lambda iterable, n: next(it.islice(iterable, n-1, n), None)


""" Упражнение 6
Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект, элементами которого являются целые числа
number — произвольное число
Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number. Если таких 
элементов нет, функция должна вернуть число −1.
Примечание 1. Рассмотрим список чисел 10, 2, 14, 7, 7, 18, 20 из первого теста. Первым числом, превосходящим 11, 
является число 14, которое имеет индекс 2.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_largest(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [10, 2, 14, 7, 7, 18, 20]
    
    print(first_largest(numbers, 11))
Sample Output 1:
    2
Sample Input 2:
    iterator = iter([-1, -2, -3, -4, -5])
    
    print(first_largest(iterator, 10))
Sample Output 2:
    -1
Sample Input 3:
    iterator = iter([18, 21, 14, 72, 73, 18, 20])
    
    print(first_largest(iterator, 10))
Sample Output 3:
    0
"""
def first_largest(iterable, n):
    return next((i for i, v in enumerate(iterable) if v > n), -1)
