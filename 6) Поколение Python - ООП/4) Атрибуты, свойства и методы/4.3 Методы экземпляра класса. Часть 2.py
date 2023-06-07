""" Упражнение 1
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь один метод экземпляра:
    shoot() — метод, при вызове которого выводится строка pif
Sample Input 1:
    gun = Gun()

    gun.shoot()
Sample Output 1:
    pif
Sample Input 2:
    gun = Gun()

    gun.shoot()
    gun.shoot()
    gun.shoot()
Sample Output 2:
    pif
    pif
    pif
"""
class Gun:
    def shoot(self):
        print('pif')


""" Упражнение 2
Вам доступен класс User, описывающий интернет-пользователя. При создании экземпляра класс принимает один аргумент:
    name — имя пользователя
Экземпляр класса User имеет два атрибута:
    name — имя пользователя
    friends — количество друзей пользователя, начальным значением является 0
Класс User имеет один метод экземпляра:
    add_friends() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество друзей 
пользователя на n
Найдите и исправьте ошибки, допущенные при реализации метода add_friends().
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    user = User('Arthur')
    
    print(user.friends)
Sample Output 1: 0
Sample Input 2:
    user = User('Timur')
    
    user.add_friends(2)
    user.add_friends(2)
    user.add_friends(3)
    
    print(user.friends)
Sample Output 2: 7
"""
class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


""" Упражнение 3
Вам доступен класс House, описывающий дом. При создании экземпляра класс принимает два аргумента в следующем порядке:
    color — цвет дома
    rooms — количество комнат в доме
Экземпляр данного класса имеет два атрибута:
    color — цвет дома
    rooms — количество комнат в доме
Реализуйте для класса House два метода экземпляра:
    paint() — метод, принимающий в качестве аргумента значение new_color и изменяющий текущий цвет дома на new_color
    add_rooms() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество комнат в доме на n
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    house = House('white', 4)
    
    print(house.color)
    print(house.rooms)
Sample Output 1:
    white
    4
Sample Input 2:
    house = House('white', 4)
    
    house.paint('black')
    house.add_rooms(1)
    
    print(house.color)
    print(house.rooms)
Sample Output 2:
    black
    5
"""
class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, n):
        self.rooms += n


""" Упражнение 4
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
    radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:
    radius — радиус круга
    diameter — диаметр круга
    area — площадь круга
Примечание 1. Площадь круга вычисляется по формуле π * r ** 2, где r — радиус круга, π — константа, которая выражает 
отношение длины окружности к ее диаметру.
Примечание 2. Импортировать константу π можно из модуля math:
    from math import pi
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    circle = Circle(1)
    
    print(circle.radius)
Sample Output 1:
    1
Sample Input 2:
    circle = Circle(5)
    
    print(circle.radius)
    print(circle.diameter)
    print(circle.area)
Sample Output 2:
    5
    10
    78.53981633974483
"""
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius ** 2


""" Упражнение 5
Реализуйте класс Bee, описывающий пчелку, которая перемещается по координатной плоскости в четырех направлениях: 
вверх, вниз, влево и вправо. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
x — координата пчелки по оси x, по умолчанию имеет значение 0
y — координата пчелки по оси y, по умолчанию имеет значение 0
Экземпляр класса Bee должен иметь два атрибута:
x — координата пчелки по оси x
y — координата пчелки по оси y
Класс Bee должен иметь четыре метода экземпляра:
move_up() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси y на n
move_down() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси y на n
move_right() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси x на n
move_left() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси x на n
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    bee = Bee()
    
    print(bee.x, bee.y)
Sample Output 1: 0 0
Sample Input 2:
    bee = Bee()
    
    bee.move_up(1)
    bee.move_right(1)
    bee.move_down(1)
    bee.move_left(1)
    
    print(bee.x, bee.y)
Sample Output 2: 0 0
Sample Input 3:
    bee = Bee()
    
    bee.move_right(2)
    bee.move_right(2)
    bee.move_up(3)
    bee.move_left(1)
    bee.move_down(1)
    
    print(bee.x, bee.y)
Sample Output 3: 3 2
"""
class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n


""" Упражнение 6
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь один метод экземпляра:
shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, 
при четвертом — paf, и так далее
Sample Input 1:
    gun = Gun()
    
    gun.shoot()
Sample Output 1:
    pif
Sample Input 2:
    gun = Gun()
    
    gun.shoot()
    gun.shoot()
    gun.shoot()
    gun.shoot()
Sample Output 2:
    pif
    paf
    pif
    paf
"""
class Gun:
    def __init__(self):
        self.counter = True

    def shoot(self):
        print('pif' if self.counter else 'paf')
        self.counter = not self.counter


""" Упражнение 7
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Gun должен иметь три метода экземпляра:
shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, 
при четвертом — paf, и так далее
shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля
Sample Input 1:
    gun = Gun()
    
    print(gun.shots_count())
    gun.shoot()
    print(gun.shots_count())
    gun.shoot()
    print(gun.shots_count())
Sample Output 1:
    0
    pif
    1
    paf
    2
Sample Input 2:
    gun = Gun()
    
    gun.shoot()
    gun.shoot()
    print(gun.shots_count())
    gun.shots_reset()
    print(gun.shots_count())
    gun.shoot()
    print(gun.shots_count())    
Sample Output 2:
    pif
    paf
    2
    0
    pif
    1
"""
class Gun:
    def __init__(self):
        self.counter = 0

    def shoot(self):
        print('pif' if self.counter % 2 == 0 else 'paf')
        self.counter += 1

    def shots_count(self):
        return self.counter

    def shots_reset(self):
        self.counter = 0


""" Упражнение 8
Реализуйте класс Scales, описывающий весы с двумя чашами. При создании экземпляра класс не должен принимать никаких 
аргументов.
Класс Scales должен иметь три метода экземпляра:
    add_right() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на правую чашу весов 
этот груз
    add_left() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на левую чашу весов 
этот груз
    get_result() — метод, возвращающий строку Весы в равновесии, если массы грузов на чашах совпадают, Правая чаша 
тяжелее — если правая чаша тяжелее, Левая чаша тяжелее — если левая чаша тяжелее
Примечание 1. Пустые весы всегда находятся в равновесии.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    scales = Scales()
    
    scales.add_right(1)
    scales.add_right(1)
    scales.add_left(2)
    
    print(scales.get_result())
Sample Output 1:
    Весы в равновесии
Sample Input 2:
    scales = Scales()
    
    scales.add_right(1)
    scales.add_left(2)
    
    print(scales.get_result())
Sample Output 2:
    Левая чаша тяжелее
Sample Input 3:
    scales = Scales()
    
    scales.add_right(2)
    scales.add_left(1)
    
    print(scales.get_result())
Sample Output 3:
    Правая чаша тяжелее
"""
class Scales:
    def __init__(self):
        self.left_cup = 0
        self.right_cup = 0

    def add_left(self, n):
        self.left_cup += n

    def add_right(self, n):
        self.right_cup += n

    def get_result(self):
        if self.left_cup > self.right_cup:
            return 'Левая чаша тяжелее'
        elif self.left_cup < self.right_cup:
            return 'Правая чаша тяжелее'
        return 'Весы в равновесии'


""" Упражнение 9
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента 
в следующем порядке:
x — координата вектора по оси x, по умолчанию имеет значение 0
y — координата вектора по оси y, по умолчанию имеет значение 0
Экземпляр класса Vector должен иметь два атрибута:
x — координата вектора по оси x
y — координата вектора по оси y
Класс Vector должен иметь один метод экземпляра:
abs() — метод, возвращающий модуль вектора
Примечание 1. Модуль вектора с координатами 
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    vector = Vector()
    
    print(vector.x, vector.y)
    print(vector.abs())
Sample Output 1:
    0 0
    0.0
Sample Input 2:
    vector = Vector(3, 4)
    
    print(vector.x, vector.y)
    print(vector.abs())
Sample Output 2:
    3 4
    5.0
"""
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


""" Упражнение 10
Реализуйте класс Numbers, описывающий изначально пустой расширяемый набор целых чисел. При создании экземпляра класс не 
должен принимать никаких аргументов.
Класс Numbers должен иметь три метода экземпляра:
    add_number() — метод, принимающий в качестве аргумента целое число и добавляющий его в набор
    get_even() — метод, возвращающий список всех четных чисел из набора
    get_odd() — метод, возвращающий список всех нечетных чисел из набора
Примечание 1. Числа в списках, возвращаемых методами get_even() и get_odd(), должны располагаться в том порядке, 
в котором они были добавлены в набор.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    numbers = Numbers()
    
    print(numbers.get_even())
    print(numbers.get_odd())
Sample Output 1:
    []
    []
Sample Input 2:
    numbers = Numbers()
    
    numbers.add_number(3)
    numbers.add_number(2)
    numbers.add_number(1)
    numbers.add_number(4)
    
    print(numbers.get_even())
    print(numbers.get_odd())
Sample Output 2:
    [2, 4]
    [3, 1]
Sample Input 3:
    numbers = Numbers()
    
    numbers.add_number(1)
    numbers.add_number(3)
    numbers.add_number(1)
    
    print(numbers.get_even())
    print(numbers.get_odd())
Sample Output 3:
    []
    [1, 3, 1]
"""
class Numbers:
    def __init__(self):
        self.lst = []

    def add_number(self, n):
        self.lst.append(n)

    def get_even(self):
        return [x for x in self.lst if x % 2 == 0]

    def get_odd(self):
        return [x for x in self.lst if x % 2 == 1]


""" Упражнение 11
Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов, разделенных 
пробелами.
Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс 
не должен принимать никаких аргументов.
Экземпляр класса TextHandler должен иметь три метода:
    add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
    get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
    get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
Примечание 1. Слова в списках, возвращаемых методами get_shortest_words() и get_longest_words(), должны располагаться 
в том порядке, в котором они были добавлены в набор.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    texthandler = TextHandler()
    
    print(texthandler.get_shortest_words())
    print(texthandler.get_longest_words())
Sample Output 1:
    []
    []
Sample Input 2:
    texthandler = TextHandler()
    
    texthandler.add_words('do not be sorry')
    texthandler.add_words('be')
    texthandler.add_words('better')
    
    print(texthandler.get_shortest_words())
    print(texthandler.get_longest_words())
Sample Output 2:
    ['do', 'be', 'be']
    ['better']
Sample Input 3:
    texthandler = TextHandler()
    
    texthandler.add_words('The world will hold my trial for your sins')
    texthandler.add_words('Never meant to see the sky, never meant to live')
    
    print(texthandler.get_shortest_words())
    print(texthandler.get_longest_words())
Sample Output 3:
    ['my', 'to', 'to']
    ['world', 'trial', 'Never', 'meant', 'never', 'meant']
"""
class TextHandler:
    def __init__(self):
        self.lst = []

    def add_words(self, words):
        self.lst.extend(words.split())

    def get_shortest_words(self):
        value = 0
        if self.lst:
            value = len(min(self.lst, key=len))
        return [x for x in self.lst if len(x) == value]

    def get_longest_words(self):
        value = 0
        if self.lst:
            value = len(max(self.lst, key=len))
        return [x for x in self.lst if len(x) == value]


""" Упражнение 12
Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Todo должен иметь один атрибут:
    things — изначально пустой список дел, которые нужно выполнить
Класс Todo должен иметь четыре метода экземпляра:
    add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в 
виде кортежа: (<название дела>, <приоритет>)
    get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, 
имеющих приоритет n
    get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет 
    get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет 
Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(), 
должны располагаться в том порядке, в котором они были добавлены в список.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    todo = Todo()
    
    print(todo.things)
    print(todo.get_by_priority(1))
    print(todo.get_low_priority())
    print(todo.get_high_priority())
Sample Output 1:
    []
    []
    []
    []
Sample Input 2:
    todo = Todo()
    
    todo.add('Проснуться', 3)
    todo.add('Помыться', 2)
    todo.add('Поесть', 2)
    
    print(todo.get_by_priority(2))
Sample Output 2:
    ['Помыться', 'Поесть']
Sample Input 3:
    todo = Todo()
    
    todo.add('Ответить на вопросы', 5)
    todo.add('Сделать картинки', 1)
    todo.add('Доделать задачи', 4)
    todo.add('Дописать конспект', 5)
    
    print(todo.get_low_priority())
    print(todo.get_high_priority())
    print(todo.get_by_priority(3))
Sample Output 3:
    ['Сделать картинки']
    ['Ответить на вопросы', 'Дописать конспект']
    []
"""
class Todo:
    def __init__(self):
        self.things = []

    def add(self, case, priority):
        self.things.append((case, priority))

    def get_by_priority(self, n):
        return [x[0] for x in self.things if x[1] == n]

    def get_low_priority(self):
        lowest = 0
        if self.things:
            lowest = min(x[1] for x in self.things)
        return self.get_by_priority(lowest)

    def get_high_priority(self):
        highest = 0
        if self.things:
            highest = max(x[1] for x in self.things)
        return self.get_by_priority(highest)


""" Упражнение 13
Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Postman должен иметь один атрибут:
    delivery_data — изначально пустой список адресов, по которым следует доставить письма
Экземпляр класса Postman должен иметь три метода экземпляра:
add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов эти 
данные в виде кортежа:
(<улица>, <дом>, <квартира>)
get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице, 
в которые требуется доставить письма
get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом 
доме, в которые требуется доставить письма
Примечание 1. Дома и квартиры в списках, возвращаемых методами get_houses_for_street() и get_flats_for_house(), должны 
располагаться в том порядке, в котором они были добавлены.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    postman = Postman()
    
    print(postman.delivery_data)
    print(postman.get_houses_for_street('3-я ул. Строителей'))
    print(postman.get_flats_for_house('3-я ул. Строителей', 25))
Sample Output 1:
    []
    []
    []
Sample Input 2:
    postman = Postman()
    
    postman.add_delivery('Советская', 151, 74)
    postman.add_delivery('Советская', 151, 75)
    postman.add_delivery('Советская', 90, 2)
    postman.add_delivery('Советская', 151, 74)
    
    print(postman.get_houses_for_street('Советская'))
    print(postman.get_flats_for_house('Советская', 151))
Sample Output 2:
    [151, 90]
    [74, 75]
"""
class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, *args):
        self.delivery_data.append(args)

    def get_houses_for_street(self, street):
        lst = []
        for x in filter(lambda x: x[0] == street, self.delivery_data):
            if x[1] not in lst:
                lst.append(x[1])
        return lst

    def get_flats_for_house(self, street, house):
        lst = []
        for x in filter(lambda x: x[0] == street and x[1] == house, self.delivery_data):
            if x[2] not in lst:
                lst.append(x[2])
        return lst


""" Упражнение 14
Будем называть словом любую последовательность из одной или более латинских букв.
Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра класс должен принимать один 
аргумент:
    words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым
Экземпляр класса Wordplay должен иметь один атрибут:
    words — список, содержащий набор слов
Класс Wordplay должен иметь четыре метода экземпляра:
    add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор. Если слово уже есть в наборе, 
метод ничего не должен делать
    words_with_length() — метод, принимающий в качестве аргумента натуральное число n и возвращающий список слов из 
набора, длина которых равна n
    only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора, которые 
состоят только из переданных букв
    avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words, 
которые не содержат ни одну из этих букв
Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(), должны располагаться 
в том порядке, в котором они были добавлены.
Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был создан. Другими словами, 
если исходный список изменится, то экземпляр класса Wordplay измениться не должен.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    wordplay = Wordplay()
    
    print(wordplay.words_with_length(1))
    print(wordplay.only('a', 'b', 'c'))
    print(wordplay.avoid('a', 'b', 'c'))
Sample Output 1:
    []
    []
    []
Sample Input 2:
    wordplay = Wordplay()
    
    print(wordplay.words)
    wordplay.add_word('bee')
    wordplay.add_word('geek')
    print(wordplay.words)
Sample Output 2:
    []
    ['bee', 'geek']
Sample Input 3:
    wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])
    
    wordplay.add_word('python')
    print(wordplay.words_with_length(4))
Sample Output 3:
    ['geek', 'cool']
Sample Input 4:
    wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])
    
    print(wordplay.only('o', 't'))
Sample Output 4:
    ['o', 'to', 'otto', 't']
"""
class Wordplay:
    def __init__(self, words=None):
        self.words = [] if words is None else words[:]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args):
        return list(filter(lambda x: set(x).issubset(set(args)), self.words))

    def avoid(self, *args):
        return list(filter(lambda x: set(x).isdisjoint(set(args)), self.words))


""" Упражнение 15
Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в 
следующем порядке:
    horizontal — координата коня по горизонтали, представленная латинской буквой от a до h
    vertical — координата коня по вертикали, представленная целым числом от 1 до 8 включительно
    color — цвет коня (black или white)
Экземпляр класса Knight должен иметь три атрибута:
    horizontal — координата коня на шахматной доске по горизонтали
    vertical — координата коня на шахматной доске по вертикали
    color — цвет коня
Класс Knight должен иметь четыре метода экземпляра:
    get_char() — метод, возвращающий символ N
    can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали, 
и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
    move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали и заменяющий 
текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с указанными 
координатами, его координаты должны остаться неизменными
    draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может 
переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может 
переместиться конь, — символом *
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    knight = Knight('c', 3, 'white')
    
    print(knight.color, knight.get_char())
    print(knight.horizontal, knight.vertical)
Sample Output 1:
    white N
    c 3
Sample Input 2:
    knight = Knight('c', 3, 'white')
    
    print(knight.horizontal, knight.vertical)
    print(knight.can_move('e', 5))
    print(knight.can_move('e', 4))
    
    knight.move_to('e', 4)
    print(knight.horizontal, knight.vertical)
Sample Output 2:
    c 3
    False
    True
    e 4
Sample Input 3:
    knight = Knight('c', 3, 'white')
    
    knight.draw_board()
Sample Output 3:
    ........
    ........
    ........
    .*.*....
    *...*...
    ..N.....
    *...*...
    .*.*....
"""
class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.pos = self.convert(vertical, horizontal)
        self.color = color

    def get_char(self):
        return 'N'

    def convert(self, v, h):
        deck = 'abcdefgh'
        return 8 - v, deck.index(h) if type(h) is str else deck[h]

    def can_move(self, h, v):
        p1, p2 = self.convert(self.vertical, self.horizontal)
        m1, m2 = self.convert(v, h) if type(h) is str else (v, h)
        return (abs(p1 - m1) == 1 and abs(p2 - m2) == 2) or (abs(p1 - m1) == 2 and abs(p2 - m2) == 1)

    def move_to(self, h, v):
        if self.can_move(h, v):
            self.horizontal = h
            self.vertical = v
            self.pos = self.convert(v, h)

    def draw_board(self):
        matrix = [['.'] * 8 for _ in range(8)]
        for i in range(8):
            for n in range(8):
                if self.can_move(n, i):
                    matrix[i][n] = '*'
                if (i, n) == self.pos:
                    matrix[i][n] = self.get_char()
        for i in range(len(matrix)):
            print(*matrix[i], sep='')
