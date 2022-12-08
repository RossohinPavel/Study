""" Упражнение 1
Реализуйте функцию hash_as_key(), которая принимает один аргумент:
objects — список хешируемых объектов
Функция должна возвращать словарь, ключом в котором является хеш-значение объекта из списка objects, а значением —
сам объект. Если хеш-значения некоторых объектов совпадают, их следует объединить в список.
Примечание 1. Элементы в возвращаемом функцией словаре, а также объекты в списке, имеющие равные хеш-значения, должны
располагаться в своем исходном порядке.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию hash_as_key(), но не код,
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    data = [1, 2, 3, 4, 5, 5]

    print(hash_as_key(data))
Sample Output 1:
    {1: 1, 2: 2, 3: 3, 4: 4, 5: [5, 5]}
Sample Input 2:
    data = [-1, -2, -3, -4, -5]

    print(hash_as_key(data))
Sample Output 2:
    {-2: [-1, -2], -3: -3, -4: -4, -5: -5}
Sample Input 3:
    data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

    print(hash_as_key(data))
Sample Output 3:
    {11: 11, 22: 22, 33: 33, 44: 44, 55: 55, 66: 66, 77: 77, 88: 88, 99: 99, 111: 111}
"""
def hash_as_key(objects):
    dct = {}
    for num in objects:
        k = hash(num)
        if k in dct:
            if not isinstance(dct[k], list):
                dct[k] = [dct[k]]
            dct[k].append(num)
        else:
            dct[k] = num
    return dct


""" Упражнение 2
Напишите программу, которая принимает на вход корректный непустой список, корректный непустой кортеж или корректное 
произвольной длины множество, и выполняет следующее:
    если введен список, выводит его последний элемент
    если введен кортеж, выводит его первый элемент
    если введено множество, выводит количество его элементов
Формат входных данных
На вход программе подается корректный непустой список, кортеж или корректное произвольной длины множество.
Формат выходных данных
Программа должна вывести определенное значение, в зависимости от типа введенной коллекции.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    [[1, 2], [3, 4], [5, 6]]
Sample Output 1:
    [5, 6]
Sample Input 2:
    {'Arthur', 'Timur', 'Anri', 'Ruslan', 'Dima'}
Sample Output 2:
    5
Sample Input 3:
    ('black', 'blue', 'red', 'orange', 'green', 'gray')
Sample Output 3:
    black
"""
lst = eval(input())
if isinstance(lst, list):
    print(lst[-1])
elif isinstance(lst, tuple):
    print(lst[0])
elif isinstance(lst, set):
    print(len(lst))


""" Упражнение 3
Напишите программу, которая принимает на вход произвольное количество строк, содержащих корректные математические 
выражения, и выводит значение наибольшего из них.
Формат входных данных
На вход программе подается произвольное количество строк, каждое из которых содержит корректное математическое 
выражение.
Формат выходных данных
Программа должна вычислить значения введенных выражений и вывести набольшее.
Примечание 1. Под корректным математическим выражением подразумевается выражение, полностью соответствующее синтаксису 
языка Python.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    1 + 2 + 3
    2 * 8
    10 * 10 - 1
Sample Output 1:
    99
Sample Input 2:
    1 + 1 + 1 + 1 + 1
    2 * 2 * 2 * 2 * 2
    3 // 3 // 3 // 3 // 3
    4 - 4 - 4 - 4 -4
Sample Output 2:
    32
Sample Input 3:
    (2**3 + 2) * 10 - 4
    100
    ((97 - 19)**4) * 0
    1 + 2 - 3 * 4 // 5 
Sample Output 3:
    100
"""
import sys
print(max(map(lambda x: eval(x.strip()), sys.stdin)), sep='\n')


""" Упражнение 4
Напишите программу, которая определяет минимальное и максимальное значения функции на отрезке в целых точках.
Формат входных данных
На вход программе в первой строке подается корректная функция f(x)f(x), в следующей строке вводятся два целых числа 
a и b, разделенные пробелом, которые представляют границы отрезка [a; b].
Формат выходных данных
Программа должна определить минимальное и максимальное значения функции f(x)f(x) на отрезке [a; b][a;b] в целых точках 
и вывести полученный результат в следующем формате:
    Минимальное значение функции <функция f(x)> на отрезке <отрезок> равно <мин. значение>
    Максимальное значение функции <функция f(x)> на отрезке <отрезок> равно <макс. значение>
Примечание 1. Под корректной функцией подразумевается выражение, полностью соответствующее синтаксису языка Python.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    2*x**2 + 5*x + 7
    -1 5
Sample Output 1:
    Минимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 4
    Максимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 82
Sample Input 2:
    x + 1
    -999 999
Sample Output 2:
    Минимальное значение функции x + 1 на отрезке [-999; 999] равно -998
    Максимальное значение функции x + 1 на отрезке [-999; 999] равно 1000
"""
import sys
form, val = map(str.strip, sys.stdin)
minv, maxv = map(int, val.split())
lst = [eval(form) for x in range(minv, maxv+1)]
print(f'Минимальное значение функции {form} на отрезке [{minv}; {maxv}] равно {min(lst)}')
print(f'Максимальное значение функции {form} на отрезке [{minv}; {maxv}] равно {max(lst)}')
