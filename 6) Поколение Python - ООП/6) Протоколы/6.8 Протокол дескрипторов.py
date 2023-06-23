""" Упражнение 1
Реализуйте класс NonKeyword, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение
атрибута не является строковым ключевым словом в Python. При создании экземпляра класс должен принимать один аргумент:
    name — имя атрибута, за которым будет закреплен дескриптор
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
    Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, не является ли это значение строковым
ключевым словом в Python. Если значение является строковым ключевым словом, должно быть возбуждено исключение ValueError
с текстом: Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса NonKeyword нет, она может быть произвольной.
Sample Input 1:
    class Student:
        name = NonKeyword('name')

    student = Student()
    student.name = 'Peter'

    print(student.name)
Sample Output 1:
    Peter
Sample Input 2:
    class Student:
        name = NonKeyword('name')

    student = Student()

    try:
        print(student.name)
    except AttributeError as e:
        print(e)
Sample Output 2:
    Атрибут не найден
Sample Input 3:
    class Student:
        name = NonKeyword('name')

    student = Student()
    student.name = 'Peter'

    try:
        student.name = 'class'
    except ValueError as e:
        print(e)
Sample Output 3:
    Некорректное значение
"""
from keyword import kwlist


class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value


""" Упражнение 2
Реализуйте класс NonNegativeInteger, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое 
значение атрибута является неотрицательным целым числом. При создании экземпляра класс должен принимать два аргумента 
в следующем порядке:
    name — имя атрибута, за которым будет закреплен дескриптор
    default — значение по умолчанию. Если не передан, имеет значение None
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение не 
установлено, должно возвращаться значение по умолчанию, указанное при создании дескриптора. Если значение по умолчанию 
равняется None, должно быть возбуждено исключение AttributeError с текстом:
    Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, является ли это значение неотрицательным 
целым числом. Если значение не является неотрицательным целым числом, должно быть возбуждено исключение ValueError 
с текстом: Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса NonNegativeInteger нет, она может быть произвольной.
Sample Input 1:
    class Student:
        score = NonNegativeInteger('score')
    
    student = Student()
    student.score = 90
    
    print(student.score)
Sample Output 1: 90
Sample Input 2:
    class Student:
        score = NonNegativeInteger('score', 0)
    
    student = Student()
    
    print(student.score)
    student.score = 0
    print(student.score)
Sample Output 2:
    0
    0
Sample Input 3:
    class Student:
        score = NonNegativeInteger('score')
    
    student = Student()
    
    try:
        print(student.score)
    except AttributeError as e:
        print(e)
Sample Output 3:
    Атрибут не найден
Sample Input 4:
    class Student:
        score = NonNegativeInteger('score')
    
    student = Student()
    
    try:
        student.score = -90
    except ValueError as e:
        print(e)
Sample Output 4:
    Некорректное значение
"""
class NonNegativeInteger:
    def __init__(self, attr, default=None):
        self._attr = attr
        self._default = default

    def __get__(self, obj, cls):
        value = obj.__dict__.get(self._attr, self._default)
        if value is None:
            raise AttributeError('Атрибут не найден')
        return value

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value


""" Упражнение 3
Реализуйте класс LimitedTakes, описывающий дескриптор, который позволяет получать значение атрибута лишь определенное 
количество раз. При создании экземпляра класс должен принимать один аргумент:
    times — количество доступных обращений к атрибуту
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение 
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
    Атрибут не найден
Если к атрибуту было выполнено times обращений, во время всех последующих обращений должно возбуждаться исключение 
MaxCallsException с текстом: Превышено количество доступных обращений
При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо 
дополнительных проверок.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса LimitedTakes нет, она может быть произвольной.
Sample Input 1:
    class Student:
        name = LimitedTakes(3)
    
    student = Student()
    student.name = 'Gwen'
    
    print(student.name)
    print(student.name)
    print(student.name)
    
    try:
        print(student.name)
    except MaxCallsException as e:
        print(e)
Sample Output 1:
    Gwen
    Gwen
    Gwen
    Превышено количество доступных обращений
Sample Input 2:
    class Student:
        name = LimitedTakes(3)
    
    student = Student()
    
    for _ in range(100):
        student.name = 'Gwen'
        
    print(student.name)
Sample Output 2:
    Gwen
"""
class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        self._times -= 1
        if self._times < 0:
            raise MaxCallsException('Превышено количество доступных обращений')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value


""" Упражнение 4
Реализуйте класс TypeChecked, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение 
атрибута принадлежит определенному типу данных. При создании экземпляра класс должен принимать произвольное количество 
позиционных аргументов, каждый из которых является типом данных.
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение 
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом: Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, принадлежит ли это значение одному из типов, 
указанных при создании дескриптора. Если значение не принадлежит ни одному из типов, должно быть возбуждено исключение 
TypeError с текстом: Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса TypeChecked нет, она может быть произвольной.
Sample Input 1:
    class Student:
        name = TypeChecked(str)
    
    student = Student()
    student.name = 'Mary'
    
    print(student.name)
Sample Output 1:
    Mary
Sample Input 2:
    class Student:
        name = TypeChecked(str)
    
    student = Student()
    
    try:
        print(student.name)
    except AttributeError as e:
        print(e)
Sample Output 2:
    Атрибут не найден
Sample Input 3:
    class Student:
        name = TypeChecked(str)
    
    student = Student()
    student.name = 'Mary'
    
    try:
        student.name = 99
    except TypeError as e:
        print(e)
    
    print(student.name)
Sample Output 3:
    Некорректное значение
    Mary
Sample Input 4:
    class Student:
        age = TypeChecked(int, float)
    
    student = Student()
    
    student.age = 18
    print(student.age)
    
    student.age = 18.5
    print(student.age)
Sample Output 4:
    18
    18.5
"""
class TypeChecked:
    def __init__(self, *types):
        self._types = types

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __set__(self, obj, value):
        if type(value) not in self._types:
            raise TypeError('Некорректное значение')
        obj.__dict__[self._attr] = value

    def __get__(self, obj, cls):
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]


""" Упражнение 5
Реализуйте класс RandomNumber, описывающий дескриптор, который при обращении к атрибуту возвращает случайное целое число 
в заданном диапазоне. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    start — целое число
    end — целое число
    cache — булево значение, по умолчанию равняется False
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
При обращении к атрибуту дескриптор должен возвращать случайное целое число от start до end включительно. Если в 
качестве значения параметра cache при создании дескриптора было указано значение True, при каждом обращении к атрибуту 
дескриптор должен возвращать то число, которое было сгенерировано при первом обращении.
При установке или изменении значения атрибута дескриптор должен возбуждать исключение AttributeError с текстом:
    Изменение невозможно
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса RandomNumber нет, она может быть произвольной.
Sample Input 1:
    class MagicPoint:
        x = RandomNumber(1, 5)
        y = RandomNumber(1, 5)
        z = RandomNumber(1, 5)
    
    magicpoint = MagicPoint()
    
    print(magicpoint.x in [1, 2, 3, 4, 5])
    print(magicpoint.y in [1, 2, 3, 4, 5])
    print(magicpoint.z in [1, 2, 3, 4, 5])
Sample Output 1:
    True
    True
    True
Sample Input 2:
    class MagicPoint:
        x = RandomNumber(1, 5)
        y = RandomNumber(1, 5)
        z = RandomNumber(1, 5)
    
    magicpoint = MagicPoint()
    
    print(magicpoint.x in [6, 7, 8, 9, 10])
    print(magicpoint.y in [6, 7, 8, 9, 10])
    print(magicpoint.z in [6, 7, 8, 9, 10])
Sample Output 2:
    False
    False
    False
Sample Input 3:
    class MagicPoint:
        x = RandomNumber(0, 5, True)
        y = RandomNumber(0, 5)
        z = RandomNumber(0, 5)
    
    magicpoint = MagicPoint()
    value = magicpoint.x
    
    print(magicpoint.x == value)
    print(magicpoint.x == value)
    print(magicpoint.x == value)
Sample Output 3:
    True
    True
    True
Sample Input 4:
    class MagicPoint:
        x = RandomNumber(0, 5)
        y = RandomNumber(0, 5)
        z = RandomNumber(0, 5)
    
    magicpoint = MagicPoint()
    
    try:
        magicpoint.x = 10
    except AttributeError as e:
        print(e)
Sample Output 4:
    Изменение невозможно
"""
from random import randint


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self._start = start
        self._end = end
        self._cache = cache

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')

    def __get__(self, obj, cls):
        if self._attr not in obj.__dict__ or not self._cache:
            obj.__dict__[self._attr] = randint(self._start, self._end)
        return obj.__dict__[self._attr]


""" Упражнение 6
Реализуйте класс Versioned, описывающий дескриптор, предоставляющий доступ как к текущему значению атрибута, так и ко 
всем предыдущим, если значение атрибута когда-либо изменялось. При создании экземпляра класс не должен принимать никаких 
аргументов.
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение 
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом: Атрибут не найден
При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо 
дополнительных проверок.
Класс Versioned должен иметь два метода экземпляра:
    get_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n. 
Метод должен возвращать n-ое по счету значение атрибута этого экземпляра класса. Например, если значение атрибута было 
установлено, а затем изменено, то метод get_version() должен уметь вернуть как установленное значение (первое по счету), 
так и измененное (второе по счету)
    set_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n. 
Метод должен устанавливать n-ое по счету значение атрибута в качестве текущего
Примечание 1. Вызов метода set_version() не должен приравниваться к изменению значения атрибута. Будем считать, что 
атрибут изменяет свое значение только в том случае, если эта операция выполняется через точечную нотацию или функцию 
setattr().
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Versioned нет, она может быть произвольной.
Sample Input 1:
    class Student:
        age = Versioned()
        
    student = Student()
    
    student.age = 18
    student.age = 19
    
    print(student.age)
Sample Output 1:
    19
Sample Input 2:
    class Student:
        age = Versioned()
        
    student = Student()
    
    student.age = 18
    student.age = 19
    student.age = 20
    
    print(student.age)
    print(Student.age.get_version(student, 1))
    print(Student.age.get_version(student, 2))
    print(Student.age.get_version(student, 3))
Sample Output 2:
    20
    18
    19
    20
Sample Input 3:
    class Student:
        age = Versioned()
        
    student = Student()
    
    student.age = 18
    student.age = 19
    student.age = 20
    
    print(student.age)
    Student.age.set_version(student, 1)
    print(student.age)
Sample Output 3:
    20
    18
"""
class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr][-1]

    def __set__(self, obj, value):
        if self._attr not in obj.__dict__:
            obj.__dict__[self._attr] = []
        obj.__dict__[self._attr].append(value)

    def get_version(self, obj, n):
        return obj.__dict__[self._attr][n - 1]

    def set_version(self, obj, n):
        obj.__dict__[self._attr][-1] = obj.__dict__[self._attr][n - 1]
