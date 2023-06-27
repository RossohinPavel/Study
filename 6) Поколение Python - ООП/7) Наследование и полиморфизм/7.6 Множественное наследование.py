""" Упражнение 1
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов:
Sample Input 1:
    print(issubclass(E, B))
    print(issubclass(E, C))
    print(issubclass(E, D))
Sample Output 1:
    True
    False
    True
Sample Input 2:
    print(issubclass(B, A))
    print(issubclass(C, A))
    print(issubclass(D, A))
Sample Output 2:
    True
    True
    True
"""
class A: pass
class C(A): pass
class B(A): pass
class D(A): pass
class E(B, D): pass


""" Упражнение 2
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов:
Sample Input 1:
    print(issubclass(D, H))
    print(issubclass(E, H))
    print(issubclass(F, H))
    print(issubclass(G, H))
Sample Output 1:
    True
    True
    True
    True
Sample Input 2:
    print(issubclass(B, D))
    print(issubclass(B, E))
    print(issubclass(B, F))
    print(issubclass(B, G))
Sample Output 2:
    True
    True
    False
    False
Sample Input 3:
    print(issubclass(C, D))
    print(issubclass(C, E))
    print(issubclass(C, F))
    print(issubclass(C, G))
Sample Output 3:
    False
    False
    True
    True
"""
class H: pass
class D(H): pass
class E(H): pass
class F(H): pass
class G(H): pass
class B(D, E): pass
class C(F, G): pass
class A(B, C): pass


""" Упражнение 3
Реализуйте функцию get_method_owner(), которая принимает два аргумента в следующем порядке:
    cls — произвольный класс
    method — строковое название метода
Функция должна возвращать класс, от которого класс cls унаследовал метод method. Если метода method нет ни в самом 
классе, ни в одном другом классе из его иерархии, функция get_method_owner() должна вернуть значение None.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_method_owner(), но не 
код, вызывающий ее.
Sample Input 1:
    class A:
        def m(self):
            pass
            
    class B(A):
        pass
    
    print(get_method_owner(B, 'm'))
Sample Output 1:
    <class '__main__.A'>
    Sample Input 2:
    
    class A:
        def m(self):
            pass
            
    class B(A):
        def m(self):
            pass
    
    print(get_method_owner(B, 'm'))
Sample Output 2:
    <class '__main__.B'>
    Sample Input 3:
    
    class A:
        pass
            
    class B(A):
        pass
    
    print(get_method_owner(B, 'm'))
Sample Output 3:
    None
"""
def get_method_owner(cls, method):
    for m in cls.mro():
        if method in m.__dict__:
            return m


""" Упражнение 4
С помощью множественного наследования постройте иерархию из приведенных ниже четырех классов. При решении старайтесь 
свести дублирование кода к минимуму.
1. Реализуйте класс Father, описывающий отца. При создании экземпляра класс должен принимать один аргумент:
    mood — настроение, по умолчанию равняется строкеneutral
Экземпляр класса Father должен иметь один атрибут:
    mood — настроение
Класс Father должен иметь два метода экземпляра:
    greet() — метод, возвращающий строку Hello!
    be_strict() — метод, изменяющий значение атрибута mood на строку strict 
2. Также реализуйте класс Mother, описывающий мать. При создании экземпляра класс должен принимать один аргумент:
    mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Mother должен иметь один атрибут:
    mood — настроение
Класс Mother должен иметь два метода экземпляра:
    greet() — метод, возвращающий строку Hi, honey!
    be_kind() — метод, изменяющий значение атрибута mood на строку kind
3. Помимо этого, реализуйте класс Daughter, описывающий дочь. При создании экземпляра класс должен принимать один 
аргумент:
    mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Daughter должен иметь один атрибут:
    mood — настроение
Класс Daughter должен иметь три метода экземпляра:
    greet() — метод, возвращающий строку Hi, honey!
    be_kind() — метод, изменяющий значение атрибута mood на строку kind
    be_strict() — метод, изменяющий значение атрибута mood на строку strict
4. Наконец, реализуйте класс Son, описывающий сына. При создании экземпляра класс должен принимать один аргумент:
    mood — настроение, по умолчанию равняется строке neutral
Экземпляр класса Son должен иметь один атрибут:
    mood — настроение
Класс Son должен иметь три метода экземпляра:
    greet() — метод, возвращающий строку Hello!
    be_kind() — метод, изменяющий значение атрибута mood на строку kind
    be_strict() — метод, изменяющий значение атрибута mood на строку strict
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используются только с корректными данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    father = Father()
    mother = Mother()
    
    print(father.mood)
    print(mother.mood)
    print(father.greet())
    print(mother.greet())
Sample Output 1:
    neutral
    neutral
    Hello!
    Hi, honey!
Sample Input 2:
    father = Father('happy')
    mother = Mother('unhappy')
    
    print(father.mood)
    print(mother.mood)
    father.be_strict()
    mother.be_kind()
    print(father.mood)
    print(mother.mood)
Sample Output 2:
    happy
    unhappy
    strict
    kind
"""
class Parent:
    def __init__(self, mood='neutral'):
        self.mood = mood


class Father(Parent):
    def be_strict(self):
        self.mood = 'strict'

    def greet(self):
        return 'Hello!'


class Mother(Parent):
    def be_kind(self):
        self.mood = 'kind'

    def greet(self):
        return 'Hi, honey!'


class Daughter(Mother, Father): pass


class Son(Father, Mother): pass


""" Упражнение 5
Реализуйте класс MROHelper, описывающий набор функций для работы с MRO произвольных классов. При создании экземпляра 
класс не должен принимать никаких аргументов.
Класс MROHelper должен иметь три статических метода:
    len() — метод, принимающий в качестве аргумента класс и возвращающий количество элементов в его MRO
    class_by_index() — метод, принимающий в качестве аргументов класс cls и целое число n, по умолчанию равное нулю, 
и возвращающий класс с индексом n в MRO класса cls
    index_by_class() — метод, принимающий в качестве аргументов два класса child и parent и возвращающий целое число — 
индекс класса parent в MRO класса child
Примечание 1. Нумерация классов в MRO начинается с нуля.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса MROHelper нет, она может быть произвольной.
Sample Input 1:
    class A:
        pass
        
    class B(A):
        pass
        
    class C(A):
        pass
        
    class D(B, C):
        pass
        
    print(MROHelper.len(D))
Sample Output 1:
    5
Sample Input 2:
    class A:
        pass
        
    class B(A):
        pass
        
    class C(A):
        pass
        
    class D(B, C):
        pass
        
    print(MROHelper.class_by_index(D, 2))
    print(MROHelper.class_by_index(B))
Sample Output 2:
    <class '__main__.C'>
    <class '__main__.B'>
    Sample Input 3:
    
    class A:
        pass
        
    class B(A):
        pass
        
    class C(A):
        pass
        
    class D(B, C):
        pass
        
    print(MROHelper.index_by_class(D, A))
Sample Output 3:
    3
"""
class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)
