""" Упражнение 1
Вам доступны классы Average, Median и Harmonic, имеющие сходный интерфейс. Все три класса используются для обработки
пользовательских оценок и оценок критиков некоторого медиаконтента по стобалльной шкале и вычисления средних значений
этих оценок. Задачей класса Average является нахождение среднего арифметического пользовательских оценок или оценок
критиков, классов Median и Harmonic — медианы и среднего гармонического соответственно.
Изучите приведенные классы, реализуйте абстрактный базовый класс Middle и постройте корректную схему наследования. При
выполнении старайтесь избегать дублирования кода.
Примечание 1. Функционал классов Average, Median и Harmonic должен остаться прежним, необходимо лишь объединить их в
иерархию, определив для них единый базовый абстрактный класс Middle.
Sample Input 1:
    user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
    expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
    average = Average(user_votes, expert_votes)

    print(average.get_correct_user_votes())
    print(average.get_correct_expert_votes())
    print(average.get_average())
    print(average.get_average(False))
Sample Output 1:
    [71, 56, 60, 80]
    [87, 90, 67, 70, 81, 85, 79, 71]
    66.75
    78.75
Sample Input 2:
    user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
    expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
    median = Median(user_votes, expert_votes)

    print(median.get_correct_user_votes())
    print(median.get_correct_expert_votes())
    print(median.get_average())
    print(median.get_average(False))
Sample Output 2:
    [71, 56, 60, 80]
    [87, 90, 67, 70, 81, 85, 79, 71]
    71
    81
Sample Input 3:
    user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
    expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
    harmonic = Harmonic(user_votes, expert_votes)

    print(harmonic.get_correct_user_votes())
    print(harmonic.get_correct_expert_votes())
    print(round(harmonic.get_average(), 2))
    print(round(harmonic.get_average(False), 2))
Sample Output 3:
    [71, 56, 60, 80]
    [87, 90, 67, 70, 81, 85, 79, 71]
    65.46
    77.92
"""
from abc import ABC, abstractmethod


class Middle(ABC):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes  # пользовательские оценки
        self.expert_votes = expert_votes  # оценки критиков

    def get_correct_user_votes(self):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.user_votes if 10 < vote < 90]

    def get_correct_expert_votes(self):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.expert_votes if 5 < vote < 95]

    @abstractmethod
    def get_average(self, users=True):
        if users:
            return self.get_correct_user_votes()
        return self.get_correct_expert_votes()


class Average(Middle):
    def get_average(self, users=True):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users)
        return sum(votes) / len(votes)


class Median(Middle):
    def get_average(self, users=True):
        """Возвращает медиану пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = sorted(super().get_average(users))
        return votes[len(votes) // 2]


class Harmonic(Middle):
    def get_average(self, users=True):
        """Возвращает среднее гармоническое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        votes = super().get_average(users)
        return len(votes) / sum(map(lambda vote: 1 / vote, votes))


""" Упражнение 2
1. Реализуйте абстрактный класс ChessPiece, описывающий шахматную фигуру. При создании экземпляра класс должен принимать 
два аргумента в следующем порядке:
    horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
    vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
Класс ChessPiece должен иметь один метод экземпляра:
    can_move() — пустой абстрактный метод
2. Также реализуйте класс King, наследника класса ChessPiece, описывающий шахматного короля. Процесс создания экземпляра 
класса King должен совпадать с процессом создания экземпляра класса ChessPiece.
Класс King должен иметь один метод экземпляра:
    can_move() — метод, принимающий в качестве аргументов шахматные координаты по горизонтали и вертикали и возвращающий 
True, если фигура может переместиться по указанным координатам, или False в противном случае
Экземпляр класса King  должен иметь два атрибута:
    horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
    vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
3. Наконец, реализуйте класс Knight, наследника класса ChessPiece, описывающий шахматного коня. Процесс создания 
экземпляра класса Knight должен совпадать с процессом создания экземпляра класса ChessPiece.
Класс Knight должен иметь один метод экземпляра:
    can_move() — переопределенный родительский метод, принимающий в качестве аргументов координаты по горизонтали и 
вертикали и возвращающий True, если фигура может переместиться по указанным координатам, и False в противном случае
Экземпляр класса Knight  должен иметь два атрибута:
    horizontal — координата фигуры по горизонтали, представленная латинской буквой от a до h
    vertical — координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализаций классов нет, она может быть произвольной.
Sample Input:
    king = King('b', 2)
    
    print(king.can_move('c', 3))
    print(king.can_move('a', 1))
    print(king.can_move('f', 7))
Sample Output:
    True
    True
    False
"""
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def convert(self, v, h):
        deck = 'abcdefgh'
        return 8 - v, deck.index(h) if type(h) is str else deck[h]

    @abstractmethod
    def can_move(self, h, v):
        pass


class Knight(ChessPiece):
    def can_move(self, h, v):
        p1, p2 = self.convert(self.vertical, self.horizontal)
        m1, m2 = self.convert(v, h) if type(h) is str else (v, h)
        return (abs(p1 - m1) == 1 and abs(p2 - m2) == 2) or (abs(p1 - m1) == 2 and abs(p2 - m2) == 1)


class King(ChessPiece):
    def can_move(self, h, v):
        p1, p2 = self.convert(self.vertical, self.horizontal)
        m1, m2 = self.convert(v, h) if type(h) is str else (v, h)
        n1, n2 = abs(p1 - m1), abs(p2 - m2)
        return 0 < n1 + n2 <= 2 and n1 < 2 and n2 < 2


""" Упражнение 3
1. Реализуйте абстрактный класс Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое 
значение является корректным. При создании экземпляра класс не должен принимать никаких аргументов.
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение 
атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом: Атрибут не найден
При установке или изменении значения атрибута дескриптор должен сперва проверять его на корректность с помощью метода 
validate().
Класс Validator должен иметь один абстрактный метод экземпляра:
    validate() — пустой метод
2. Также реализуйте класс Number, наследника класса Validator, описывающий дескриптор, который проверяет, что 
устанавливаемое или изменяемое значение является числом из определенного диапазона. Дескриптор должен закрепляться за 
атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен 
принимать два аргумента в следующем порядке:
    minvalue — левая граница диапазона, по умолчанию имеет значение None и не ограничивает число слева
    maxvalue — правая граница диапазона, по умолчанию имеет значение None и не ограничивает число справа
Класс Number должен иметь один метод экземпляра:
    validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не 
удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу int или float, должно быть возбуждено 
исключение TypeError с текстом: Устанавливаемое значение должно быть числом
Если указанный объект является числом меньше minvalue, должно быть возбуждено исключение ValueError с текстом:
    Устанавливаемое число должно быть больше или равно <minvalue>
Если указанный объект является числом больше maxvalue, должно быть возбуждено исключение ValueError с текстом:
    Устанавливаемое число должно быть меньше или равно <maxvalue>
3. Наконец, реализуйте класс String, наследника класса Validator, описывающий дескриптор, который проверяет, что 
устанавливаемое или изменяемое значение является строкой определенной длины. Дескриптор должен закрепляться за 
атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен 
принимать три аргумента в следующем порядке:
    minsize — минимальная длина слова, по умолчанию имеет значение None и не ограничивает минимальную длину
    maxsize — максимальная длина слова, по умолчанию имеет значение None и не ограничивает максимальную длину
    predicate — функция-предикат для дополнительной валидации, по умолчанию имеет значение None и не используется
Класс String должен иметь один метод экземпляра:
    validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не 
удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу str, метод должен возбуждать исключение 
TypeError с сообщением: Устанавливаемое значение должно быть строкой
Если указанный объект является строкой с длиной меньше minsize, должно быть возбуждено исключение ValueError с текстом:
    Длина устанавливаемой строки должна быть больше или равна <minsize>
Если указанный объект является строкой с длиной больше maxsize, должно быть возбуждено исключение ValueError с текстом:
    Длина устанавливаемой строки должна быть меньше или равна <maxsize>
Если указанный объект при передаче в функцию predicate() возвращает False, должно быть возбуждено исключение ValueError 
с текстом:
    Устанавливаемая строка не удовлетворяет дополнительным условиям
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
Sample Input 1:
    class Student:
        age = Number(18, 99)
    
    
    student = Student()
    student.age = 19
    print(student.age)
Sample Output 1:
    19
Sample Input 2:
    class Student:
        age = Number(18, 99)
    
    try:
        student = Student()
        student.age = '19'
    except TypeError as error:
        print(error)
Sample Output 2:
    Устанавливаемое значение должно быть числом
Sample Input 3:
    class Student:
        age = Number(18, 99)
    
    try:
        student = Student()
        student.age = 16
    except ValueError as error:
        print(error)
Sample Output 3:
    Устанавливаемое число должно быть больше или равно 18
Sample Input 4:
    class Student:
        age = Number(18, 99)
    
    try:
        student = Student()
        student.age = 101
    except ValueError as error:
        print(error)
Sample Output 4:
    Устанавливаемое число должно быть меньше или равно 99
"""
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self._attr] = value

    def __delete__(self, obj):
        del obj.__dict__[self._attr]

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, int | float):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate is not None and not self.predicate(value):
            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')


""" Упражнение 4
1. Реализуйте функцию is_iterable(), которая принимает один аргумент:
    obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.
2. Также реализуйте функцию is_iterator(), которая принимает один аргумент:
    obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимые функции, но не код, вызывающий их.
Sample Input 1:
    print(is_iterable(123))
    print(is_iterable([1, 2, 3]))
    print(is_iterable((1, 2, 3)))
    print(is_iterable('123'))
    print(is_iterable(iter('123')))
    print(is_iterable(map(int, '123')))
Sample Output 1:
    False
    True
    True
    True
    True
    True
Sample Input 2:
    print(is_iterator(123))
    print(is_iterator([1, 2, 3]))
    print(is_iterator((1, 2, 3)))
    print(is_iterator('123'))
    print(is_iterator(iter('123')))
    print(is_iterator(map(int, '123')))
Sample Output 2:
    False
    False
    False
    False
    True
    True
"""
from collections.abc import *


def is_iterable(obj):
    return isinstance(obj, Iterable)


def is_iterator(obj):
    return isinstance(obj, Iterator)


""" Упражнение 5
Назовем диапазоном запись двух целых неотрицательных чисел через дефис a-b, где a — левая граница диапазона, b — правая 
граница диапазона, причем a <= b. Диапазон содержит в себе все числа от a до b включительно. Например, диапазон 1-4 
содержит числа 1, 2, 3 и 4.
Реализуйте класс CustomRange, описывающий последовательность, элементами которой являются одиночные целые числа и числа 
из определенных диапазонов. При создании экземпляра класс должен принимать произвольное количество позиционных 
аргументов, каждый из которых является одиночным целым числом либо диапазоном.
При передаче экземпляра класса CustomRange в функцию len() должно возвращаться количество элементов в нем. При передаче 
экземпляра класса CustomRange в функцию reversed() должен возвращаться итератор, элементами которого являются элементы 
переданного экземпляра класса CustomRange, расположенные в обратном порядке.
Экземпляр класса CustomRange должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, 
с помощью цикла for.
Помимо этого, экземпляр класса CustomRange должен поддерживать операцию проверки на принадлежность с помощью in.
Наконец, экземпляр класса CustomRange должен позволять получать значения своих элементов с помощью индексов, причем как 
как положительных, так и отрицательных
Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве 
родительского.
Примечание 2. Реализация класса CustomRange может быть произвольной, то есть требований к наличию определенных 
атрибутов нет.
Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный 
класс используется только с корректными данными.
Sample Input 1:
    customrange = CustomRange(1, '2-5', 5, '6-8')
    
    print(customrange[0])
    print(customrange[1])
    print(customrange[2])
    print(customrange[-1])
    print(customrange[-2])
    print(customrange[-3])
Sample Output 1:
    1
    2
    3
    8
    7
    6
Sample Input 2:
    customrange = CustomRange(1, '2-5', 3, '1-4')
    
    print(*customrange)
    print(*reversed(customrange))
    print(len(customrange))
    print(1 in customrange)
    print(10 in customrange)
Sample Output 2:
    1 2 3 4 5 3 1 2 3 4
    4 3 2 1 3 5 4 3 2 1
    10
    True
    False
Sample Input 3:
    customrange = CustomRange()
    
    print(len(customrange))
    print(*customrange)
    print(*reversed(customrange))
Sample Output 3:
    0
"""
from collections.abc import *


class CustomRange(Sequence):
    def __init__(self, *args):
        self._lst = []
        for i in args:
            if isinstance(i, str):
                lst = tuple(map(int, i.split('-')))
                self._lst.extend(range(lst[0], lst[1] + 1))
            else:
                self._lst.append(i)

    def __len__(self):
        return len(self._lst)

    def __getitem__(self, key):
        return self._lst[key]


""" Упражнение 6
Реализуйте класс BitArray, описывающий битовый список, то есть список, элементами которого являются только нули и 
единицы. При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект, определяющий начальный набор элементов битового списка. Если не передан, начальный 
набор считается пустым
Экземпляр класса BitArray должен иметь следующее неформальное строковое представление:
[<первый элемент битового списка>, <второй элемент битового списка>, ...]
При передаче экземпляра класса BitArray в функцию len() должно возвращаться количество элементов в нем. При передаче 
экземпляра класса BitArray в функцию reversed() должен возвращаться итератор, элементами которого являются элементы 
переданного экземпляра класса BitArray , расположенные в обратном порядке.
Экземпляр класса BitArray должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, 
с помощью цикла for.
Помимо этого, экземпляр класса BitArray должен поддерживать операцию проверки на принадлежность с помощью оператора in.
Также экземпляр класса BitArray должен позволять получать значения своих элементов с помощью индексов, причем как 
положительных, так и отрицательных.
Вдобавок ко всему, экземпляр класса BitArray должен поддерживать унарный оператор ~, выполняющий операцию логического 
отрицания для каждого бита битового списка, тем самым преобразуя 0 в 1, а 1 в 0. Результатом работы оператора должен 
являться новый экземпляр класса BitArray.
Наконец, экземпляры класса BitArray должны поддерживать между собой логические операции с помощью операторов & и |:
оператор & должен выполнять операцию логического И над каждой парой битов двух битовых списков равной длины. Результатом
работы оператора должен являться новый экземпляр класса BitArray
оператор | должен выполнять операцию логического ИЛИ над каждой парой битов двух битовых списков равной длины. 
Результатом работы оператора должен являться новый экземпляр класса BitArray
Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве 
родительского.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используется только с корректными данными.
Примечание 3. Экземпляр класса BitArray не должен зависеть от итерируемого объекта, на основе которого он был создан. 
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса BitArray измениться  не должен.
Примечание 4. Если объект, с которым выполняется логическая операция, некорректен, метод, реализующий эту операцию, 
должен вернуть константу NotImplemented.
Примечание 5. Никаких ограничений касательно реализации класса BitArray нет, она может быть произвольной.
Sample Input 1:
    bitarray = BitArray([1, 0, 1, 1])
    
    print(bitarray)
    print(~bitarray)
    print(bitarray[0])
    print(bitarray[1])
    print(bitarray[-1])
    print(0 in bitarray)
    print(1 not in bitarray)
Sample Output 1:
    [1, 0, 1, 1]
    [0, 1, 0, 0]
    1
    0
    1
    True
    False
Sample Input 2:
    bitarray1 = BitArray([1, 0, 1, 1])
    bitarray2 = BitArray([0, 0, 0, 1])
    
    bitarray3 = bitarray1 | bitarray2
    bitarray4 = bitarray1 & bitarray2
    bitarray5 = ~bitarray1
    
    print(bitarray3, type(bitarray3))
    print(bitarray4, type(bitarray4))
    print(bitarray5, type(bitarray5))
Sample Output 2:
    [1, 0, 1, 1] <class '__main__.BitArray'>
    [0, 0, 0, 1] <class '__main__.BitArray'>
    [0, 1, 0, 0] <class '__main__.BitArray'>
"""
from collections.abc import *


class BitArray(Sequence):
    def __init__(self, iterable=None):
        self._lst = []
        if iterable is not None:
            self._lst.extend(list(iterable))

    def __len__(self):
        return len(self._lst)

    def __getitem__(self, key):
        return self._lst[key]

    def __str__(self):
        return str(self._lst)

    def __invert__(self):
        return BitArray([int(not x) for x in self._lst])

    def __and__(self, other):
        if not isinstance(other, BitArray) or len(other) != len(self):
            return NotImplemented
        return BitArray(int(all((self[i], other[i]))) for i in range(len(self)))

    def __or__(self, other):
        if not isinstance(other, BitArray) or len(other) != len(self):
            return NotImplemented
        return BitArray(max((self[i], other[i])) for i in range(len(self)))


""" Упражнение 7
ДНК состоит из двух цепей, ориентированных азотистыми основаниями друг к другу. В ДНК встречается четыре вида азотистых 
оснований: аденин (A), гуанин (G), тимин (T) и цитозин (C). Азотистые основания одной из цепей соединены с азотистыми 
основаниями другой цепи водородными связями согласно принципу комплементарности: аденин (A) соединяется только с 
тимином (T), гуанин (G) — только с цитозином (C).
Реализуйте класс DNA, описывающий двухцепочную спираль ДНК. При создании экземпляра класс должен принимать 1 аргумент:
    chain — первая цепь ДНК, представляющая собой строку из символов A, G, T и C (азотистых оснований)
Экземпляр класса DNA должен иметь следующее неформальное строковое представление:
    <азотистые основания первой цепи ДНК>
При передаче экземпляра класса DNA в функцию len() должно возвращаться количество азотистых оснований в одной из его 
цепей. При передаче экземпляра класса в функцию reversed() должен возвращаться итератор, элементами которого являются 
элементы переданного экземпляра класса DNA, расположенные в обратном порядке.
Помимо этого, экземпляр класса DNA должен быть итерируемым объектом, то есть позволять перебирать свои элементы, 
например, с помощью цикла for.
Также экземпляр класса DNA должен позволять получать значения своих элементов с помощью индексов, причем как 
положительных, так и отрицательных.
В случае с функцией reversed(), итерацией и доступу по индексам элементы экземпляра класса DNA должны быть представлены 
в виде кортежей из двух элементов, первым из которых является основание первой цепи ДНК по указанному индексу, вторым — 
азотистое основание второй цепи ДНК по указанному индексу. Азотистое основание второй цепи ДНК можно получить при помощи 
принципа комплементарности.
Вдобавок ко всему, экземпляр класса DNA должен поддерживать операцию проверки на принадлежность с помощью оператора in. 
В данном случае должно проверяться, входит ли азотистое основание в первую цепь ДНК.
Экземпляры класса DNA должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две ДНК считаются 
равными, если их первые цепи совпадают.
Наконец, экземпляры класса DNA должны поддерживать между собой операцию сложения с помощью оператора +, результатом 
которой должен являться новый экземпляр класса DNA, первой цепью которого является конкатенация первых цепей исходных 
экземпляров класса DNA.
Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве 
родительского.
Примечание 2. Если объект, с которым выполняется операция сравнения или сложения, некорректен, метод, реализующий эту 
операцию, должен вернуть константу NotImplemented.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса DNA нет, она может быть произвольной.
Sample Input 1:
    dna = DNA('AGTC')
    
    print(dna[0])
    print(dna[1])
    print(dna[2])
    print(dna[3])
    print(dna[-1])
    print(dna[-2])
Sample Output 1:
    ('A', 'T')
    ('G', 'C')
    ('T', 'A')
    ('C', 'G')
    ('C', 'G')
    ('T', 'A')
Sample Input 2:
    dna = DNA('AGT')
    
    print(dna)
    print(len(dna))
    print('A' in dna)
    print('C' in dna)
Sample Output 2:
    AGT
    3
    True
    False
Sample Input 3:
    dna1 = DNA('ACG')
    dna2 = DNA('TTTAAT')
    dna3 = dna1 + dna2
    dna4 = dna2 + dna1
    
    print(dna3, type(dna3))
    print(dna4, type(dna4))
Sample Output 3:
    ACGTTTAAT <class '__main__.DNA'>
    TTTAATACG <class '__main__.DNA'>
Sample Input 4:
    dna1 = DNA('ACG')
    dna2 = DNA('TTTAAT')
    dna3 = DNA('TTTAAT')
    
    print(dna1 == dna2)
    print(dna2 == dna3)
    print(dna1 != dna3)
    print(dna2 != dna3)
Sample Output 4:
    False
    True
    True
    False
"""
from collections.abc import Sequence


class DNA(Sequence):
    def __init__(self, chain):
        self._chain = chain
        self._comp = {"T": "A", "A": "T", "G": "C", "C": "G"}

    def __len__(self):
        return len(self._chain)

    def __str__(self):
        return self._chain

    def __getitem__(self, key):
        return self._chain[key], self._comp[self._chain[key]]

    def __eq__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self._chain == other._chain

    def __add__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return DNA(self._chain + other._chain)

    def __contains__(self, obj):
        return obj in self._chain


""" Упражнение 8
Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении. При 
создании экземпляра класс должен принимать один аргумент:
iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка. Если не передан, 
начальный набор элементов считается пустым
Класс SortedList должен иметь три метода экземпляра:
    add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
    discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра 
класса SortedList, если он в нем присутствует
    update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы в экземпляр 
класса SortedList
Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(), при попытке 
воспользоваться которыми должно быть возбуждено исключение NotImplementedError.
Экземпляр класса SortedList должен иметь следующее формальное строковое представление:
    SortedList([<первый элемент списка>, <второй элемент списка>, ...])
При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем. При попытке 
передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено исключение NotImplementedError.
Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы, 
например, с помощью цикла for.
Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.
Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов с помощью 
индексов, причем как положительных, так и отрицательных. При попытке изменить значение элемента по его индексу должно 
быть возбуждено исключение NotImplementedError.
Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:
    оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей 
сортировки. Результатом работы оператора должен являться новый экземпляр класса SortedList
    оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей 
сортировки. Результатом работы оператора должен являться левый экземпляр класса SortedList
Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n с помощью операторов * и *=
    оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. 
Результатом работы оператора должен являться новый экземпляр класса SortedList
    оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. 
Результатом работы оператора должен являться левый экземпляр класса SortedList
Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.
Примечание 2. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве 
родительского.
Примечание3. Экземпляр класса SortedList не должен зависеть от итерируемого объекта, на основе которого он был создан. 
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса SortedList измениться  не должен.
Примечание 4.  Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий операцию 
сравнения, должен вернуть константу NotImplemented.
Примечание 5. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 6. Никаких ограничений касательно реализации класса SortedList нет, она может быть произвольной. Однако 
попробуйте решить задачу так, чтобы операция добавления элементов в список выполнялась как можно быстрее.
Sample Input 1:
    numbers = SortedList([5, 3, 4, 2, 1])
    
    
    print(numbers)
    print(numbers[1])
    print(numbers[-2])
    numbers.add(0)
    print(numbers)
    numbers.discard(4)
    print(numbers)
    numbers.update([4, 6])
    print(numbers)
Sample Output 1:
    SortedList([1, 2, 3, 4, 5])
    2
    4
    SortedList([0, 1, 2, 3, 4, 5])
    SortedList([0, 1, 2, 3, 5])
    SortedList([0, 1, 2, 3, 4, 5, 6])
Sample Input 2:
    numbers = SortedList([5, 3, 4, 2, 1])
    
    print(len(numbers))
    print(*numbers)
    print(1 in numbers)
    print(6 in numbers)
Sample Output 2:
    5
    1 2 3 4 5
    True
    False
Sample Input 3:
    numbers1 = SortedList([1, 3, 5])
    numbers2 = SortedList([2, 4])
    
    print(numbers1 + numbers2)
    print(numbers1 * 2)
    print(numbers2 * 2)
Sample Output 3:
    SortedList([1, 2, 3, 4, 5])
    SortedList([1, 1, 3, 3, 5, 5])
    SortedList([2, 2, 4, 4])
"""
from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=None):
        self._lst = []
        if iterable:
            self._lst.extend(list(iterable))
        self._lst.sort()

    def __getitem__(self, key):
        return self._lst[key]

    def __setitem__(self, *args):
        raise NotImplementedError

    def __delitem__(self, key):
        del self._lst[key]

    def __len__(self):
        return len(self._lst)

    def add(self, obj):
        self._lst.append(obj)
        self._lst.sort()

    def discard(self, obj):
        while obj in self._lst:
            self._lst.remove(obj)

    def update(self, iterable):
        self._lst.extend(list(iterable))
        self._lst.sort()

    insert = append = extend = reverse = __reversed__ = __setitem__

    def __repr__(self):
        return f'SortedList({str(self._lst)})'

    def __add__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented
        return SortedList(self._lst + other._lst)

    def __iadd__(self, other):
        if not isinstance(other, SortedList):
            return NotImplemented
        self.update(other._lst)
        return self

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return SortedList(self._lst * n)

    def __imul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        lst = self._lst * n
        self._lst = lst
        self._lst.sort()
        return self
