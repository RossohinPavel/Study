""" Упражнение 1
1. Реализуйте класс Point, описывающий точку на плоскости. При создании экземпляра класс должен принимать два аргумента
в следующем порядке:
x — координата точки по оси x, y — координата точки по оси y
Экземпляр класса Point должен иметь следующее неформальное строковое представление:
    (<координата x>, <координата y>)
2. Также реализуйте класс Circle, описывающий окружность на плоскости. При создании экземпляра класс должен принимать
два аргумента в следующем порядке:
    radius — радиус окружности
    center — точка с координатами центра окружности, представленная экземпляром класса Point
Экземпляр класса Circle должен иметь следующее неформальное строковое представление:
    (<координата центра по оси x>, <координата центра по оси y>), r = <радиус>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input:
    point = Point(1, 1)
    circle = Circle(5, point)

    print(point)
    print(circle)
Sample Output:
    (1, 1)
    (1, 1), r = 5
"""
class Point:
    def __init__(self, x, y):
        self.coords = x, y

    def __str__(self):
        return str(self.coords)


class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def __str__(self):
        return str(self.center) + ', r = ' + str(self.radius)


""" Упражнение 2
1. Реализуйте класс Item, описывающий товар. При создании экземпляра класс должен принимать два аргумента в следующем 
порядке:
    name — название товара
    price — цена товара в долларах
Экземпляр класса Item должен иметь следующее неформальное строковое представление:
    <название товара>, <цена товара>$
2. Также реализуйте класс ShoppingCart, описывающий корзину для покупок. При создании экземпляра класс должен принимать 
один аргумент:
    items — итерируемый объект, определяющий начальный набор товаров в корзине. Если не передан, корзина считается 
пустой
Класс ShoppingCart должен иметь три метода экземпляра:
    add() — метод, принимающий в качестве аргумента товар и добавляющий его в корзину
    total() — метод, возвращающий суммарную стоимость всех товаров в корзине
    remove() — метод, принимающий в качестве аргумента название товара и удаляющий его из корзины. Если в корзине 
несколько товаров с указанным именем, они должны быть удалены все
Экземпляр класса ShoppingCart должен иметь следующее неформальное строковое представление:
    <название первого товара в корзине>, <цена первого товара в корзине>$
    <название второго товара в корзине>, <цена второго товара в корзине>$
    ...
Примечание 1. Если корзина для покупок пуста, то ее неформальным строковым представлением должна быть пустая строка.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используются только с корректными данными.
Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    item1 = Item('Yoga Mat', 130)
    item2 = Item('Flannel Shirt', 22)
    
    print(item1)
    print(item2)
Sample Output 1:
    Yoga Mat, 130$
    Flannel Shirt, 22$
Sample Input 2:
    shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])
    
    shopping_cart.add(Item('Flannel Shirt', 22))
    print(shopping_cart)
    print(shopping_cart.total())
Sample Output 2:
    Yoga Mat, 130$
    Flannel Shirt, 22$
    152
Sample Input 3:
    shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])
    
    shopping_cart.remove('Yoga Mat')
    print(shopping_cart)
    print(shopping_cart.total())
Sample Output 3:
    Flannel Shirt, 22$
    22
"""
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'

    def __eq__(self, other):
        return self.name == other


class ShoppingCart:
    def __init__(self, items=None):
        self.items = []
        if items:
            self.items.extend(list(items))

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(i.price for i in self.items)

    def remove(self, item):
        while item in self.items:
            self.items.remove(item)

    def __str__(self):
        return '\n'.join(str(x) for x in self.items)

    
""" Упражнение 3
1. Реализуйте класс Card, описывающий игральную карту. При создании экземпляра класс должен принимать два аргумента в 
следующем порядке:
    suit — масть игральной карты, представленная одним из следующих символов: ♣, ♢, ♡, ♠
    rank — ранг игральной карты, представленный одним из следующих символов или парой символов: 2, 3, 4, 5, 6, 7, 8, 9, 
10, J, Q, K, A
Экземпляр класса Card должен иметь следующее неформальное строковое представление:
    <масть игральной карты><ранг игральной карты>
2. Также реализуйте класс данных Deck, описывающий классическую колоду из 52 игральных карт. Карты в колоде должны быть 
расположены сперва в порядке возрастания мастей, а затем — в порядке возрастания рангов. При создании экземпляра класс 
не должен принимать никаких аргументов.
Класс Deck должен иметь два метода экземпляра:
    shuffle() — метод, перемешивающий все карты в колоде. Перемешивать колоду можно только в том случае, если в колоде 
на данный момент находятся все 52 карты. Если в колоде меньше 52 карт, должно быть возбуждено исключение ValueError 
с текстом: Перемешивать можно только полную колоду
    deal() — метод, удаляющий из колоды последнюю карту и возвращающий ее. Если колода пуста, должно быть возбуждено 
исключение ValueError с текстом: Все карты разыграны
Экземпляр класса Deck должен иметь следующее неформальное строковое представление:
    Карт в колоде: <текущее количество карт в колоде>
Примечание 1. Порядок старшинства карточных рангов от младшего к старшему:
    2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
Порядок старшинства карточных мастей от младшего к старшему:
    ♣, ♢, ♡, ♠
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используются только с корректными данными.
Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    print(Card('♣', '4'))
    print(Card('♡', 'A'))
    print(Card('♢', '10'))
Sample Output 1:
    ♣4
    ♡A
    ♢10 
Sample Input 2:
    deck = Deck()
    
    print(deck)
    print(deck.deal())
    print(deck.deal())
    print(deck.deal())
    print(deck)
Sample Output 2:
    Карт в колоде: 52
    ♠A
    ♠K
    ♠Q
    Карт в колоде: 49
Sample Input 3:
    deck = Deck()
    
    for _ in range(52):
        deck.deal()
        
    try:
        deck.deal()
    except ValueError as error:
        print(error)
Sample Output 3:
    Все карты разыграны
Sample Input 4:
    deck = Deck()
    
    deck.deal()
        
    try:
        deck.shuffle()
    except ValueError as error:
        print(error)
Sample Output 4:
    Перемешивать можно только полную колоду
"""
import random as r


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    __suits = ("♣", "♢", "♡", "♠")
    __ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self):
        self._deck = [Card(s, r) for s in self.__suits for r in self.__ranks]

    def shuffle(self):
        if len(self._deck) != 52:
            raise ValueError('Перемешивать можно только полную колоду')
        r.shuffle(self._deck)

    def deal(self):
        if not self._deck:
            raise ValueError('Все карты разыграны')
        return self._deck.pop(-1)

    def __str__(self):
        return f'Карт в колоде: {len(self._deck)}'


""" Упражнение 4
Реализуйте класс Queue, описывающий очередь, элементами которой являются пары ключ: значение. При создании экземпляра 
класс должен принимать один аргумент:
    pairs — список или словарь, определяющий начальный набор элементов очереди. Порядок элементов в очереди должен 
совпадать с их порядком в переданном итерируемом объекте. Если не передан, очередь считается пустой
Класс Queue должен иметь два метода экземпляра:
    add() — метод, принимающий в качестве аргумента элемент и добавляющий его в конец очереди. Элементом в данном случае 
является двухэлементный кортеж, содержащий ключ и значение. Если в очереди уже содержится элемент с указанным ключом, он 
должен быть перенесен в конец очереди, а его значение должно быть обновлено
    pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Элементом в данном случае является 
двухэлементный кортеж, содержащий ключ и значение. Если очередь пуста, должно быть возбуждено исключение KeyError 
с текстом: Очередь пуста
Экземпляр класса Queue должен иметь следующее формальное строковое представление:
    Queue([(<ключ 1-го элемента>, <значение 1-го элемента>), (<ключ 2-го элемента>, <значение 2-го элемента>), ...])
При передаче экземпляра класса Queue в функцию len() должно возвращаться количество элементов в нем.
Примечание 1. Вероятно, при решении задачи будет удобно воспользоваться одним из классов из модуля collections.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной.
Sample Input 1:
    queue = Queue()
    
    queue.add(('one', 1))
    queue.add(('two', 2))
    print(queue)
Sample Output 1:
    Queue([('one', 1), ('two', 2)])
Sample Input 2:
    queue = Queue([('one', 1)])
    
    queue.add(('two', 2))
    print(queue.pop())
    print(queue.pop())
    print(queue)
Sample Output 2:
    ('one', 1)
    ('two', 2)
    Queue([])
Sample Input 3:
    queue = Queue({'one': 1, 'two': 2})
    
    print(len(queue))
    queue.add(('three', 1))
    print(len(queue))
Sample Output 3:
    2
    3
Sample Input 4:
    queue = Queue()
    
    queue.add(('one', 1))
    queue.add(('two', 2))
    print(queue)
    queue.add(('one', 10))
    print(queue)
Sample Output 4:
    Queue([('one', 1), ('two', 2)])
    Queue([('two', 2), ('one', 10)])
Sample Input 5:
    queue = Queue()
    
    try:
        queue.pop()
    except KeyError as error:
        print(error)
Sample Output 5:
    'Очередь пуста'
"""
class Pair:
    def __init__(self, key, value):
        self.values = key, value

    def __eq__(self, other):
        if isinstance(other, Pair):
            other = other.values
        return self.values[0] == other[0]

    def __repr__(self):
        return str(self.values)


class Queue:
    def __init__(self, pairs=None):
        self._lst = []
        if isinstance(pairs, dict):
            pairs = list(pairs.items())
        if isinstance(pairs, list):
            for item in pairs:
                self.add(item)

    def add(self, pair):
        pair = Pair(*pair)
        if pair in self._lst:
            self._lst.remove(pair)
        self._lst.append(pair)

    def pop(self):
        if not self._lst:
            raise KeyError('Очередь пуста')
        return self._lst.pop(0)

    def __repr__(self):
        return f'Queue({repr(self._lst)})'

    def __len__(self):
        return len(self._lst)


""" Упражнение 5
1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать три 
аргумента в следующем порядке:
    topic — тема выступления
    start_time — время начала выступления в виде строки в формате HH:MM
    duration — длительность выступления в виде строки в формате HH:MM
2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день. Конференция представляет 
собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Conference должен иметь четыре метода экземпляра:
    add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление 
пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:
    Провести выступление в это время невозможно
    total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
    longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки 
в формате HH:MM
    longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде 
строке в формате HH:MM
Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, 
например, в 12:00, а другое начинаться в 12:00.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используются только с корректными данными.
Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    conference = Conference()
    
    conference.add(Lecture('Простые числа', '08:00', '01:30'))
    conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
    conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
    print(conference.total())
    print(conference.longest_lecture())
    print(conference.longest_break())
Sample Output 1:
    05:20
    02:00
    01:30
Sample Input 2:
    conference = Conference()
    conference.add(Lecture('Простые числа', '08:00', '01:30'))
    
    try:
        conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
    except ValueError as error:
        print(error)
Sample Output 2:
    Провести выступление в это время невозможно
Sample Input 3:
    conference = Conference()
    conference.add(Lecture('Простые числа', '08:00', '01:00'))
    conference.add(Lecture('Жизнь после ChatGPT', '11:00', '02:00'))
    
    try:
        conference.add(Lecture('Муравьиный алгоритм', '10:00', '04:00'))
    except ValueError as error:
        print(error)
Sample Output 3:
    Провести выступление в это время невозможно
"""
from datetime import timedelta


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = timedelta(**self.convert(start_time))
        self.duration = timedelta(**self.convert(duration))
        self.end_time = self.start_time + self.duration

    @staticmethod
    def convert(time):
        return {'hours': int(time[:2]), 'minutes': int(time[-2:])}

    def __lt__(self, other):
        return self.start_time < other.start_time


class Conference:
    def __init__(self):
        self._lst = []

    def add(self, lecture):
        for l in self._lst:
            old = l if l < lecture else lecture
            new = l if l > lecture else lecture
            if old.end_time > new.start_time:
                raise ValueError('Провести выступление в это время невозможно')
        self._lst.append(lecture)
        self._lst.sort()

    def total(self):
        total = timedelta()
        for l in self._lst:
            total += l.duration
        return self.convert(total)

    def longest_lecture(self):
        return self.convert(max(self._lst, key=lambda x: x.duration).duration)

    def longest_break(self):
        br = timedelta()
        for i in range(len(self._lst)):
            res = self._lst[i].start_time - self._lst[i - 1].end_time
            if res > br:
                br = res
        return self.convert(br)

    @staticmethod
    def convert(delta):
        return ':'.join(x.rjust(2, '0') for x in str(delta).split(':')[:2])
