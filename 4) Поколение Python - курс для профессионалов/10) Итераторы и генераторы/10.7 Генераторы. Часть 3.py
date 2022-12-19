""" Упражнение 1
Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым элементом именованного кортежа
является имя и фамилия человека, вторым — национальность, третьим — пол, четвертым — год рождения, пятым — год смерти.
Если человек жив, год смерти считается равным 00. Также доступен список persons, содержащий эти кортежи.
Дополните приведенный ниже код с использованием конвейеров генераторов, чтобы он вывел имя и фамилию самого молодого
живого мужчины из Швеции (Swedish).
Примечание 1. Пример вывода:
    Goran Aslin
Примечание 2. Гарантируется, что искомый человек единственный.
"""
from collections import namedtuple
Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 1950, 0)]
res = (x for x in persons if x[-1] == 0 and x[-3] == 'male' and x[-4] == 'Swedish')
print(max(res, key=lambda x: x[-2])[0])


""" Упражнение 2
Назовем диапазоном запись двух натуральных чисел через дефис a-b, где a — левая граница диапазона, b — правая граница 
диапазона, причем a <= b. Диапазон содержит в себе все числа от a до b включительно. Например, диапазон 1-4 содержит 
числа 1, 2, 3 и 4.
Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:
    ranges — строка, в которой через запятую указаны диапазоны чисел
Функция должна возвращать генератор, порождающий последовательность чисел, содержащихся в диапазонах ranges.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию parse_ranges(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(*parse_ranges('1-2,4-4,8-10'))
Sample Output 1:
    1 2 4 8 9 10
Sample Input 2:
    print(*parse_ranges('1-10,2-10'))
Sample Output 2:
    1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10
Sample Input 3:
    print(*parse_ranges('7-32'))
Sample Output 3:
    7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
"""
def parse_ranges(ranges):
    spl = (x.split('-') for x in ranges.split(','))
    yield from (y for x in spl for y in range(int(x[0]), int(x[1])+1))


""" Упражнение 3
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:
    names — список имен
    ignore_char — одиночный символ
    max_names — натуральное число
Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые
    начинаются на ignore_char (в любом регистре)
    содержат хотя бы одну цифру
Если max_names больше количества имен в списке names, то генератор должен породить все имена из данного списка. 
Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_names(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
    
    print(*filter_names(data, 'D', 3))
Sample Output 1:
    Timur Arthur Arina
Sample Input 2:
    data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
    
    print(*filter_names(data, 't', 20))
Sample Output 2:
    Dima Arthur Arina German Ruslan
Sample Input 3:
    data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 
    'Geo000000r']
    
    print(*filter_names(data, 'A', 100))
Sample Output 3:
"""
def filter_names(names, ignore_char, max_names):
    ignored = (x for x in names if x.isalpha() and x[0].lower() != ignore_char.lower())
    for i, v in enumerate(ignored):
        if i < max_names:
            yield v


""" Упражнение 4
Вам доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы. В первом столбце записано 
название компании (стартапа), во втором — инвестируемая сумма в долларах, в третьем — раунд инвестиции:
    company,raisedAmt,round
    LifeLock,6850000,b
    LifeLock,6000000,a
    LifeLock,25000000,c
    MyCityFaces,50000,seed
    Flypaper,3000000,a
    ...
Напишите программу с использованием конвейеров генераторов, определяющую общую сумму, которая была инвестирована 
в раунде а, и выводящую полученный результат.
Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.
Примечание 2. Указанный файл доступен по ссылке.
Примечание 3. Пример вывода:
    86900000000
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
import csv
with open('data.csv', 'r', encoding='UTF-8') as file:
    data = csv.DictReader(file)
    print(sum(int(x['raisedAmt']) for x in data if x['round'] == 'a'))


""" Упражнение 5
Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
year — натуральное число
Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
Примечание 1. Возьмем в качестве примера 2022 год. В январе этого года 31 день, в феврале — 28, в марте — 31, 
и так далее. Тогда генератор, полученный при вызове years_days(2022), должен порождать сначала все даты с 1 по 31 
января, затем с 1 по 28 февраля, и так далее до 31 декабря.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию years_days(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input:
dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
Sample Output:
    2022-01-01
    2022-01-02
    2022-01-03
    2022-01-04
"""
from datetime import date

def years_days(year):
    itb = date(year, 1, 1)
    x = 0
    while itb.year == date.fromordinal(itb.toordinal() + x).year:
        res = date.fromordinal(itb.toordinal() + x)
        x += 1
        yield res


""" Упражнение 6
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:
    file — название текстового файла, например, data.txt
Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным символом 
переноса строки \n. Если строка содержит более 2525 символов, она заменяется троеточием ....
Примечание 1. При открытии файла используйте явное указание кодировки UTF-8.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию nonempty_lines(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    lines = nonempty_lines('file1.txt')
    
    print(next(lines))
    print(next(lines))
    print(next(lines))
Sample Output 1:
    bee
    geek
    stepik
Sample Input 2:
    print(*nonempty_lines('file2.txt'))
Sample Output 2:
    short line another short line ... end of file
"""
def nonempty_lines(file):
    with open(file, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    yield from (y if len(y) <= 25 else '...' for y in (x.strip() for x in data if x.strip() != ''))


""" Упражнение 7
Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех строках указаны 
характеристики первой планеты, после чего следует пустая строка, затем характеристики второй планеты, и так далее:
    Name = Mercury
    Diameter = 4879.4
    Mass = 3.302×10^23
    OrbitalPeriod = 0.241
    
    Name = Venus
    Diameter = 12103.6
    Mass = 4.869×10^24
    OrbitalPeriod = 0.615
    ...
Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.
Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых содержит информацию 
об очередной планете из файла planets.txt, а именно ее название, диаметр, массу и орбитальный период. Например:
{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
Примечание 1. Указанный файл доступен по ссылке.
Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию txt_to_dict(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input:
    planets = txt_to_dict()
    
    print(next(planets))
Sample Output:
    {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
"""
def txt_to_dict():
    with open('planets.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
        splited = (x for x in data.split('\n\n'))
        ll = (x.split('\n') for x in splited)
        yield from ({y.split(' = ')[0]: y.split(' = ')[1] for y in x} for x in ll)


""" Упражнение 8
Реализуйте генераторную функцию, которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без 
дубликатов.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию unique(), но не код, 
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [1, 2, 2, 3, 4, 5, 5, 5]
    
    print(*unique(numbers))
Sample Output 1:
    1 2 3 4 5
Sample Input 2:
    iterator = iter('111222333')
    uniques = unique(iterator)
    
    print(next(uniques))
    print(next(uniques))
    print(next(uniques))
Sample Output 2:
    1
    2
    3
"""
from collections import Counter
unique = lambda x: (y for y in Counter(x))


""" Упражнение 9
Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:
    iterable — итерируемый объект
    obj — произвольный объект
Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable до тех пор, 
пока не будет достигнут элемент, равный obj. Если итерируемый объект iterable не содержит ни одного элемента, равного 
obj, генератор должен породить все элементы iterable.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию stop_on(), но не код, 
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [1, 2, 3, 4, 5]
    
    print(*stop_on(numbers, 4))
Sample Output 1:
    1 2 3
Sample Input 2:
    iterator = iter('beegeek')
    
    print(*stop_on(iterator, 'a'))
Sample Output 2:
    b e e g e e k
"""
# Решение в лоб
def stop_on(iterable, obj):
    for i in iterable:
        if i == obj:
            return
        yield i
# У Итер есть 2 аргумент - когда функция останавливается
def stop_on(iterable, obj):
    iterator = iter(iterable)
    return iter(lambda: next(iterator), obj)


""" Упражнение 10
Реализуйте генераторную функцию, которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной 
элемент итерируемого объекта iterable, а также предшествующий ему элемент:
(<очередной элемент>, <предыдущий элемент>)
Для первого элемента предыдущим считается значение None.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию with_previous(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [1, 2, 3, 4, 5]
    
    print(*with_previous(numbers))
Sample Output 1:
    (1, None) (2, 1) (3, 2) (4, 3) (5, 4)
Sample Input 2:
    iterator = iter('stepik')
    
    print(*with_previous(iterator))
Sample Output 2:
    ('s', None) ('t', 's') ('e', 't') ('p', 'e') ('i', 'p') ('k', 'i')
"""
def with_previous(iterable):
    iterable = iter(iterable)
    old = None
    for i in iterable:
        yield i, old
        old = i


""" Упражнение 11
Реализуйте генераторную функцию, которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной 
элемент итерируемого объекта iterable, а также следующий за ним элемент:
(<очередной элемент>, <следующий элемент>)
Для последнего элемента следующим считается значение None.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию pairwise(), но не код, 
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [1, 2, 3, 4, 5]
    
    print(*pairwise(numbers))
Sample Output 1:
    (1, 2) (2, 3) (3, 4) (4, 5) (5, None)
Sample Input 2:
    iterator = iter('stepik')
    
    print(*pairwise(iterator))
Sample Output 2:
    ('s', 't') ('t', 'e') ('e', 'p') ('p', 'i') ('i', 'k') ('k', None)
"""
def pairwise(iterable):
    old = None
    for i in iterable:
        if old is not None:
            yield old, i
        old = i
    if old is not None:
        yield old, None


""" Упражнение 12
Реализуйте генераторную функцию, которая принимает один аргумент:
iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной 
элемент итерируемого объекта iterable, а также предыдущий и следующий за ним элементы:
(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)
Для первого элемента предыдущим считается значение None, для последнего элемента следующим считается так же значение 
None.
Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном 
порядке.
Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию around(), но не код, 
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [1, 2, 3, 4, 5]
    
    print(*around(numbers))
Sample Output 1:
    (None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)
Sample Input 2:
    iterator = iter('hey')
    
    print(*around(iterator))
Sample Output 2:
    (None, 'h', 'e') ('h', 'e', 'y') ('e', 'y', None)
"""
def around(iterable):
    old = None
    cur = None
    for i in iterable:
        if cur is not None:
            yield old, cur, i
        old, cur = cur, i
    if cur is not None:
        yield old, cur, None
