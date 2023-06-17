""" Упражнение 1
Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен был принимать три
аргумента в следующем порядке:
    name — название предмета
    price — цена предмета в рублях
    quantity — количество предметов
Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной
буквы, а при обращении к атрибуту total — произведение цены предмета на его количество.
Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Item нет, она может быть произвольной.
Sample Input 1:
    fruit = Item('banana', 15, 5)

    print(fruit.price)
    print(fruit.quantity)
Sample Output 1:
    15
    5
Sample Input 2:
    fruit = Item('banana', 15, 5)

    print(fruit.name)
    print(fruit.total)
Sample Output 2:
    Banana
    75
Sample Input 3:
    course = Item('pygen', 3900, 2)

    print(course.name)
    print(course.price)
    print(course.quantity)
    print(course.total)
Sample Output 3:
    Pygen
    3900
    2
    7800
"""
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return super().__getattribute__('price') * super().__getattribute__('quantity')
        elif name == 'name':
            return super().__getattribute__(name).title()
        return super().__getattribute__(name)


""" Упражнение 2
Требовалось реализовать класс Logger. При создании экземпляра класс не должен был принимать никаких аргументов.
Предполагалось, что при установке или изменении значения атрибута экземпляра класса Logger будет выводиться текст:
    Изменение значения атрибута <имя атрибута> на <новое значение атрибута>
Также планировалось, что при удалении атрибута будет выводиться текст:
    Удаление атрибута <имя атрибута>
Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Logger.
Примечание. Никаких ограничений касательно реализации класса Logger нет, она может быть произвольной.
Sample Input 1:
    obj = Logger()
    
    obj.attr = 1
    del obj.attr
Sample Output 1:
    Изменение значения атрибута attr на 1
    Удаление атрибута attr
Sample Input 2:
    obj = Logger()
    
    obj.name = 'pygen'
    obj.rating = '5*'
    obj.ceo = 'Timur'
    del obj.rating
    obj.rating = '6*'
Sample Output 2:
    Изменение значения атрибута name на pygen
    Изменение значения атрибута rating на 5*
    Изменение значения атрибута ceo на Timur
    Удаление атрибута rating
    Изменение значения атрибута rating на 6*
"""
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]


""" Упражнение 3
Реализуйте класс Ord. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Ord должен выступать в качестве альтернативы функции ord(). При обращении к атрибуту экземпляра, именем 
которого является одиночный символ, должна возвращаться его позиция в таблице символов Unicode.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Ord нет, она может быть произвольной.
Sample Input 1:
    obj = Ord()
    
    print(obj.a)
    print(obj.b)
Sample Output 1:
    97
    98
Sample Input 2:
    obj = Ord()
    
    print(obj.в)
    print(obj.г)
Sample Output 2:
    1074
    1075
"""
class Ord:
    def __getattr__(self, value):
        return ord(value)


""" Упражнение 4
Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default, 
имеющий значение по умолчанию None, а после произвольное количество именованных аргументов. Аргументы, передаваемые 
после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.
При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default.
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса DefaultObject нет, она может быть произвольной.
Sample Input 1:
    god = DefaultObject(name='Ares', mythology='greek')
    
    print(god.name)
    print(god.mythology)
    print(god.age)
Sample Output 1:
    Ares
    greek
    None
Sample Input 2:
    god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')
    
    print(god.name)
    print(god.mythology)
    print(god.age)
Sample Output 2:
    Tyr
    scandinavian
    0
"""
class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, value):
        return self.default


""" Упражнение 5
Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных 
аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов, причем если 
значением атрибута является отрицательное число, оно должно быть взято с противоположным знаком.
Примечание 1. Числами будем считать экземпляры классов int и float.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной.
Sample Input 1:
    point = NonNegativeObject(x=1, y=-2, z=0, color='black')
    
    print(point.x)
    print(point.y)
    print(point.z)
    print(point.color)
Sample Output 1:
    1
    2
    0
    black
Sample Input 2:
    point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')
    
    print(point.x)
    print(point.y)
    print(point.z)
    print(point.color)
Sample Output 2:
    1.5
    2.3
    0.0
    yellow
"""
class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __setattr__(self, name, value):
        if isinstance(value, int | float):
            value = abs(value)
        self.__dict__[name] = value


""" Упражнение 6
Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных 
аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
Экземпляр класса AttrsNumberObject должен иметь один атрибут:
    attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам 
атрибут attrs_num
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.
Sample Input 1:
    music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')
    
    print(music_group.attrs_num)
Sample Output 1: 3
Sample Input 2:
    music_group = AttrsNumberObject()
    
    print(music_group.attrs_num)
Sample Output 2: 1
Sample Input 3:
    music_group = AttrsNumberObject(name='Woodkid', genre='pop')
    
    print(music_group.attrs_num)
    music_group.country = 'France'
    print(music_group.attrs_num)
Sample Output 3:
    3
    4
Sample Input 4:
    music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')
    
    print(music_group.attrs_num)
    del music_group.genre
    print(music_group.attrs_num)
Sample Output 4:
    3
    2
"""
# Скорее всего, по задумкам авторов предполагалась существование attrs_num в виде атрибута, а не свойства property.
# Соответственно, его нужно было пересчитывать при вызове соответствующих методов. Но так изящнее!
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def attrs_num(self):
        return len(self.__dict__) + 1


""" Упражнение 7
Реализуйте класс Const. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. 
Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
Класс Const должен разрешать устанавливать атрибуты своим экземплярам и получать их значения, но не разрешать изменять 
значения этих атрибутов, а также удалять их. При попытке изменить значение атрибута должно возбуждаться исключение 
AttributeError с текстом:
    Изменение значения атрибута невозможно
При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:
    Удаление атрибута невозможно
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Const нет, она может быть произвольной.
Sample Input 1:
    videogame = Const(name='Cuphead')
    
    videogame.developer = 'Studio MDHR'
    print(videogame.name)
    print(videogame.developer)
Sample Output 1:
    Cuphead
    Studio MDHR
Sample Input 2:
    videogame = Const(name='Dicso Elysium')
    
    try:
        videogame.name = 'Half-Life: Alyx'
    except AttributeError as e:
        print(e)
Sample Output 2:
    Изменение значения атрибута невозможно
Sample Input 3:
    videogame = Const(name='The Last of Us')
    
    try:
        del videogame.name
    except AttributeError as e:
        print(e)
Sample Output 3:
    Удаление атрибута невозможно
"""
class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        self.__dict__[name] = value

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')


""" Упражнение 8
Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_). Например, _password, 
__email и __dict__.
Реализуйте класс ProtectedObject. При создании экземпляра класс должен принимать произвольное количество именованных 
аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров, а также 
удалять эти атрибуты. При попытке получить или изменить значение защищенного атрибута, а также попытке удалить атрибут, 
должно возбуждаться исключение AttributeError с текстом:
    Доступ к защищенному атрибуту невозможен
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса ProtectedObject нет, она может быть произвольной.
Sample Input:
    user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
    
    try:
        print(user.login)
        print(user._password)
    except AttributeError as e:
        print(e)
Sample Output:
    PG_kamiya
    Доступ к защищенному атрибуту невозможен
"""
class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    @staticmethod
    def _check(func):
        def wrapper(base, *args):
            if args[0].startswith('_'):
                raise AttributeError('Доступ к защищенному атрибуту невозможен')
            return func(base, *args)
        return wrapper

    @_check
    def __getattribute__(self, name):
        return super().__getattribute__(name)

    @_check
    def __setattr__(self, *args):
        return super().__setattr__(*args)

    @_check
    def __delattr__(self, *args):
        super().__delattr__(*args)
