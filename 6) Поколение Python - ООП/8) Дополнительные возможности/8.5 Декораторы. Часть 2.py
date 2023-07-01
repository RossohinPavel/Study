""" Упражнение 1
Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут
instances, содержащий список всех созданных экземпляров этого класса.
Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке, в
котором они были созданы.
Sample Input:
    @track_instances
    class Person:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f'Person({self.name!r})'


    obj1 = Person('object 1')
    obj2 = Person('object 2')

    print(Person.instances)
Sample Output:
    [Person('object 1'), Person('object 2')]
"""
def track_instances(cls):
    cls.instances = []
    old_init = cls.__init__

    def new_init(self, *args, **kwrags):
        old_init(self, *args, **kwrags)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls


""" Упражнение 2
Словарь атрибутов класса, в отличие от словаря атрибутов экземпляра класса, является объектом типа mappingproxy, а не 
dict.
Приведенный ниже код:
    class MyClass:
        pass
    print(type(MyClass.__dict__))
выводит:
    <class 'mappingproxy'>
Тип mappingproxy представляет собой упрощенный словарь. От типа dict он отличается меньшим количеством методов, а 
главное — отсутствием магического метода __setitem__(). Это значит, в объект типа mappingproxy нельзя напрямую добавить 
новую пару ключ-значение, а также изменить значение имеющегося ключа.
Приведенный ниже код:
    class MyClass:
        pass
    MyClass.__dict__['__doc__'] = 'docstring'
приводит к возбуждению исключения:
    TypeError: 'mappingproxy' object does not support item assignment
Для добавления классу необходимого атрибута можно использовать функцию setattr().
Приведенный ниже код:
    class MyClass:
        pass
    setattr(MyClass, '__doc__', 'docstring')
    print(MyClass.__doc__)
выводит:
    docstring
Реализуйте декоратор @add_attr_to_class для декорирования класса. Декоратор должен принимать произвольное количество 
именованных аргументов и добавлять их декорируемому классу в качестве атрибутов.
Sample Input:
    @add_attr_to_class(first_attr=1, second_attr=2)
    class MyClass:
        pass
    
    print(MyClass.first_attr)
    print(MyClass.second_attr)
Sample Output:
    1
    2
"""
def add_attr_to_class(**kwargs):
    def decorator(cls):
        for key, value in kwargs.items():
            setattr(cls, key, value)
        return cls
    return decorator


""" Упражнение 3
Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:
filename — имя json файла, содержимым которого является JSON объект
Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение 
JSON объекта, содержащегося в этом файле.
Sample Input:
    with open('test.json', 'w') as file:
        file.write('{"x": 1, "y": 2}')
    
    @jsonattr('test.json')
    class MyClass:
        pass
        
    print(MyClass.x)
    print(MyClass.y)
Sample Output:
    1
    2
"""
import json


def jsonattr(filename):
    def decorator(cls):
        with open(filename) as file:
            for key, value in json.load(file).items():
                setattr(cls, key, value)
        return cls
    return decorator


""" Упражнение 4
Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, 
то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.
Примечание 1. Подробнее почитать про шаблон проектирования синглтон можно по ссылке.
Sample Input:
    @singleton
    class MyClass:
        pass
        
    obj1 = MyClass()
    obj2 = MyClass()
    
    print(obj1 is obj2)
Sample Output:
    True
"""
def singleton(cls):
    cls._instance = None
    old__new__ = cls.__new__
    def new__new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = old__new__(cls)
        return cls._instance
    cls.__new__ = new__new__
    return cls


""" Упражнение 5
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) 
и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.
Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом 
каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:
    attrs — булево значение, по умолчанию равняется False
Декоратор должен переименовать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и 
Lower Camel Case на Snake case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты
класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и Lower Camel 
Case на Snake case, если False — остаться прежним.
Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case, 
LowerCamelCase или Snake Case.
Sample Input 1:
    @snake_case()
    class MyClass:
        def FirstMethod(self):
            return 1
        
        def superSecondMethod(self):
            return 2
    
    obj = MyClass()
    
    print(obj.first_method())
    print(obj.super_second_method())
Sample Output 1:
    1
    2
Sample Input 2:
    @snake_case(attrs=True)
    class MyClass:
        FirstAttr = 1
        superSecondAttr = 2
    
    print(MyClass.first_attr)
    print(MyClass.super_second_attr)
Sample Output 2:
    1
    2
Sample Input 3:
    @snake_case()
    class MyClass:
        FirstAttr = 1
    
        def FirstMethod(self):
            return 1
    
    
    obj = MyClass()
    
    print(MyClass.FirstAttr)
    print(obj.first_method())
Sample Output 3:
    1
    1
"""
def snake_case(attrs=False):
    def decorator(cls):
        back = {k: v for k, v in cls.__dict__.items() if not k.startswith('__') and not k.endswith('__')}
        for k, v in back.items():
            delattr(cls, k)
            if callable(v) or not callable(v) == attrs:
                k = k[0].lower() + ''.join(s if s != s.upper() else f'_{s.lower()}' for s in k[1:])
            setattr(cls, k, v)
        return cls
    return decorator


""" Упражнение 6
Реализуйте декоратор @auto_repr для декорирования класса. Декоратор должен принимать два аргумента в следующем порядке:
    args — список имен атрибутов
    kwargs — список имен атрибутов`
Декоратор должен реализовывать формальное строковое представление для экземпляров декорируемого класса. Строковое 
представление должно содержать имя класса и значения атрибутов экземпляра класса и иметь вид:
    <имя класса>(<атрибут>, <атрибут>, ...)
Если атрибут указан в списке args, в строковом представлении должно быть только его значение, если же атрибут указан 
в списке kwargs, в строковом представлении должно быть его значение вместе с именем.
Примечание 1. Атрибуты в форматированной строке должны располагаться в том порядке, в котором они были присвоены экземпляру.
Примечание 2. Гарантируется, что при декорировании указываются все необходимые имена атрибутов. Также гарантируется, 
что имя атрибута указывается либо только в списке args, либо только в списке kwargs. Причем порядок расположения имен 
атрибутов в списках args и kwargs повторяет их расположение в сигнатуре инициализатора декорируемого класса.
Sample Input:
    @auto_repr(args=['x', 'y'], kwargs=['color'])
    class Point:
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color
    
    point = Point(1, 2, color='green')
    print(point)
    
    point.x = 10
    point.y = 20
    print(point)
Sample Output:
    Point(1, 2, color='green')
    Point(10, 20, color='green')
"""
def auto_repr(args, kwargs):
    def decorator(cls):
        old_repr = cls.__repr__
        def new_repr(self):
            lst_args = [repr(self.__dict__[x]) for x in args]
            lst_kwargs = [f'{x}={repr(self.__dict__[x])}' for x in kwargs]
            return f'{cls.__name__}({", ".join(lst_args + lst_kwargs)})'
        cls.__repr__ = new_repr
        return cls
    return decorator


""" Упражнение 7
Любой пользовательский класс по умолчанию способен создавать бесконечное количество собственных экземпляров. Шаблон 
проектирования синглтон, напротив, гарантирует, что класс имеет только один собственный экземпляр, и при попытке создать 
новый, он возвращает уже имеющийся. 
Реализуйте декоратор @limiter для декорирования класса, с помощью которого можно ограничивать количество создаваемых 
декорируемым классом экземпляров до определенного числа. Декоратор должен принимать три аргумента в следующем порядке:
    limit — количество экземпляров, которое может создать декорируемый класс
    unique — имя атрибута экземпляра декорируемого класса, значение которого является его идентификатором. Два 
экземпляра с одинаковыми идентификаторами существовать не могут. Если происходит попытка создать экземпляр, 
идентификатор которого совпадает с идентификатором одного из ранее созданных экземпляров, должен быть возвращен этот 
ранее созданный экземпляр
    lookup — определяет, какой объект должен быть возвращен, если превышено ограничение limit, а значение атрибута 
unique ранее не использовалось. При значении FIRST возвращается самый первый созданный экземпляр, при значении LAST 
— самый последний созданный экземпляр
Примечание 1. Гарантируется, что экземпляры декорируемого класса всегда имеют атрибут, который содержит их 
идентификатор.
Sample Input 1:
    @limiter(2, 'ID', 'FIRST')
    class MyClass:
        def __init__(self, ID, value):
            self.ID = ID
            self.value = value
    
    obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1
    obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2
    
    obj3 = MyClass(1, 20)         # возвращается obj1, так как экземпляр с идентификатором 1 уже есть
    obj4 = MyClass(3, 0)          # превышено ограничение limit, возвращается первый созданный экземпляр
    
    print(obj3.value)
    print(obj4.value)
Sample Output 1:
    5
    5
Sample Input 2:
    @limiter(3, 'ID', 'LAST')
    class MyClass:
        def __init__(self, ID, value):
            self.ID = ID
            self.value = value
    
    obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1
    obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2
    obj3 = MyClass(3, 10)         # создается экземпляр класса с идентификатором 3
    
    obj4 = MyClass(4, 0)          # превышено ограничение limit, возвращается последний созданный экземпляр
    obj5 = MyClass(2, 20)         # возвращается obj2, так как экземпляр с идентификатором 2 уже есть
    
    print(obj4.value)
    print(obj5.value)
Sample Output 2:
    10
    8
"""
def limiter(limit, unique, lookup):
    dct = {}
    def decorator(cls):
        def wrapper(*args, **kwargs):
            obj = cls(*args, **kwargs)
            if getattr(obj, unique) in dct:
                return dct[getattr(obj, unique)]
            ind = -1
            if len(dct) == limit and lookup == 'FIRST':
                ind = 0
            if len(dct) < limit:
                dct[getattr(obj, unique)] = obj
            return dct[list(dct.keys())[ind]]
        return wrapper
    return decorator
