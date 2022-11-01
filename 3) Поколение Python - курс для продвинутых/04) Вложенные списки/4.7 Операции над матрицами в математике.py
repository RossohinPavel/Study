""" Упражнение 1
Напишите программу для вычисления суммы двух матриц.
Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах, затем элементы первой
матрицы, затем пустая строка, далее следуют элементы второй матрицы.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
Sample Input 1:
    2 4
    1 2 3 4
    5 6 7 1

    3 2 1 2
    1 3 1 3
Sample Output 1:
    4 4 4 6
    6 9 8 4
Sample Input 2:
    3 3
    9 6 3
    3 1 1
    4 7 5

    0 3 2
    1 7 8
    4 2 3
Sample Output 2:
    9 9 5
    4 8 9
    8 9 8
"""
n, m = map(int, input().split())
m1 = [list(map(int, input().split())) for _ in range(n)]
input()
m2 = [list(map(int, input().split())) for _ in range(n)]
res = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        res[i][j] = m1[i][j] + m2[i][j]
for i in res:
    print(*i)


""" Упражнение 2
Напишите программу, которая перемножает две матрицы.
Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице, затем элементы 
первой матрицы, затем пустая строка. Далее следуют числа m и k — количество строк и столбцов второй матрицы затем 
элементы второй матрицы.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
Sample Input 1:
    2 2
    1 2
    3 2

    2 2
    3 2
    1 1
Sample Output 1:
    5 4
    11 8
Sample Input 2:
    3 2
    2 5
    6 7
    1 8

    2 3
    1 2 1
    0 1 0
Sample Output 2:
    2 9 2
    6 19 6
    1 10 1
"""
n1, m1 = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(n1)]
input()
n2, m2 = map(int, input().split())
mat2 = [list(map(int, input().split())) for _ in range(n2)]
res = [[0] * n1 for _ in range(m2)]
for i in range(n1):
    for j in range(m1):
        for x in range(m2):
            res[i][x] += mat1[i][j] * mat2[j][x]
for i in res:
    print(*i)


""" Упражнение 3
Напишите программу, которая возводит квадратную матрицу в m-ую степень.
Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы, 
затем натуральное число m.
Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
Sample Input 1:
    3
    1 2 3
    4 5 6
    7 8 9
    2
Sample Output 1:
    30 36 42
    66 81 96
    102 126 150
Sample Input 2:
    3
    1 2 1
    3 3 3
    1 2 1
    5
Sample Output 2:
    1666 2222 1666
    3333 4443 3333
    1666 2222 1666
"""
n1 = int(input())
mat = [list(map(int, input().split())) for _ in range(n1)]
step = int(input())
res = [[0] * n1 for _ in range(n1)]
end = mat[:]
while step > 1:
    res = [[0] * n1 for _ in range(n1)]
    for i in range(n1):
        for j in range(n1):
            for x in range(n1):
                res[i][x] += end[i][j] * mat[j][x]
    end = res[:]
    step -= 1
for i in res:
    print(*i)
