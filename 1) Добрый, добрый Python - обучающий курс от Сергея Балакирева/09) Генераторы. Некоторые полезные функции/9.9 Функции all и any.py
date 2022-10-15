""" Упражнение 1
Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными. Вывести True, если
это так и False - в противном случае. Задачу реализовать с использованием одной из функций: any или all.
Sample Input: 2 4 6 8 22 56
Sample Output: True
"""
print(all(map(lambda x: int(x) % 2 == 0, input().split())))


""" Упражнение 2
Вводится строка вещественных чисел через пробел. Необходимо определить, есть ли среди них хотя бы одно отрицательное. 
Вывести True, если это так и False - в противном случае.
Задачу реализовать с использованием одной из функций: any или all.
Sample Input: 8.2 -11.0 20 3.4 -1.2
Sample Output: True
"""
print(any(map(lambda x: float(x) <= 0, input().split())))


""" Упражнение 3
Объявить функцию с именем is_string, на вход которой поступает коллекция (список, кортеж, множество). Она должна 
возвращать True, если все элементы коллекции строки и False - в противном случае.
Сигнатура функции должна быть, следующей: def is_string(lst): ...
Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран. Задачу реализовать с 
использованием одной из функций: any или all.
Sample Input:
Sample Output: True
"""
def is_string(lst):
    return all(map(lambda x: type(x) == str, lst))


""" Упражнение 4
Вводятся оценки студента в одну строчку через пробел. Необходимо определить, имеется ли в этом списке хотя бы одна 
оценка ниже тройки. Если это так, то вывести на экран строку "отчислен", иначе - "учится".
Задачу реализовать с использованием одной из функций: any или all.
Sample Input: 3 3 3 2 3 3
Sample Output: отчислен
"""
print("отчислен" if any(map(lambda x: int(x) < 3, input().split())) else "учится")


""" Упражнение 5
Вводится текущее игровое поле для игры "Крестики-нолики" в виде следующей таблицы:
# x o
x # x
o o #
Здесь # - свободная клетка. Нужно объявить функцию с именем is_free, на вход которой поступает игровое поле в виде 
двумерного (вложенного) списка. Данная функция должна возвращать True, если есть хотя бы одна свободная клетка и 
False - в противном случае. Сигнатура функции должна быть, следующей: def is_free(lst): ...
Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран. Задачу реализовать с 
использованием одной из функций: any или all.
P. S. Считывание входного списка делать не нужно!!! Только определить функцию.
Sample Input:
    # x o
    x # x
    o o #
Sample Output:
    True
"""
def is_free(lst):
    return any(map(lambda x: '#' in x, lst))
