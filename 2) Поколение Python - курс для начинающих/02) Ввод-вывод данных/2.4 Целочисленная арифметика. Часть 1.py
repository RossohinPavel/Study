""" Упражнение 1
Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке. Первое число вводит
пользователь, остальные числа вычисляются в программе.
Формат входных данных
На вход программе подается одно целое число.
Формат выходных данных
Программа должна вывести три последовательно идущих числа в соответствии с условием задачи.
Sample Input 1: 8
Sample Output 1: 8 / 9 / 10
Sample Input 2: -341
Sample Output 2: -341 / -340 / -339
Sample Input 3: -1
Sample Output 3: -1 / 0 / 1
"""
print(a := int(input()), a+1, a+2, sep='\n')


""" Упражнение 2
Напишите программу, которая считывает три целых числа и выводит на экран их сумму. 
Каждое число записано в отдельной строке.
Формат входных данных
На вход программе подаётся три целых числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести сумму введенных чисел.
Sample Input 1: 9 / 11 / 2
Sample Output 1: 22
Sample Input 2: -1 / 10 / 1
Sample Output 2: 10
Sample Input 3: -7 / -10 / -3
Sample Output 3: -20
"""
print(sum(list(map(lambda x: int(input()), range(3)))))


""" Упражнение 3
Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
Формат входных данных
На вход программе подается одно целое число – длина ребра.
Формат выходных данных
Программа должна вывести текст и числа в соответствии с условием задачи.
Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3, S = 6a^2
Sample Input 1: 25
Sample Output 1:
    Объем = 15625
    Площадь полной поверхности = 3750
Sample Input 2: 13
Sample Output 2:
    Объем = 2197
    Площадь полной поверхности = 1014
Sample Input 3: 56
Sample Output 3:
    Объем = 175616
    Площадь полной поверхности = 18816 
"""
print(*(a := int(input()), f'Объем = {a ** 3}', f'Площадь полной поверхности = {6*a**2}')[1:], sep='\n')


""" Упражнение 4
Напишите программу вычисления значения функции f(a, b) = 3*(a + b)^3 + 275*b^2 - 127*a - 41
по введеным целым значениям aa и bb.
Формат входных данных
На вход программе подаётся два целых числа, каждое на отдельной строке. В первой строке — значение aa, 
во второй строке — значение bb.
Формат выходных данных
Программа должна вывести значение функции по введённым числам aa и bb.

Sample Input 1: 1 / 1
Sample Output 1: 131
Sample Input 2: 1 / 0
Sample Output 2: -165
Sample Input 3: 0 / 1
Sample Output 3: 237
"""
print((a := list(map(lambda x: int(input()), range(2))), 3 * (a[0] + a[1]) ** 3 + 275 * a[1] ** 2 - 127 * a[0] - 41)[-1])


""" Упражнение 5
Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с 
пояснительным текстом.
Формат входных данных
На вход программе подаётся целое число.
Формат выходных данных
Программа должна вывести текст согласно условию задачи.
Sample Input 1: 20
Sample Output 1:
    Следующее за числом 20 число: 21
    Для числа 20 предыдущее число: 19
Sample Input 2: 0
Sample Output 2: 
    Следующее за числом 0 число: 1
    Для числа 0 предыдущее число: -1
Sample Input 3: -10
Sample Output 3:
    Следующее за числом -10 число: -9
    Для числа -10 предыдущее число: -11
"""
print(*(a := int(input()), f'Следующее за числом {a} число: {a+1}', f'Для числа {a} предыдущее число: {a-1}')[1:], sep='\n')


""" Упражнение 6
Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, системного блока, клавиатуры и
мыши.
Формат входных данных
На вход программе подаётся четыре целых числа, каждое на отдельной строке. В первой строке — стоимость монитора, 
во второй строке — стоимость системного блока, в третьей строке — стоимость клавиатуры и в четвертой строке — 
стоимость мыши.
Формат выходных данных
Программа должна вывести одно число – стоимость покупки (трех компьютеров).
Sample Input 1:
    9900
    55600
    3999
    2990
Sample Output 1: 217467
Sample Input 2:
    15700
    80550
    12050
    5890
Sample Output 2: 342570
Sample Input 3:
    44990
    123300
    19600
    8990
Sample Output 3: 590640
"""
print(sum(list(map(lambda x: int(input()), range(4))))*3)


""" Упражнение 7
Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.
Формат входных данных
На вход программе подаётся два целых числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести сумму, разность и произведение введённых чисел, каждое на отдельной строке.
Sample Input 1:
    2
    7
Sample Output 1:
    2 + 7 = 9
    2 - 7 = -5
    2 * 7 = 14
Sample Input 2:
    5
    8
Sample Output 2:
    5 + 8 = 13
    5 - 8 = -3
    5 * 8 = 40
Sample Input 3:
    10
    10
Sample Output 3:
    10 + 10 = 20
    10 - 10 = 0
    10 * 10 = 100
"""
print(*(a := int(input()), b := int(input()), f'{a} + {b} = {a+b}', f'{a} - {b} = {a-b}', f'{a} * {b} = {a*b}')[2:], sep='\n')


""" Упражнение 8
Арифметической прогрессией называется последовательность чисел a1, a2, ..., an, каждое из которых, начиная с a2
, получается из предыдущего прибавлением к нему одного и того же постоянного числа dd (разность прогрессии), то есть:
an=a{n−1}+d
Если известен первый член прогрессии и её разность, то n-ый член арифметической прогрессии находится по формуле:
an=a1+d(n-1)
Входные данные
На вход программе подаётся три целых числа: a1, d и n, каждое на отдельной строке.
Выходные данные
Программа должна вывести nn-ый член арифметической прогрессии.
Sample Input 1:
    1
    1
    10
Sample Output 1: 10
Sample Input 2:
    -1
    1
    2
Sample Output 2: 0
Sample Input 3:
    100
    50
    1
Sample Output 3: 100
"""
print(int(input()) + int(input())*(int(input())-1))


""" Упражнение 9
Напишите программу, которая считывает целое положительное число xx и выводит на экран последовательность 
чисел x, 2x, 3x, 4x и 5x, разделённых тремя черточками.
Формат входных данных
На вход программе подаётся целое положительное число.
Формат выходных данных
Программа должна вывести текст согласно условию задачи.
Sample Input 1: 7
Sample Output 1: 7---14---21---28---35
Sample Input 2: 1
Sample Output 2: 1---2---3---4---5
Sample Input 3: 5
Sample Output 3: 5---10---15---20---25
"""
print(*(a := int(input()), (a * x for x in range(1, 6)))[1], sep='---')
