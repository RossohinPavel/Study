""" Упражнение 1
Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2 и возвращающую
значение True если число num1 делится без остатка на число num2 и False в противном случае.
Результатом вывода программы должно быть "делится" (если функция func() вернула True) и "не делится"
(если функция func() вернула False).
Примечание. Следующий программный код:
    print(func(10, 2))
    print(func(5, 7))
    print(func(15, 15))
должен выводить:
    True
    False
    True
а вся программа должна выводить:
    делится
    не делится
    делится
Sample Input 1:
    10
    2
Sample Output 1:
    делится
Sample Input 2:
    5
    7
Sample Output 2:
    не делится
"""
def func(num1, num2):
    return num1 % num2 == 0
num1, num2 = int(input()), int(input())
if func(num1, num2):
    print('делится')
else:
    print('не делится')
