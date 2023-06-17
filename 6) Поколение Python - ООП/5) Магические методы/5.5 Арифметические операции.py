""" Упражнение 1
Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании экземпляра класс должен принимать три
аргумента в следующем порядке:
    proteins — количество белков в граммах
    fats — количество жиров в граммах
    carbohydrates — количество углеводов в граммах
Экземпляр класса FoodInfoдолжен иметь три атрибута:
    proteins — количество белков в граммах
    fats — количество жиров в граммах
    carbohydrates — количество углеводов в граммах
И следующее формальное строковое представление:
    FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью оператора +, результатом
которой должен являться новый экземпляр класса FoodInfo с суммарным количеством белков, жиров и углеводов исходных
экземпляров.
Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления нацело на число n с помощью
операторов *, / и // соответственно:
    результатом умножения должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого
умножены на n
    результатом деления должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого
поделены на n
    результатом деления нацело должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов
которого поделены нацело на n
Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса
FoodInfo всегда делится на ненулевое число.
Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию,
должен вернуть константу NotImplemented.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса FoodInfo нет, она может быть произвольной.
Sample Input 1:
    food1 = FoodInfo(10, 20, 30)
    food2 = FoodInfo(10, 10, 20)

    print(food1 + food2)
    print(food1 * 2)
    print(food1 / 2)
    print(food1 // 2)
Sample Output 1:
    FoodInfo(20, 30, 50)
    FoodInfo(20, 40, 60)
    FoodInfo(5.0, 10.0, 15.0)
    FoodInfo(5, 10, 15)
Sample Input 2:
    food1 = FoodInfo(10, 20, 30)

    try:
        food2 = (5, 10, 15) + food1
    except TypeError:
        print('Некорректный тип данных')
Sample Output 2:
    Некорректный тип данных
"""
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'FoodInfo{self.proteins, self.fats, self.carbohydrates}'

    def __add__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(self.proteins + other.proteins, self.fats + other.fats,
                        self.carbohydrates + other.carbohydrates)

    @staticmethod
    def _check(func):
        def wrapper(obj, other):
            if not isinstance(other, int | float):
                return NotImplemented
            return func(obj, other)

        return wrapper

    @_check
    def __mul__(self, other):
        return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)

    @_check
    def __truediv__(self, other):
        return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)

    @_check
    def __floordiv__(self, other):
        return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)


""" Упражнение 2
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента 
в следующем порядке:
    x — координата вектора по оси x
    y — координата вектора по оси y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:
    Vector(<координата x>, <координата y>)
Также экземпляры класса Vector должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - 
соответственно:
    результатом сложения должен являться новый экземпляр класса Vector, координата по оси x которого равна сумме 
координат по оси x исходных векторов, координата по оси y — сумме координат по оси y исходных векторов
    результатом вычитания должен являться новый экземпляр класса Vector координата по оси x которого равна разности 
координат по оси x исходных векторов с учетом порядка, координата по оси y — разности координат по оси y исходных
векторов с учетом порядка
Наконец, экземпляр класса Vector должен поддерживать операции умножения и деления на число n с помощью операторов * и / 
соответственно:
    результатом умножения должен являться новый экземпляр класса Vector, координаты которого умножены на n
    результатом деления должен являться новый экземпляр класса Vector, координаты которого поделены на n
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как 
вектор на число, так и число на вектор.
Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса 
Vector всегда делится на ненулевое число.
Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, 
должен вернуть константу NotImplemented.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса Vector нет, она может быть произвольной.
Sample Input 1:
    a = Vector(1, 2)
    b = Vector(3, 4)
    
    print(a + b)
    print(a - b)
    print(b + a)
    print(b - a)
Sample Output 1:
    Vector(4, 6)
    Vector(-2, -2)
    Vector(4, 6)
    Vector(2, 2)
Sample Input 2:
    a = Vector(3, 4)
    
    print(a * 2)
    print(2 * a)
    print(a / 2)
Sample Output 2:
    Vector(6, 8)
    Vector(6, 8)
    Vector(1.5, 2.0)
"""
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Vector{self.x, self.y}'

    @staticmethod
    def _check(func):
        def wrapper(obj, other):
            dct = {'__add__': Vector, '__sub__': Vector, '__mul__': int | float, '__truediv__': int | float}
            if not isinstance(other, dct[func.__name__]):
                return NotImplemented
            return func(obj, other)

        return wrapper

    @_check
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    @_check
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    @_check
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    @_check
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)


""" Упражнение 3
Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
    string — значение строки
Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:
    <значение строки>
Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +, 
результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.
Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и побитового 
сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:
    результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку, 
умноженную на n
    результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m символов 
исходной строки, где m — длина исходной строки, поделенная нацело на n
    результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий исходную 
строку без последних n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр 
класса SuperString, представляющий пустую строку
    результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий исходную 
строку без первых n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр 
класса SuperString, представляющий пустую строку
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как 
строку на число, так и число на строку.
Примечание 1. Будем гарантировать, что экземпляр класса SuperString всегда делится на ненулевое число.
Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, 
должен вернуть константу NotImplemented.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса SuperString нет, она может быть произвольной.
Sample Input 1:
    s1 = SuperString('bee')
    s2 = SuperString('geek')
    
    print(s1 + s2)
    print(s2 + s1)
Sample Output 1:
    beegeek
    geekbee
Sample Input 2:
    s = SuperString('beegeek')
    
    print(s * 2)
    print(3 * s)
    print(s / 3)
Sample Output 2:
    beegeekbeegeek
    beegeekbeegeekbeegeek
    be
Sample Input 3:
    s = SuperString('beegeek')
    
    print(s << 4)
    print(s >> 3)
Sample Output 3:
    bee
    geek
"""


class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if not isinstance(other, SuperString):
            return NotImplemented
        return SuperString(str(self) + str(other))

    @staticmethod
    def _check(func):
        def wrapper(obj, other):
            if not isinstance(other, int):
                return NotImplemented
            return func(obj, other)

        return wrapper

    @_check
    def __mul__(self, other):
        return SuperString(str(self) * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    @_check
    def __truediv__(self, other):
        return SuperString(str(self)[:len(self.string) // other])

    @_check
    def __lshift__(self, other):
        other = other if other <= len(self.string) else len(self.string)
        return SuperString(self.string[:len(self.string) - other])

    @_check
    def __rshift__(self, other):
        return SuperString(self.string[other:])


""" Упражнение 4
Реализуйте класс Time, описывающий время на цифровых часах. При создании экземпляра класс должен принимать два аргумента 
в следующем порядке:
    hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
    minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час    
Экземпляр класса Time должен иметь следующее неформальное строковое представление:
    <количество часов в формате HH>:<количество минут в формате MM>
Также экземпляры класса Time должны поддерживать между собой операцию сложения с помощью операторов + и +=:
    результатом сложения с помощью оператора + должен являться новый экземпляр класса Time, количество часов которого 
равно сумме часов исходных экземпляров класса Time, количество минут — сумме минут исходных экземпляров класса Time
    результатом сложения с помощью оператора += должен являться левый экземпляр класса Time, количество часов которого 
увеличено на количество часов правого экземпляра класса Time, количество минут — на количество минут правого экземпляра 
класса Time
Примечание 1. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, 
должен вернуть константу NotImplemented.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Time нет, она может быть произвольной.
Sample Input 1:
    time1 = Time(2, 30)
    time2 = Time(3, 10)
    
    print(time1 + time2)
    print(time2 + time1)
Sample Output 1:
    05:40
    05:40
Sample Input 2:
    time1 = Time(2, 30)
    time2 = Time(3, 10)
    
    time1 += time2
    
    print(time1)
    print(time2)
Sample Output 2:
    05:40
    03:10
Sample Input 3:
    time1 = Time(25, 20)
    time2 = Time(10, 130)
    
    print(time1)
    print(time2)
Sample Output 3:
    01:20
    12:10
"""


class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = self.convert(hours, minutes)

    @staticmethod
    def convert(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60

    def __str__(self):
        return str(self.hours).rjust(2, '0') + ':' + str(self.minutes).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return Time(*self.convert(self.hours + other.hours, self.minutes + other.minutes))

    def __iadd__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        self.hours, self.minutes = self.convert(self.hours + other.hours, self.minutes + other.minutes)
        return self


""" Упражнение 5
Очередь — абстрактный тип данных с дисциплиной доступа к элементам "первый пришёл — первый вышел". Добавление элемента 
возможно лишь в конец очереди, выборка — только из начала очереди, при этом выбранный элемент из очереди удаляется.
Реализуйте класс Queue, описывающий очередь. При создании экземпляра класс должен принимать произвольное количество 
позиционных аргументов, каждый из которых является элементом очереди. Порядок следования аргументов образует порядок 
элементов в очереди, то есть первый аргумент — первый элемент очереди, второй аргумент — второй элемент очереди, и так 
далее.
Класс Queue должен иметь два метода экземпляра:
    add() — метод, принимающий произвольное количество позиционных аргументов и добавляющий их в конец очереди в том 
порядке, в котором они были переданы
    pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Если очередь пуста, метод должен вернуть 
значение None
Экземпляр класса Queue должен иметь следующее неформальное строковое представление:
    <первый элемент очереди> -> <второй элемент очереди> -> <третий элемент очереди> -> ...
Помимо этого, экземпляры класса Queue должны поддерживать между собой операции сравнения с помощью операторов == и!=. 
Две очереди считаются равными, если они имеют равную длину и содержат равные элементы на равных позициях.
Также экземпляры класса Queue должны поддерживать между собой операцию сложения с помощью операторов + и +=:
    результатом сложения с помощью оператора + должен являться новый экземпляр класса Queue, представляющий очередь со 
всеми элементами исходных очередей: сначала все элементы левой очереди, затем все элементы правой очереди
    результатом сложения с помощью оператора += должен являться левый экземпляр класса Queue, представляющий очередь, к 
которой добавлены все элементы правой очереди
Наконец, экземпляр класса Queue должен поддерживать операцию побитового сдвига вправо на целое число n с помощью 
оператора >>, результатом которой должен являться новый экземпляр класса Queue, представляющий исходную очередь без 
первых n элементов. Если n больше или равно длине исходной очереди, результатом должен являться экземпляр класса Queue, 
представляющий пустую очередь.
Примечание 1. Если объект, с которым выполняется операция сравнения или арифметическая операция, некорректен, метод, 
реализующий эту операцию, должен вернуть константу NotImplemented.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной.
Sample Input 1:
    queue = Queue(1, 2)
    queue.add(3)
    queue.add(4, 5)
    
    print(queue)
    print(queue.pop())
    print(queue)
Sample Output 1:
    1 -> 2 -> 3 -> 4 -> 5
    1
    2 -> 3 -> 4 -> 5
Sample Input 2:
    queue1 = Queue(1, 2, 3)
    queue2 = Queue(1, 2)
    
    print(queue1 == queue2)
    queue2.add(3)
    print(queue1 == queue2)
Sample Output 2:
    False
    True
Sample Input 3:
    queue1 = Queue(1, 2, 3)
    queue2 = Queue(4, 5)
    
    print(queue1 + queue2)
Sample Output 3:
    1 -> 2 -> 3 -> 4 -> 5
Sample Input 4:
    queue1 = Queue(1, 2, 3)
    queue2 = Queue(4, 5)
    
    queue1 += queue2
    
    print(queue1)
Sample Output 4:
    1 -> 2 -> 3 -> 4 -> 5
Sample Input 5:
    queue = Queue(1, 2, 3, 4, 5)
    
    print(queue >> 3)
Sample Output 5:
    4 -> 5
"""
class Queue:
    def __init__(self, *args):
        self._queue = list(args)

    def add(self, *args):
        self._queue.extend(list(args))

    def pop(self):
        if self._queue:
            return self._queue.pop(0)
        return None

    def __str__(self):
        return ' -> '.join(str(x) for x in self._queue)

    @staticmethod
    def _check(func):
        def wrapper(inst, obj):
            if not isinstance(obj, Queue):
                return NotImplemented
            return func(inst, obj)

        return wrapper

    @_check
    def __eq__(self, other):
        return self._queue == other._queue

    @_check
    def __add__(self, other):
        return Queue(*self._queue, *other._queue)

    @_check
    def __iadd__(self, other):
        self.add(*other._queue)
        return self

    def __rshift__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return Queue(*self._queue[n:])
