""" Упражнение 1
Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.
Класс Processor имеет один статический метод:
process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его в зависимости от его
типа и возвращает полученный результат. Если тип переданного объекта не поддерживается методом, возбуждается исключение
TypeError с текстом:
Аргумент переданного типа не поддерживается
Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod, чтобы он выполнял ту же задачу.
Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе process() класса Processor.
Примечание 2. Никаких ограничений касательно реализации класса Processor нет, она может быть произвольной.
Sample Input 1:
    print(Processor.process(10))
    print(Processor.process(5.2))
    print(Processor.process('hello'))
    print(Processor.process((4, 3, 2, 1)))
    print(Processor.process([3, 2, 1]))
Sample Output 1:
    20
    10.4
    HELLO
    (1, 2, 3, 4)
    [1, 2, 3]
Sample Input 2:
    try:
        Processor.process({1, 2, 3})
    except TypeError as e:
        print(e)
Sample Output 2: Аргумент переданного типа не поддерживается
"""
from functools import singledispatchmethod


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_nums(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def _from_str(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def _from_list(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(data):
        return tuple(sorted(data))


""" Упражнение 2
Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Negator должен иметь один статический метод:
    neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение. Если методу 
передается целое или вещественное число, он должен возвращать это число, взятое с противоположным знаком. Если методу 
в качестве аргумента передается булево значение, он должен возвращать булево значение, противоположное переданному. Если 
переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError 
с текстом: Аргумент переданного типа не поддерживается
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Negator нет, она может быть произвольной.
Sample Input 1:
    print(Negator.neg(11.0))
    print(Negator.neg(-12))
    print(Negator.neg(True))
    print(Negator.neg(False))
Sample Output 1:
    -11.0
    12
    False
    True
Sample Input 2:
    try:
        Negator.neg('number')
    except TypeError as e:
        print(e)
Sample Output 2: Аргумент переданного типа не поддерживается
"""
from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(value):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _from_nums(value):
        return abs(value) if value < 0 else - value

    @neg.register
    @staticmethod
    def _from_bool(value: bool):
        return not value


""" Упражнение 3
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Formatter должен иметь один статический метод:
    format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий 
информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо другому 
типу, должно быть возбуждено исключение TypeError с текстом: Аргумент переданного типа не поддерживается
Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.
Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.
Sample Input 1:
    Formatter.format(1337)
    Formatter.format(20.77)
Sample Output 1:
    Целое число: 1337
    Вещественное число: 20.77
Sample Input 2:
    Formatter.format([10, 20, 30, 40, 50])
    Formatter.format(([1, 3], [2, 4, 6]))
Sample Output 2:
    Элементы списка: 10, 20, 30, 40, 50
    Элементы кортежа: [1, 3], [2, 4, 6]
Sample Input 3:
    Formatter.format({'Cuphead': 1, 'Mugman': 3})
    Formatter.format({1: 'one', 2: 'two'})
    Formatter.format({1: True, 0: False})   
Sample Output 3:
    Пары словаря: ('Cuphead', 1), ('Mugman', 3)
    Пары словаря: (1, 'one'), (2, 'two')
    Пары словаря: (1, True), (0, False)
Sample Input 4:
    try:
        Formatter.format('All them years, Dutch, for this snake?')
    except TypeError as e:
        print(e)
Sample Output 4: Аргумент переданного типа не поддерживается
"""
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(value):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(float)
    @format.register(int)
    @staticmethod
    def _from_nums(value):
        print('Целое' if isinstance(value, int) else 'Вещественное', 'число:', str(value))

    @format.register(list)
    @format.register(tuple)
    @staticmethod
    def _from_iterable(value):
        print('Элементы', 'списка:' if isinstance(value, list) else 'кортежа:', ', '.join(str(x) for x in value))

    @format.register(dict)
    @staticmethod
    def _from_dict(value):
        print('Пары словаря:', ', '.join(str(x) for x in value.items()))


""" Упражнение 4
Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один 
аргумент: birth_date — дата рождения, представленная в одном из следующих вариантов:
    экземпляр класса date
    строка с датой в ISO формате
    список или кортеж из трех целых чисел: года, месяца и дня
Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение 
TypeError с текстом: Аргумент переданного типа не поддерживается
Экземпляр класса BirthInfo должен иметь один атрибут:
    birth_date — дата рождения в виде экземпляра класса date
Класс BirthInfo должен иметь одно свойство:
    age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, 
прошедших с даты рождения на сегодняшний день
Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его 
возраст увеличивается на один год.
Приведенный ниже код:
    birthinfo = BirthInfo(date(2023, 2, 26))
    
    print(birthinfo.age)
в 2024-02-25 должен выводить: 0
в 2024-02-26 должен выводить: 1
в 2025-02-25 должен выводить: 1
в 2025-02-26 должен выводить: 2
Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную функцию 
current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса BirthInfo нет, она может быть произвольной.
Sample Input 1:
    birthinfo1 = BirthInfo('2020-09-18')
    birthinfo2 = BirthInfo(date(2010, 10, 10))
    birthinfo3 = BirthInfo([2016, 1, 1])
    
    print(birthinfo1.birth_date)
    print(birthinfo2.birth_date)
    print(birthinfo3.birth_date)
Sample Output 1:
    2020-09-18
    2010-10-10
    2016-01-01
Sample Input 2:
    birthday = date(2020, 9, 18)
    today = date.today()
    birthinfo = BirthInfo(birthday)
    true_age = current_age(birthday, today)
    
    print(birthinfo.age == true_age)
Sample Output 2: True
"""
from functools import singledispatchmethod
from datetime import date


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _from_dastetype(self, value):
        self.birth_date = value

    @__init__.register(str)
    def _from_iso(self, value):
        self.birth_date = date.fromisoformat(value)

    @__init__.register(tuple)
    @__init__.register(list)
    def _from_iterable(self, value):
        self.birth_date = date(*value)

    @property
    def age(self):
        today = date.today()
        count = 0
        while True:
            birth_date = list(map(int, str(self.birth_date).split('-')))
            birth_date[0] += count
            if date(*birth_date) <= today:
                count += 1
            else:
                return count - 1
