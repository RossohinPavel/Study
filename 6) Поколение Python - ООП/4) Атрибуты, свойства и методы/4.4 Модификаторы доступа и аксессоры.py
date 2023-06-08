""" Упражнение 1
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
    radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:
    _radius — радиус круга
    _diameter — диаметр круга
    _area — площадь круга
Класс Circle должен иметь три метода экземпляра:
    get_radius() — метод, возвращающий радиус круга
    get_diameter() — метод, возвращающий диаметр круга
    get_area() — метод, возвращающий площадь круга
Примечание 1. Площадь круга вычисляется по формуле pi * r ** 2 π — константа, которая выражает отношение длины
окружности к ее диаметру.
Примечание 2. Импортировать константу π можно из модуля math: from math import pi
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Sample Input 1:
    circle = Circle(1)

    print(circle.get_radius())
    print(circle.get_diameter())
    print(round(circle.get_area()))
Sample Output 1:
    1
    2
    3
Sample Input 2:
    circle = Circle(5)

    print(circle.get_radius())
    print(circle.get_diameter())
    print(round(circle.get_area()))
Sample Output 2:
    5
    10
    79
"""
from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * radius ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


""" Упражнение 2
Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен принимать один аргумент:
    balance — баланс счета, по умолчанию имеет значение 0
Экземпляр класса BankAccount должен иметь один атрибут:
    _balance — баланс счета
Класс BankAccount должен иметь четыре метода экземпляра:
    get_balance() — метод, возвращающий актуальный баланс счета
    deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount
    withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount. Если amount 
превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением: На счете 
недостаточно средств
    transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount. Метод должен уменьшать 
баланс текущего счета на amount и увеличивать баланс счета account на amount. Если amount превышает количество средств 
на балансе текущего счета, должно быть возбуждено исключение ValueError с сообщением: На счете недостаточно средств
Примечание 1. Числами будем считать экземпляры классов int и float.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Sample Input 1:
    account = BankAccount()
    
    print(account.get_balance())
    account.deposit(100)
    print(account.get_balance())
    account.withdraw(50)
    print(account.get_balance())
Sample Output 1:
    0
    100
    50
Sample Input 2:
    account = BankAccount(100)
    
    try:
        account.withdraw(150)
    except ValueError as e:
        print(e)
Sample Output 2:
    На счете недостаточно средств
Sample Input 3:
    account1 = BankAccount(100)
    account2 = BankAccount(200)
    
    account1.transfer(account2, 50)
    print(account1.get_balance())
    print(account2.get_balance())
Sample Output 3:
    50
    250
Sample Input 4:
    account1 = BankAccount(100)
    account2 = BankAccount(200)
    
    try:
        account1.transfer(account2, 150)
    except ValueError as e:
        print(e)
Sample Output 4:
    На счете недостаточно средств
"""
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


""" Упражнение 3
Реализуйте класс User, описывающий интернет-пользователя. При создании экземпляра класс должен принимать два аргумента 
в следующем порядке:
    name — имя пользователя. Если name не является непустой строкой, состоящей только из букв, должно быть возбуждено 
исключение ValueError с текстом: Некорректное имя
    age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110], должно быть 
возбуждено исключение ValueError с текстом: Некорректный возраст
Экземпляр класса User должен иметь два атрибута:
    _name — имя пользователя
    _age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:
    get_name() — метод, возвращающий имя пользователя
    set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name. 
Если new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с 
текстом: Некорректное имя
    get_age() — метод, возвращающий возраст пользователя
    set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age. 
    Если new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError 
с текстом: Некорректный возраст
Примечание 1. Если при создании экземпляра класса User имя и возраст одновременно являются некорректными, должно быть 
возбуждено исключение, связанное с именем.
Sample Input 1:
    user = User('Гвидо', 67)
    
    print(user.get_name())
    print(user.get_age())
Sample Output 1:
    Гвидо
    67
Sample Input 2:
    user = User('Гвидо', 67)
    
    user.set_name('Тимур')
    user.set_age(30)
    
    print(user.get_name())
    print(user.get_age())
Sample Output 2:
    Тимур
    30
"""
class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        if not name or not type(name) == str or not name.isalpha():
            raise ValueError('Некорректное имя')
        self._name = name

    def set_age(self, age):
        if not type(age) is int or not 0 <= age <= 110:
            raise ValueError('Некорректный возраст')
        self._age = age
