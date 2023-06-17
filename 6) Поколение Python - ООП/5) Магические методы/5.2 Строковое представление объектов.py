""" Упражнение 1
Требовалось реализовать класс Book, описывающий книгу. При создании экземпляра класс должен был принимать три аргумента
в следующем порядке:
    title — название книги
    author — автор книги
    year — год выпуска книги
Предполагалось, что экземпляры класса Book будут иметь следующее формальное строковое представление:
    Book('<название книги>', '<автор книги>', <год выпуска книги>)
И следующее неформальное строковое представление:
    <название книги> (<автор книги>, <год выпуска книги>)
Программист торопился и решил задачу неправильно. Исправьте приведенный ниже код и реализуйте класс Book правильно.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Book нет, она может быть произвольной.
Sample Input 1:
    book = Book('Изучаем Python', 'Марк Лутц', 2021)

    print(book)
    print(repr(book))
Sample Output 1:
    Изучаем Python (Марк Лутц, 2021)
    Book('Изучаем Python', 'Марк Лутц', 2021)
Sample Input 2:
    book = Book('Программируем на Python', 'Майкл Доусон', 2023)

    print(str(book))
    print(repr(book))
Sample Output 2:
    Программируем на Python (Майкл Доусон, 2023)
    Book('Программируем на Python', 'Майкл Доусон', 2023)
"""
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'


""" Упражнение 2
Вам доступен класс Rectangle, описывающий прямоугольник. При создании экземпляра класс принимает два аргумента в 
следующем порядке:
    length — длина прямоугольника
    width — ширина прямоугольника   
Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:
    Rectangle(<длина прямоугольника>, <ширина прямоугольника>)
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Rectangle нет, она может быть произвольной.
Sample Input 1:
    rectangle = Rectangle(1, 2)
    
    print(str(rectangle))
    print(repr(rectangle))
Sample Output 1:
    Rectangle(1, 2)
    Rectangle(1, 2)
Sample Input 2:
    rectangle1 = Rectangle(1, 2)
    rectangle2 = Rectangle(3, 4)
    
    print(rectangle1)
    print(repr(rectangle2))
Sample Output 2:
    Rectangle(1, 2)
    Rectangle(3, 4)
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


""" Упражнение 3
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента 
в следующем порядке:
    x — координата вектора по оси x
    y — координата вектора по оси y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:
    Vector(<координата x>, <координата y>)
И следующее неформальное строковое представление:
    Вектор на плоскости с координатами (<координата x>, <координата y>)
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.
Sample Input 1:
    vector = Vector(1, 2)
    
    print(str(vector))
    print(repr(vector))
Sample Output 1:
    Вектор на плоскости с координатами (1, 2)
    Vector(1, 2)
Sample Input 2:
    vectors = [Vector(1, 2), Vector(3, 4)]
    
    print(vectors)
Sample Output 2:
    [Vector(1, 2), Vector(3, 4)]
"""
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Vector{self.x, self.y}'

    def __str__(self):
        return f'Вектор на плоскости с координатами {self.x, self.y}'


""" Упражнение 4
IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете или локальной сети. IP-адреса представляют 
собой набор из четырех целых чисел, разделенных точками. Например, 192.158.1.38. Каждое число в наборе принадлежит 
интервалу от 0 до 255. Таким образом, полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.
Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра класс должен принимать один аргумент:
    ipaddress — IP-адрес, представленный в одном из следующих вариантов:
        строка из четырех целых чисел, разделенных точками
        список или кортеж из четырех целых чисел
Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:
    IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:
    <IP-адрес в виде четырех целых чисел, разделенных точками>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса IPAddress нет, она может быть произвольной.
Sample Input 1:
    ip = IPAddress('8.8.1.1')
    
    print(str(ip))
    print(repr(ip))
Sample Output 1:
    8.8.1.1
    IPAddress('8.8.1.1')
Sample Input 2:
    ip = IPAddress([1, 1, 10, 10])
    
    print(str(ip))
    print(repr(ip))
Sample Output 2:
    1.1.10.10
    IPAddress('1.1.10.10')
Sample Input 3:
    ip = IPAddress((1, 1, 11, 11))
    
    print(str(ip))
    print(repr(ip))
Sample Output 3:
    1.1.11.11
    IPAddress('1.1.11.11')
"""
from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, string):
        self.ip_adress = string

    @__init__.register(list)
    @__init__.register(tuple)
    def from_iterable(self, iterable):
        self.ip_adress = '.'.join(str(x) for x in iterable)

    def __str__(self):
        return self.ip_adress

    def __repr__(self):
        return f"IPAddress('{str(self.ip_adress)}')"


""" Упражнение 5
Реализуйте класс PhoneNumber, описывающий телефонный номер. При создании экземпляра класс должен принимать один аргумент:
    phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих форматов:
    dddddddddd
    ddd ddd dddd
Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:
    PhoneNumber('<телефонный номер в формате dddddddddd>')
И следующее неформальное строковое представление:
    <телефонный номер в формате (ddd) ddd-dddd>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса PhoneNumber нет, она может быть произвольной.
Sample Input 1:
    phone = PhoneNumber('9173963385')
    
    print(str(phone))
    print(repr(phone))
Sample Output 1:
    (917) 396-3385
    PhoneNumber('9173963385')
Sample Input 2:
    phone = PhoneNumber('918 396 3389')
    
    print(str(phone))
    print(repr(phone))
Sample Output 2:
    (918) 396-3389
    PhoneNumber('9183963389')
Sample Input 3:
    phone1 = PhoneNumber('9173963385')
    phone2 = PhoneNumber('918 396 3389')
    phone3 = PhoneNumber('919 333 3344')
    
    print(phone1, phone2, phone3, sep=', ')
    print([phone1, phone2, phone3])
Sample Output 3:
    (917) 396-3385, (918) 396-3389, (919) 333-3344
    [PhoneNumber('9173963385'), PhoneNumber('9183963389'), PhoneNumber('9193333344')]
"""
class PhoneNumber:
    def __init__(self, string):
        self.number = ''.join(string.split())

    def __repr__(self):
        return f'PhoneNumber({repr(self.number)})'

    def __str__(self):
        return f'({self.number[0:3]}) {self.number[3:6]}-{self.number[6:]}'

""" Упражнение 6
Реализуйте класс AnyClass. При создании экземпляра класс должен принимать произвольное количество именованных аргументов 
и устанавливать их в качестве атрибутов создаваемому экземпляру.
Экземпляр класса AnyClass должен иметь следующее формальное строковое представление:
    AnyClass(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)
И следующее неформальное строковое представление:
    AnyClass: <имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...
Примечание 1. Обратите внимание, что в формальном строковом представлении значения атрибутов, которые принадлежат типу 
str, должны быть обрамлены апострофами.
Примечание 2. Никаких ограничений касательно реализации класса AnyClass нет, она может быть произвольной.
Sample Input 1:
    any = AnyClass()
    
    print(str(any))
    print(repr(any))
Sample Output 1:
    AnyClass: 
    AnyClass()
Sample Input 2:
    cowboy = AnyClass(name='John', surname='Marston')
    
    print(str(cowboy))
    print(repr(cowboy))
Sample Output 2:
    AnyClass: name='John', surname='Marston'
    AnyClass(name='John', surname='Marston')
Sample Input 3:
    obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)
    
    print(str(obj))
    print(repr(obj))
Sample Output 3:
    AnyClass: attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None
    AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)
"""


class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_kwargs(self):
        return ', '.join(f'{k}={repr(v)}' for k, v in self.__dict__.items())

    def __repr__(self):
        return 'AnyClass(' + self.get_kwargs() + ')'

    def __str__(self):
        return "AnyClass: " + self.get_kwargs()
