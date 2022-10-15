""" Упражнение 1
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
    fill – символ заполнитель;
    base – величина основания равнобедренного треугольника;
а затем выводит его.
Примечание. Гарантируется, что основание треугольника – нечетное число.
Sample Input 1:
    *
    9
Sample Output 1:
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
"""
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill*i)
    for i in range(base // 2, 0, -1):
        print(fill*i)
fill = input()
base = int(input())
draw_triangle(fill, base)


""" Упражнение 2
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
    name – имя человека;
    surname – фамилия человека;
    patronymic – отчество человека;
а затем выводит на печать ФИО человека.
Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
Sample Input 1:
    Александр
    Пушкин
    Сергеевич
Sample Output 1:
    ПАС
Sample Input 2:
    тимур
    Гуев
    ахсарбекович
Sample Output 2:
    ГТА
"""
def print_fio(name, surname, patronymic):
    print(''.join([surname[0], name[0], patronymic[0]]).upper())
name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)


""" Упражнение 3
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
Sample Input 1: 12345
Sample Output 1: 15
Sample Input 2: 12
Sample Output 2: 3
"""
def print_digit_sum(num):
    print(sum([int(x) for x in str(num)]))
n = int(input())
print_digit_sum(n)
