""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/lI99OdJt71w
Подвиг 3. Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:
    book = Book()
    book = Book(название, автор, число страниц, год издания)
В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:
    title - заголовок книги (строка, по умолчанию пустая строка);
    author - автор книги (строка, по умолчанию пустая строка);
    pages - число страниц (целое число, по умолчанию 0);
    year - год издания (целое число, по умолчанию 0).
Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным свойствам title,
author, pages и year. Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на строку,
а pages - на целое число), то генерировать исключение командой:
    raise TypeError("Неверный тип присваиваемых данных.")
Создайте в программе объект book класса Book для книги:
    автор: Сергей Балакирев
    заголовок: Python ООП
    pages: 123
    year: 2022
P.S. На экран ничего выводить не нужно.
"""
class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author') and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('pages', 'year') and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DVydksYIejk
Подвиг 4. Вы создаете интернет-магазин. Для этого нужно объявить два класса:
    Shop - класс для управления магазином в целом;
    Product - класс для представления отдельного товара.
Объекты класса Shop следует создавать командой:
    shop = Shop(название магазина)
В каждом объекте класса Shop должно создаваться локальное свойство:
    goods - список товаров (изначально список пустой).
А также в классе объявить методы:
    add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
    remove_product(self, product) - удаление товара product из магазина (из списка goods);
Объекты класса Product следует создавать командой:
    p = Product(название, вес, цена)
В них автоматически должны формироваться локальные атрибуты:
    id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
    name - название товара (строка);
    weight - вес товара (целое или вещественное положительное число);
    price - цена (целое или вещественное положительное число).
В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых данных локальным 
атрибутам объектов класса (например, id - целое число, name - строка и т.п.). Если проверка не проходит, то генерировать 
исключение командой:
    raise TypeError("Неверный тип присваиваемых данных.")
Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id. При попытке это 
сделать генерировать исключение:
    raise AttributeError("Атрибут id удалять запрещено.")
Пример использования классов (в программе эти строчки не писать):
    shop = Shop("Балакирев и К")
    book = Product("Python ООП", 100, 1024)
    shop.add_product(book)
    shop.add_product(Product("Python", 150, 512))
    for p in shop.goods:
        print(f"{p.name}, {p.weight}, {p.price}")
P.S. На экран ничего выводить не нужно. 
"""
class Product:
    __ID_COUNT = 0

    @classmethod
    def __get_id(cls):
        cls.__ID_COUNT += 1
        return cls.__ID_COUNT

    def __init__(self, name, weight, price):
        self.id = self.__get_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('weight', 'price') and (type(value) not in (int, float) or value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        return object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        self.__dict__.pop(item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        """добавление нового товара в магазин (в конец списка goods)"""
        self.goods.append(product)

    def remove_product(self, product):
        """удаление товара product из магазина (из списка goods)"""
        self.goods.remove(product)


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7b8d5zqiiAM
Подвиг 5. Необходимо создать программу для обучающего курса. Для этого объявляются три класса:
    Course - класс, отвечающий за управление курсом в целом;
    Module - класс, описывающий один модуль (раздел) курса;
    LessonItem - класс одного занятия (урока).
Структура курса на уровне этих классов, приведена на рисунке ниже:
Объекты класса LessonItem должны создаваться командой:
    lesson = LessonItem(название урока, число практических занятий, общая длительность урока)
Соответственно, в каждом объекте класса LessonItem должны создаваться локальные атрибуты:
    title - название урока (строка);
    practices - число практических занятий (целое положительное число);
    duration - общая длительность урока (целое положительное число).
Необходимо с помощью магических методов реализовать следующую логику взаимодействия с объектами класса LessonItem:
1. Проверять тип присваиваемых данных локальным атрибутам. Если типы не соответствуют требованиям, то генерировать 
исключение командой:
    raise TypeError("Неверный тип присваиваемых данных.")
2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
Объекты класса Module должны создаваться командой:
    module = Module(название модуля)
Каждый объект класса Module должен содержать локальные атрибуты:
    name - название модуля;
    lessons - список из уроков (объектов класса LessonItem), входящих в модуль (изначально список пуст).
Также в классе Module должны быть реализованы методы:
    add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
    remove_lesson(self, indx) - удаление урока по индексу в списке lessons.
Наконец, объекты класса Course создаются командой:
    course = Course(название курса)
И содержат следующие локальные атрибуты:
    name - название курса (строка);
    modules - список модулей в курсе (изначально список пуст).
Также в классе Course должны присутствовать следующие методы:
    add_module(self, module) - добавление нового модуля в конце списка modules;
    remove_module(self, indx) - удаление модуля из списка modules по индексу в этом списке.
Пример использования классов (в программе эти строчки не писать):
    course = Course("Python ООП")
    module_1 = Module("Часть первая")
    module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
    module_1.add_lesson(LessonItem("Урок 3", 5, 800))
    course.add_module(module_1)
    module_2 = Module("Часть вторая")
    module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
    course.add_module(module_2)
P.S. На экран ничего выводить не нужно. 
"""
class LessonItem:
    """класс одного занятия (урока)"""

    def __init__(self, title, practices, duration):
        self.title = title  # название урока (строка)
        self.practices = practices  # число практических занятий (целое положительное число)
        self.duration = duration  # общая длительность урока (целое положительное число)

    def __setattr__(self, key, value):
        dct = {
            'title': lambda x: type(x) != str,
            'practices': lambda x: type(x) != int or (type(x) == int and x <= 0),
            'duration': lambda x: type(x) != int or (type(x) == int and x <= 0)
        }
        if key in dct and dct[key](value):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ('title', 'practices', 'duration'):
            return None
        object.__delattr__(self, item)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, lesson):
        self.modules.append(lesson)

    def remove_module(self, indx):
        self.modules.pop(indx)


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/oyeub94DCKw
Подвиг 6. Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum, объекты которого 
формируются командой:
    mus = Museum(название музея)
В объектах этого класса должны формироваться следующие локальные атрибуты:
    name - название музея (строка);
    exhibits - список экспонатов (изначально пустой список).
Сам класс Museum должен иметь методы:
    add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
    remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
    get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).
Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие классы экспонатов:
    Picture - для картин;
    Mummies - для мумий;
    Papyri - для папирусов.
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
    p = Picture(название, художник, описание)            # локальные атрибуты: name - название; author - художник; descr - описание
    m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
    pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:
    "Описание экспоната {name}: {descr}"
Например:
    "Описание экспоната Девятый вал: Айвазовский написал супер картину."
Пример использования классов (в программе эти строчки писать не нужно - только для примера):
    mus = Museum("Эрмитаж")
    mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
    mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
    p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
    mus.add_exhibit(p)
    for x in mus.exhibits:
        print(x.descr)
    P.S. На экран ничего выводить не нужно. 
"""
class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies(Picture):
    def __setattr__(self, key, value):
        key = key if key != 'author' else 'location'
        object.__setattr__(self, key, value)


class Papyri(Picture):
    def __setattr__(self, key, value):
        key = key if key != 'author' else 'date'
        object.__setattr__(self, key, value)


class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        exhibit = self.exhibits[indx]
        return f'Описание экспоната {exhibit.name}: {exhibit.descr}'


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Xq19kCDRaag
Подвиг 7 (на повторение). Объявите класс SmartPhone, объекты которого предполагается создавать командой:
    sm = SmartPhone(марка смартфона)
Каждый объект должен содержать локальные атрибуты:
    model - марка смартфона (строка);
    apps - список из установленных приложений (изначально пустой).
Также в классе SmartPhone должны быть объявлены следующие методы:
    add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
    remove_app(self, app) - удаление приложения по ссылке на объект app.
При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего 
класса).
Каждое приложение должно определяться своим классом. Для примера объявите следующие классы:
    AppVK - класс приложения ВКонтаке;
    AppYouTube - класс приложения YouTube;
    AppPhone - класс приложения телефона.
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
    app_1 = AppVK() # name = "ВКонтакте"
    app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
    app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = 
словарь с контактами
Пример использования классов (в программе эти строчки не писать):
    sm = SmartPhone("Honor 1.0")
    sm.add_app(AppVK())
    sm.add_app(AppVK())  # второй раз добавляться не должно
    sm.add_app(AppYouTube(2048))
    for a in sm.apps:
        print(a.name)
P.S. На экран ничего выводить не нужно. 
"""
class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        for i in self.apps:
            if type(i) == type(app):
                return
        self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


""" Упражнение 6
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/vOh4gzHnMWg
Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:
    circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:
    __x, __y - координаты центра окружности (вещественные или целые числа);
    __radius - радиус окружности (вещественное или целое положительное число).
Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):
    x, y - для изменения и доступа к значениям __x, __y, соответственно;
    radius - для изменения и доступа к значению __radius.
При изменении значений приватных атрибутов через объекты-свойства нужно проверять, что присваиваемые значения - числа 
(целые или вещественные). Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля). 
Сделать все эти проверки нужно через магические методы. При некорректных переданных числовых значениях, прежние значения 
меняться не должны (исключений никаких генерировать при этом не нужно).
Если присваиваемое значение не числовое, то генерировать исключение командой:
    raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.
Пример использования класса (эти строчки в программе писать не нужно):
    circle = Circle(10.5, 7, 22)
    circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    x, y = circle.x, circle.y
    res = circle.name # False, т.к. атрибут name не существует
P.S. На экран ничего выводить не нужно. 
"""
class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value <= 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value


""" Упражнение 7
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2iS8qnEK9to
Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
Каждый объект класса Dimensions должен создаваться командой:
    d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
и содержать локальные атрибуты:
    __a, __b, __c - габаритные размеры (целые или вещественные числа).
Для работы с этими локальными атрибутами в классе Dimensions следует прописать следующие объекты-свойства:
    a, b, c - для изменения и считывания соответствующих локальных атрибутов __a, __b, __c.
При изменении значений __a, __b, __c следует проверять, что присваиваемое значение число в диапазоне 
[MIN_DIMENSION; MAX_DIMENSION]. Если это не так, то новое значение не присваивается (игнорируется).
С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в 
объектах класса Dimensions. При попытке это сделать генерировать исключение:
    raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
Пример использования класса  (эти строчки в программе писать не нужно):
    d = Dimensions(10.5, 20.1, 30)
    d.a = 8
    d.b = 15
    a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
    d.MAX_DIMENSION = 10  # исключение AttributeError
P.S. В программе нужно объявить только класс Dimensions. На экран ничего выводить не нужно. 
"""
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if key in ('a', 'b', 'c') and (type(value) not in (int, float) or not self.MIN_DIMENSION <= value <= self.MAX_DIMENSION):
            return
        object.__setattr__(self, key, value)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value


""" Упражнение 8
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/FaHqn8Yr45o
Подвиг 10. Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров. 
Каждый слот строго для своего класса фильтра:
    Mechanical - для очистки от крупных механических частиц;
    Aragon - для последующей очистки воды;
    Calcium - для обработки воды на третьем этапе.
Объекты классов фильтров должны создаваться командами:
    filter_1 = Mechanical(дата установки)
    filter_2 = Aragon(дата установки)
    filter_3 = Calcium(дата установки)
Во всех объектах этих классов должен формироваться локальный атрибут:
date - дата установки фильтров (для простоты - положительное вещественное число).
Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение). В случае присвоения 
нового значения, прежнее значение не менять. Ошибок никаких не генерировать.
Объекты класса GeyserClassic должны создаваться командой:
    g = GeyserClassic()
А сам класс иметь атрибут:
    MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)
и следующие методы:
    add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3), 
если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только объекты 
класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.
    remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
    get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
    water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.
Метод water_on() должен возвращать значение True при выполнении следующих условий:
- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах 
[0; MAX_DATE_FILTER])
Пример использования классов  (эти строчки в программе писать не нужно):
    my_water = GeyserClassic()
    my_water.add_filter(1, Mechanical(time.time()))
    my_water.add_filter(2, Aragon(time.time()))
    w = my_water.water_on() # False
    my_water.add_filter(3, Calcium(time.time()))
    w = my_water.water_on() # True
    f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
    my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
    my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
P.S. На экран ничего выводить не нужно. 
"""
import time


class Filter:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if 'date' in self.__dict__ or value <= 0:
            return
        object.__setattr__(self, key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.__slots = {1: None, 2: None, 3: None}
        self.__comp = {1: Mechanical, 2: Aragon, 3: Calcium}

    def add_filter(self, slot_num, filter):
        if self.__slots[slot_num] is None and type(filter) == self.__comp[slot_num]:
            self.__slots[slot_num] = filter

    def remove_filter(self, slot_num):
        self.__slots[slot_num] = None

    def get_filters(self):
        return tuple(self.__slots.values())

    def water_on(self):
        return all([True if x is not None and 0 <= time.time() - x.date <= self.MAX_DATE_FILTER else False for x in self.__slots.values()])
