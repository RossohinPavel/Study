""" Упражнение 1
Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max()
выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое
значение элементов.
Примечание. Используйте необязательный аргумент key.
"""
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]
print(min(numbers, key=lambda x: sum(x)/len(x)))
print(max(numbers, key=lambda x: sum(x)/len(x)))


""" Упражнение 2
Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от 
начала координат (точки (0;0)). Программа должна вывести отсортированный список.
Примечание. Расстояние от начала координат O(0;0) до точки A(x;y) равно OA = {x^2+y^2}**0.5
Примечание. Используйте необязательный аргумент key.
"""
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
points.sort(key=lambda x: (x[0]**2 + x[1]**2)**0.5)
print(points)


""" Упражнение 3
Дан список numbers, содержащий кортежи чисел. Напишите программу, которая сортирует и выводит список numbers 
в соответствии с суммой минимального и максимального элемента кортежа.
Примечание 1. В этой задаче мы считаем, что кортеж (2,1,3) меньше кортежа (6,4,5), так как 1+3<4+6. 
При этом кортеж (1,2,9) равен кортежу (4,5,6), так как 1+9 = 4+6.
Примечание 2. Используйте необязательный аргумент key.
"""
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
           (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
numbers.sort(key=lambda x: min(x) + max(x))


""" Упражнение 4
писок athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
Напишите программу сортировки списка спортсменов по указанному полю:
    1: по имени;
    2: по возрасту;
    3: по росту;
    4: по весу.
Формат входных данных
    На вход программе подается натуральное число от 1 до 4 – номер поля по которому требуется отсортировать список.
Формат выходных данных
    Программа должна вывести отсортированный по заданному полю список в соответствии с примерами.
Примечание. Решите задачу без использования условного оператора.
Sample Input 1: 
    3
Sample Output 1:
    Рустам 10 128 30
    Дима 10 130 35
    Тимур 11 135 39
    Руслан 9 140 33
    Матвей 17 168 68
    Амир 16 170 70
    Рома 16 188 100
    Петя 15 190 90
"""
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
d = {'1': lambda x: x[0], '2': lambda x: x[1], '3': lambda x: x[2], '4': lambda x: x[3]}
athletes.sort(key=d[input()])
for i in athletes:
    print(*i)


""" Упражнение 5
Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.
Список возможных функций:
    квадрат: функция принимает число и возвращает его квадрат;
    куб: функция принимает число и возвращает его куб;
    корень: функция принимает число и возвращает корень квадратный из этого числа;
    модуль: функция принимает число и возвращает его модуль;
    синус: функция принимает число (в радианах) и возвращает синус этого числа.
Формат входных данных
На вход программе подается целое число и название функции, записанные на отдельных строках.
Формат выходных данных
Программа должна выдать результат применения функции к числу.
Примечание. Решите задачу без использования условного оператора.
Sample Input 1:
    5
    квадрат
Sample Output 1:
    25
Sample Input 2:
    -3
    модуль
Sample Output 2:
    3
Sample Input 3:
    10
    куб
Sample Output 3:
    1000
"""
from math import sin
d = {'квадрат': lambda x: x ** 2,
     'куб': lambda x: x ** 3,
     'корень': lambda x: x ** 0.5,
     'модуль': lambda x: abs(x),
     'синус': lambda x: sin(x)}
a = int(input())
print(d[input()](a))


""" Упражнение 6
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.

Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если два числа имеют 
одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.
Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
Формат выходных данных
Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы 
одним пробелом.
Sample Input 1:
    12 14 79 7 4 123 45 90 111
Sample Output 1:
    12 111 4 14 123 7 45 90 79
Sample Input 2:
    10 11 12 13 14 15 16 17 18 19 20 21 22 23
Sample Output 2:
    10 11 20 12 21 13 22 14 23 15 16 17 18 19
"""
l = input().split()
l.sort(key=lambda x: sum(map(int, x)))
print(*l)


""" Упражнение 7
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. При этом, если у двух чисел 
одинаковая сумма цифр, их следует вывести в порядке неубывания.
Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
Формат выходных данных
Программа должна вывести отсортированный список чисел в соответствии с условием задачи, разделяя его элементы 
одним пробелом.
"""
l = input().split()
l.sort(key=lambda x: int(x))
l.sort(key=lambda x: sum(map(int, x)))
print(*l)
