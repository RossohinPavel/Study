""" Упражнение 1
Подвиг 5. Объявите класс Animal (животное), объекты которого создаются командой:
    an = Animal(name, kind, old)
где name - название животного (строка); kind - вид животного (строка); old - возраст (целое число). В каждом объекте
этого класса должны создаваться соответствующие приватные атрибуты: __name, __kind, __old.
В классе Animal должны быть объявлены объекты-свойства для изменения и считывания приватных атрибутов:
    name - для работы с приватным атрибутом __name;
    kind - для работы с приватным атрибутом __kind;
    old - для работы с приватным атрибутом __old.
Создайте в программе список с именем animals, который содержит три объекта класса Animal со следующими данными:
Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3
P.S. В программе нужно объявить только класс и создать список animals. На экран выводить ничего не нужно.
"""
class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3)]


""" Упражнение 2
Подвиг 6. Объявите класс Furniture (мебель), объекты которого создаются командой:
    f = Furniture(name, weight)
где name - название предмета (строка); weight - вес предмета (целое или вещественное число).
В каждом объекте класса Furniture должны создаваться защищенные локальные атрибуты с именами _name и _weight. В самом 
классе Furniture нужно объявить приватные методы:
    __verify_name() - для проверки корректности имени;
    __verify_weight() - для проверки корректности веса.
Метод __verify_name() проверяет, что имя должно быть строкой, если это не так, то генерируется исключение командой:
    raise TypeError('название должно быть строкой')
Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля), если это не так, то 
генерируется исключение командой:
    raise TypeError('вес должен быть положительным числом')
Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их создании).
На основе базового класса Furniture объявить следующие дочерние классы:
    Closet - для представления шкафов;
    Chair - для представления стульев;
    Table - для представления столов.
Объекты этих классов должны создаваться командами:
    obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей (целое число)
    obj = Chair(name, weight, height)       # height - высота стула (любое положительное число)
    obj = Table(name, weight, height, square) # height - высота стола; square - площадь поверхности (любые положительные числа)
В каждом объекте этих классов должны создаваться соответствующие защищенные атрибуты:
    - в объектах класса Closet: _name, _weight, _tp, _doors
    - в объектах класса Chair: _name, _weight, _height
    - в объектах класса Table: _name, _weight, _height, _square
В каждом классе (Closet, Chair, Table) объявить метод:
    get_attrs()
который возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.
Пример использования классов (эти строчки в программе писать не нужно):
    cl = Closet('шкаф-купе', 342.56, True, 3)
    chair = Chair('стул', 14, 55.6)
    tb = Table('стол', 34.5, 75, 10)
    print(tb.get_attrs())
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""
class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self._name = name
        self.__verify_weight(weight)
        self._weight = weight

    @staticmethod
    def __verify_name(value):
        if type(value) != str:
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(value):
        if type(value) not in (int, float) or not 0 < value:
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self):
        return tuple(self.__dict__.values())

class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/d5aNVdHGj44
Подвиг 7 (введение в паттерн слушатель). Своей работой вы немного впечатлили начальство и оно поручило вам доделать
паттерн слушатель (listener). Идея этого паттерна очень проста и основа реализуется следующим образом:
    class Observer:
        def update(self, data):
            pass
    
        def __hash__(self):
            return hash(id(self))
    
    
    class Subject:
        def __init__(self):
            self.__observers = {}
            self.__data = None
    
        def add_observer(self, observer):
            self.__observers[observer] = observer
    
        def remove_observer(self, observer):
            if observer in self.__observers:
                self.__observers.pop(observer)
    
        def __notify_observer(self):
            for ob in self.__observers:
                ob.update(self.__data)
    
        def change_data(self, data):
            self.__data = data
            self.__notify_observer()
Здесь в объектах класса Subject можно зарегистрировать (добавить) множество объектов класса Observer (наблюдатель, 
слушатель). Это делается с помощью метода add_observer(). Затем, когда данные (self.__data) меняются путем вызова метода 
change_data() класса Subject, то у всех слушателей автоматически вызывается метод update(). В этом методе можно 
прописать самую разную логику работы при изменении данных в каждом конкретном слушателе.
В проекте данный паттерн предполагается использовать для отображения информации о погоде в различных форматах:
    - текущая температура;
    - текущее атмосферное давление;
    - текущая влажность воздуха.
Для этого сами данные определяются классом:
    class Data:
        def __init__(self, temp, press, wet):
            self.temp = temp    # температура
            self.press = press  # давление
            self.wet = wet      # влажность
А вам поручается разработать дочерние классы, унаследованные от класса Observer, с именами:
    TemperatureView - слушатель для отображения информации о температуре;
    PressureView - слушатель для отображения информации о давлении;
    WetView - слушатель для отображения информации о влажности.
Каждый из этих классов должен переопределять метод update() базового класса так, чтобы выводилась в консоль информация 
в формате:
    TemperatureView: "Текущая температура <число>"
    PressureView: "Текущее давление <число>"
    WetView: "Текущая влажность <число>"
Важно: для вывода информации в консоль используйте функцию print() с одним аргументом в виде F-строки.
Пример использования классов (эти строчки в программе писать не нужно):
    subject = Subject()
    tv = TemperatureView()
    pr = PressureView()
    wet = WetView()
    
    subject.add_observer(tv)
    subject.add_observer(pr)
    subject.add_observer(wet)
    
    subject.change_data(Data(23, 150, 83))
    # выведет строчки:
    # Текущая температура 23
    # Текущее давление 150
    # Текущая влажность 83
    subject.remove_observer(wet)
    subject.change_data(Data(24, 148, 80))
    # выведет строчки:
    # Текущая температура 24
    # Текущее давление 148
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""
class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность


# здесь объявляйте дочерние классы TemperatureView, PressureView и WetView
class TemperatureView(Observer):
    def update(self, data):
        if data:
            print(f'Текущая температура {data.temp}')


class PressureView(Observer):
    def update(self, data):
        if data:
            print(f'Текущее давление {data.press}')


class WetView(Observer):
    def update(self, data):
        if data:
            print(f'Текущая влажность {data.wet}')


""" Упражнение 4
Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:
    air = Aircraft(model, mass, speed, top)
где model - модель самолета (строка); mass - подъемная масса самолета (любое положительное число); speed - максимальная 
скорость (любое положительное число); top - максимальная высота полета (любое положительное число).
В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами: _model, _mass, _speed, _top и 
соответствующими значениями. Если передаваемые аргументы не соответствуют указанным критериям (строка, любое 
положительное число), то генерируется исключение командой:
    raise TypeError('неверный тип аргумента')
Далее, в программе объявите следующие дочерние классы:
    PassengerAircraft - пассажирский самолет;
    WarPlane - военный самолет.
Объекты этих классов создаются командами:
    pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест (целое положительное число)
    wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь); ключи - название оружия, значение - количество
В каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты с именами _chairs и 
_weapons соответственно. Инициализация остальных атрибутов должна выполняться через инициализатор базового класса.
В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов chairs и weapons. 
Если тип данных не совпадает, то генерировать исключение командой:
    raise TypeError('неверный тип аргумента')
Создайте в программе четыре объекта самолетов со следующими данными:
    PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
    PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
    WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
    WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}
Все эти объекты представить в виде списка planes.
P.S. В программе нужно объявить только классы и сформировать список На экран выводить ничего не нужно.
"""
class Aircraft:
    @staticmethod
    def check(arg, t_arg):
        t = type(arg)
        if t_arg == (int, float) and t in t_arg and 0 < arg:
            return arg
        if t_arg == t:
            return arg
        raise TypeError('неверный тип аргумента')



    def __init__(self, model, mass, speed, top):
        self._model = self.check(model, str)
        self._mass = self.check(mass, (int, float))
        self._speed = self.check(speed, (int, float))
        self._top = self.check(top, (int, float))


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self.check(chairs, int)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = self.check(weapons, dict)


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ArF90ldgm70
Подвиг 9 (на повторение). Необходимо объявить функцию-декоратор class_log для класса, которая бы создавала логирование 
вызовов методов класса. Например следующие строчки программы:
    vector_log = []
    
    
    @class_log(vector_log)
    class Vector:
        def __init__(self, *args):
            self.__coords = list(args)
    
        def __getitem__(self, item):
            return self.__coords[item]
    
        def __setitem__(self, key, value):
            self.__coords[key] = value
декорируют класс Vector и в список vector_log добавляются имена методов, которые были вызваны при использовании этого 
класса. В частности, после выполнения команд:
    v = Vector(1, 2, 3)
    v[0] = 10
в списке vector_log должны быть два метода:
['__init__', '__setitem__']
Ваша задача реализовать декоратор с именем class_log.
Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим образом:
    def integer_params(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, integer_params_decorated(v))
    
        return cls
Используйте этот принцип для успешного прохождения подвига.
P.S. В программе нужно объявить только класс и необходимые функции. На экран выводить ничего не нужно.
"""
# здесь объявляйте декоратор и все что с ним связано
class class_log:
    def __init__(self, lst):
        self.lst = lst

    def decorator(self, name, func):
        def wrapper(*args, **kwargs):
            self.lst.append(name)
            return func(*args, **kwargs)
        return wrapper

    def __call__(self, cls):
        for k, v in cls.__dict__.items():
            if callable(v):
                setattr(cls, k, self.decorator(k, v))
        return cls

vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


""" Упражнение 6
Подвиг 10 (на повторение). В программе объявлены два класса и глобальная переменная:
    CURRENT_OS = 'windows'   # 'windows', 'linux'
    
    
    class WindowsFileDialog:
        def __init__(self, title, path, exts):
            self.__title = title # заголовок диалогового окна
            self.__path = path  # начальный каталог с файлами
            self.__exts = exts  # кортеж из отображаемых расширений файлов
    
    
    class LinuxFileDialog:
        def __init__(self, title, path, exts):
            self.__title = title # заголовок диалогового окна
            self.__path = path  # начальный каталог с файлами
            self.__exts = exts  # кортеж из отображаемых расширений файлов
Вам необходимо объявить класс с именем FileDialogFactory (фабрика классов), который бы при выполнении команды:
    dlg = FileDialogFactory(title, path, exts)
возвращал объект класса WindowsFileDialog, если CURRENT_OS равна строке 'windows', в противном случае - объект класса 
LinuxFileDialog. Объект самого класса FileDialogFactory создаваться не должен.
Для реализации такой логики, объявите внутри класса FileDialogFactory два статических метода:
    def create_windows_filedialog(title, path, exts) - для создания объектов класса WindowsFileDialog;
    def create_linux_filedialog(title, path, exts) - для создания объектов класса LinuxFileDialog.
Эти методы следует вызывать в магическом методе __new__() класса FileDialogFactory. Подумайте, как это правильно 
сделать, чтобы не создавался объект самого класса, а лишь возвращался объект или класса WindowsFileDialog, или класса 
LinuxFileDialog.
Пример использования класса (эту строчку в программе не писать):
    dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
P.S. В программе нужно дополнительно объявить только класс FileDialogFactory. На экран выводить ничего не нужно.
"""
CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


# здесь объявляйте класс FileDialogFactory
class FileDialogFactory:
    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)

    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == 'windows':
            cls = WindowsFileDialog
        if CURRENT_OS == 'linux':
            cls = LinuxFileDialog
        return cls(*args, **kwargs)
