""" Упражнение 1
Реализуйте класс UpperPrintString, наследника класса str, описывающий строку. Процесс создания экземпляра класса
UpperPrintString должен совпадать с процессом создания экземпляра класса str.
Экземпляр класса UpperPrintString должен иметь следующее неформальное строковое представление:
    <значение строки в верхнем регистре>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса UpperPrintString нет, она может быть произвольной.
Sample Input 1:
    s1 = UpperPrintString('beegeek')
    s2 = UpperPrintString('BeeGeek')

    print(s1)
    print(s2)
Sample Output 1:
    BEEGEEK
    BEEGEEK
Sample Input 2:
    s = UpperPrintString('beegeek')
    print(list(s))
Sample Output 2:
    ['b', 'e', 'e', 'g', 'e', 'e', 'k']
"""
class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()


""" Упражнение 2
Реализуйте класс LowerString, наследника класса str, описывающий строку, которая во время создания автоматически 
переводится в нижний регистр. При создании экземпляра класс должен принимать один аргумент:
    obj — объект, определяющий начальное значение строки. Может быть не передан, в таком случае начальное значение 
считается пустой строкой
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса LowerString нет, она может быть произвольной.
Sample Input 1:
    s1 = LowerString('BEEGEEK')
    s2 = LowerString('BeeGeek')
    
    print(s1)
    print(s2)
    print(s1 == s2)
    print(issubclass(LowerString, str))
Sample Output 1:
    beegeek
    beegeek
    True
    True
Sample Input 2:
    print(LowerString(['Bee', 'Geek']))
    print(LowerString({'A': 1, 'B': 2, 'C': 3}))
Sample Output 2:
    ['bee', 'geek']
    {'a': 1, 'b': 2, 'c': 3}
Sample Input 3:
    s = LowerString('BeeGeek')
    
    print(s[0], s[3])
Sample Output 3:
    b g
"""
class LowerString(str):
    def __new__(cls, value=''):
        value = str(value).lower()
        return super().__new__(cls, value)


""" Упражнение 3
Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=, 
<=) и проверках на принадлежность (in, not in) не учитывает регистр. Процесс создания экземпляра класса FuzzyString 
должен совпадать с процессом создания экземпляра класса str.
Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, 
должен вернуть константу NotImplemented.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса FuzzyString нет, она может быть произвольной.
Sample Input:
    s1 = FuzzyString('BeeGeek')
    s2 = FuzzyString('beegeek')
    
    print(s1 == s2)
    print(s1 in s2)
    print(s2 in s1)
    print(s2 not in s1)
    print(s2 not in s1)
Sample Output:
    True
    True
    True
    False
    False
"""
class FuzzyString(str):
    @staticmethod
    def _c(func):
        def wrapper(obj, other):
            wrapper.__name__ = func.__name__
            if not isinstance(obj, str | FuzzyString) or not isinstance(other, str | FuzzyString):
                return NotImplemented
            return eval(f'str.{func.__name__}(obj.lower(), other.lower())')
        return wrapper

    @_c
    def __gt__(self, other): pass

    @_c
    def __ge__(self, other): pass

    @_c
    def __lt__(self, other): pass

    @_c
    def __le__(self, other): pass

    @_c
    def __eq__(self, other): pass

    @_c
    def __contains__(self, other): pass

    @_c
    def __ne__(self, other): pass


""" Упражнение 4
Реализуйте класс TitledText, наследника класса str, который описывает текст, имеющий заголовок. При создании экземпляра 
класс должен принимать два аргумента в следующем порядке:
    content — текст
    text_title — заголовок текста   
Класс TitleText должен иметь один метод экземпляра:
    title() — метод, возвращающий заголовок текста
Примечание 1. Значением экземпляра класса TitledText должен быть именно текст, а не заголовок текста или текст вместе 
с заголовком.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса TitledText нет, она может быть произвольной.
Sample Input 1:
    titled = TitledText('Сreate a class Soda', 'Homework')
    
    print(titled)
    print(titled.title())
    print(issubclass(TitledText, str))
Sample Output 1:
    Сreate a class Soda
    Homework
    True
Sample Input 2:
    titled1 = TitledText('Сreate a class Soda', 'Homework')
    titled2 = TitledText('Сreate a class Soda', 'Exam')
    
    print(titled1 == titled2)
Sample Output 2:
    True
"""
class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance._text_title = text_title
        return instance

    def title(self):
        return self._text_title


""" Упражнение 5
Реализуйте класс SuperInt, наследника класса int, описывающий целое число с дополнительным функционалом. Процесс 
создания экземпляра класса SuperInt должен совпадать с процессом создания экземпляра класса int.
Класс SuperInt должен иметь четыре метода экземпляра:
    repeat() — метод, принимающий в качестве аргумента целое число n, по умолчанию равное 2, и возвращающий экземпляр 
класса SuperInt, продублированный n раз
    to_bin() — метод, возвращающий двоичное представление экземпляра класса SuperInt. Двоичное представление может быть 
как в виде экземпляра класса str, так и int
    next() — метод, возвращающий новый экземпляр класса SuperInt, который больше текущего на единицу
    prev() — метод, возвращающий новый экземпляр класса SuperInt, который меньше текущего на единицу
Также экземпляр класса SuperInt должен быть итерируемым объектом, элементами которого являются его цифры слева направо. 
Сами цифры так же должны быть представлены в виде экземпляров класса SuperInt.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса SuperInt нет, она может быть произвольной.
Sample Input 1:
    superint = SuperInt(17)
    
    print(superint.repeat())
    print(superint.repeat(3))
Sample Output 1:
    1717
    171717
Sample Input 2:
    superint1 = SuperInt(17)
    superint2 = SuperInt(-17)
    
    print(superint1.to_bin())
    print(superint2.to_bin())
Sample Output 2:
    10001
    -10001
Sample Input 3:
    superint = SuperInt(17)
    
    print(superint.prev())
    print(superint.next())
Sample Output 3:
    16
    18
Sample Input 4:
    superint1 = SuperInt(1337)
    superint2 = SuperInt(-2077)
    
    print(*superint1)
    print(*superint2)
Sample Output 4:
    1 3 3 7
    2 0 7 7
"""
class SuperInt(int):
    def repeat(self, n=2):
        return SuperInt(str(self) * n)

    def to_bin(self):
        return format(self, 'b')

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        yield from (SuperInt(x) for x in str(self) if x.isdigit())


""" Упражнение 6
Ближайшим четным числом для целого нечетного числа n будем считать n + 1, ближайшим четным числом для целого четного 
числа будет оно само. Аналогично ближайшим нечетным числом для целого четного числа n будем считать n + 1. ближайшим 
нечетным числом для целого нечетного числа будет оно само.
Реализуйте класс RoundedInt, наследника класса int, описывающий целое число, которое во время создания автоматически 
округляется до ближайшего четного или нечетного числа. При создании экземпляра класс должен принимать два аргумента в 
следующем порядке:
    num — объект, определяющий числовое значение экземпляра класса RoundedInt
    even — булево значение, определяющее четность при округлении. Если имеет значение True, округление происходит до 
ближайшего четного, если False — до ближайшего нечетного. По умолчанию имеет значение True
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса RoundedInt нет, она может быть произвольной.
Sample Input 1:
    print(RoundedInt(7))
    print(RoundedInt(8))
    print(RoundedInt(7, False))
    print(RoundedInt(8, False))
Sample Output 1:
    8
    8
    7
    9
Sample Input 2:
    roundedint1 = RoundedInt(7)
    roundedint2 = RoundedInt(7, False)
    
    print(roundedint1 + roundedint2)
    print(roundedint1 + 1)
    print(roundedint2 + 1)
    
    print(type(roundedint1))
    print(type(roundedint2))
Sample Output 2:
    15
    9
    8
    <class '__main__.RoundedInt'>
    <class '__main__.RoundedInt'>
"""
class RoundedInt(int):
    def __new__(cls, num, even=True):
        num += 0 if num % 2 == (0 if even else 1) else 1
        return super().__new__(cls, num)


""" Упражнение 7
Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения 
(+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания 
экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.
Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый 
экземпляр класса AdvancedTuple.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной.
Sample Input 1:
    advancedtuple = AdvancedTuple([1, 2, 3])
    
    print(advancedtuple + (4, 5))
    print(advancedtuple + [4, 5])
    print({'a': 1, 'b': 2} + advancedtuple)
Sample Output 1:
    (1, 2, 3, 4, 5)
    (1, 2, 3, 4, 5)
    ('a', 'b', 1, 2, 3)
Sample Input 2:
    advancedtuple = AdvancedTuple([1, 2, 3])
    
    advancedtuple += [4, 5]
    advancedtuple += iter([6, 7, 8])
    print(advancedtuple)
    print(type(advancedtuple))
Sample Output 2:
    (1, 2, 3, 4, 5, 6, 7, 8)
    <class '__main__.AdvancedTuple'>
"""
class AdvancedTuple(tuple):
    def __add__(self, other):
        return AdvancedTuple(super().__add__(tuple(other)))

    def __radd__(self, other):
        return AdvancedTuple(other).__add__(self)


""" Упражнение 8
Реализуйте класс ModularTuple, наследника класса tuple, описывающий кортеж, элементы которого во время создания 
автоматически делятся с остатком на заданное число. При создании экземпляра класс должен принимать два аргумента в 
следующем порядке:
    iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса ModularTuple. Если 
не передан, начальный набор элементов считается пустым
    size — целое число, на которое делятся с остатком все элементы создаваемого экземпляра класса ModularTuple, 
по умолчанию имеет значение 100
Примечание 1. Экземпляр класса ModularTuple не должен зависеть от итерируемого объекта, на основе которого он был 
создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса ModularTuple измениться  
не должен.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса ModularTuple нет, она может быть произвольной.
Sample Input 1:
    modulartuple = ModularTuple([101, 102, 103, 104, 105])
    
    print(modulartuple)
    print(type(modulartuple))
Sample Output 1:
    (1, 2, 3, 4, 5)
    <class '__main__.ModularTuple'>
Sample Input 2:
    modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)
    
    print(modulartuple)
Sample Output 2:
    (1, 0, 1, 0, 1)
"""
class ModularTuple(tuple):
    def __new__(cls, iterable=tuple(), size=100):
        return super().__new__(cls, map(lambda x: x % size, iterable))
