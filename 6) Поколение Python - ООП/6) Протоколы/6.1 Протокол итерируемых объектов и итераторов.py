""" Упражнение 1
Реализуйте класс Point, описывающий точку в пространстве. При создании экземпляра класс должен принимать три аргумента
в следующем порядке:
    x — координата точки по оси x
    y — координата точки по оси y
    z — координата точки по оси z
Экземпляр класса Point должен иметь следующее формальное строковое представление:
    Point(<координата x>, <координата y>, <координата z>)
Также экземпляр класса Point должен быть итерируемым объектом, элементами которого являются его координаты по осям x, y
и z.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Point нет, она может быть произвольной.
Sample Input 1:
    point = Point(1, 2, 3)

    print(list(point))
Sample Output 1:
    [1, 2, 3]
Sample Input 2:
    point = Point(1, 2, 3)
    x, y, z = point

    print(x, y, z)
Sample Output 2:
    1 2 3
Sample Input 3:
    points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
    print(points)
Sample Output 3:
    [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
"""
class Point:
    def __init__(self, x, y, z):
        self.coords = x, y, z

    def __repr__(self):
        return f'Point{self.coords}'

    def __iter__(self):
        return iter(self.coords)


""" Упражнение 2
Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший). 
При создании экземпляра класс не должен принимать никаких аргументов.
Класс DevelopmentTeam должен иметь два метода экземпляра:
    add_junior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем 
разработчика, и добавляющий их в число junior-разработчиков
    add_senior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем 
разработчика, и добавляющий их в число senior-разработчиков
Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его 
junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:
    (<имя разработчика>, 'junior')
в то время как senior-разработчики — в виде кортежей:
    (<имя разработчика>, 'senior')
Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
 используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса DevelopmentTeam нет, она может быть произвольной.
Sample Input 1:
    beegeek = DevelopmentTeam()
    
    beegeek.add_junior('Timur')
    beegeek.add_junior('Arthur', 'Valery')
    beegeek.add_senior('Gvido')
    print(*beegeek, sep='\n')
Sample Output 1:
    ('Timur', 'junior')
    ('Arthur', 'junior')
    ('Valery', 'junior')
    ('Gvido', 'senior')
Sample Input 2:
    beegeek = DevelopmentTeam()
    
    print(len(list(beegeek)))
Sample Output 2: 0
Sample Input 3:
    beegeek = DevelopmentTeam()
    
    beegeek.add_junior('Timur')
    beegeek.add_junior('Arthur', 'Valery')
    print(*beegeek, sep='\n')
Sample Output 3:
    ('Timur', 'junior')
    ('Arthur', 'junior')
    ('Valery', 'junior')
"""
class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self, *args):
        self.junior.extend(list(args))

    def add_senior(self, *args):
        self.senior.extend(list(args))

    def __iter__(self):
        return iter([(x, 'junior') for x in self.junior] + [(x, 'senior') for x in self.senior])


""" Упражнение 3
Реализуйте класс AttrsIterator. При создании экземпляра класс должен принимать один аргумент:
    obj — произвольный объект
Экземпляр класса AttrsIterator должен являться итератором, который генерирует все атрибуты объекта obj в виде кортежей 
из двух элементов, первый из которых представляет имя атрибута, второй — значение атрибута.
Примечание 1. Порядок атрибутов при генерации должен совпадать с их порядком в словаре атрибутов __dict__.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс AttrsIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и 
__next__(). Реализация же протокола может быть произвольной.
Sample Input:
    class User:
        def __init__(self, name, surname, age):
            self.name = name
            self.surname = surname
            self.age = age
            
    user = User('Debbie', 'Harry', 77)
    attrsiterator = AttrsIterator(user)
    
    print(*attrsiterator)
Sample Output:
    ('name', 'Debbie') ('surname', 'Harry') ('age', 77)
"""
class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj
        self.keys = []

    def __iter__(self):
        return self

    def __next__(self):
        for k, v in self.obj.__dict__.items():
            if k not in self.keys:
                self.keys.append(k)
                return k, v
        raise StopIteration


""" Упражнение 4
Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    iterable — итерируемый объект
    n — целое неотрицательное число
Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable, 
пропуская по n элементов, а затем возбуждает исключение StopIteration.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). 
Реализация же протокола может быть произвольной.
Sample Input 1:
    skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу
    
    print(*skipiterator)
Sample Output 1:    1 3 5 7 9
Sample Input 2:
    skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента
    
    print(*skipiterator)
Sample Output 2:    1 4 7 10
Sample Input 3:
    skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы
    
    print(*skipiterator)
Sample Output 3:    1 2 3 4 5 6 7 8 9 10
"""
class SkipIterator:
    def __init__(self, iterable, n):
        self.iterator = iter(list(iterable)[::1 + n])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)


""" Упражнение 5
Реализуйте класс RandomLooper. При создании экземпляра класс должен принимать произвольное количество позиционных 
аргументов, каждый из которых является итерируемым объектом.
Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке все элементы всех 
итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration.
Примечание 1. Порядок элементов в возвращаемом итераторе необязательно должен совпадать с их порядком в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс RandomLooper должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). 
Реализация же протокола может быть произвольной.
Sample Input 1:
    randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])
    
    print(list(randomlooper))
    print(list(randomlooper))
Sample Output 1:
    ['green', 'red', 'blue', 'purple']
    []
Sample Input 2:
    colors = ['red', 'blue', 'green', 'purple']
    shapes = ['square', 'circle', 'triangle', 'octagon']
    randomlooper = RandomLooper(colors, shapes)
    
    print(list(randomlooper))
Sample Output 2:
    ['circle', 'red', 'purple', 'octagon', 'triangle', 'green', 'blue', 'square']
"""
from random import shuffle


class RandomLooper:
    def __init__(self, *args):
        self.iterator = [i for x in args for i in x]
        shuffle(self.iterator)
        self.iterator = iter(self.iterator)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)


""" Упражнение 6
Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект
Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в 
исходном порядке, а затем возбуждает исключение StopIteration.
Класс Peekable должен иметь один метод экземпляра:
    peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий 
итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен уметь принимать один 
необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если 
итератор пуст
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). 
Реализация же протокола может быть произвольной.
Sample Input 1:
    iterator = Peekable('beegeek')
    
    print(next(iterator))
    print(next(iterator))
    print(*iterator)
Sample Output 1:
    b
    e
    e g e e k
Sample Input 2:
    iterator = Peekable('Python')
    
    print(next(iterator))
    print(iterator.peek())
    print(iterator.peek())
    print(next(iterator))
    print(iterator.peek())
    print(iterator.peek())
Sample Output 2:
    P
    y
    y
    y
    t
    t
Sample Input 3:
    iterator = Peekable('Python')
    
    print(*iterator)
    print(iterator.peek(None))
Sample Output 3:
    P y t h o n
    None
"""
class Peekable:
    def __init__(self, iterable):
        self.__lst = list(iterable)
        self.__ind = 0

    def __iter__(self):
        return self

    def __get(self):
        if self.__ind < len(self.__lst) and self.__ind != len(self.__lst):
            return self.__lst[self.__ind]
        raise StopIteration

    def __next__(self):
        res = self.__get()
        self.__ind += 1
        return res

    def peek(self, default=StopIteration):
        try:
            return self.__get()
        except StopIteration:
            if default != StopIteration:
                return default
        raise StopIteration


""" Упражнение 7
Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект
Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable в 
исходном порядке, а затем возбуждает исключение StopIteration.
Класс LoopTracker должен иметь четыре свойства:
    accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором 
на данный момент
    empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент 
опустевшего итератора
    first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если 
итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено 
исключение AttributeError с текстом: Исходный итерируемый объект пуст
    last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный 
момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError 
с текстом: Последнего элемента нет
Класс LoopTracker должен иметь один метод экземпляра:
    is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). 
Реализация же протокола может быть произвольной.
Sample Input 1:
    loop_tracker = LoopTracker([1, 2, 3])
    
    print(next(loop_tracker))
    print(list(loop_tracker))
Sample Output 1:
    1
    [2, 3]
Sample Input 2:
    loop_tracker = LoopTracker([1, 2, 3])
    
    print(loop_tracker.accesses)
    next(loop_tracker)
    next(loop_tracker)
    print(loop_tracker.accesses)
Sample Output 2:
    0
    2
Sample Input 3:
    loop_tracker = LoopTracker([1, 2, 3])
    print(loop_tracker.first)
    
    print(next(loop_tracker))
    print(loop_tracker.first)
    
    print(next(loop_tracker))
    print(loop_tracker.first)
    
    print(next(loop_tracker))
    print(loop_tracker.first)
Sample Output 3:
    1
    1
    1
    2
    1
    3
    1
Sample Input 4:
    loop_tracker = LoopTracker([1, 2, 3])
    
    print(next(loop_tracker))
    print(loop_tracker.last)
    
    print(next(loop_tracker))
    print(loop_tracker.last)
    
    print(next(loop_tracker))
    print(loop_tracker.last)
Sample Output 4:
    1
    1
    2
    2
    3
    3
"""
class LoopTracker:
    def __init__(self, iterable):
        self.__lst = tuple(iterable)
        self.__ind = -1
        self.__accesses = 0
        self.__empty_accesses = 0
        self.__last = None

    def __iter__(self):
        return self

    def __next__(self):
        self.__ind += 1
        if self.__ind < len(self.__lst) and self.__ind != len(self.__lst):
            self.__accesses += 1
            self.__last = self.__lst[self.__ind]
            return self.__last
        self.__empty_accesses += 1
        raise StopIteration

    @property
    def accesses(self):
        return self.__accesses

    @property
    def empty_accesses(self):
        return self.__empty_accesses

    @property
    def first(self):
        if not self.__lst:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self.__lst[0]

    @property
    def last(self):
        if self.__last is None:
            raise AttributeError('Последнего элемента нет')
        return self.__last

    def is_empty(self):
        return not bool(self.__lst) or self.__ind + 1 >= len(self.__lst)
