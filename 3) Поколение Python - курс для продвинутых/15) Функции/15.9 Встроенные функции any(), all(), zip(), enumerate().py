""" Упражнение 1
Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    for word in ignore:
        if word in command:
            return True
    return False
Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any() сохранив при этом ее функционал.
Примечание 1. Следующий программный код:
    print(ignore_command('get ip'))
    print(ignore_command('select all'))
    print(ignore_command('delete'))
    print(ignore_command('trancate'))
должен выводить:
    True
    True
    True
    False
Примечание 2. Вызывать функцию ignore_command() не нужно, требуется только реализовать.
"""
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return not all(map(lambda x: command.find(x) == -1, ignore))


""" Упражнение 2
Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о 
стране в формате:
<capital> is the capital of <country>, population equal <population> people.
    Moscow is the capital of Russia, population equal 145934462 people.
    Washington is the capital of USA, population equal 331002651 people.
    ...
Для каждой страны информацию выводить на отдельной строке. 
"""
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
for cy, cp, po in zip(countries, capitals, population):
    print(f'{cp} is the capital of {cy}, population equal {po} people.')


""" Упражнение 3
На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y) 
и аппликат (z) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с введенными 
координатами внутри либо на поверхности шара с центром в начале координат и радиусом R =2.
Формат входных данных
На вход программе подаются три строки текста с вещественными числами, разделенными символом пробела – абсциссы, 
ординаты и аппликаты точек в трехмерной системе координат.
Формат выходных данных
Программа должна вывести True если все точки с введенными координатами находятся внутри или на границе шара и False, 
если вне.
Примечание 1. Гарантируется, что количество чисел во всех трех строках одинаковое.
Примечание 2. Уравнение поверхности шара (сферы) имеет вид x^2+y^2+z^2 = R^2 
Примечание 3. Для решения задачи используйте встроенные функции all() и zip().
Примечание 4. Используйте следующие названия abscissas, ordinates, applicates для соответствующих списков.
Sample Input 1:
    0.0 1.0 2.0
    0.0 0.0 1.1
    0.0 1.0 1.5
Sample Output 1:
    False
Sample Input 2:
    0.0 0.0
    1.5 0.0
    1.1 1.1
Sample Output 2:
    True
"""
abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))
print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))


""" Упражнение 4
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу TCP/IP.
В 4-й версии IP-адрес представляет собой 32-битное число. Адрес записывается в виде четырёх десятичных чисел 
(октетов) со значением от 0 до 255 (включительно), разделённых точками, например, 192.168.1.2
Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в 
IP-адресе – числа со значением от 0 до 255.
Формат входных данных
На вход программе подается строка в формате x.x.x.x, где x – непустой набор символов 0-9, a-z.
Формат выходных данных
Программа должна вывести True если введенная строка – корректный IP-адрес и False в противном случае.
Примечание. Ведущие нули следует игнорировать:
    0001 = 1
    006 = 6
    0213 = 213
    0000 = 0
    00345 = 345
    ...
Sample Input 1:
    10.0.1.1
Sample Output 1:
    True
Sample Input 2:
    10.1.1.a
Sample Output 2:
    False
"""
print(all(map(lambda x: x.isdigit() and int(x) < 256, input().split('.'))))


""" Упражнение 5
На вход программе подаются два натуральных числа a и b. Напишите программу с использованием встроенной функции all() 
для обнаружения всех целых чисел в диапазоне [a;b], которые делятся на каждую содержащуюся в них цифру без остатка.
Формат входных данных
На вход программе подаются два натуральных числа a и b на отдельных строках.
Формат выходных данных
Программа должна вывести все числа из диапазона [a;b], удовлетворяющие условию задачи, на одной строке, 
разделяя их символом пробела.
Примечание. Числа, содержащие нули, неинтересны, их выводить не нужно.
Sample Input 1:
    1
    25
Sample Output 1:
    1 2 3 4 5 6 7 8 9 11 12 15 22 24
Sample Input 2:
    20
    30
Sample Output 2:
    22 24
"""
# Ппц как неудобная в прочтении 2х-строчная реализация
l = range(int(input()), int(input())+1)
print(*filter(lambda x: all(map(lambda y: x % int(y) == 0 if y != '0' else False, str(x))), l))


""" Упражнение 6
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную 
и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.
Формат входных данных
На вход программе подаётся одна строка текста.
Формат выходных данных
Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.
Sample Input 1:
    abcABC9
Sample Output 1:
    YES
Sample Input 2:
    abAB34
Sample Output 2:
    NO
"""
a = input()
c = zip(*map(lambda x: (x.islower(), x.isupper(), x.isdigit()), a))
x = all(map(lambda x: any(x), c))
print('YES' if x and len(a) >= 7 else 'NO')


""" Упражнение 7
Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться, 
что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе. Напишите программу с 
использованием встроенных функций all(), any() для помощи Тимуру в проверке.
Формат входных данных
На вход программе подается натуральное число nn – количество классов. Затем для каждого класса вводится блок 
информации вида:
    натуральное число k – количество учеников в классе;
    далее вводится k строк вида: фамилия оценка.
Формат выходных данных
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае.
Sample Input 2:
    4
    3
    Васечкин 4
    Илюшин 5
    Кривцов 3
    2
    Боталов 5
    Петров 5
    3
    Лебеда 4
    Ивлев 4
    Суворов 4
    2
    Ласкер 4
    Козлов 5
Sample Output 2:
    NO
"""
a = []
for i in range(int(input())):
    l = []
    for j in range(int(input())):
        l.append(input().endswith('5'))
    a.append(any(l))
a = all(a)
print('YES' if a else 'NO')
