""" Упражнение 1
Дополните приведенный ниже код, чтобы он создал именованный кортеж Fruit с полями name, color и vitamins.
Примечание. Программа ничего не должна выводить.
"""
from collections import namedtuple
Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])


""" Упражнение 2
Вам доступен именованный кортеж Game. Дополните приведенный ниже код, чтобы он создал именованный кортеж типа 
ExtendedGame, имеющий те же поля, что и Game, а также два дополнительных поля — release_date и price.
Примечание. Программа ничего не должна выводить.
"""
from collections import namedtuple
Game = namedtuple('Game', 'name developer publisher')
ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])


""" Упражнение 3
Вам доступен именованный кортеж Animal, который содержит данные о животном. Первым элементом именованного кортежа 
является имя животного, вторым — семейство, третьим — пол, четвертым — цвет. Также доступен файл data.pkl, содержащий 
сериализованный список этих кортежей.
Дополните приведенный ниже код, чтобы для каждого кортежа из этого списка он вывел названия его полей и значения этих 
полей в следующем формате:
    name: <значение>
    family: <значение>
    sex: <значение>
    color: <значение>
Между полями и значениями двух разных кортежей должна располагаться пустая строка.
Примечание 1. Сначала должно следовать содержание первого кортежа из списка, затем второго, и так далее.
Примечание 2. Например, если бы файл data.pkl содержал следующий сериализованный список:
[Animal(name='Alex', family='dogs', sex='m', color='brown'), Animal(name='Nancy', family='dogs', sex='w', color='black')]
то программа должна была бы вывести: 
    name: Alex
    family: dogs
    sex: m
    color: brown
    
    name: Nancy
    family: dogs
    sex: w
    color: black
"""
import pickle
from collections import namedtuple as nt
Animal = nt('Animal', ['name', 'family', 'sex', 'color'])
with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
for line in data:
    for x, y in zip(line._fields, line):
        print(x, ': ', y, sep='')
    if data.index(line) != len(data) - 1:
        print()


""" Упражнение 4
Вам доступен именованный кортеж User, который содержит данные о пользователе некоторого ресурса. Первым элементом 
именованного кортежа является имя пользователя, вторым — фамилия, третьим — адрес электронной почты, четвертым — статус 
оформленной подписки. Также доступен список users, содержащий эти кортежи.
Дополните приведенный ниже код, чтобы вывел данные о каждом пользователе из этого списка, предварительно отсортировав 
их по статусу подписки от дорогой к дешевой, а при совпадении статусов — в лексикографическом порядке адресов 
электронных почт. Данные о каждом пользователе должны быть указаны в следующем формате:
    <имя> <фамилия>
      Email: <адрес электронной почты>
      Plan: <статус подписки>
Между данными двух разных пользователей должна располагаться пустая строка.
Примечание 1. Самой дорогой подпиской считается Gold, затем Silver, Bronze и Basic.
Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):
    Kathleen Lyons
      Email: balchen@att.net
      Plan: Gold
    
    William Townsend
      Email: kosact@verizon.net
      Plan: Gold
    
    ...
"""
from collections import namedtuple
User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
status = ['Gold', 'Silver', 'Bronze', 'Basic']
sorted_users = sorted(users, key=lambda x: (status.index(x.plan), x.email))
for line in sorted_users:
    print(line.name, line.surname)
    print(' ', 'Email:', line.email)
    print(' ', 'Plan:', line.plan, end='')
    print(end='\n\n' if sorted_users.index(line) != len(sorted_users) - 1 else '')


""" Упражнение 5
У Тимура имеется немало друзей из других городов или стран, которые часто приезжают к нему в гости с целью увидеться и 
развлечься. Чтобы не забыть ни об одной встрече, Тимур записывает имена и фамилии друзей в csv файл, дополнительно 
указывая для каждого дату и время встречи. Вам доступен этот файл, имеющий название meetings.csv, в котором в первом 
столбце записана фамилия, во втором — имя, в третьем — дата в формате DD.MM.YYYY , в четвертом — время в формате HH:MM:
    surname,name,meeting_date,meeting_time
    Харисов,Артур,15.07.2022,17:00
    Геор,Гагиев,14.12.2022,18:00
    ...
Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и времени 
встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.
Примечание 1. Начальная часть ответа выглядит так:
    Гудцев Таймураз
    Харисов Артур
    Базиев Герман
...
Примечание 2. Гарантируется, что никакие две встречи не имеют одновременно одинаковые даты и время.
Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
Примечание 4. Разделителем в файле meetings.csv является запятая, при этом кавычки не используются.
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
"""
import csv
def sorted_func(dct) -> tuple:
    return *map(int, dct['meeting_date'].split('.')[::-1]), *map(int, dct['meeting_time'].split(':'))
with open('meetings.csv', encoding='UTF-8') as file:
    data = csv.DictReader(file)
    for line in sorted(data, key=sorted_func):
        print(line['surname'], line['name'])
