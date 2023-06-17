""" Упражнение 1
Реализуйте класс Calculator, экземпляры которого позволяют выполнять различные арифметические операции с двумя числами.
При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Calculator должен являться вызываемым объектом и принимать три аргумента:
    a — число
    b — число
    operation — один из символов +, -, * и /
Если operation равняется +, экземпляр класса Calculator должен вернуть сумму a и b, если - — разность a и b, если * —
произведение a и b, если / — частное a и b. При попытке выполнить деление на ноль должно быть возбуждено исключение
ValueError с текстом: Деление на ноль невозможно
Примечание 1. Числами будет считать экземпляры классов int и float.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Calculator нет, она может быть произвольной.
Sample Input 1:
    calculator = Calculator()

    print(calculator(10, 5, '+'))
    print(calculator(10, 5, '-'))
    print(calculator(10, 5, '*'))
    print(calculator(10, 5, '/'))
Sample Output 1:
    15
    5
    50
    2.0
Sample Input 2:
    calculator = Calculator()

    try:
        print(calculator(10, 0, '/'))
    except ValueError as e:
        print(e)
Sample Output 2: Деление на ноль невозможно
"""
class Calculator:
    def __call__(self, a, b, operation):
        if b == 0 and operation == '/':
            raise ValueError('Деление на ноль невозможно')
        return eval(str(a) + operation + str(b))


""" Упражнение 2
Реализуйте класс RaiseTo, экземпляры которого позволяют возводить числа в фиксированную степень. При создании экземпляра 
класс должен принимать один аргумент:
    degree — показатель степени
Экземпляр класса RaiseTo должен являться вызываемым объектом и принимать один аргумент:
    x — число
Экземпляр класса RaiseTo должен возвращать значение x в степени degree.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса RaiseTo нет, она может быть произвольной.
Sample Input 1:
    raise_to_two = RaiseTo(2)
    
    print(raise_to_two(2))
    print(raise_to_two(3))
    print(raise_to_two(4))
Sample Output 1:
    4
    9
    16
Sample Input 2:
    raise_to_three = RaiseTo(3)
    raise_to_four = RaiseTo(4)
    
    print(raise_to_three(3))
    print(raise_to_four(2))
Sample Output 2:
    27
    16
"""
class RaiseTo:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x ** self.degree


""" Упражнение 3
Реализуйте класс Dice, описывающий игральный кубик с определенным количеством граней. При создании экземпляра класс 
должен принимать один аргумент:
    sides — количество граней игрального кубика
Экземпляр класса Dice должен являться вызываемым объектом и не принимать никаких аргументов. При вызове он должен 
возвращать значение случайной грани игрального кубика. Например, если кубик имеет 6 граней, экземпляр класса Dice должен 
вернуть случайное число из диапазона [1; 6].
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Dice нет, она может быть произвольной.
Sample Input:
    kingdice = Dice(6)
    
    print(kingdice() in [1, 2, 3, 4, 5, 6])
    print(kingdice() in [1, 2, 3, 4, 5, 6])
    print(kingdice() in [7, 8, 9, 10])
Sample Output:
    True
    True
    False
"""
from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randint(1, self.sides)


""" Упражнение 4
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать 
три аргумента в следующем порядке:
    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен являться вызываемым объектом и принимать один аргумент:
    x — число
Экземпляр класса QuadraticPolynomial должен возвращать значение выражения ax ** 2 +bx+c, где a,b и c — коэффициенты 
квадратного трехчлена.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.
Sample Input 1:
    func = QuadraticPolynomial(1, 2, 1)
    
    print(func(1))
    print(func(2))
Sample Output 1:
    4
    9
Sample Input 2:
    func = QuadraticPolynomial(1, 3, 4)
    
    print(func(1))
    print(func(2))
Sample Output 2:
    8
    14
"""
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


""" Упражнение 5
Реализуйте класс Strip, экземпляры которого позволяют удалять из начала и конца строки определенные символы. При 
создании экземпляра класс должен принимать один аргумент:
    chars — строка, в которой перечислены удаляемые символы
Экземпляр класса Strip должен являться вызываемым объектом и принимать один аргумент:
    string — строка
Экземпляр класса Strip должен удалять из начала и конца строки string все символы, перечисленные в chars, и возвращать 
полученный результат.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Strip нет, она может быть произвольной.
Sample Input 1:
    strip = Strip('!? ')
    
    print(strip('     ?beegeek!'))
    print(strip('!bee?geek!'))
Sample Output 1:
    beegeek
    bee?geek
Sample Input 2:
    strip = Strip('.,+-')
    
    print(strip('     --++beegeek++--'))
    print(strip('-bee...geek-'))
    print(strip('-+,.b-e-e-g-e-e-k-+,.'))
Sample Output 2:
         --++beegeek
    bee...geek
    b-e-e-g-e-e-k
"""
class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)


""" Упражнение 6
Реализуйте класс Filter, описывающий объект для фильтрации элементов итерируемых объектов. При создании экземпляра класс 
должен принимать один аргумент:
    predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Экземпляр класса Filter должен являться вызываемым объектом и принимать один аргумент:
    iterable — итерируемый объект
Экземпляр класса Filter должен возвращать список, элементами которого являются элементы итерируемого объекта iterable, 
для которых функция predicate вернула значение True.
Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве 
аргумента значения.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Filter нет, она может быть произвольной.
Sample Input 1:
    leave_even = Filter(lambda x: x % 2 == 0)
    numbers = [1, 2, 3, 4, 5, 6]
    
    print(leave_even(numbers))
Sample Output 1:
    [2, 4, 6]
Sample Input 2:
    more_than_five = Filter(lambda x: x > 5)
    numbers = [13, 1, 4, 10, 10, 7]
    
    print(more_than_five(numbers))
Sample Output 2:
    [13, 10, 10, 7]
"""
class Filter:
    def __init__(self, predicate=bool):
        self.predicate = predicate

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))


""" Упражнение 7
Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
    код страны	формат даты
    ru	DD.MM.YYYY
    us	MM-DD-YYYY
    ca	YYYY-MM-DD
    br	DD/MM/YYYY
    fr	DD.MM.YYYY
    pt	DD-MM-YYYY
Реализуйте класс DateFormatter, экземпляры которого позволяют преобразовывать даты в формат определенной страны из 
таблицы выше. При создании экземпляра класс должен принимать один аргумент:
    country_code — код страны
Экземпляр класса DateFormatter должен являться вызываемым объектом и принимать один аргумент:
    d — дата (тип date)
Экземпляр класса DateFormatter должен возвращать строку с датой d в формате страны с кодом country_code.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса DateFormatter нет, она может быть произвольной.
Sample Input 1:
    ru_format = DateFormatter('ru')
    
    print(ru_format(date(2022, 11, 7)))
Sample Output 1: 07.11.2022
Sample Input 2:
    us_format = DateFormatter('us')
    
    print(us_format(date(2022, 11, 7)))
Sample Output 2: 11-07-2022
Sample Input 3:
    ca_format = DateFormatter('ca')
    
    print(ca_format(date(2022, 11, 7)))
Sample Output 3: 2022-11-07
"""
from datetime import date


class DateFormatter:
    def __init__(self, country_code):
        self.__data = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d',
                       'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}[country_code]

    def __call__(self, date):
        return date.strftime(self.__data)


""" Упражнение 8
Реализуйте декоратор @CountCalls, который считает количество вызовов декорируемой функции. Счетчик вызовов должен быть 
доступен по атрибуту calls.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также 
должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CountCalls, но не код, 
вызывающий его.
Sample Input 1:
    @CountCalls
    def add(a, b):
        return a + b
        
    print(add(1, 2))
    print(add(2, 3))
    print(add.calls)
Sample Output 1:
    3
    5
    2
Sample Input 2:
    @CountCalls
    def square(a):
        return a ** 2
        
    for i in range(100):
        square(i)
        
    print(square.calls)
Sample Output 2:
    100
"""
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)


""" Упражнение 9
Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции. Кэш должен быть 
доступен по атрибуту cache и представлять собой словарь, ключом в котором является кортеж с аргументами, а значением — 
возвращаемое значение декорируемой функции при вызове с этими аргументами.
Примечание 1. Для однозначного кеширования гарантируется, что декорируемая функция принимает только позиционные 
аргументы.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CachedFunction, но не 
код, вызывающий его.
Sample Input 1:
    @CachedFunction
    def slow_fibonacci(n):
        if n == 1:
            return 0
        elif n in (2, 3):
            return 1
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
        
    print(slow_fibonacci(100))
Sample Output 1: 218922995834555169026
Sample Input 2:
    @CachedFunction
    def slow_fibonacci(n):
        if n == 1:
            return 0
        elif n in (2, 3):
            return 1
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
        
    slow_fibonacci(5)
    
    for args, value in sorted(slow_fibonacci.cache.items()):
        print(args, value)
Sample Output 2:
    (2,) 1
    (3,) 1
    (4,) 2
    (5,) 3
"""
class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        res = self.cache.setdefault(args, None)
        if res is None:
            res = self.func(*args)
            self.cache[args] = res
        return res


""" Упражнение 10
Нередко во время сортировки объектов мы используем дополнительную функцию, которая описывает правило сортировки. 
Например, если нам нужно отсортировать список экземпляров некоторого класса на основе значений определенного атрибута, 
мы можем реализовать функцию, которая принимает в качестве аргумента этот экземпляр и возвращает значение необходимого 
атрибута.
Приведенный ниже код:
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def __repr__(self):
            return f'User({self.name}, {self.age})'
    
    
    users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]
    
    print(sorted(users, key=lambda user: user.age))
выводит: [User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
Удобно было бы иметь класс SortKey, позволяющий сортировать объекты на основе значений различных атрибутов, лишь 
перечисляя имена этих атрибутов.
Чтобы приведенный ниже код:
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def __repr__(self):
            return f'User({self.name}, {self.age})'
    
    
    users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]
    
    print(sorted(users, key=SortKey('age')))            # сортировка на основе атрибута age
    print(sorted(users, key=SortKey('name', 'age')))    # сортировка на основе атрибута name, а затем age
выводил:
    [User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
    [User(Arthur, 20), User(Gvido, 67), User(Timur, 30)]
Реализуйте класс SortKey, описывающий ключ для сортировки объектов на основе значений их определенных атрибутов. При 
создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых 
представляет имя атрибута, участвующего в сортировке.
Примечание 1. Имена атрибутов при создании экземпляра класса SortKey передаются в порядке приоритета, то есть при 
сортировке сначала должно учитываться значение первого атрибута, затем второго, и так далее.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса SortKey нет, она может быть произвольной.
Sample Input 1:
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def __repr__(self):
            return f'User({self.name}, {self.age})'
    
    users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]
    
    print(sorted(users, key=SortKey('name')))
    print(sorted(users, key=SortKey('name', 'age')))
    print(sorted(users, key=SortKey('age')))
    print(sorted(users, key=SortKey('age', 'name')))
Sample Output 1:
    [User(Arthur, 20), User(Gvido, 67), User(Gvido, 60), User(Timur, 30), User(Timur, 45)]
    [User(Arthur, 20), User(Gvido, 60), User(Gvido, 67), User(Timur, 30), User(Timur, 45)]
    [User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)]
    [User(Arthur, 20), User(Timur, 30), User(Timur, 45), User(Gvido, 60), User(Gvido, 67)]
Sample Input 2:
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def __repr__(self):
            return f'User({self.name}, {self.age})'
    
    users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]
    
    print(max(users, key=SortKey('name')))
    print(max(users, key=SortKey('age')))
    print(max(users, key=SortKey('name', 'age')))
    print(max(users, key=SortKey('age', 'name')))
Sample Output 2:
    User(Timur, 30)
    User(Gvido, 67)
    User(Timur, 45)
    User(Gvido, 67)
"""
class SortKey:
    def __init__(self, *args):
        self.attr = args

    def __call__(self, obj):
        return tuple(getattr(obj, x) for x in self.attr)
