""" Упражнение 1
Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам.
Выполним такой пример.
Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:
    Digit, Integer, Float, Positive, Negative
Каждый объект этих классов должен создаваться однотипной командой вида:
    obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:
    - в классе Digit: value - любое число;
    - в классе Integer: value - целое число;
    - в классе Float: value - вещественное число;
    - в классе Positive: value - положительное число;
    - в классе Negative: value - отрицательное число.
Если проверка не проходит, то генерируется исключение командой:
    raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:
    PrimeNumber - простые числа; наследуется от классов Integer и Positive;
    FloatPositive - наследуется от классов Float и Positive.
Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них
значениями. Сохраните все эти объекты в виде списка digits.
Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:
    lst_positive - все объекты, относящиеся к классу Positive;
    lst_float - все объекты, относящиеся к классу Float.
P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно.
"""
class Digit:
    @classmethod
    def check(cls, value, func):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        if func and not func(value):
            raise TypeError('значение не соответствует типу объекта')

    def __init__(self, value, func=None):
        self.check(value, func)
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        Digit.__init__(self, value, lambda x: type(x) == int)


class Float(Digit):
    def __init__(self, value):
        Digit.__init__(self, value, lambda x: type(x) == float)


class Positive(Digit):
    def __init__(self, value):
        Digit.__init__(self, value, lambda x: x > 0)


class Negative(Digit):
    def __init__(self, value):
        Digit.__init__(self, value, lambda x: x < 0)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        Integer.__init__(self, value)
        Positive.__init__(self, value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        Float.__init__(self, value)
        Positive.__init__(self, value)


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2),
          FloatPositive(6.5), FloatPositive(3.5), FloatPositive(8.9)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))


""" Упражнение 2
Подвиг 5. В программе объявлены два класса:
    class ShopItem:
        ID_SHOP_ITEM = 0
    
        def __init__(self):
            super().__init__()
            ShopItem.ID_SHOP_ITEM += 1
            self._id = ShopItem.ID_SHOP_ITEM
    
        def get_pk(self):
            return self._id
    
    
    class Book(ShopItem):
        def __init__(self, title, author, year):
            super().__init__()
            self._title = title
            self._author = author
            self._year = year
Затем, создается объект класса Book (книга) и отображается в консоль:
    book = Book("Python ООП", "Балакирев", 2022)
    print(book)
В результате, на экране увидим что то вроде:
    <__main__.Book object at 0x0000015FBA4B3D00>
Но нам требуется, чтобы здесь отображались локальные атрибуты объекта с их значениями в формате:
    <атрибут_1>: <значение_1>
    <атрибут_2>: <значение_2>
    ...
    <атрибут_N>: <значение_N>
Для этого вам дают задание разработать два класса:
    ShopGenericView - для отображения всех локальных атрибутов объектов любых дочерних классов (не только Book);
    ShopUserView - для отображения всех локальных атрибутов, кроме атрибута _id, объектов любых дочерних классов 
(не только Book).
То есть, в этих классах нужно переопределить два магических метода: __str__() и __repr__().
Пример использования классов (эти строчки в программе писать не нужно):
    class Book(ShopItem, ShopGenericView): ...
    book = Book("Python ООП", "Балакирев", 2022)
    print(book)
    # на экране увидим строчки:
    # _id: 1
    # _title: Python ООП
    # _author: Балакирев
    # _year: 2022
Другой вариант использования классов:
    class Book(ShopItem, ShopUserView): ...
    book = Book("Python ООП", "Балакирев", 2022)
    print(book)
    # на экране увидим строчки:
    # _title: Python ООП
    # _author: Балакирев
    # _year: 2022
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:
    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items())


class ShopUserView:
    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items() if k != '_id')


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/yXPFcDe6jco
Подвиг 8 (введение в паттерн миксинов - mixins). Часто множественное наследование используют для наполнения дочернего 
класса определенным функционалом. То есть, с указанием каждого нового базового класса, дочерний класс приобретает все 
больше и больше возможностей. И, наоборот, убирая часть базовых классов, дочерний класс теряет соответствующую часть 
функционала. 
Например, паттерн миксинов активно используют в популярном фреймворке Django.  В частности, когда нужно указать 
дочернему классу, какие запросы от клиента он должен обрабатывать (запросы типа GET, POST, PUT, DELETE и т.п.). 
В качестве примера реализуем эту идею в очень упрощенном виде, но сохраняя суть паттерна миксинов.
Предположим, что в программе уже существует следующий набор классов:
    class RetriveMixin:
        def get(self, request):
            return "GET: " + request.get('url')
    
    
    class CreateMixin:
        def post(self, request):
            return "POST: " + request.get('url')
    
    
    class UpdateMixin:
        def put(self, request):
            return "PUT: " + request.get('url')
Здесь в каждом классе выполняется имитация обработки запросов. За GET-запрос отвечает метод get() класса RetriveMixin, 
за POST-запрос - метод post() класса CreateMixin, за PUT-запрос - метод put() класса UpdateMixin.
Далее, вам нужно объявить класс с именем GeneralView, в котором следует указать атрибут (на уровне класса):
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
для перечня разрешенных запросов. А также объявить метод render_request со следующей сигнатурой:
    def render_request(self, request): ...
Здесь request - это словарь (объект запроса), в котором обязательно должны быть два ключа:
    'url' - адрес для обработки запроса;
    'method' - метод запроса: 'GET', 'POST', 'PUT', 'DELETE' и т. д.
В методе render_request() нужно сначала проверить, является ли указанный запрос в словаре request разрешенным 
(присутствует в списке allowed_methods). И если это не так, то генерировать исключение командой:
    raise TypeError(f"Метод {request.get('method')} не разрешен.")
Иначе, вызвать метод по его имени:
    method_request = request.get('method').lower()  # имя метода, малыми буквами
Подсказка: чтобы получить ссылку на метод с именем method_request, воспользуйтесь магическим методом __getattribute__().
Для использования полученных классов, в программе объявляется следующий дочерний класс:
    class DetailView(RetriveMixin, GeneralView):
        allowed_methods = ('GET', 'PUT', )
Воспользоваться им можно, например, следующим образом (эти строчки в программе не писать):
    view = DetailView()
    html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
    print(html)   # GET: https://stepik.org/course/116336/
Если в запросе указать другой метод:
    html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
то естественным образом возникнет исключение (реализовывать в программе не нужно, это уже встроено в сам язык Python):
    AttributeError: 'DetailView' object has no attribute 'put'
так как дочерний класс DetailView не имеет метода put. Поправить это можно, если указать соответствующий базовый класс:
    class DetailView(RetriveMixin, UpdateMixin, GeneralView):
        allowed_methods = ('GET', 'PUT', )
Теперь, при выполнении команд:
    view = DetailView()
    html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
    print(html)
будет выведено:
    PUT: https://stepik.org/course/116336/
Это и есть принцип работы паттерна миксинов.
P.S. В программе требуется объявить только класс GeneralView. На экран выводить ничего не нужно.
"""
class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if request.get('method') not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        return self.__getattribute__(request.get('method').lower())(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )


""" Упражнение 4
Подвиг 9. Объявите класс с именем Money (деньги), объекты которого создаются командой:
    money = Money(value)
где value - любое число (целое или вещественное). Если указывается не числовое значение, то генерируется исключение 
командой:
    raise TypeError('сумма должна быть числом')
В каждом объекте этого класса должен формироваться локальный атрибут _money с соответствующим значением. Также в классе 
Money должно быть объект-свойство (property):
    money - для записи и считывания значения из атрибута _money.
В связке с классом Money работает еще один класс:
    class MoneyOperators:
        def __add__(self, other):
            if type(other) in (int, float):
                return self.__class__(self.money + other)
    
            if type(self) != type(other):
                raise TypeError('Разные типы объектов')
    
            return self.__class__(self.money + other.money)
Он определяет работу арифметических операторов. В данном примере описан алгоритм сложения двух объектов класса Money 
(или объектов его дочерних классов).
Обратите внимание, как реализован метод __add__() в этом классе. Он универсален при работе с любыми объектами класса 
Money или его дочерних классов. Здесь атрибут __class__ - это ссылка на класс объекта self. С помощью __class__ можно 
создавать объекты того же класса, что и self.
Вам необходимо добавить в класс MoneyOperators аналогичную реализацию оператора вычитания.
На основе двух классов (Money и MoneyOperators) предполагается создавать классы кошельков разных валют. Например, так:
    class MoneyR(Money, MoneyOperators):
        def __str__(self):
            return f"MoneyR: {self.money}"
    
    
    class MoneyD(Money, MoneyOperators):
        def __str__(self):
            return f"MoneyD: {self.money}"
И, затем применять их следующим образом (эти строчки в программе писать не нужно):
    m1 = MoneyR(1)
    m2 = MoneyD(2)
    m = m1 + 10
    print(m)  # MoneyR: 11
    m = m1 - 5.4
    m = m1 + m2  # TypeError
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    # здесь объявляйте еще один метод
    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)

# здесь объявляйте класс Money
class Money:
    def __init__(self, value):
        self.money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if type(value) not in (int, float):
            raise TypeError('сумма должна быть числом')
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"
