""" Упражнение 1
Дополните приведенный ниже код, чтобы он вывел текущую дату в ISO формате (YYYY-MM-DD).
"""
from datetime import date
print(date.today())


""" Упражнение 2
Ураган Эндрю, обрушившийся на Флориду 2424 августа 19921992 года, был одним из самых дорогостоящих и смертоносных 
ураганов в истории США. Дополните приведенный ниже код, чтобы он вывел день недели (начиная с 0), в который ураган 
Эндрю достиг берегов США.
"""
from datetime import date
hurricane_andrew = date(1992, 8, 24)
print(hurricane_andrew.weekday())


""" Упражнение 3
На Флориду с 19501950 по 20172017 год всего обрушилось 235235 ураганов. В переменной florida_hurricane_dates хранится 
список дат, в которые произошел ураган. Сезон ураганов в Атлантике официально начинается 11 июня. Дополните приведенный 
ниже код, чтобы он вывел количество ураганов с 19501950 года, которые обрушились на Флориду до официального начала 
сезона ураганов.
Примечание 1. Считайте, что переменная florida_hurricane_dates объявлена и доступна вашей программе.
Примечание 2. Считайте, что тип date уже импортирован в программу.
"""
# счетчик для нужного количества ураганов
early_hurricanes = 0
# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1
print(early_hurricanes)


""" Упражнение 4
Вам доступен список dates, содержащий даты. Дополните приведенный ниже код, чтобы он вывел год и номер квартала каждой 
даты из данного списка. Компоненты дат должны быть расположены в исходном порядке, каждые на отдельной строке, 
в следующем формате:
    <год>-Q<номер квартала>
Примечание 1. Продолжительность кварталов:
    1 квартал	январь, февраль, март
    2 квартал	апрель, май, июнь
    3 квартал	июль, август, сентябрь
    4 квартал	октябрь, ноябрь, декабрь
Примечание 2. Начальная часть ответа выглядит так:
    2010-Q3
    2017-Q1
    ...
"""
from datetime import date
dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
         date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
         date(1666, 6, 6), date(1968, 5, 26)]
qu = {1:'Q1',2:'Q1',3:'Q1',4:'Q2',5:'Q2',6:'Q2',7:'Q3',8:'Q3',9:'Q3',10:'Q4',11:'Q4',12:'Q4'}
for i in dates:
    print(f'{i.year}-{qu[i.month]}')


""" Упражнение 5
Реализуйте функцию get_min_max(), которая принимает один аргумент:
dates — список дат (тип date)
Функция должна возвращать кортеж, первым элементом которого является минимальная дата из списка dates, вторым — 
максимальная дата из списка dates. Если список dates пуст, функция должна вернуть пустой кортеж.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
    print(get_min_max(dates))
Sample Output 1:
    (datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))
Sample Input 2:
    print(get_min_max([]))
Sample Output 2:
    ()
"""
from datetime import date
def get_min_max(lst):
    if lst:
        return min(lst), max(lst)
    return tuple()


""" Упражнение 6
Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
    start — начальная дата, тип date
    end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. 
Если start > end, функция должна вернуть пустой список.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_date_range(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    date1 = date(2021, 10, 1)
    date2 = date(2021, 10, 5)
    print(*get_date_range(date1, date2), sep='\n')
Sample Output 1:
    2021-10-01
    2021-10-02
    2021-10-03
    2021-10-04
    2021-10-05
Sample Input 2:
    date1 = date(2019, 6, 5)
    date2 = date(2019, 6, 5)
    print(get_date_range(date1, date2))
Sample Output 2:
    [datetime.date(2019, 6, 5)]
"""
from datetime import date
def get_date_range(start, end):
    lst = []
    for i in range(date.toordinal(start), date.toordinal(end)+1):
        lst.append(date.fromordinal(i))
    return lst


""" Упражнение 7
Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
    start — начальная дата, тип date
    end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.
Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию 
saturdays_between_two_dates(), но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    date1 = date(2021, 11, 1)
    date2 = date(2021, 11, 22)
    print(saturdays_between_two_dates(date1, date2))
Sample Output 1:
    3
Sample Input 2:
    date1 = date(2020, 7, 26)
    date2 = date(2020, 7, 2)
    print(saturdays_between_two_dates(date1, date2))
Sample Output 2:
    4
Sample Input 3:
    date1 = date(2018, 7, 13)
    date2 = date(2018, 7, 13)
    print(saturdays_between_two_dates(date1, date2))
Sample Output 3:
    0
"""
from datetime import date
def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    c = 0
    for i in range(date.toordinal(start), date.toordinal(end)+1):
        # В методе weekdey() номерация дней начинается с 0. 0 - понедельник, 5 - суббота.
        if date.fromordinal(i).weekday() == 5:
            c += 1
    return c
