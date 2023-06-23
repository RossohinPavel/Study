""" Упражнение 1
Реализуйте класс DefaultList, наследника класса UserList, описывающий список, который при попытке получить элемент по
несуществующему индексу возвращает значение по умолчанию. При создании экземпляра класс должен принимать два аргумента
в следующем порядке:
    iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса DefaultList. Если не
передан, начальный набор элементов считается пустым
    default — значение, возвращаемое при попытке получить элемент по несуществующему индексу. По умолчанию равняется
None
Примечание 1. Экземпляр класса DefaultList не должен зависеть от итерируемого объекта, на основе которого он был создан.
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса DefaultList измениться  не должен.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса DefaultList нет, она может быть произвольной.
Sample Input 1:
    defaultlist = DefaultList([1, 2, 3])

    print(defaultlist[0])
    print(defaultlist[-1])
    print(defaultlist[100])
    print(defaultlist[-100])
Sample Output 1:
    1
    3
    None
    None
Sample Input 2:
    defaultlist = DefaultList([1, 2, 3], 0)

    print(defaultlist[0])
    print(defaultlist[-1])
    print(defaultlist[100])
    print(defaultlist[-100])
Sample Output 2:
    1
    3
    0
    0
"""
from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=None, default=None):
        if iterable is None:
            iterable = []
        super().__init__(list(iterable))
        self._default = default

    def __getitem__(self, key):
        try:
            return self.data[key]
        except IndexError:
            return self._default


""" Упражнение 2
Реализуйте класс EasyDict, наследника класса dict, описывающий словарь, значения элементов которого можно получать как 
по ключам ([key]), так и по одноименным атрибутам (.key). Процесс создания экземпляра класса EasyDict должен совпадать 
с процессом создания экземпляра класса dict.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса EasyDict нет, она может быть произвольной.
Sample Input 1:
    easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})
    
    print(easydict['name'])
    print(easydict.city)
Sample Output 1:
    Timur
    Moscow
Sample Input 2:
    easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})
    
    easydict['city'] = 'Dubai'
    easydict['age'] = 30
    print(easydict.city)
    print(easydict.age)
Sample Output 2:
    Dubai
    30
Sample Input 3:
    easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})
    
    easydict.age = 21
    print(easydict)
Sample Output 3:
    {'name': 'Artur', 'city': 'Almetevsk'}
"""
class EasyDict(dict):
    def __getattribute__(self, key):
        return self[key]


""" Упражнение 3
Реализуйте класс TwoWayDict, наследника класса UserDict, описывающий двунаправленный словарь, в который при добавлении 
пары ключ: значение также добавляется и пара значение: ключ. Процесс создания экземпляра класса TwoWayDict должен 
совпадать с процессом создания экземпляра класса UserDict.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса TwoWayDict нет, она может быть произвольной.
Sample Input 1:
    twowaydict = TwoWayDict({'apple': 1})
    
    twowaydict['banana'] = 2
    
    print(twowaydict['apple'])
    print(twowaydict[1])
    print(twowaydict['banana'])
    print(twowaydict[2])
Sample Output 1:
    1
    apple
    2
    banana
Sample Input 2:
    d = TwoWayDict()
    d[3] = 8
    d[7] = 6
    print(d[3], d[8])
    print(d[7], d[6])
    
    d.update({9: 7, 8: 2})
    print(d[9], d[7])
    print(d[8], d[2])
Sample Output 2:
    8 3
    6 7
    7 9
    2 8
"""
from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().__setitem__(value, key)


""" Упражнение 4
Реализуйте класс AdvancedList, наследника класса list, описывающий список с дополнительным функционалом. Процесс 
создания экземпляра класса AdvancedList должен совпадать с процессом создания экземпляра класса list.
Класс AdvancedList должен иметь три метода экземпляра:
    join() — метод, объединяющий все элементы экземпляра класса AdvancedList в строку и возвращающий полученный 
результат. Метод должен принимать один строковый аргумент, по умолчанию равный пробелу, который является разделителем
элементов списка в результирующей строке
    map() — метод, принимающий в качестве аргумента функцию func и применяющий ее к каждому элементу экземпляра класса 
AdvancedList. Метод должен изменять исходный экземпляр класса AdvancedList, а не возвращать новый
    filter() — метод, принимающий в качестве аргумента функцию func и удаляющий из экземпляра класса AdvancedList те 
элементы, для которых функция func вернула значение False. Метод должен изменять исходный экземпляр класса AdvancedList, 
а не возвращать новый
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса AdvancedList нет, она может быть произвольной.
Sample Input 1:
    advancedlist = AdvancedList([1, 2, 3, 4, 5])
    
    print(advancedlist.join())
    print(advancedlist.join('-'))
Sample Output 1:
    1 2 3 4 5
    1-2-3-4-5
Sample Input 2:
    advancedlist = AdvancedList([1, 2, 3, 4, 5])
    
    advancedlist.map(lambda x: -x)
    
    print(advancedlist)
Sample Output 2:
    [-1, -2, -3, -4, -5]
Sample Input 3:
    advancedlist = AdvancedList([1, 2, 3, 4, 5])
    
    advancedlist.filter(lambda x: x % 2 == 0)
    
    print(advancedlist)
Sample Output 3:
    [2, 4]
Sample Input 4:
    advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
    id1 = id(advancedlist)
    
    advancedlist.filter(bool)
    id2 = id(advancedlist)
    
    print(advancedlist)
    print(id1 == id2)
Sample Output 4:
    [1, 2, 3, 4, 5]
    True
"""
class AdvancedList(list):
    def join(self, char=' '):
        return char.join(str(x) for x in self)

    def map(self, func):
        self[:] = map(func, self)

    def filter(self, func):
        self[:] = filter(func, self)


""" Упражнение 5
Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа. 
При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList. Если хотя бы 
один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
    Элементами экземпляра класса NumberList должны быть числа
Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и 
insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно 
возбуждаться исключение TypeError с текстом: Элементами экземпляра класса NumberList должны быть числа
Примечание 1. Числами будет считать экземпляры классов int и float.
Примечание 2. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан. 
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться  не должен.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса NumberList нет, она может быть произвольной.
Sample Input 1:
    numberlist = NumberList([1, 2])
    
    numberlist.append(3)
    numberlist.extend([4, 5])
    numberlist.insert(0, 0)
    print(numberlist)
Sample Output 1:
    [0, 1, 2, 3, 4, 5]
Sample Input 2:
    numberlist = NumberList([0, 1.0])
    
    numberlist[1] = 1
    numberlist = numberlist + NumberList([2, 3])
    numberlist += NumberList([4, 5])
    print(numberlist)
Sample Output 2:
    [0, 1, 2, 3, 4, 5]
Sample Input 3:
    try:
        numberlist = NumberList(['a', 'b', 'c'])
    except TypeError as error:
        print(error)
Sample Output 3:
    Элементами экземпляра класса NumberList должны быть числа
Sample Input 4:
    numberlist = NumberList([1, 2, 3])
    
    try:
        numberlist.append('4')
    except TypeError as error:
        print(error)
Sample Output 4:
    Элементами экземпляра класса NumberList должны быть числа
"""
from collections import UserList


class NumberList(UserList):
    @staticmethod
    def _check(num):
        if not isinstance(num, int | float):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return num

    def __init__(self, iterable):
        super().__init__(self._check(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = self._check(item)

    def insert(self, index, item):
        self.data.insert(index, self._check(item))

    def append(self, item):
        self.data.append(self._check(item))

    def extend(self, other):
        self.data.extend(self._check(item) for item in other)

    def __add__(self, other):
        return self.data + NumberList(other)

    def __iadd__(self, other):
        self.extend(other)
        return self


""" Упражнение 6
Реализуйте класс ValueDict, наследника класса dict, описывающий словарь c дополнительным функционалом. Процесс создания 
экземпляра класса ValueDict должен совпадать с процессом создания экземпляра класса dict.
Класс ValueDict должен иметь два метода экземпляра:
    key_of() — метод, принимающий в качестве аргумента объект value и возвращающий первый ключ экземпляра класса 
ValueDict, имеющий значение value. Если такого ключа нет, метод должен вернуть None.
    keys_of() — метод, принимающий в качестве аргумента объект value и возвращающий итерируемый объект, элементами 
которого являются все ключи экземпляра класса ValueDict, имеющие значение value
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса ValueDict нет, она может быть произвольной.
Sample Input 1:
    valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})
    
    print(valuedict.key_of(2))
    print(*valuedict.keys_of(2))
Sample Output 1:
    banana
    banana orange
Sample Input 2:
    countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
                 'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
                 'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
                 'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
    
    valuedict = ValueDict(countries)
    
    print(valuedict.key_of('Moscow'))
    print(*valuedict.keys_of('Washington'))
Sample Output 2:
    None
Sample Input 3:
    valuedict = ValueDict({})
    
    print(valuedict.key_of(12))
    print(*valuedict.keys_of(33))
Sample Output 3:
    None
"""
class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k

    def keys_of(self, value):
        return (x[0] for x in filter(lambda x: x[1] == value, self.items()))


""" Упражнение 7
Реализуйте класс BirthdayDict, наследника класса UserDict, описывающий словарь с информацией о днях рождения, ключами в 
котором являются имена, а значениями — даты дней рождения. Процесс создания экземпляра класса BirthdayDict должен 
совпадать с процессом создания экземпляра класса UserDict.
При добавлении новой пары ключ: значение в экземпляр класса BirthdayDict должна производиться проверка на наличие в этом 
экземпляре пары, которая имеет такое же значение, что и добавляемая пара. И если такая пара есть, должен выводиться 
текст: Хей, <ключ добавляемой пары>, не только ты празднуешь день рождения в этот день!
Аналогичное поведение должно быть и при изменении значения по ключу.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса BirthdayDict нет, она может быть произвольной.
Sample Input 1:
    from datetime import date
    
    birthdaydict = BirthdayDict()
    
    birthdaydict['Боб'] = date(1987, 6, 15)
    birthdaydict['Том'] = date(1984, 7, 15)
    birthdaydict['Мария'] = date(1987, 6, 15)
Sample Output 1:
    Хей, Мария, не только ты празднуешь день рождения в этот день!
Sample Input 2:
    from datetime import date
    
    birthdaydict = BirthdayDict()
    
    birthdaydict['Боб'] = date(1987, 6, 15)
    birthdaydict['Том'] = date(1984, 7, 15)
    birthdaydict['Мария'] = date(1989, 10, 1)
    birthdaydict['Боб'] = date(1989, 10, 1)
Sample Output 2:
    Хей, Боб, не только ты празднуешь день рождения в этот день!
"""
from collections import UserDict


class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if value in self.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        super().__setitem__(key, value)


""" Упражнение 8
Реализуйте класс MutableString, наследника класса UserString, описывающий изменяемую строку. Процесс создания экземпляра 
класса MutableString должен совпадать с процессом создания экземпляра класса UserString.
Класс MutableString должен иметь три метода экземпляра:
    lower() — метод, переводящий все символы изменяемой строки в нижний регистр
    upper() — метод, переводящий все символы изменяемой строки в верхний регистр
    sort() — метод, сортирующий символы изменяемой строки. Может принимать два необязательных именованных аргумента key 
и reverse, выполняющих ту же задачу, что и в функции sorted()
Экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью 
индексов, причем как положительных, так и отрицательных.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса MutableString нет, она может быть произвольной.
Sample Input 1:
    mutablestring = MutableString('Beegeek')
    
    mutablestring.lower()
    print(mutablestring)
    mutablestring.upper()
    print(mutablestring)
    mutablestring.sort()
    print(mutablestring)
Sample Output 1:
    beegeek
    BEEGEEK
    BEEEEGK
Sample Input 2:
    mutablestring = MutableString('beegeek')
    
    print(mutablestring)
    mutablestring[0] = 'B'
    mutablestring[-4] = 'G'
    print(mutablestring)
Sample Output 2:
    beegeek
    BeeGeek
"""
from collections import UserString


class MutableString(UserString):
    def __setitem__(self, key, value):
        temp = list(self.data)
        temp[key] = value
        self.data = ''.join(temp)

    def __delitem__(self, key):
        self[key] = ['' for _ in range(len(self))][key]

    def lower(self):
        for i in range(len(self)):
            self[i] = self.data[i].lower()

    def upper(self):
        for i in range(len(self)):
            self[i] = self.data[i].upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))
