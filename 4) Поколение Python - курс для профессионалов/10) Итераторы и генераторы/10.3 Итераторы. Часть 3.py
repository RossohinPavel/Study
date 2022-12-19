""" Упражнение 1
Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор, бесконечно генерирующий
единственное значение — строку i love beegeek!.
Примечание. В тестирующую систему сдайте программу, содержащую только необходимый итератор infinite_love.
Sample Input 1:
    print(next(infinite_love))
Sample Output 1:
    i love beegeek!
Sample Input 2:
    print(next(infinite_love))
    print(next(infinite_love))
    print(next(infinite_love))
Sample Output 2:
    i love beegeek!
    i love beegeek!
    i love beegeek!
"""
infinite_love = iter(lambda: 'i love beegeek!', 0)


""" Упражнение 2
Реализуйте функцию is_iterable(), которая принимает один аргумент:
    obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_iterable(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(is_iterable(18731))
Sample Output 1:
    False
Sample Input 2:
    print(is_iterable('18731'))
Sample Output 2:
    True
Sample Input 3:
    objects = [(1, 13), 7.0004, [1, 2, 3]]
    
    for obj in objects:
        print(is_iterable(obj))
Sample Output 3:
    True
    False
    True
"""
is_iterable = lambda x: '__iter__' in dir(x)


""" Упражнение 3
Реализуйте функцию is_iterator(), которая принимает один аргумент:
obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае. 
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_iterator(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(is_iterator([1, 2, 3, 4, 5]))
Sample Output 1:
    False
Sample Input 2:
    beegeek = map(str.upper, 'beegeek')
    
    print(is_iterator(beegeek))
Sample Output 2:
    True
Sample Input 3:
    beegeek = filter(None, [0, 0, 1, 1, 0, 1])
    
    print(is_iterator(beegeek))
Sample Output 3:
    True
"""

""" Упражнение 4
Реализуйте функцию random_numbers(), которая принимает два аргумента:
    left — целое число
    right — целое число
Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел в диапазоне 
от left до right включительно.
Примечание 1. Гарантируется, что left <= right.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый итератор random_numbers(), 
но не код, вызывающий её.
Примечание 3. Тестовые данные доступны по ссылке.
    Sample Input 1:
    
    iterator = random_numbers(1, 1)
    
    print(next(iterator))
    print(next(iterator))
Sample Output 1:
    1
    1
Sample Input 2:
    iterator = random_numbers(1, 10)
    
    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))
Sample Output 2:
    True
    True
    True
"""
import random

random_numbers = lambda x, y: iter(lambda: random.choice(range(x, y+1)), y+1)
