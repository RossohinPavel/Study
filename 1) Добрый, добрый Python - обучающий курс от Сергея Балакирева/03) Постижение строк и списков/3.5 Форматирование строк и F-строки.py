""" Упражнение 1
Вводятся: имя, фамилия и возраст (целое положительное число) каждое значение с новой строки.
Используя метод строки format, через индексы переменных необходимо сформировать строку по шаблону:
"Уважаемый <имя> <фамилия>! Поздравляем Вас с <возраст>-летием!" Результат вывести на экран (без кавычек).
Sample Input:
    Sergey
    Balakirev
    35
Sample Output: Уважаемый Sergey Balakirev! Поздравляем Вас с 35-летием!
"""
name = input()
sname = input()
age = str(input())
print('Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!'.format(name, sname, age))


""" Упражнение 2
Вводятся: габариты изделия (целые числа): ширина, глубина, высота - в одну строчку через пробел. 
С помощью метода format, используя ключи в качестве имен переменных, сформировать строку: 
"Габариты: <ширина> x <глубина> x <высота>". Результат вывести на экран.
Sample Input: 8 11 13
Sample Output: Габариты: 8 x 11 x 13
"""
w, d, h = map(int, input().split())
print('Габариты: {0} x {1} x {2}'.format(w, d, h))


""" Упражнение 3
Вводятся: два целых числа в одну строку через пробел. С помощью F-строки отобразить их по возрастанию 
в одну строку через пробел. Результат вывести на экран.
P. S. Реализовать программу без использования условных операторов. Подумайте, как это можно сделать.
Sample Input: 18 11
Sample Output: 11 18
"""
n = input().split()
print(min(n), max(n))


""" Упражнение 4
Вводится адрес (каждое значение с новой строки) в формате: 
город, улица, номер дома (целое число), номер квартиры (целое число). 
Сформировать строку по шаблону: "г. <город>, ул. <улица>, д. <номер дома>, кв. <номер квартиры>", используя F-строку. 
Результат вывести на экран.
Sample Input:
    Москва
    Воздвиженка
    9
    1
Sample Output: г. Москва, ул. Воздвиженка, д. 9, кв. 1
"""
c = input()
s = input()
h = input()
a = input()
print(f'г. {c}, ул. {s}, д. {h}, кв. {a}')


""" Упражнение 5
Вводятся (каждое с новой строки): курс доллара (вещественное значение) и 
число рублей (целое число) для обмена рублей на доллары. Вычислить целое количество получаемых долларов 
(с отбрасыванием дробной части) и сформировать строку, используя F-строку:
"Вы можете получить <долларов>$ за <число рублей> рублей по курсу <курс доллара>".
Вывести результат на экран (без кавычек).
Sample Input: 73.54 / 1000
Sample Output: Вы можете получить 13$ за 1000 рублей по курсу 73.54
"""
b = float(input())
r = int(input())
print(f'Вы можете получить {int(r / b)}$ за {r} рублей по курсу {b}')
