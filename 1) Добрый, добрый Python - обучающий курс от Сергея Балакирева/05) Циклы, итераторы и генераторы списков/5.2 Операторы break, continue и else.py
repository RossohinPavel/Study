""" Упражнение 1
Имеется одномерный список длиной 10 элементов, состоящий из нулей: p = [0] * 10
На каждой итерации цикла пользователь вводит целое число - индекс элемента списка p,
по которому записывается значение 1, если ее там еще нет. Если же 1 уже проставлена,
то список не менять и снова запросить у пользователя очередное число.
Необходимо расставить так пять единиц в список. (После этого цикл прерывается).
Программу реализовать с помощью цикла while и с использованием оператора continue,
когда 1 не может быть добавлена в список.
Результат вывести на экран в виде последовательности чисел, записанных через пробел.
Sample Input: 1 / 2 / 2 / 5 / 7 / 5 / 9
Sample Output: 0 1 1 0 0 1 0 1 0 1
"""
p = [0] * 10
n = 0
while n != 5:
    i = int(input())
    if p[i] == 1:
        continue
    p[i] = 1
    n += 1
print(*p)


""" Упражнение 2
На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных чисел, 
до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue, 
а также использовать цикл while. Результат произведения вывести на экран.
Sample Input: 2 / -1 / 3 / 2 / -5 / 7 / 0
Sample Output: 84
"""
s = 1
n = 1
while n != 0:
    n = int(input())
    if n <= 0:
        continue
    s *= n
print(s)


""" Упражнение 3
Вводится список названий городов в одну строчку через пробел. Определить, что в этом списке все города 
имеют длину более 5 символов. Реализовать программу с использованием цикла while и оператора break. 
Вывести ДА, если условие выполняется и НЕТ - в противном случае.
Sample Input: Самара Ульяновск Новгород Воронеж
Sample Output: ДА
"""
c = list(map(str, input().split()))
i = 0
flag = True
while i < len(c):
    if len(c[i]) < 5:
        flag = False
        break
    i += 1
print('ДА' if flag else 'НЕТ')


""" Упражнение 4
Вводится список имен студентов в одну строчку через пробел. Определить, что хотя бы одно имя в этом списке 
начинается и заканчивается на ту же самую букву (без учета регистра). Реализовать программу с 
использованием цикла while и оператора break. Вывести ДА, если условие выполняется и НЕТ - в противном случае.
Sample Input: Петр Анна Иван Сергей Михаил Федор
Sample Output: ДА
"""
n = input().split()
i = 0
flag = 'НЕТ'
while i < len(n):
    q = n[i].lower()
    if q[0] == q[-1]:
        flag = 'ДА'
        break
    i += 1
print(flag)


""" Упражнение 5
Вводится натуральное число n (то есть, целое положительное). В цикле перебрать все целые числа в интервале [1; n] 
и сформировать список из чисел, кратных 3 и 5 одновременно. Вывести полученную последовательность чисел в виде 
строки через пробел, если значение n меньше 100. Иначе вывести на экран сообщение 
"слишком большое значение n" (без кавычек). Использовать в программе оператор else после цикла while.
Sample Input 1: 49
Sample Output 1: 15 30 45
Sample Input 2: 100
Sample Output 2: слишком большое значение n
"""
n = int(input())
i = 1
l = []
if n < 100:
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            l.append(i)
        i += 1
    else:
        print(*l)
else:
    print('слишком большое значение n')


""" Упражнение 6
Вводится натуральное число n. Вывести первое найденное натуральное число (то есть, перебирать числа, начиная с 1), 
квадрат которого больше значения n. Реализовать программу с использованием цикла while.
Sample Input: 10
Sample Output: 4
"""
n = int(input())
i = 1
while True:
    if i ** 2 > n:
        break
    i += 1
print(i)


""" Упражнение 7
(На использование цикла while). Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий день 
он увеличивал пробег на 10 % от пробега предыдущего дня. Определить в какой день он пробежит больше x км 
(натуральное число x вводится с клавиатуры). Результат (искомый день) вывести на экран.
Sample Input: 20
Sample Output: 9
"""
d = 10
day = 1
a = int(input())
while d < a:
    d += d * 0.1
    day += 1
print(day)


""" Упражнение 8
(На использование цикла while). Вводятся названия книг (каждое с новой строки). Удалить из введенного списка 
все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом). 
Результат вывести на экран в виде строки из оставшихся названий через пробел.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки
Sample Input: Муму / Евгений Онегин / Сияние / Мастер и Маргарита / Пиковая дама / Колобок
Sample Output: Муму Сияние Колобок
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
i = 0
while i < len(lst_in):
    if len(lst_in[i].split()) > 1:
        lst_in.pop(i)
    else:
        i += 1
print(*lst_in)
