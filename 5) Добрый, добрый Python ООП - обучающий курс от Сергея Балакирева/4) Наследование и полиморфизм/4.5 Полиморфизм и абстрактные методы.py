""" Упражнение 1
Подвиг 3. В программе объявлены два класса:
    class Student:
        def __init__(self, fio, group):
            self._fio = fio  # ФИО студента (строка)
            self._group = group # группа (строка)
            self._lect_marks = []  # оценки за лекции
            self._house_marks = []  # оценки за домашние задания

        def add_lect_marks(self, mark):
            self._lect_marks.append(mark)

        def add_house_marks(self, mark):
            self._house_marks.append(mark)

        def __str__(self):
            return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


    class Mentor:
        def __init__(self, fio, subject):
            self._fio = fio
            self._subject = subject
Первый класс описывает студентов, а второй - менторов. Вам поручается на основе базового класса Mentor разработать еще
два дочерних класса:
    Lector - для описания лекторов;
    Reviewer - для описания экспертов.
    Объекты этих классов должны создаваться командами:
    lector = Lector(fio, subject)
    reviewer = Reviewer(fio, subject)
где fio - ФИО (строка); subject - предмет (строка). Инициализации этих параметров (fio, subject) должна выполняться
базовым классом Mentor.
В самих классах Lector и Reviewer необходимо объявить метод:
    def set_mark(self, student, mark): ...
для простановки оценки (mark) студенту (student). Причем, в классе Lector оценки добавляются в список _lect_marks
объекта класса Student, а в классе Reviewer - в список _house_marks. Используйте для этого методы add_lect_marks() и
add_house_marks() класса Student.
Также в классах Lector и Reviewer должен быть переопределен магический метод:
    __str__()
для формирования следующей информации об объектах:
    - для объектов класса Lector: Лектор <ФИО>: предмет <предмет>
    - для объектов класса Reviewer: Эксперт <ФИО>: предмет <предмет>
Пример использования классов (эти строчки в программе писать не нужно):
    lector = Lector("Балакирев С.М.", "Информатика")
    reviewer = Reviewer("Гейтс Б.", "Информатика")
    students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
    persons = [lector, reviewer]
    lector.set_mark(students[0], 4)
    lector.set_mark(students[1], 2)
    reviewer.set_mark(students[0], 5)
    reviewer.set_mark(students[1], 3)
    for p in persons + students:
        print(p)
# в консоли будет отображено:
    # Лектор Балакирев С.М.: предмет Информатика
    # Эксперт Гейтс Б.: предмет Информатика
    # Студент Иванов А.Б.: оценки на лекциях: [4]; оценки за д/з: [5]
    # Студент Гаврилов С.А.: оценки на лекциях: [2]; оценки за д/з: [3]
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
P.P.S. Подумайте, где в этой программе полиморфизм.
"""
class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


# здесь продолжайте программу
class Lector(Mentor):
    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f'Лектор {self._fio}: предмет {self._subject}'


class Reviewer(Mentor):
    def set_mark(self, student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return f'Эксперт {self._fio}: предмет {self._subject}'


""" Упражнение 2
Подвиг 4. Вам необходимо объявить базовый класс ShopInterface с абстрактным методом:
    def get_id(self): ...
В самом методе должно генерироваться исключение командой:
    raise NotImplementedError('в классе не переопределен метод get_id')
Инициализатор в классе ShopInterface прописывать не нужно.
Далее объявите дочерний класс ShopItem (от базового класса ShopInterface), объекты которого создаются командой:
    item = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (любое положительное число); price - цена товара (любое 
положительное число).
В каждом объекте класса ShopItem должны формироваться локальные атрибуты с именами _name, _weight, _price и 
соответствующими значениями. Также в объектах класса ShopItem должен автоматически формироваться локальный приватный 
атрибут __id с уникальным (для каждого товара) целым значением.
В классе ShopItem необходимо переопределить метод get_id() базового класса так, чтобы он (метод) возвращал значение 
атрибута __id.
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    ID = -1

    @classmethod
    def __set_id(cls):
        cls.ID += 1
        return cls.ID

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__set_id()

    def get_id(self):
        return self.__id


""" Упражнение 3
Подвиг 5. Ранее вы уже создавали классы валидации в виде иерархии базового класса Validator и дочерних:
    StringValidator
    IntegerValidator
    FloatValidator
для валидации (проверки) корректности данных. Повторим этот функционал с некоторыми изменениями.
Итак, вначале нужно объявить базовый класс Validator, в котором должен отсутствовать инициализатор (магический метод 
__init__) и объявлен метод со следующей сигнатурой:
    def _is_valid(self, data): ...
По идее, этот метод возвращает булево значение True, если данные (data) корректны с точки зрения валидатора, и False - 
в противном случае. Но в базовом классе Validator он должен генерировать исключение командой:
    raise NotImplementedError('в классе не переопределен метод _is_valid')
Затем, нужно объявить дочерний класс FloatValidator для валидации вещественных чисел. Объекты этого класса создаются
командой:
    float_validator = FloatValidator(min_value, max_value)
где min_value - минимально допустимое значение; max_value - максимально допустимое значение.
Пользоваться объектами класса FloatValidator предполагается следующим образом:
    res = float_validator(value)
где value - проверяемое значение (должно быть вещественным и находиться в диапазоне [min_value; max_value]). Данный 
валидатор должен возвращать True, если значение value проходит проверку, и False - в противном случае.
Пример использования классов (эти строчки писать не нужно):
    float_validator = FloatValidator(0, 10.5)
    res_1 = float_validator(1)  # False (целое число, а не вещественное)
    res_2 = float_validator(1.0)  # True
    res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return type(data) == float and self.min_value <= data <= self.max_value

    def __call__(self, value):
        return self._is_valid(value)


""" Упражнение 4
Подвиг 6 (про модуль abc). В языке Python есть еще один распространенный способ объявления абстрактных методов класса 
через декоратор abstractmethod модуля abc:
    from abc import ABC, abstractmethod
Чтобы корректно работал декоратор abstractmethod сам класс должен наследоваться от базового класса ABC. Например, так:

class Transport(ABC):
    @abstractmethod
    def go(self):
        Метод для перемещения транспортного средства

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        Абстрактный метод класса
Мы здесь имеем два абстрактных метода внутри класса Transport, причем, первый метод go() - это обычный метод, а второй 
abstract_class_method() - это абстрактный метод уровня класса. Обратите внимание на порядок использования декораторов 
classmethod и abstractmethod. Они должны быть записаны именно в такой последовательности.
Теперь, если объявить какой-либо дочерний класс, например:
    class Bus(Transport):
        def __init__(self, model, speed):
            self._model = model
            self._speed = speed
    
        def go(self):
            print("bus go")
    
        @classmethod
        def abstract_class_method(cls):
            pass
То в нем обязательно нужно переопределить абстрактные методы go и abstract_class_method класса Transport. Иначе, объект 
класса Bus не будет создан (возникнет исключение TypeError).
Используя эту информацию, объявите базовый класс Model (модель), в котором нужно объявить один абстрактный метод с 
сигнатурой:
    def get_pk(self): ...
и один обычный метод:
    def get_info(self): ...
который бы возвращал строку "Базовый класс Model".
На основе класса Model объявите дочерний класс ModelForm, объекты которого создаются командой:
    form = ModelForm(login, password)
где login - заголовок перед полем ввода логина (строка); password - заголовок перед полем ввода пароля (строка). В
каждом объекте класса ModelForm должны формироваться локальные атрибуты с именами _login и _password, а также 
автоматически появляться локальный атрибут _id с уникальным целочисленным значением для каждого объекта класса ModelForm.
В классе ModelForm переопределите метод:
    def get_pk(self): ...
который должен возвращать значение атрибута _id.
Пример использования классов (эти строчки в программе писать не нужно):
    form = ModelForm("Логин", "Пароль")
    print(form.get_pk())
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
from abc import ABC, abstractmethod


# здесь объявляйте классы
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    ID = -1

    @classmethod
    def __set_id(cls):
        cls.ID += 1
        return cls.ID

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__set_id()

    def get_pk(self):
        return self._id


""" Упражнение 5
Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
Подвиг 7. Используя информацию о модуле abc из предыдущего подвига 6, объявите базовый класс с именем StackInterface со 
следующими абстрактными методами:
    def push_back(self, obj) - добавление объекта в конец стека;
    def pop_back(self) - удаление последнего объекта из стека.
На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:
    st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут:
    _top - ссылка на первый объект стека (для пустого стека _top = None).
В самом классе Stack переопределить абстрактные методы базового класса:
    def push_back(self, obj) - добавление объекта в конец стека;
    def pop_back(self) - удаление последнего объекта из стека.
Сами объекты стека должны определяться классом StackObj и создаваться командой:
    obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка). В каждом объекте класса StackObj должны автоматически 
формироваться атрибуты:
    _data - информация, хранящаяся в объекте (строка);
    _next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).
Пример использования классов (эти строчки в программе писать не нужно):
    st = Stack()
    st.push_back(StackObj("obj 1"))
    obj = StackObj("obj 2")
    st.push_back(obj)
    del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
from abc import ABC, abstractmethod


# здесь объявляйте классы
class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        """добавление объекта класса StackObj в конец односвязного списка"""

        def func(last_obj):
            if last_obj._next is None:
                return last_obj
            return func(last_obj._next)

        if self._top is None:
            self._top = obj
        else:
            func(self._top)._next = obj

    def pop_back(self):
        """извлечение последнего объекта с его удалением из односвязного списка"""

        def func(last_obj):
            if last_obj._next._next is None:
                obj = last_obj._next
                last_obj._next = None
                return obj
            return func(last_obj._next)

        if self._top is None:
            return None
        if self._top._next is None:
            obj = self._top
            self._top = None
            return obj
        return func(self._top)


""" Упражнение 6
Подвиг 8. С помощью модуля abc можно определять не только абстрактные методы, но и абстрактные объекты-свойства 
(property). Делается это следующим образом:
    from abc import ABC, abstractmethod
    
    
    class Transport(ABC):
        @abstractmethod
        def go(self):
            Метод для перемещения транспортного средства
    
        @property
        @abstractmethod
        def speed(self):
            Абстрактный объект-свойство
Используя эту информацию и информацию о модуле abc из подвига 6, объявите базовый класс с именем CountryInterface со 
следующими абстрактными методами и свойствами:
    name - абстрактное свойство (property), название страны (строка);
    population - абстрактное свойство (property), численность населения (целое положительное число);
    square - абстрактное свойство (property), площадь страны (положительное число);
    get_info() - абстрактный метод для получения сводной информации о стране.
На основе класса CountryInterface объявите дочерний класс Country, объекты которого создаются командой:
    country = Country(name, population, square)
В самом классе Country должны быть переопределены следующие свойства и методы базового класса:
    name - свойство (property) для считывания названия страны (строка);
    population - свойство (property) для записи и считывания численности населения (целое положительное число);
    square - свойство (property) для записи и считывания площади страны (положительное число);
    get_info() - метод для получения сводной информации о стране в виде строки:
        "<название>: <площадь>, <численность населения>"
Пример использования классов (эти строчки в программе писать не нужно):
    country = Country("Россия", 140000000, 324005489.55)
    name = country.name
    pop = country.population
    country.population = 150000000
    country.square = 354005483.0
    print(country.get_info()) # Россия: 354005483.0, 150000000
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
from abc import ABC, abstractmethod

# здесь объявляйте классы
class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f'{self._name}: {self._square}, {self._population}'


""" Упражнение 7
Подвиг 9 (на повторение). Вам поручают разработать класс для представления маршрутов в навигаторе. Для этого требуется 
объявить класс с именем Track, объекты которого могут создаваться командами:
    tr = Track(start_x, start_y)
    tr = Track(pt1, pt2, ..., ptN)
где start_x, start_y - начальная координата маршрута (произвольные числа); pt1, pt2, ..., ptN - набор из произвольного 
числа точек (координат) маршрута (объекты класса PointTrack).
При передаче аргументов (start_x, start_y) координата должна представляться первым объектом класса PointTrack. Наборы 
всех точек (объектов PointTrack) должны сохраняться в локальном приватном атрибуте объекта класса Track:
    __points - список из точек (координат) маршрута.
Далее, каждая точка (координата) должна определяться классом PointTrack, объекты которого создаются командой:
    pt = PointTrack(x, y)
где x, y - числа (целые или вещественные). Если передается другой тип данных, то должно генерироваться исключение 
командой:
    raise TypeError('координаты должны быть числами')
В классе PointTrack переопределите магический метод __str__, чтобы информация об объекте класса возвращалась в виде 
строки:
    "PointTrack: <x>, <y>"
Например:
    pt = PointTrack(1, 2)
    print(pt) # PointTrack: 1, 2
В самом классе Track должно быть свойство (property) с именем:
    points - для получения кортежа из точек маршрута.
Также в классе Track должны быть методы:
    def add_back(self, pt) - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
    def add_front(self, pt) - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
    def pop_back(self) - удаление последней точки из маршрута;
    def pop_front(self) - удаление первой точки из маршрута.
Пример использования классов (эти строчки в программе писать не нужно):
    tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
    tr.add_back(PointTrack(1.4, 0))
    tr.pop_front()
    for pt in tr.points:
        print(pt)
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
class PointTrack:
    @staticmethod
    def __check_value(value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
        return value

    def __init__(self, x, y):
        self.x = self.__check_value(x)
        self.y = self.__check_value(y)

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        self.__points = []
        if len(args) == 2 and type(args[0]) != PointTrack and type(args[1]) != PointTrack:
            self.__points.append(PointTrack(*args))
        else:
            self.__points.extend(list(args))

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


""" Упражнение 8
Подвиг 10 (на повторение, релакс). Объявите класс с именем Food (еда), объекты которого создаются командой:
    food = Food(name, weight, calories)
где name - название продукта (строка); weight - вес продукта (любое положительное число); calories - калорийная ценность 
продукта (целое положительное число).
Объявите следующие дочерние классы с именами:
    BreadFood - хлеб;
    SoupFood - суп;
    FishFood - рыба.
Объекты этих классов должны создаваться командами:
    bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба, False - для остальных
    sf = SoupFood(name, weight, calories, dietary) # dietary - True для диетического супа, False - для других видов
    ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь, сардина и т.д.)
В каждом объекте этих дочерних классов должны формироваться соответствующие локальные атрибуты с именами:
    BreadFood: _name, _weight, _calories, _white
    SoupFood: _name, _weight, _calories, _dietary
    FishFood: _name, _weight, _calories, _fish
Пример использования классов (эти строчки в программе писать не нужно):
    bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
    sf = SoupFood("Черепаший суп", 520, 890.5, False)
    ff = FishFood("Консерва рыбная", 340, 1200, "семга")
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
class Food:
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish
