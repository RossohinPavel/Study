""" Упражнение 1
Вводится целое положительное число N. Необходимо написать рекурсивную функцию с именем get_rec_N, которая отображает на
экране последовательность целых чисел от 1 до N (включительно). Каждое число выводится с новой строки.
В качестве параметра функция get_rec_N должна принимать одно числовое значение. То есть, иметь только один параметр.
Начальный вызов функции будет выглядеть так: get_rec_N(N)
Вызывать функцию не нужно, только объявить.
Sample Input: 8
Sample Output: 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8
"""
N = int(input())
def get_rec_N(N):
    if N > 1:
        get_rec_N(N - 1)
    print(N)


""" Упражнение 2
Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений, используя 
рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать значение суммы. 
(Выводить на экран она ничего не должна). Вызовите эту функцию и выведите вычисленное значение суммы на экран.
Sample Input: 8 11 -5 4 3
Sample Output: 21
"""
N = list(map(int, input().split()))
def get_rec_sum(N):
    *a, b = N
    if len(a) == 1:
        return int(*a) + b
    else:
        return b + get_rec_sum(a)
print(get_rec_sum(N))


""" Упражнение 3
Вводится натуральное число N. Необходимо с помощью рекурсивной функции fib_rec(N, f=[]) (здесь N - общее количество 
чисел Фибоначчи; f - начальный список этих чисел) сформировать последовательность чисел Фибоначчи по правилу: первые 
два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих. Пример такой последовательности для 
первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...
Функция должна возвращать список сформированной последовательности длиной N. Вызывать функцию не нужно, только объявить.
Sample Input: 7
Sample Output: 1 1 2 3 5 8 13
"""
N = int(input())
def fib_rec(N, f=[]):
    if len(f) < 2:
        f.append(1)
        fib_rec(N, f)
    elif 1 < len(f) < N:
        f.append(f[-2] + f[-1])
        fib_rec(N, f)
    return f


""" Упражнение 4
Вводится целое неотрицательное число n. Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n. 
Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать вычисленное значение.
Вызывать функцию не нужно, только объявить со следующей сигнатурой:
def fact_rec(n): ...
Sample Input: 6
Sample Output: 720
"""
n = int(input())
def fact_rec(n):
    if n == 0:
        return 1
    return fact_rec(n - 1) * n


""" Упражнение 5
Имеется следующий многомерный список:
С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d. 
Функция должна возвращать новый созданный одномерный список.  (Только возвращать, выводить на экран ничего не нужно.)
Вызывать функцию не нужно, только объявить со следующей сигнатурой:
def get_line_list(d,a=[]): ...
где d - исходный список; a - новый формируемый.
"""
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
def get_line_list(d, a=[]):
    for i in d:
        if type(i) == list:
            get_line_list(i)
        else:
            a.append(i)
    return a


""" Упражнение 6
Лягушка прыгает вперед и может скакнуть либо на одно деление, либо сразу на два. Наша задача определить количество 
вариантов маршрутов, которыми лягушка может достичь риски под номером N (натуральное число N вводится с клавиатуры).
Решать задачу следует с применением рекурсивной функции. Назовем ее get_path. Алгоритм решения будет следующий. 
Рассмотрим, например, риску под номером 4. Очевидно, в нее лягушка может скакнуть либо с риски номер 2, либо с риски 
номер 3. Значит, общее число вариантов перемещений лягушки можно определить как: 
get_path(4) = get_path(3) + get_path(2)
Аналогично будет справедливо и для любой риски N: get_path(N) = get_path(N-1) + get_path(N-2)
А начальные условия задачи, следующие:
get_path(1) = 1
get_path(2) = 2
Реализуйте такую рекурсивную функцию, которая должна возвращать количество вариантов перемещений лягушки для 
риски под номером N. Вызовите эту функцию для введенного числа N и отобразите результат на экране.
Sample Input: 7
Sample Output: 21
"""
N = int(input())
def get_path(n):
    if n <= 1:
        return 1
    else:
        return get_path(n-1) + get_path(n-2)
print(get_path(N))


""" Упражнение 7
Вводится список из целых чисел в одну строчку через пробел. Необходимо выполнить его сортировку по возрастанию с помощью 
алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список. Вызовите результирующую функцию 
сортировки для введенного списка и отобразите результат на экран в виде последовательности чисел, записанных через 
пробел. Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.
P. S. Теория сортировки в видео предыдущего шага.
Sample Input: 8 11 -6 3 0 1 1
Sample Output: -6 0 1 1 3 8 11
"""
N = list(map(int, input().split()))
def merge(a:list, b:list):
    c = [0] * (len(a) + len(b))
    ai = bi = ci = 0
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            c[ci] = a[ai]
            ai += 1
        else:
            c[ci] = b[bi]
            bi += 1
        ci += 1
    while ai < len(a):
        c[ci] = a[ai]
        ai += 1
        ci += 1
    while bi < len(b):
        c[ci] = b[bi]
        bi += 1
        ci += 1
    return c
def s_list(n):
    if len(n) <= 1:
        return n
    x = len(n) // 2
    l = n[:x]
    r = n[x:]
    s_list(l)
    s_list(r)
    c = merge(l, r)
    for i in range(len(n)):
        n[i] = c[i]
    return n
print(*s_list(N))
