""" Упражнение 1
Реализуйте декоратор sandwich, который выводит тексты:
    ---- Верхний ломтик хлеба ----
    ---- Нижний ломтик хлеба ----
до и после вызова декорируемый функции соответственно.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор sandwich, но не код,
вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @sandwich
    def add_ingredients(ingredients):
        print(' | '.join(ingredients))

    add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
Sample Output 1:
    ---- Верхний ломтик хлеба ----
    томат | салат | сыр | бекон
    ---- Нижний ломтик хлеба ----
Sample Input 2:
    @sandwich
    def beegeek():
        return 'beegeek'

    print(beegeek())
Sample Output 2:
    ---- Верхний ломтик хлеба ----
    ---- Нижний ломтик хлеба ----
    beegeek
"""
def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res
    return wrapper


""" Упражнение 2
Напишите программу с использованием декоратора, которая переопределяет функцию print() так, чтобы она печатала весь 
текст в верхнем регистре.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в верхнем регистре.
Примечание 1. Значения sep и end также должны переводиться в верхний регистр.
Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    print('hi', 'there', end='!')
Sample Output 1:
    HI THERE!
Sample Input 2:
    print('are you in trouble?')
Sample Output 2:
    ARE YOU IN TROUBLE?
Sample Input 3:
    print(111, 222, 333, sep='xxx')
Sample Output 3:
    111XXX222XXX333
"""
def new_print(func):
    def wrapper(*args, **kwargs):
        args = [x.upper() if isinstance(x, str) else x for x in args]
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        func(*args, **kwargs)
    return wrapper

print = new_print(print)


""" Упражнение 3
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор do_twice, но не код, 
вызывающий его. 
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @do_twice
    def beegeek():
        print('beegeek')
        
    beegeek()
Sample Output 1:
    beegeek
    beegeek
Sample Input 2:
    @do_twice
    def beegeek():
        print('beegeek')
        
    print(beegeek())
Sample Output 2:
    beegeek
    beegeek
    None
"""
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


""" Упражнение 4
Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func в 
обратном порядке.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор reverse_args, но не код, 
вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @reverse_args
    def power(a, n):
        return a ** n
        
    print(power(2, 3))
Sample Output 1:
    9
Sample Input 2:
    @reverse_args
    def concat(a, b, c):
        return a + b + c
        
    print(concat('apple', 'cherry', 'melon'))
Sample Output 2:
    meloncherryapple
"""
def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*reversed(args), **kwargs)
    return wrapper


""" Упражнение 5
Реализуйте декоратор exception_decorator, который возвращает
кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила свою работу без ошибок, 
где value — возвращаемое значение декорируемой функции
кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор exception_decorator, 
но не код, вызывающий его. 
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @exception_decorator
    def f(x):
        return x**2 + 2*x + 1
        
    print(f(7))
Sample Output 1:
    (64, 'Функция выполнилась без ошибок')
Sample Input 2:
    sum = exception_decorator(sum)
    
    print(sum(['199', '1', 187]))
Sample Output 2:
    (None, 'При вызове функции произошла ошибка')
"""
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper


""" Упражнение 6
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию, 
являются положительными целыми числами.
Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
    TypeError, если аргумент не является целым числом
    ValueError, если аргумент является целым числом, но отрицательным или равным нулю
Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных 
аргументов, несоответствующих разным условиям: TypeError, затем ValueError.
Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes_positive, но не код, 
вызывающий его.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    @takes_positive
    def positive_sum(*args):
        return sum(args)
        
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
Sample Output 1:
    55
Sample Input 2:
    @takes_positive
    def positive_sum(*args):
        return sum(args)
        
    try:
        print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
    except Exception as err:
        print(type(err))
Sample Output 2:
    <class 'ValueError'>
Sample Input 3:
    @takes_positive
    def positive_sum(*args):
        return sum(args)
        
    try:
        print(positive_sum('10', 20, 10))
    except Exception as err:
        print(type(err))
Sample Output 3:
    <class 'TypeError'>
"""
def takes_positive(func):
    def wrapper(*args, **kwargs):
        for i in [*args, *kwargs.values()]:
            if not isinstance(i, int):
                raise TypeError
            if i <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper
