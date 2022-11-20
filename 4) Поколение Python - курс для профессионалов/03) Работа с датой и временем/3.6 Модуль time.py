""" Упражнение 1
Реализуйте функцию calculate_it(), которая принимает один или более аргументов в следующем порядке:
func — произвольная функция
*args — переменное количество позиционных аргументов, каждый из которых является произвольным объектом
Функция должна возвращать кортеж, первым элементом которого является возвращаемое значение функции func при вызове
с аргументами *args, а вторым — примерное время (в секундах), затраченное на вычисление этого значения.
Примечание 1. Например, если функция add() определена так:
def add(a, b, c):
    time.sleep(3)
    return a + b + c
то вызов
calculate_it(add, 1, 2, 3)
должен вернуть кортеж (6, 3.000720262527466), где 6 — результат вызова add(1, 2, 3), а 3.000720262527466 — примерное
время работы функции add() в секундах.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию calculate_it(), но не код,
вызывающий ее.
"""
import time
def calculate_it(func, *args):
    start = time.monotonic()
    res = func(*args)
    end = time.monotonic()
    return res, end - start


""" Упражнение 2
Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

funcs — список произвольных функций
arg — произвольный объект
Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения 
при вызове с аргументом arg наименьшее количество времени.
Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_the_fastest_func(), 
но не код, вызывающий ее.
"""
import time
def get_the_fastest_func(funcs, arg):
    lst = []
    for f in funcs:
        start = time.monotonic()
        f(arg)
        end = time.monotonic()
        lst.append(end-start)
    return funcs[lst.index(min(lst))]
