""" Упражнение 1
Вводится двумерный список в виде таблицы целых чисел (см. пример ниже). С помощью list comprehension
преобразовать двумерный список в одномерный так, чтобы значения элементов шли в обратном порядке.
Результат отобразить в виде строки из чисел, записанных через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
    1 2 3 4
    5 6 7 8
    9 8 7 6
    5 4 3 2
Sample Output: 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
"""
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
lst_in = [lst_in[row][x] for row in range(len(lst_in) - 1, -1, -1) for x in range(len(lst_in[row]) - 1, -1, -1)]
print(*lst_in)


""" Упражнение 2
Вводится список целых чисел в строку через пробел. С помощью list comprehension сформировать из них двумерный список 
lst размером N x N (квадратную таблицу чисел). Гарантируется, что из набора введенных чисел можно сформировать 
квадратную матрицу (таблицу). Результат отобразить в виде списка командой: print(lst)
Sample Input: 1 2 3 4 5 6 7 8 9
Sample Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
a = list(map(int, input().split()))
len_a = int(len(a) ** 0.5)
lst = [a[0+x:len_a+x] for x in range(0, len(a), len_a)]
print(lst)


""" Упражнение 3
Используйте следующий список из строк: t 
Необходимо преобразовать его в двумерный (вложенный) список lst, где каждая строка представляется списком из слов 
(слова разделяются пробелом), но сохранять слова только длиной более трех символов. Решить данную задачу с 
использованием list comprehension. Результат отобразить с помощью команды: print(lst)
Sample Input:
Sample Output: [['Скажи-ка,', 'дядя,', 'ведь', 'даром'], ['Python', 'выучил', 'каналом'], ['Балакирев', 'раздавал?'], 
['Ведь', 'были', 'заданья', 'боевые,'], ['говорят,', 'какие!'], ['Недаром', 'помнит', 'Россия'], ['рубили', 'тогда!']]
"""
t = ["– Скажи-ка, дядя, ведь не даром", "Я Python выучил с каналом", "Балакирев что раздавал?",
     "Ведь были ж заданья боевые,", "Да, говорят, еще какие!", "Недаром помнит вся Россия", "Как мы рубили их тогда!"]
lst = [[x for x in row.split() if len(x) > 3] for row in t]
print(lst)


""" Упражнение 4
Повторите задачу с транспонированием прямоугольной матрицы с помощью list comprehension, изложенной в видео-уроке 
к этой практике. На вход поступает таблица целых чисел, на выходе нужно отобразить эту же таблицу в транспонированном 
виде (строки заменяются на столбцы), используя команду:
for row in A:
    print(*row)
где A - транспонированный двумерный список. Желательно сделать эту задачу не пересматривая видео.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки. 
Sample Input:
    1 2 3
    4 5 6
    7 8 9
    5 4 3
Sample Output:
    1 4 7 5
    2 5 8 4
    3 6 9 3
"""
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
A = [[x[row] for x in lst_in] for row in range(len(lst_in[0]))]
for row in A:
    print(*row)
