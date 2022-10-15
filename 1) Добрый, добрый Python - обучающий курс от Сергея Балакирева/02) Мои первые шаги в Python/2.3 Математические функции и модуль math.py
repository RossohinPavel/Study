""" Упражнение 1
Допишите текст программы для вычисления модуля введенного с клавиатуры числа в
переменную d и вывода значения в консоль с помощью функции print.
Sample Input: -5
Sample Output: 5
"""
d = int(input())
print(abs(d))


""" Упражнение 2
Допишите текст программы для нахождения минимального значения из пяти введенных целых чисел
 с выводом результата в консоль с помощью функции print.
Sample Input: 8 11 -5 3 0
Sample Output: -5
"""
d1, d2, d3, d4, d5 = map(int, input().split())
print(min(d1, d2, d3, d4, d5))


""" Упражнение 3
Допишите текст программы для нахождения максимального значения 
из пяти введенных целых чисел с выводом результата в консоль с помощью функции print.
Sample Input: 8 11 0 -5 3
Sample Output: 11
"""
d1, d2, d3, d4, d5 = map(int, input().split())
print(max(d1, d2, d3, d4, d5))


""" Упражнение 4
Допишите текст программы для вычисления евклидового расстояния (гипотенузы) по перемещениям a и b (формула: ). 
Округлите результат с точностью до сотых. Полученное значение выведите на экран.
Sample Input: 3 4
Sample Output: 5.0
"""
a, b = map(int, input().split())
c = (a ** 2 + b ** 2) ** 0.5
print(round(c, 2))


""" Упражнение 5
Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе), 
используя формулу. Выведите результат в консоль в виде целого числа с помощью функции print.
Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.
Sample Input: 6 3
Sample Output: 20
"""
import math
n, k = map(int, input().split())
c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(int(c))


""" Упражнение 6
В летний лагерь нужно отвести n детей и m вожатых с помощью автобусов. Максимальная вместимость 
каждого автобуса 20 человек. Допишите программу для вычисления минимального числа автобусов, 
необходимых для перевозки детей вместе с вожатыми. Результат выведите в консоль в виде целого числа.
Sample Input: 40 5
Sample Output: 3
"""
import math
n, m = map(int, input().split())
print(math.ceil((n + m) / 20))


""" Упражнение 7
Гелевая ручка стоит x рублей. Сегодня магазин предоставляет скидку в 10% на каждую купленную ручку. 
Какое наибольшее количество таких ручек можно будет купить на 500 рублей? 
Результат выведите в консоль в виде целого числа.
Sample Input: 20
Sample Output: 27
"""
x = int(input())
print(int(500 / (x - x/10)))
