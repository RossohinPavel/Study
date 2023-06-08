""" Упражнение 1
Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен принимать два аргумента
в следующем порядке:
    length — длина прямоугольника
    width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:
    length — длина прямоугольника
    width — ширина прямоугольника
Класс Rectangle должен иметь два свойства:
    perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
    area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
Примечание 1. При изменении сторон прямоугольника должны изменяться его периметр и площадь.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Sample Input 1:
    rectangle = Rectangle(4, 5)

    print(rectangle.length)
    print(rectangle.width)
    print(rectangle.perimeter)
    print(rectangle.area)
Sample Output 1:
    4
    5
    18
    20
Sample Input 2:
    rectangle = Rectangle(4, 5)

    rectangle.length = 2
    rectangle.width = 3
    print(rectangle.length)
    print(rectangle.width)
    print(rectangle.perimeter)
    print(rectangle.area)
Sample Output 2:
    2
    3
    10
    6
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)


""" Упражнение 2
Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой. При создании экземпляра класс должен 
принимать один аргумент:
    hours — количество часов. Если hours не является целым числом, принадлежащим диапазону [1; 12], должно быть 
возбуждено исключение ValueError с текстом: Некорректное время
Класс HourClock должен иметь одно свойство:
hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов. При изменении свойство должно 
проверять, что новое значение является целым числом, принадлежащим диапазону [1; 12], в противном случае должно быть 
возбуждено исключение ValueError с текстом: Некорректное время
Примечание 1. Никаких ограничений касательно реализации класса HourClock нет, она может быть произвольной.
Sample Input 1:
    time = HourClock(7)
    
    print(time.hours)
    time.hours = 9
    print(time.hours)
Sample Output 1:
    7
    9
Sample Input 2:
    time = HourClock(7)
    
    try:
        time.hours = 15
    except ValueError as e:
        print(e)
Sample Output 2: Некорректное время
Sample Input 3:
    try:
        HourClock('pizza time 🕷')
    except ValueError as e:
        print(e)
Sample Output 3:
    Некорректное время
"""
class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, value):
        if not type(value) is int or not 1 <= value <= 12:
            raise ValueError('Некорректное время')
        self._hours = value

    hours = property(get_hours, set_hours)


""" Упражнение 3
Реализуйте класс Person, описывающий человека. При создании экземпляра класс должен принимать два аргумента в следующем 
порядке:
    name — имя человека
    surname — фамилия человека
Экземпляр класса Person должен иметь два атрибута:
    name — имя человека
    surname — фамилия человека
Класс Person должен иметь одно свойство:
    fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки: <имя> <фамилия>
Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении 
полного имени должны изменяться имя и фамилия.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    person = Person('Меган', 'Фокс')
    
    print(person.name)
    print(person.surname)
    print(person.fullname)
Sample Output 1:
    Меган
    Фокс
    Меган Фокс
Sample Input 2:
    person = Person('Меган', 'Фокс')
    
    person.name = 'Стефани'
    print(person.fullname)
Sample Output 2:
    Стефани Фокс
Sample Input 3:
    person = Person('Алан', 'Тьюринг')
    
    person.surname = 'Вирт'
    print(person.fullname)
Sample Output 3:
    Алан Вирт
Sample Input 4:
    person = Person('Джон', 'Маккарти')
    
    person.fullname = 'Алан Тьюринг'
    print(person.name)
    print(person.surname)
Sample Output 4:
    Алан
    Тьюринг
"""
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fn(self):
        return f'{self.name} {self.surname}'

    def set_fn(self, full_name):
        self.name, self.surname = full_name.split()

    fullname = property(get_fn, set_fn)
