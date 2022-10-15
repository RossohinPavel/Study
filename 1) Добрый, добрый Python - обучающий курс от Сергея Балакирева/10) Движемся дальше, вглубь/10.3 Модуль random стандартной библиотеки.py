""" Упражнение 1
Вводятся два натуральных числа a, b (a < b) в одну строчку через пробел. Выполните генерацию вещественной случайной
величины в диапазоне [a; b). Округлите результат до сотых и выведите его на экран.
Sample Input: -4 5
Sample Output: -2.79
"""
import random
random.seed(1)
a, b = map(int, input().split())
print(round(random.uniform(a, b), 2))


""" Упражнение 2
Вводятся два натуральных числа a, b (a < b) в одну строчку через пробел. Выполните генерацию целочисленной случайной 
величины в диапазоне [a; b]. Выведите результат на экран.
Sample Input: -2 3
Sample Output: -1
"""
import random
random.seed(1)
a, b = map(int, input().split())
print(random.randint(a, b))


""" Упражнение 3
Вводится список названий городов в одну строчку через пробел. Выберите из этого списка один город случайным образом и 
отобразите его на экране.
Sample Input: Тула Казань Смоленск Семипалатинск Уфа Москва Самара
Sample Output: Казань
"""
import random
random.seed(1)
a = input().split()
print(random.choice(a))


""" Упражнение 4
Вводится таблица целых чисел, записанных через пробел. Необходимо перемешать столбцы этой таблицы, используя функции 
shuffle и zip и вывести результат на экран (также в виде таблицы).
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
    1 2 3 4
    5 6 7 8
    9 8 6 7
Sample Output:
    4 1 3 2
    8 5 7 6
    7 9 6 8
"""
import sys
import random
random.seed(1)
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = [list(map(int, line.split())) for line in lst_in]
z = zip(*lst2D)
ls = list(z)
random.shuffle(ls)
z2 = list(zip(*ls))
for i in z2:
    print(*i)


""" Упражнение 5
Вводятся имена студентов в одну строчку через пробел. Требуется случайным образом выбрать трех студентов из этого 
списка, используя функцию sample. (Полагается, что в исходном списке более трех студентов). Результат вывести на экран в 
одну строчку через пробел.
Sample Input: Петров Иванов Сидоров Балакирев Фридман
Sample Output: Иванов Петров Фридман
"""
import random
random.seed(1)
a = input().split()
print(*random.sample(a, 3))


""" Упражнение 6
Имеется двумерное игровое поле размером N x N (N - натуральное число, вводится с клавиатуры), представленное в виде 
вложенного списка: P = [[0] * N for i in range(N)]
Требуется расставить в нем случайным образом M = 10 единиц (целочисленных) так, чтобы они не соприкасались друг с 
другом (то есть, вокруг каждой единицы должны быть нули, либо граница поля). 
P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.
Sample Input: 10
Sample Output: True
"""
import random
random.seed(1)
N = int(input())
P = [[0] * N for i in range(N)]
def is_isolate(l):
    if 2 in l:
        return False
    for i in range(len(l) - 1):
        if l[i] == 1 and l[i + 1] == 1:
            return False
    return True
def verify(a):
    flag = True
    for i in range(len(a) - 1):
        lst = [a[i][x] + a[i + 1][x] for x in range(len(a[i]))]
        if is_isolate(lst) == False:
            flag = False
    return True if flag else False
n = 0
while n < 10:
    ppw = random.randint(0, N - 1)
    pos = random.randint(0, N - 1)
    if P[ppw][pos] == 1:
        continue
    P[ppw][pos] = 1
    if verify(P):
        n += 1
        continue
    P[ppw][pos] = 0
