""" Упражнение 1
1. Реализуйте класс BasicPlan, описывающий подписку базового уровня на некотором онлайн-сервисе. При создании экземпляра
класс не должен принимать никаких аргументов.
Класс BasicPlan должен иметь семь атрибутов:
    can_stream —  атрибут, имеющий значение True
    can_download — атрибут, имеющий значение True
    has_SD — атрибут, имеющий значение True
    has_HD — атрибут, имеющий значение False
     has_UHD — атрибут, имеющий значение False
    num_of_devices — атрибут, имеющий значение 1
    price — атрибут, имеющий значение 8.99$
2. Также реализуйте класс SilverPlan, наследника класса BasicPlan, описывающий подписку среднего уровня на некотором
онлайн-сервисе. Процесс создания экземпляра класса SilverPlan должен совпадать с процессом создания экземпляра класса
BasicPlan.
Класс SilverPlan должен иметь семь атрибутов:
    can_stream —  атрибут, имеющий значение True
    can_download — атрибут, имеющий значение True
    has_SD — атрибут, имеющий значение True
    has_HD — атрибут, имеющий значение True
     has_UHD — атрибут, имеющий значение False
    num_of_devices — атрибут, имеющий значение 2
    price — атрибут, имеющий значение 12.99$
3. Наконец, реализуйте класс GoldPlan, наследника класса BasicPlan, описывающий подписку высокого уровня на некотором
онлайн-сервисе. Процесс создания экземпляра класса GoldPlan должен совпадать с процессом создания экземпляра класса
BasicPlan.
Класс GoldPlan должен иметь семь атрибутов:
    can_stream —  атрибут, имеющий значение True
    can_download — атрибут, имеющий значение True
    has_SD — атрибут, имеющий значение True
    has_HD — атрибут, имеющий значение True
     has_UHD — атрибут, имеющий значение True
    num_of_devices — атрибут, имеющий значение 4
    price — атрибут, имеющий значение 15.99$
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
Sample Input 1:
    print(BasicPlan.can_stream)
    print(BasicPlan.can_download)
    print(BasicPlan.has_SD)
    print(BasicPlan.has_HD)
    print(BasicPlan.has_UHD)
    print(BasicPlan.num_of_devices)
    print(BasicPlan.price)
Sample Output 1:
    True
    True
    True
    False
    False
    1
    8.99$
Sample Input 2:
    print(SilverPlan.can_stream)
    print(SilverPlan.can_download)
    print(SilverPlan.has_SD)
    print(SilverPlan.has_HD)
    print(SilverPlan.has_UHD)
    print(SilverPlan.num_of_devices)
    print(SilverPlan.price)
Sample Output 2:
    True
    True
    True
    True
    False
    2
    12.99$
Sample Input 3:
    print(GoldPlan.can_stream)
    print(GoldPlan.can_download)
    print(GoldPlan.has_SD)
    print(GoldPlan.has_HD)
    print(GoldPlan.has_UHD)
    print(GoldPlan.num_of_devices)
    print(GoldPlan.price)
Sample Output 3:
    True
    True
    True
    True
    True
    4
    15.99$
"""
class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'


class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99$'


class GoldPlan(SilverPlan):
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'


""" Упражнение 2
Реализуйте класс WeatherWarning, описывающий объект, предупреждающий о погодных изменениях. При создании экземпляра 
класс не должен принимать никаких аргументов.
Класс WeatherWarning должен иметь три метода экземпляра:
    rain() — метод, выводящий текст: Ожидаются сильные дожди и ливни с грозой
    snow() — метод, выводящий текст: Ожидается снег и усиление ветра
    low_temperature() — метод, выводящий текст: Ожидается сильное понижение температуры
Также реализуйте класс WeatherWarningWithDate, наследника класса WeatherWarning, описывающий объект, предупреждающий 
о погодных изменениях с указанием даты. Процесс создания экземпляра класса WeatherWarningWithDate должен совпадать с 
процессом создания экземпляра класса WeatherWarning.
Класс WeatherWarningWithDate должен иметь три метода экземпляра:
    rain() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст: 
        <дата в формате DD.MM.YYYY>
        Ожидаются сильные дожди и ливни с грозой
    snow() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
        <дата в формате DD.MM.YYYY>
        Ожидается снег и усиление ветра
    low_temperature() — метод, принимающий в качестве аргумента дату (тип date) и выводящий текст:
        <дата в формате DD.MM.YYYY>
        Ожидается сильное понижение температуры
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
Sample Input 1:
    print(issubclass(WeatherWarningWithDate, WeatherWarning))
Sample Output 1:
    True
Sample Input 2:
    weatherwarning = WeatherWarning()
    
    weatherwarning.rain()
    weatherwarning.snow()
    weatherwarning.low_temperature()
Sample Output 2:
    Ожидаются сильные дожди и ливни с грозой
    Ожидается снег и усиление ветра
    Ожидается сильное понижение температуры
Sample Input 3:
    from datetime import date
    
    weatherwarning = WeatherWarningWithDate()
    dt = date(2022, 12, 12)
    
    weatherwarning.rain(dt)
    weatherwarning.snow(dt)
    weatherwarning.low_temperature(dt)
Sample Output 3:
    12.12.2022
    Ожидаются сильные дожди и ливни с грозой
    12.12.2022
    Ожидается снег и усиление ветра
    12.12.2022
    Ожидается сильное понижение температуры
"""
class WeatherWarning:
    def rain(self): print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self): print('Ожидается снег и усиление ветра')

    def low_temperature(self): print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date):
        print(date.strftime(r'%d.%m.%Y'))
        super().rain()

    def snow(self, date):
        print(date.strftime(r'%d.%m.%Y'))
        super().snow()

    def low_temperature(self, date):
        print(date.strftime(r'%d.%m.%Y'))
        super().low_temperature()

""" Упражнение 3
Реализуйте класс Triangle, описывающий треугольник. При создании экземпляра класс должен принимать три аргумента 
в следующем порядке:
    a — длина стороны треугольника
    b — длина стороны треугольника
    c — длина стороны треугольника
Класс Triangle должен иметь один метод экземпляра:
    perimeter() — метод, возвращающий периметр треугольника
Также реализуйте класс EquilateralTriangle, наследника класса Triangle, описывающий равносторонний треугольник. При 
создании экземпляра класс должен принимать один аргумент:
    side — длина стороны треугольника
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
Sample Input 1:
    print(issubclass(EquilateralTriangle, Triangle))
Sample Output 1:
    True
Sample Input 2:
    triangle1 = Triangle(3, 4, 5)
    triangle2 = EquilateralTriangle(3)
    
    print(triangle1.perimeter())
    print(triangle2.perimeter())
Sample Output 2:
    12
    9
"""
class Triangle:
    def __init__(self, a, b, c):
        self.sides = a, b, c

    def perimeter(self):
        return sum(self.sides)


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


""" Упражнение 4
Вам доступен класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс принимает один аргумент:
    start — начальное значение счетчика, по умолчанию равняется 0
Экземпляр класса Counter имеет один атрибут:
    value — текущее значение счетчика
Класс Counter имеет два метода экземпляра:
    inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число. Если 
число не передано, метод увеличивает значение счетчика на единицу
    dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число. Если число 
не передано, метод уменьшает значение счетчика на единицу. Значение счетчика считается равным 0, если при уменьшении оно 
становится отрицательным
Реализуйте класс DoubledCounter, наследника класса Counter, описывающий неотрицательный счетчик, значение которого 
увеличивается и уменьшается дважды при вызове соответствующих методов. Процесс создания экземпляра класса DoubledCounter 
должен совпадать с процессом создания экземпляра класса Counter.
Экземпляр класса DoubledCounter должен иметь один атрибут:
    value — текущее значение счетчика
Класс DoubledCounter должен иметь два метода экземпляра:
    inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число дважды. 
Если число не передано, метод должен увеличить значение счетчика на два
    dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число дважды. 
Если число не передано, метод должен уменьшить значение счетчика на два. Значение счетчика считается равным 0, если при 
уменьшении оно становится отрицательным
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
Sample Input 1:
    print(issubclass(DoubledCounter, Counter))
Sample Output 1:
    True
Sample Input 2:
    counter = Counter(10)
    
    print(counter.value)
    counter.inc()
    counter.inc(5)
    print(counter.value)
    counter.dec()
    counter.dec(10)
    print(counter.value)
    counter.dec(10)
    print(counter.value)
Sample Output 2:
    10
    16
    5
    0
Sample Input 3:
    counter = DoubledCounter(20)
    
    print(counter.value)
    counter.inc()
    counter.inc(5)
    print(counter.value)
    counter.dec()
    counter.dec(10)
    print(counter.value)
    counter.dec(10)
    print(counter.value)
Sample Output 3:
    20
    32
    10
    0
"""
class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def inc(self, n=1):
        super().inc(n * 2)

    def dec(self, n=1):
        super().dec(n * 2)


""" Упражнение 5
1. Реализуйте класс Summator, описывающий объект, вычисляющий сумму натуральных чисел от 1 до n: 1+2+3+...+n
При создании экземпляра класс не должен принимать никаких аргументов.
Класс Summator должен иметь один метод экземпляра:
    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел от 1 
до n включительно
2. Помимо этого, реализуйте класс SquareSummator, наследника класса Summator, описывающий объект, вычисляющий сумму 
квадратов натуральных чисел от 1 до n
Процесс создания экземпляра класса SquareSummator должен совпадать с процессом создания экземпляра класса Summator.
Класс SquareSummator должен иметь один метод экземпляра:
    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму квадратов целых чисел от 1 
до n включительно
3. Также реализуйте класс QubeSummator, наследника класса Summator, описывающий объект, вычисляющий сумму кубов 
натуральных чисел от 1 до n:
Процесс создания экземпляра класса QubeSummator должен совпадать с процессом создания экземпляра класса Summator.
Класс QubeSummator должен иметь один метод экземпляра:
    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму кубов целых чисел от 1 
до n включительно
4. Наконец, реализуйте класс CustomSummator, наследника класса Summator, описывающий объект, вычисляющий сумму 
произвольных степеней натуральных чисел от 1 до n:
При создании экземпляра класс должен принимать один аргумент:
    m — степень чисел в последовательности
Класс CustomSummator должен иметь один метод экземпляра:
    total() — метод, принимающий в качестве аргумента целое число n и возвращающий сумму целых чисел в степени m от 1 
до n включительно
Примечание 1. Попытайтесь реализовать классы таким образом, чтобы метод total() был определен лишь в классе Summator.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
Sample Input 1:
    print(issubclass(SquareSummator, Summator))
    print(issubclass(QubeSummator, Summator))
Sample Output 1:
    True
    True
Sample Input 2:
    summator1 = Summator()
    summator2 = SquareSummator()
    summator3 = QubeSummator()
    
    print(summator1.total(3))    # 1 + 2 + 3
    print(summator2.total(3))    # 1 + 4 + 9
    print(summator3.total(3))    # 1 + 8 + 27
Sample Output 2:
    6
    14
    36
Sample Input 3:
    summator1 = Summator()
    summator2 = CustomSummator(2)
    summator3 = CustomSummator(3)
    
    print(summator1.total(3))    # 1 + 2 + 3
    print(summator2.total(3))    # 1 + 4 + 9
    print(summator3.total(3))    # 1 + 8 + 27
Sample Output 3:
    6
    14
    36
"""
class Summator:
    def __init__(self, m=1):
        self.mult = m

    def total(self, n):
        return sum(x ** self.mult for x in range(1, n + 1))


class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)


class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)


class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(m)


""" Упражнение 6
Реализуйте класс FieldTracker, наследники которого получают возможность отслеживать состояние определенных атрибутов 
своих экземпляров класса. Дочерние классы должны наследовать четыре метода экземпляра:
    base() — метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута, 
либо исходное (указанное при определении) значение этого атрибута, если оно было изменено
    has_changed() — метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого 
атрибута было изменено хотя бы раз, или False в противном случае
    changed() — метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои значения, 
а значениями — их исходные значения
    save() — метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли свои 
значения, а их текущие значения считаются исходными
Гарантируется, что наследники класса FieldTracker:
    всегда имеют атрибут класса fields, содержащий кортеж с атрибутами, которые необходимо отслеживать
    в своем инициализаторе всегда вызывают инициализатор класса FieldTracker после установки первичных значений 
отслеживаемым атрибутам
Примечание 1. Будем считать, что атрибут изменяет свое значение только в том случае, если устанавливаемое значение 
отличается от текущего.
Примечание 2. Реализация класса FieldTracker может быть произвольной, то есть требований к наличию определенных 
атрибутов нет.
Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный 
класс используется только с корректными данными.
Sample Input 1:
    class Point(FieldTracker):
        fields = ('x', 'y', 'z')
    
        def __init__(self, x, y, z):
            self.x, self.y, self.z = x, y, z
            super().__init__()
    
    point = Point(1, 2, 3)
    
    print(point.base('x'))
    print(point.has_changed('x'))
    print(point.changed())
Sample Output 1:
    1
    False
    {}
Sample Input 2:
    class Point(FieldTracker):
        fields = ('x', 'y', 'z')
    
        def __init__(self, x, y, z):
            self.x, self.y, self.z = x, y, z
            super().__init__()
    
    point = Point(1, 2, 3)
    point.x = 0
    point.z = 4
    point.z = 5
    
    print(point.base('x'))
    print(point.base('z'))
    print(point.has_changed('x'))
    print(point.has_changed('z'))
    print(point.changed())
Sample Output 2:
    1
    3
    True
    True
    {'x': 1, 'z': 3}
Sample Input 3:
    class Point(FieldTracker):
        fields = ('x', 'y', 'z')
    
        def __init__(self, x, y, z):
            self.x, self.y, self.z = x, y, z
            super().__init__()
    
    point = Point(1, 2, 3)
    point.x = 0
    point.z = 4
    point.save()
    
    print(point.base('x'))
    print(point.base('z'))
    print(point.has_changed('x'))
    print(point.has_changed('z'))
    print(point.changed())
Sample Output 3:
    0
    4
    False
    False
    {}
"""
class FieldTracker:
    fields = tuple()

    def __init__(self):
        self.__dct = self.__create_fields()

    def __create_fields(self):
        return {k: v for k, v in self.__dict__.items() if k in self.fields}

    def base(self, attr):
        return self.__dct[attr]

    def has_changed(self, attr):
        return self.__dict__[attr] != self.__dct[attr]

    def changed(self):
        return {k: v for k, v in self.__dct.items() if self.has_changed(k)}

    def save(self):
        self.__dct = self.__create_fields()
