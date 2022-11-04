""" Упражнение 1
Вам доступно время alarm. Дополните приведенный ниже код, чтобы он вывел следующие его компоненты:
    количество часов в формате HH
    количество минут в формате MM
    количество секунд в формате SS
"""
from datetime import time
alarm = time(7, 30, 25)
print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.strftime('%M'))
print('Секунды:', alarm.strftime('%S'))


""" Упражнение 2
Вам доступна дата birthday. Дополните приведенный ниже код, чтобы он вывел следующие её компоненты:
    полное название месяца на английском
    полное название дня недели на английском
    год в формате YYYY
    номер месяца в формате MM
    день месяца в формате DD
"""
from datetime import date
birthday = date(1992, 10, 6)
print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))


""" Упражнение 3
В переменной florida_hurricane_dates хранится список дат, в которые произошел ураган во Флориде с 1950 по 2017 год.
Дополните приведенный ниже код, чтобы он вывел самую раннюю дату из списка florida_hurriance_dates в 
трех различных форматах:
    в стандарте ISO (YYYY-MM-DD)
    в типичном для России стиле (DD.MM.YYYY)
    в типичном для Америки стиле (MM/DD/YYYY)
Примечание 1. Считайте, что переменная florida_hurricane_dates объявлена и доступна вашей программе.
Примечание 2. Считайте, что тип date уже импортирован в программу.
"""
first_date = min(florida_hurricane_dates)
iso = 'Дата первого урагана в ISO формате: ' + first_date.strftime('%Y-%m-%d')
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
print(iso)
print(ru)
print(us)


""" Упражнение 4
Ураган Эндрю, который обрушился на Флориду 2424 августа 19921992 года, был одним из самых дорогостоящих и смертоносных 
ураганов в истории США. Дополните приведенный ниже код, чтобы он вывел дату 2424 августа 19921992 года в трех 
различных форматах:
    в формате YYYY-MM
    в формате month_name (YYYY), где month_name – полное название месяца на английском
    в формате YYYY-day_number, где day_number – день года
"""
from datetime import date
andrew = date(1992, 8, 24)
print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


""" Упражнение 5
Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.
Формат входных данных
На вход программе подаются две корректные даты в ISO формате (YYYY-MM-DD), каждая на отдельной строке.
Формат выходных данных
Программа должна выбрать из двух введенных дат меньшую и вывести ее в формате DD-MM (YYYY).
Примечание. Тестовые данные доступны по ссылке.
Таблица форматирования
Sample Input 1:
    2021-05-12
    2021-05-04
Sample Output 1:
    04-05 (2021)
Sample Input 2:
    1999-07-14
    1999-07-14
Sample Output 2:
    14-07 (1999)
"""
from datetime import date
f_d = min(map(lambda x: date.fromisoformat(input()), range(2)))
print(f_d.strftime('%d-%m (%Y)'))


""" Упражнение 6
Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.
Формат входных данных
На вход программе подается натуральное число n, а затем nn корректных дат в 
ISO формате (YYYY-MM-DD), каждая на отдельной строке.
Формат выходных данных
Программа должна вывести введенные даты в порядке неубывания, каждую на отдельной строке, в формате DD/MM/YYYY.
Примечание 1. Последовательность называется неубывающей, если каждый ее следующий член не меньше предыдущего, например:
1,1,2,3,4,4,4,5,6,...
1,1,2,3,4,4,4,5,6,...
Обратите внимание, что такая последовательность не является возрастающей.
Примечание 2. Считайте, что при форматировании даты с помощью %Y год выводится без ведущих нулей, так как на серверах 
Stepik установлен Linux.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    5
    2021-08-01
    2021-08-02
    2021-07-01
    2021-06-01
    2021-05-01
Sample Output 1:
    01/05/2021
    01/06/2021
    01/07/2021
    01/08/2021
    02/08/2021
Sample Input 2:
    3
    2021-11-01
    2021-11-01
    2021-11-01
Sample Output 2:
    01/11/2021
    01/11/2021
    01/11/2021
"""
from datetime import date
lst = map(lambda x: date.fromisoformat(x), sorted([input() for _ in range(int(input()))]))
for i in lst:
    print(i.strftime('%d/%m/%Y'))


""" Упражнение 7
Тимур считает дату «интересной», если её год совпадает с годом его рождения, а сумма номера месяца и номера дня равна 
его возрасту. Год рождения Тимура — 1992, возраст — 29 лет.
Реализуйте функцию print_good_dates(), которая принимает один аргумент:
    dates — список дат (тип date)
Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке, в формате  
month_name DD, YYYY, где month_name — полное название месяца на английском. 
Примечание 1. Если в функцию передается пустой список или список без интересных дат, функция ничего не должна выводить.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_good_dates(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
    print_good_dates(dates)
Sample Output 1:
    September 20, 1992
    October 19, 1992
Sample Input 2:
    dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
    print_good_dates(dates)
Sample Output 2: 
"""
from datetime import date
def print_good_dates(lst):
    lst.sort()
    if lst:
        for i in lst:
            if i.year == 1992 and i.month + i.day == 29:
                print(i.strftime('%B %d, %Y'))


""" Упражнение 8
Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:
    day — натуральное число, день
    month — натуральное число, месяц
    year — натуральное число, год
Функция должна возвращать True, если дата с компонентами day, month и year является корректной, 
или False в противном случае.
Примечание 1. Вспомните про конструкцию try-except. 
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_correct(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(is_correct(31, 12, 2021))
Sample Output 1:
    True
Sample Input 2:
    print(is_correct(31, 13, 2021))
Sample Output 2:
    False
"""
from datetime import date
def is_correct(d, m, y):
    try:
        c_d = date(int(y), int(m), int(d))
        return True
    except:
        return False


""" Упражнение 9
Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.
Формат входных данных
На вход программе подается последовательность дат в формате DD.MM.YYYY, каждая на отдельной строке. 
Концом последовательности является слово end.
Формат выходных данных
Программа должна для каждой введенной даты вывести текст Корректная или Некорректная в зависимости от того, 
является ли дата корректной, а затем вывести количество корректных дат.
Примечание 1. Для анализа даты на корректность можете использовать уже реализованную функцию is_correct() из 
предыдущей задачи.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    19.05.2016
    05.13.2010
    21.12.2012
    01.01.1000
    32.04.2003
    end
Sample Output 1:
    Корректная
    Некорректная
    Корректная
    Корректная
    Некорректная
    3
Sample Input 2:
    15.02.1524
    29.02.2017
    27.05.1528
    13.10.1736
    40.06.431
    31.07.5200
    29.02.2016
    end
Sample Output 2:
    Корректная
    Некорректная
    Корректная
    Корректная
    Некорректная
    Корректная
    Корректная
    5
"""
# put your python code here
from datetime import date
def is_correct(d, m, y):
    try:
        c_d = date(int(y), int(m), int(d))
        return True
    except:
        return False
a = input()
c = 0
while a != 'end':
    if is_correct(*a.split('.')):
        print('Корректная')
        c += 1
    else:
        print('Некорректная')
    a = input()
else:
    print(c)
