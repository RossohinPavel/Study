""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/xHINhSQJh5c
Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи
вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать
исключение командой:
    raise TypeError("Присваивать можно только вещественный тип данных.")
Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться
командой:
    cell = Cell(начальное значение ячейки)
Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:
table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект
value (начальное значение должно быть 0.0).
В каждом объекте класса TableSheet должен формироваться локальный атрибут:
cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).
Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0
(по порядку).
P.S. На экран в программе выводить ничего не нужно.
"""
class FloatValue:
    @staticmethod
    def check_value(value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self._name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)


for j in range(len(table.cells)):
    for i in range(len(table.cells[j])):
        table.cells[j][i].value = float(i + 1 + j * len(table.cells[i]))


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/zCD5_APRzes
Подвиг 7. Объявите класс ValidateString для проверки корректности переданной строки. Объекты этого класса создаются командой:
    validate = ValidateString(min_length=3, max_length=100)
    где min_length - минимальное число символов в строке; max_length - максимальное число символов в строке.
В классе ValidateString должен быть реализован метод:
    validate(self, string) - возвращает True, если string является строкой (тип str) и длина строки в пределах 
[min_length; max_length]. Иначе возвращается False.
Объявите дескриптор данных StringValue для работы со строками, объекты которого создаются командой:
    st = StringValue(validator=ValidateString(min_length, max_length))
При каждом присвоении значения объекту st должен вызываться валидатор (объект класса ValidateString) и с помощью метода 
validate() проверяться корректность присваиваемых данных. Если данные некорректны, то присвоение не выполняется 
(игнорируется).
Объявите класс RegisterForm с тремя объектами дескриптора StringValue:
    login = StringValue(...) - для ввода логина;
    password = StringValue(...)  - для ввода пароля;
    email = StringValue(...)  - для ввода Email.
Объекты класса RegisterForm создаются командой:
    form = RegisterForm(логин, пароль, email)
    где логин, пароль, email - начальные значения логина, пароля и Email.
В классе RegisterForm также должны быть объявлены методы:
    get_fields() - возвращает список из значений полей в порядке [login, password, email];
    show() - выводит в консоль многострочную строку в формате:
        <form>
        Логин: <login>
        Пароль: <password>
        Email: <email>
        </form>
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""
class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self._name, value)

class RegisterForm:
    login = StringValue(ValidateString(min_length=3, max_length=100))
    password = StringValue(ValidateString(min_length=3, max_length=100))
    email = StringValue(ValidateString(min_length=3, max_length=100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/l0U_3dTJZyc
Подвиг 8. Вы начинаете создавать интернет-магазин. Для этого в программе объявляется класс SuperShop, объекты которого 
создаются командой:
    myshop = SuperShop(название магазина)
В каждом объекте класса SuperShop должны формироваться следующие локальные атрибуты:
    name - название магазина (строка);
    goods - список из товаров.
Также в классе SuperShop должны быть методы:
    add_product(product) - добавление товара в магазин (в конец списка goods);
    remove_product(product) - удаление товара из магазина (из списка goods).
Здесь product - это объект класса Product, описывающий конкретный товар. В этом классе следует объявить следующие 
дескрипторы:
    name = StringValue(min_length, max_length)    # min_length - минимально допустимая длина строки; max_length - 
максимально допустимая длина строки
    price = PriceValue(max_value)    # max_value - максимально допустимое значение
Объекты класса Product будут создаваться командой:
    pr = Product(наименование, цена)
Классы StringValue и PriceValue - это дескрипторы данных. Класс StringValue должен проверять, что присваивается 
строковый тип с длиной строки в диапазоне [2; 50], т.е. min_length = 2, max_length = 50. Класс PriceValue должен 
проверять, что присваивается вещественное или целочисленное значение в диапазоне [0; 10000], т.е. max_value = 10000. 
Если проверки не проходят, то соответствующие (прежние) значения меняться не должны.
Пример использования класса SuperShop (эти строчки в программе писать не нужно):
    shop = SuperShop("У Балакирева")
    shop.add_product(Product("Курс по Python", 0))
    shop.add_product(Product("Курс по Python ООП", 2000))
    for p in shop.goods:
        print(f"{p.name}: {p.price}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно. 
"""
class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self._name, value)


class PriceValue:
    def __init__(self, max_value):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if (type(value) == int or type(value) == float) and 0 <= value <= self.max_value:
            setattr(instance, self._name, value)


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)



""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/S4CDXCG9nbA
Подвиг 9 (на повторение). Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:
    bag = Bag(max_weight)
где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).
В каждом объекте этого класса должен создаваться локальный приватный атрибут:
    __things - список вещей в рюкзаке (изначально список пуст).
Сам же класс Bag должен иметь объект-свойство:
    things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).
Также в классе Bag должны быть реализованы следующие методы:
    add_thing(self, thing) - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
    remove_thing(self, indx) - удаление предмета по индексу списка __things;
    get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.
Каждая вещь описывается как объект класса Thing и создается командой:
    t = Thing(название, вес)
где название - наименование предмета (строка); вес - вес предмета (целое или вещественное число).
В каждом объекте класса Thing должны формироваться локальные атрибуты:
    name - наименование предмета;
    weight - вес предмета.
Пример использования классов (эти строчки в программе писать не нужно):
    bag = Bag(1000)
    bag.add_thing(Thing("Книга по Python", 100))
    bag.add_thing(Thing("Котелок", 500))
    bag.add_thing(Thing("Спички", 20))
    bag.add_thing(Thing("Бумага", 100))
    w = bag.get_total_weight()
    for t in bag.things:
        print(f"{t.name}: {t.weight}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно. 
"""
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.max_weight - thing.weight >= 0:
            self.max_weight -= thing.weight
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(x.weight for x in self.__things)


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/45q8BT03c_U
Подвиг 10 (на повторение). Необходимо написать программу для представления и управления расписанием телевизионного 
вещания. Для этого нужно объявить класс TVProgram, объекты которого создаются командой:
    pr = TVProgram(название канала)
где название канала - это строка с названием телеканала.
В каждом объекте класса TVProgram должен формироваться локальный атрибут:
    items - список из телепередач (изначально список пуст).
В самом классе TVProgram должны быть реализованы следующие методы:
    add_telecast(self, tl) - добавление новой телепередачи в список items;
    remove_telecast(self, indx) - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).
Каждая телепередача должна описываться классом Telecast, объекты которого создаются командой:
    tl = Telecast(порядковый номер, название, длительность)
где порядковый номер - номер телепередачи в сетке вещания (от 1 и далее); название - наименование телепередачи; 
длительность - время телепередачи (в секундах - целое число).
Соответственно, в каждом объекте класса Telecast должны формироваться локальные приватные атрибуты:
    __id - порядковый номер (целое число);
    __name - наименование телепередачи (строка);
    __duration - длительность телепередачи в секундах (целое число).
Для работы с этими приватными атрибутами в классе Telecast должны быть объявлены соответствующие объекты-свойства 
(property):
    uid - для записи и считывания из локального атрибута __id;
    name - для записи и считывания из локального атрибута __name;
    duration - для записи и считывания из локального атрибута __duration.
Пример использования классов (эти строчки в программе писать не нужно):
    pr = TVProgram("Первый канал")
    pr.add_telecast(Telecast(1, "Доброе утро", 10000))
    pr.add_telecast(Telecast(2, "Новости", 2000))
    pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
    for t in pr.items:
        print(f"{t.name}: {t.duration}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно. 
"""


class Telecast:
    def __init__(self, tc_id, name, duration):
        self.__id = tc_id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        """добавление новой телепередачи в список items"""
        self.items.append(tl)

    def remove_telecast(self, indx):
        """удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее)"""
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)


