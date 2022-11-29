""" Упражнение 1
Вам доступен список кортежей data с данными о доходах некоторого образовательного ресурса. Первым элементом кортежа
является название продукта, вторым — прибыль в долларах.
Дополните приведенный ниже код, чтобы он определил, какой общий доход принес каждый продукт и вывел названия всех
продуктов, указав для каждого соответствующую общую прибыль. Продукты должны быть расположены в лексикографическом
порядке, каждый на отдельной строке, в следующем формате:
    <продукт>: $<общая прибыль>
Примечание. Начальная часть ответа выглядит так:
    Books: $7969
    Courses: $2991
    ...
"""
from collections import defaultdict
data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]
results = defaultdict(int)
for key, value in data:
    results[key] += value
for name in sorted(results):
    print(f'{name}: ${results[name]}')


""" Упражнение 2
Вам доступен список кортежей staff с данными о сотрудниках некоторой компании. Первым элементом кортежа является 
название отдела, вторым — имя и фамилия сотрудника, работающего в этом отделе.
Дополните приведенный ниже код, чтобы он определил, какое число сотрудников работает в каждом отделе и вывел названия 
всех отделов, указав для каждого соответствующее количество сотрудников. Отделы должны быть расположены в 
лексикографическом порядке, каждый на отдельной строке, в следующем формате:
    <отдел>: <количество сотрудников>
Примечание. Начальная часть ответа выглядит так:
    Accounting: 17
    Developing: 7
    ...
"""
from collections import defaultdict
staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'),
         ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
         ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'),
         ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
         ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'),
         ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
         ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'),
         ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
         ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'),
         ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
         ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'),
         ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
         ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'),
         ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
         ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'),
         ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
         ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
result = defaultdict(int)
for key, value in staff:
    result[key] += 1
for key in sorted(result):
    print(f'{key}: {result[key]}')


""" Упражнение 3
Вам доступен список кортежей staff_broken с данными о сотрудниках некоторой компании. Первым элементом кортежа является 
название отдела, вторым — имя и фамилия сотрудника, работающего в этом отделе. Некоторые сотрудники могут встречаться 
в списке несколько раз.
Дополните приведенный ниже код, чтобы он сгруппировал сотрудников по соответствующим отделам и вывел названия всех 
отделов, указав для каждого имена и фамилии его сотрудников. Отделы, а также имена и фамилии сотрудников в этих отделах, 
должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:
    <отдел>: <имя> <фамилия>, <имя> <фамилия>, ...
Примечание. Начальная часть ответа выглядит так:
Accounting: Aaron Ferguson, Ann Bell, Brenda Davis, Casey Jenkins, Craig Wood, Dale Houston, Edna Cunningham, Gloria Higgins, James Wilkins, Jane Jackson, John Watts, Kay Scott, Kimberly Reynolds, Linda Hudson, Michelle Wright, Rosemary Garcia, Steven Diaz
Developing: Arlene Gibson, Deborah George, Joyce Rivera, Miguel Norris, Nicole Watts, Thomas Porter, Wilma Woods
...
"""
from collections import defaultdict
staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]
result = defaultdict(set)
for key, value in staff_broken:
    result[key].add(value)
for key in sorted(result):
    print(f'{key}: {", ".join(sorted(result[key]))}')


""" Упражнение 4
В онлайн-школе BEEGEEK каждое лето проходят соревнования по шахматам, во время которых ведется статистика побед и 
поражений. Каждая партия описывается кортежем из двух элементов, где первый элемент — имя победившего ученика, 
второй элемент — имя проигравшего ученика.
Реализуйте функцию wins(), которая принимает один аргумент:
pairs — итерируемый объект, элементами которого являются кортежи, каждый из которых представляет собой пару имён 
победитель-проигравший
Функция должна возвращать словарь, в котором ключом служит имя ученика, а значением — множество имен учеников, 
которых он победил.
Примечание 1. Гарантируется, что каждая партия заканчивается победой одного из учеников, то есть ничьей быть не может.
Примечание 2. Элементы в возвращаемом функцией могут располагаться в произвольном порядке.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию wins(), но не код, 
вызывающий ее.
Sample Input 1:
    result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
    for winner, losers in sorted(result.items()):
        print(winner, '->', *sorted(losers))
Sample Output 1:
    Дима -> Артур
    Тимур -> Артур Дима
Sample Input 2:
    result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])
    for winner, losers in sorted(result.items()):
        print(winner, '->', *sorted(losers))
Sample Output 2:
    Артур -> Анри Дима Тимур
    Дима -> Артур
"""
from collections import defaultdict
def wins(pairs):
    dd = defaultdict(set)
    for key, value in pairs:
        dd[key].add(value)
    return dd


""" Упражнение 5
Рассмотрим следующий словарь:
    {'a': [1, 2], 'b': [3, 1], 'c': [2]}
«Перевернем» его, представив ключи в виде значений, а значения — в виде ключей:
    {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}
Реализуйте функцию flip_dict(), которая принимает один аргумент:
dict_of_lists — словарь, в котором ключом является число или строка, а значением — список чисел или строк
Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве значения по умолчанию), 
который представляет собой «перевернутый» словарь dict_of_lists.
Примечание 1. Ключи в возвращаемом функцией словаре, а также элементы в списках должны располагаться в 
своем исходном порядке.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию flip_dict(), но не код, 
вызывающий ее.
Sample Input 1:
    print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))
Sample Output 1:
    defaultdict(<class 'list'>, {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']})
Sample Input 2:
    data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}
    
    for key, values in flip_dict(data).items():
        print(f'{key}: {", ".join(values)}')
Sample Output 2:
    cacao: Arthur
    tea: Arthur, Timur
    juice: Arthur, Timur, Anri
    coffee: Timur, Anri
"""
from collections import defaultdict
def flip_dict(dict_of_lists):
    res = defaultdict(list)
    for key, values in dict_of_lists.items():
        for value in values:
            res[value].append(key)
    return res


""" Упражнение 6
Рассмотрим два списка:
    messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
    senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
Первый список представляет набор отправленных сообщений в некотором мессенджере, второй список — набор отправителей этих 
сообщений. Причем сообщение messages[i] отправлено пользователем senders[i]. Каждое сообщение представляет собой 
последовательность слов, разделенных пробелом (знаки препинания считаются частями слов). Количество слов — это общее 
число слов, отправленное пользователем. Обратите внимание, что каждый пользователь может отправлять более одного 
сообщения. Например, пользователь Sam Fisher отправил 22 слова в первом сообщении и 44 слова во втором, следовательно, 
его количество слов равно 2 + 4 = 62+4=6. 
Реализуйте функцию best_sender(), которая принимает два аргумента в следующем порядке:
    messages — список сообщений
    senders — список имен отправителей
Функция должна определять отправителя, имеющего наибольшее количество слов, и возвращать его имя. Если таких 
отправителей несколько, следует вернуть имя того, чье имя больше в лексикографическом сравнении.
Примечание 1. Гарантируется, что длины передаваемых в функцию списков совпадают.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию best_sender(), 
но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
    senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
    print(best_sender(messages, senders))
Sample Output 1:
    Sam Fisher
Sample Input 2:
    messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
    senders = ['Bob', 'Charlie']
    print(best_sender(messages, senders))
Sample Output 2:
    Charlie
"""
from collections import defaultdict
def best_sender(messages, senders):
    res = defaultdict(int)
    for i in range(len(senders)):
        res[senders[i]] += len(messages[i].split())
    return max(res, key=lambda x: (res[x], x))
