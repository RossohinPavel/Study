""" Упражнение 1
На вход программы поступает список наименований рек, записанных в одну строчку через пробел. Необходимо отсортировать
этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.
Sample Input: Лена Енисей Волга Дон
Sample Output: Енисей Волга Лена Дон
"""
a = input().split()
a.sort(key=len, reverse=True)
print(*a)


""" Упражнение 2
На вход программы поступает строка в формате:
предмет_1=вес_1
...
предмет_N=вес_N
Веса предметов заданы целыми числами. Необходимо на основе этих данных сформировать словарь и, затем, на основе этого 
словаря сформировать список предметов по убыванию их веса. (В списке должны находиться только наименования предметов без 
их весов). Отобразить полученный результат в виде строки с названиями через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
    ножницы=100
    котелок=500
    спички=20
    зажигалка=40
    зеркальце=50
Sample Output: котелок ножницы зеркальце зажигалка спички
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {x: int(y) for x, y in [z.split('=') for z in lst_in]}
s_lst = sorted(d, key=lambda x: d[x], reverse=True)
print(*s_lst)


""" Упражнение 3
Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си. На вход программы поступает строка с набором этих 
нот, записанных через пробел. Необходимо сформировать список из входной строки с нотами, отсортированными указанным 
образом. Результат вывести в виде строки из нот, записанными через пробел.
Sample Input: до фа соль до ре фа ля си
Sample Output: до до ре фа фа соль ля си
"""
n = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a = input().split()
a.sort(key=lambda x: n.index(x))
print(*a)


""" Упражнение 4
Имеется таблица с данными, представленная в формате:
Номер;Имя;Оценка;Зачет
1;Иванов;3;Да
2;Петров;2;Нет
...
N;Балакирев;4;Да
Эти данные необходимо представить в виде двумерного (вложенного) кортежа. Все числа должны быть представлены как целые 
числа. Затем, отсортировать данные так, чтобы столбцы шли в порядке: Имя;Зачет;Оценка;Номер
Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа и 
присвоен переменной с именем t_sorted.
Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
    Номер;Имя;Оценка;Зачет
    1;Портос;5;Да
    2;Арамис;3;Да
    3;Атос;4;Да
    4;д'Артаньян;2;Нет
    5;Балакирев;1;Нет
Sample Output: True
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
def t_f(x):
    n = x.copy()
    for i, v in enumerate(n):
        q = []
        for o in v.split(';'):
            if o.isdigit():
                q.append(int(o))
            else:
                q.append(o)
        a, b, c, d = q
        n[i] = tuple([b, d, c, a])
    return tuple(n)
a = t_f(lst_in)
t_sorted = (tuple(a[0]), ) + tuple(sorted(a[1:], key=lambda x: x[1]))


""" Упражнение 5
Известно, что звания военнослужащих имеют следующий порядок:
рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник
На вход поступает список военнослужащих в формате:

имя_1=звание_1
...
имя_N=звание_N
Необходимо входные данные представить в виде вложенного списка вида:
[['имя_1', 'звание_1'], ['имя_2', 'звание_2'], ..., ['имя_N', 'звание_N']]
Этот список присвоить переменной с именем lst. Затем, отсортировать его по возрастанию званий.
Выводить на экран ничего не нужно, только сформировать список и указать на него переменную lst.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
    Атос=лейтенант
    Портос=прапорщик
    д'Артаньян=капитан
    Арамис=лейтенант
    Балакирев=рядовой
Sample Output: True
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
rank = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант',
        'капитан', 'майор', 'подполковник', 'полковник']
lst = sorted([x.split('=') for x in lst_in], key=lambda y: rank.index(y[-1]))
