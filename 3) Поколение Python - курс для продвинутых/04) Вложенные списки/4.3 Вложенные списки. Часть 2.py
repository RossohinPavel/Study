""" Упражнение 1
На вход программе подается число n. Напишите программу, которая создает и выводит построчно список, состоящий
из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
Формат входных данных
На вход программе подается натуральное число n.
Формат выходных данных
Программа должна вывести построчно указанный список.
Sample Input 1:
    3
Sample Output 1:
    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 3]
Sample Input 2:
    2
Sample Output 2:
    [1, 2]
    [1, 2]
"""
n = int(input())
for i in range(n):
    print(list(range(1, n+1)))


""" Упражнение 2
На вход программе подается число nn. Напишите программу, которая создает и выводит построчно вложенный список, 
состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
Формат входных данных
На вход программе подается натуральное число nn.
Формат выходных данных
Программа должна вывести построчно указанный вложенный список.
Sample Input 1:
    4
Sample Output 1:
    [1]
    [1, 2]
    [1, 2, 3]
    [1, 2, 3, 4]
Sample Input 2:
    3
Sample Output 2:
    [1]
    [1, 2]
    [1, 2, 3]
Sample Input 3:
    1
Sample Output 3:
    [1]
"""
n = int(input())
for i in range(1, n+1):
    print(list(range(1, i+1)))


""" Упражнение 3
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике 
на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число n. Напишите программу, которая возвращает указанную строку треугольника 
Паскаля в виде списка (нумерация строк начинается с нуля).
Формат входных данных
На вход программе подается число n (n≥0).
Формат выходных данных
Программа должна вывести указанную строку треугольника Паскаля в виде списка.
Примечание 1. Решение удобно оформить в виде функции pascal(), которая принимает номер строки и возвращает 
соответствующую строку треугольника Паскаля.
Примечание 2. Графическая иллюстрация формирования треугольника Паскаля.
Примечание 3. Подробнее прочитать о треугольнике Паскаля можно тут. 
Sample Input 1: 0
Sample Output 1: [1]
Sample Input 2: 1
Sample Output 2: [1, 1]
Sample Input 3: 2
Sample Output 3: [1, 2, 1]
Sample Input 4: 3
Sample Output 4: [1, 3, 3, 1]
"""
def pascal(st: int) -> list:
    pasc = [[1] * x for x in range(1, st+2)]
    if len(pasc) > 2:
        for i in range(2, len(pasc)):
            for n in range(1, len(pasc[i])-1):
                pasc[i][n] = pasc[i-1][n-1] + pasc[i-1][n]
    return pasc
a = int(input())
print(pascal(a)[a])


""" Упражнение 4
На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника Паскаля.
Формат входных данных
На вход программе подается число n, (n≥1).
Формат выходных данных
Программа должна вывести первые n строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.
Sample Input 1: 4
Sample Output 1:
    1
    1 1
    1 2 1
    1 3 3 1
Sample Input 2:
    5
Sample Output 2:
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
"""
def pascal(st: int) -> list:
    pasc = [[1] * x for x in range(1, st+2)]
    if len(pasc) > 2:
        for i in range(2, len(pasc)):
            for n in range(1, len(pasc[i])-1):
                pasc[i][n] = pasc[i-1][n-1] + pasc[i-1][n]
    return pasc
a = int(input())
for i in pascal(a-1):
    print(*i)


""" Упражнение 5
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает 
последовательности одинаковых символов заданной строки в подсписки.
Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
Формат выходных данных
Программа должна вывести указанный вложенный список.
Sample Input 1: a b c d
Sample Output 1: [['a'], ['b'], ['c'], ['d']]
Sample Input 2:  w w o r l d g g g g r e a t t e c c h e m g g p w w
Sample Output 2: [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], 
['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
"""
a = input().split()
lst = [[a[0]]]
ind = 0
for i in range(1, len(a)):
    temp = [a[i]]
    if lst[ind][0] == temp[0]:
        lst[ind].append(temp[0])
    else:
        lst.append(temp)
        ind += 1
print(lst)


""" Упражнение 6
На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает 
список из чанков указанной длины.
Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной строке.
Формат выходных данных
Программа должна вывести указанный вложенный список.
Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.
Sample Input 1:
    a b c d e f
    2
Sample Output 1:
    [['a', 'b'], ['c', 'd'], ['e', 'f']]
Sample Input 2:
    a b c d e f
    3
Sample Output 2:
    `[['a', 'b', 'c'], ['d', 'e', 'f']]
"""
# Вариант 1
def chunked(lst, num):
    chunk = []
    temp = []
    c = 0
    for i in lst.split():
        temp.append(i)
        c += 1
        if c == num:
            chunk.append(temp)
            temp = []
            c = 0
    if temp:
        chunk.append(temp)
    return chunk
print(chunked(input(), int(input())))


# Вариант 2 Через срезы
def chunked(lst, num):
    lst = lst.split()
    chunk = []
    for i in range(0, len(lst), num):
        chunk.append(lst[i:i+num])
    return chunk
print(chunked(input(), int(input())))


""" Упражнение 7
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. 
Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], 
но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. 
Пустой список — подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок 
списка [1, 2, 3, 4].
На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. 
Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
Формат выходных данных
Программа должна вывести указанный список, содержащий все возможные подсписки, включая пустой список 
в соответствии с примерами.
Примечание. Порядок списков одинаковой длины должен соответствовать порядку их вхождения в основной список.
Sample Input 1: a b
Sample Output 1: [[], ['a'], ['b'], ['a', 'b']]
Sample Input 2: a b v
Sample Output 2: [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]
"""
a = input().split()
temp = [[]]
for i in range(0, len(a)+1):
    for n in range(0, i):
        x = a[n:i]
        temp.append(x)
temp.sort(key=len)
print(temp)
