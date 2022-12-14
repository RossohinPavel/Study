""" Упражнение 1
Имеется кортеж: t = (3.4, -56.7)
Вводится последовательность целых чисел в одну строчку через пробел. Необходимо их добавить в кортеж t.
Результат вывести на экран командой: print(t)
Sample Input: 8 11 -5 2
Sample Output: (3.4, -56.7, 8, 11, -5, 2)
"""
t = (3.4, -56.7)
a = tuple(map(int, input().split()))
t += a
print(t)


""" Упражнение 2
Вводятся названия городов в одну строку через пробел. На их основе формируется кортеж. Если в этом кортеже нет города 
"Москва", то следует его добавить в конец кортежа. Результат вывести на экран в виде строки с названиями городов 
через пробел.
Sample Input: Уфа Казань Самара
Sample Output: Уфа Казань Самара Москва
"""
c = tuple(input().split())
if 'Москва' not in c:
    c += ('Москва', )
print(*c)


""" Упражнение 3
Вводятся названия городов в одну строку через пробел. На их основе формируется кортеж. Если в этом кортеже присутствует 
город "Ульяновск", то этот элемент следует удалить (создав новый кортеж). Результат вывести на экран в виде строки с 
названиями городов через пробел.
Sample Input: Воронеж Самара Тольятти Ульяновск Пермь
Sample Output: Воронеж Самара Тольятти Пермь
"""
c = tuple(input().split())
d = ()
for i in c:
    if i != 'Ульяновск':
        d += (i,)
print(*d)


""" Упражнение 4
Вводятся имена студентов в одну строчку через пробел. На их основе формируется кортеж. Отобразите на экране все имена 
из этого кортежа, которые содержат фрагмент "ва" (без учета регистра). Имена выводятся в одну строчку через пробел в 
нижнем регистре (малыми буквами).
Sample Input: Петя Варвара Венера Василиса Василий Федор
Sample Output: варвара василиса василий
"""
a = tuple(input().split())
ll = []
for i in a:
    if 'ва' in i.lower():
        ll.append(i.lower())
print(*ll)


""" Упражнение 5
Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж. Необходимо создать еще один кортеж с 
уникальными (не повторяющимися) значениями из первого кортежа. Результат отобразите в виде списка чисел через пробел.
P. S. Подобные задачи решаются, как правило, с помощью множеств, но в качестве практики пока обойдемся без них.
Sample Input: 8 11 -5 -2 8 11 -5
Sample Output: 8 11 -5 -2
"""
a = tuple(input().split())
b = ()
for i in a:
    if i not in b:
        b += (i,)
print(*b)


""" Упражнение 6
Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж. Необходимо найти и вывести все индексы 
неуникальных (повторяющихся) значений в этом кортеже. Результат отобразите в виде строки чисел, записанных через пробел.
Sample Input: 5 4 -3 2 4 5 10 11
Sample Output: 0 1 4 5
"""
a = tuple(input().split())
ll = []
for i, v in enumerate(a):
    if a.count(v) > 1:
        ll.append(i)
print(*ll)


""" Упражнение 7

"""

""" Упражнение
Имеется двумерный кортеж, размером 5 x 5 элементов: t
Вводится натуральное число N (N < 5). Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 
размером N x N элементов. Результат вывести на экран в виде таблицы чисел.
Sample Input: 3
Sample Output:
    1 0 0
    0 1 0
    0 0 1
"""
t = ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 1))
N = int(input())
t2 = tuple([tuple([t[i][n] for n in range(N)]) for i in range(N)])
for i in t2:
    print(*i)
