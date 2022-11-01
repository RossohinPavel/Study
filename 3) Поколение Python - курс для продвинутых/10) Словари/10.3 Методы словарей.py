""" Упражнение 1
Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 1 до 15
(включительно), а значения представляют собой квадраты ключей.
Примечание. Выводить содержимое словаря result не нужно.
"""
result = {x: x**2 for x in range(1, 16)}


""" Упражнение 2
Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, складывая значения 
по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий словарь необходимо 
присвоить переменной result.
Примечание. Выводить содержимое словаря result не нужно.
"""
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = dict1.copy()
for i in dict2:
    if i in result:
        result[i] += dict2[i]
    else:
        result.update({i: dict2[i]})


""" Упражнение 3
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text 
будет подсчитано количество его вхождений.
Примечание. Выводить содержимое словаря result не нужно.
"""
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {x: text.count(x) for x in set(text)}


""" Упражнение 4
Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, 
должно быть выведено то, что меньше в лексикографическом порядке.
"""
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry ' \
    'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon ' \
    'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple ' \
    'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
    'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
d = {x: s.count(x) for x in set(s.split())}
print(sorted(d, key=d.get, reverse=True)[0])


""" Упражнение 5
Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж вида 
(кличка собаки, имя владельца, фамилия владельца, возраст владельца).
Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут 
перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список 
кличек собак (сохранив исходный порядок следования).
Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.
Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
Примечание 3. Выводить содержимое словаря result не нужно.
"""
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for line in pets:
    key, value = line[1:], line[0]
    if key in result:
        result[key].append(value)
    else:
        result[key] = [value]


""" Упражнение 6
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, 
без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать 
как одинаковые.
Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки 
препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
Sample Input 1: home sweet home
Sample Output 1: sweet
Sample Input 2: home sweet home sweet.
Sample Output 2: home
"""
st = [x.strip('.,!?:;-') for x in input().lower().split()]
d = {x: st.count(x) for x in sorted(set(st))}
print(sorted(d, key=d.get)[0])


""" Упражнение 7
На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, 
чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам 
постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
Формат входных данных
На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.
Формат выходных данных
Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.
Sample Input 1: a b c a a d c
Sample Output 1: a b c a_1 a_2 d c_1
Sample Input 2: a b c
Sample Output 2: a b c
"""
st = input().split()
d = {}
for i in st:
    if i in d:
        print(f'{i}_{d[i]}', end=' ')
        d[i] += 1
    else:
        d[i] = 1
        print(i, end=' ')
