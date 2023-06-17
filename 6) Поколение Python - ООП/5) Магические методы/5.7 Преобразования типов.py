""" Упражнение 1
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента
в следующем порядке:
    x — координата вектора по оси x
    y — координата вектора по оси y
Экземпляр класса Vector должен иметь следующее неформальное строковое представление:
    (<координата x>, <координата y>)
Также экземпляр класса Vector должен поддерживать приведение к типам bool, int, float и complex:
    при приведении к типу bool значением вектора должно являться значение True, если хотя бы одна его координата
не равна нулю, или False в противном случае
    при приведении к типу int значением вектора должен являться его модуль в виде целого числа с отброшенной дробной
частью
    при приведении к типу float значением вектора должен являться его модуль в виде вещественного числа
    при приведении к типу complex значением вектора должно являться комплексное число, вещественная часть которого равна
координате вектора по оси x, мнимая часть — координате вектора по оси y
Примечание 1. Модуль вектора с координатами (x,y) вычисляется по формуле (x ** 2 + y ** 2) ** 0.5
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.
Sample Input 1:
    vector = Vector(3, 4)

    print(vector)
    print(int(vector))
    print(float(vector))
    print(complex(vector))
Sample Output 1:
    (3, 4)
    5
    5.0
    (3+4j)
Sample Input 2:
    print(bool(Vector(1, 2)))
    print(bool(Vector(1, 0)))
    print(bool(Vector(0, 1)))
    print(bool(Vector(0, 0)))
Sample Output 2:
    True
    True
    True
    False
"""
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return str((self.x, self.y))

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __float__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __complex__(self):
        return complex(self.x, self.y)


""" Упражнение 2
Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия. При создании экземпляра класс должен 
принимать один аргумент:
    temperature — температура в градусах по шкале Цельсия
Класс Temperature должен иметь один метод экземпляра:
    to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта
Класс Temperature должен иметь один метод класса:
    from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта и возвращающий экземпляр 
класса Temperature, созданный на основе переданной температуры
Экземпляр класса Temperature должен иметь следующее неформальное строковое представление:
    <температура в градусах по шкале Цельсия с округлением до двух знаков после запятой>°C
Также экземпляр класса Temperature должен поддерживать приведение к типам bool, int и float:
    при приведении к типу bool значением экземпляра класса Temperature должно являться значение True, если его 
температура выше нуля, или False в противном случае
    при приведении к типу int значением экземпляра класса Temperature должна являться его температура в виде целого 
числа с отброшенной дробной частью
    при приведении к типу float значением экземпляра класса Temperature должна являться его температура в виде 
вещественного числа
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Temperature нет, она может быть произвольной.
Sample Input 1:
    t = Temperature(5.5)
    
    print(t)
    print(int(t))
    print(float(t))
    print(t.to_fahrenheit())
Sample Output 1:
    5.5°C
    5
    5.5
    41.9
Sample Input 2:
    t1 = Temperature(1)
    t2 = Temperature(0)
    t3 = Temperature(-1)
    
    print(bool(t1))
    print(bool(t2))
    print(bool(t3))
Sample Output 2:
    True
    False
    False
Sample Input 3:
    t = Temperature.from_fahrenheit(41)
    
    print(t)
    print(int(t))
    print(float(t))
    print(t.to_fahrenheit())
Sample Output 3:
    5.0°C
    5
    5.0
    41.0
"""
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return 9 / 5 * self.temperature + 32

    @classmethod
    def from_fahrenheit(cls, temperature):
        return cls(5 / 9 * (temperature - 32))

    def __str__(self):
        return str(round(self.temperature, 2)) + '°C'

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


""" Упражнение 3
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен 
принимать один аргумент:
    number — число в римской системе счисления. Например, IV
Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:
    <число в римской системе счисления>
Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому его 
значением должно являться целое число в десятичной системе счисления, которому он соответствует.
Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, 
!=, >, <, >=, <=.
Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью 
операторов + и - соответственно:
    результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
    результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.
Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.
Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих 
арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.
Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 5. Никаких ограничений касательно реализации класса RomanNumeral нет, она может быть произвольной.
Sample Input 1:
    number = RomanNumeral('IV') + RomanNumeral('VIII')
    
    print(number)
    print(int(number))
Sample Output 1:
    XII
    12
Sample Input 2:
    number = RomanNumeral('X') - RomanNumeral('VI')
    
    print(number)
    print(int(number))
Sample Output 2:
    IV
    4
Sample Input 3:
    a = RomanNumeral('X')
    b = RomanNumeral('XII')
    
    print(a == b)
    print(a > b)
    print(a < b)
    print(a >= b)
    print(a <= b)
Sample Output 3:
    False
    False
    True
    False
    True
"""
from functools import total_ordering


@total_ordering
class RomanNumeral:
    __roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
               'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        number = self.number
        int_number = 0
        while number:
            for key in self.__roman:
                if number.startswith(key):
                    int_number += self.__roman[key]
                    number = number[len(key):]
                    break
        return int_number

    @classmethod
    def __to_roman(cls, num):
        roman = ''
        while num:
            for key, value in cls.__roman.items():
                if num - value >= 0:
                    num -= value
                    roman = roman + key
                    break
        return roman

    @staticmethod
    def _check(func):
        def wrapper(base, obj):
            if not isinstance(obj, RomanNumeral):
                return NotImplemented
            return func(base, obj)

        return wrapper

    @_check
    def __eq__(self, other):
        return int(self) == int(other)

    @_check
    def __lt__(self, other):
        return int(self) < int(other)

    @_check
    def __add__(self, other):
        return RomanNumeral(self.__to_roman(int(self) + int(other)))

    @_check
    def __sub__(self, other):
        return RomanNumeral(self.__to_roman(int(self) - int(other)))
