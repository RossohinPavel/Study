""" Упражнение 1
Вам доступен класс Person, описывающий человека. При создании экземпляра класс принимает два аргумента в следующем
порядке:
    name — имя человека
    surname — фамилия человека
Экземпляр класса Person имеет два атрибута:
    name — имя человека
    surname — фамилия человека
Класс Person имеет одно свойство:
    fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки: <имя> <фамилия>
Реализуйте свойство fullname класса Person с помощью декоратора @property.
Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении
полного имени должны изменяться имя и фамилия.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Sample Input 1:
    person = Person('Mike', 'Pondsmith')

    print(person.name)
    print(person.surname)
    print(person.fullname)
Sample Output 1:
    Mike
    Pondsmith
    Mike Pondsmith
Sample Input 2:
    person = Person('Mike', 'Pondsmith')

    person.name = 'Troy'
    print(person.fullname)
Sample Output 2:
    Troy Pondsmith
Sample Input 3:
    person = Person('Mike', 'Pondsmith')

    person.surname = 'Baker'
    print(person.fullname)
Sample Output 3:
    Mike Baker
Sample Input 4:
    person = Person('Mike', 'Pondsmith')

    person.fullname = 'Troy Baker'
    print(person.name)
    print(person.surname)
Sample Output 4:
    Troy
    Baker
"""
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


""" Упражнение 2
В целях безопасности в базах данных пароли от аккаунтов пользователей хранятся не в явном виде, а в виде хеш-значений 
— чисел, вычисленных по специальному алгоритму на основе паролей.
Вам доступна функция hash_function(), которая принимает в качестве аргумента пароль и возвращает его хеш-значение.
Реализуйте класс Account, описывающий аккаунт интернет-пользователя на некотором сервисе. При создании экземпляра класс 
должен принимать два аргумента в следующем порядке:
    login — логин пользователя
    password — пароль пользователя
Класс Account должен иметь два свойства:
    login — свойство, доступное только для чтения, возвращающее логин пользователя. При попытке изменения свойство 
должно быть возбуждено исключение AttributeError с текстом: Изменение логина невозможно
    password — свойство, доступное для чтения и записи, возвращающее хеш-значение пароля от аккаунта пользователя. 
При изменении свойство должно вычислять хеш-значение нового пароля и сохранять его, а не сам пароль
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса Account нет, она может быть произвольной.
Sample Input 1:
    account = Account('hannymad', 'cakeisalie')
    
    print(account.login)
    print(account.password)
Sample Output 1:
    hannymad
    4696
Sample Input 2:
    account = Account('timyr-guev', 'lovebeegeek')
    
    print(account.password)
    account.password = 'verylovebeegeek'
    print(account.password)
Sample Output 2:
    5661
    10953
Sample Input 3:
    account = Account('timyr-guev', 'lovebeegeek')
    try:
        account.login = 'timyrik30'
    except AttributeError as e:
        print(e)
Sample Output 3:
    Изменение логина невозможно
"""
def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10 ** 9


class Account:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        if hasattr(self, '_login'):
            raise AttributeError('Изменение логина невозможно')
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = hash_function(value)


""" Упражнение 3
Квадратный трехчлен – это многочлен вида ax ** 2 +bx+c, где a ≠ 0. Например: x**2 + 1, x**2 −5x+6
Значение переменной x, при котором квадратный трехчлен обращается в ноль, называют его корнем. Квадратный трехчлен может 
иметь один корень, два корня или вовсе не иметь корней. Корни квадратного трехчлена, если они существуют, находятся по 
формуле:
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать 
три аргумента в следующем порядке:
    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен иметь три атрибута:
    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена
Класс QuadraticPolynomial должен иметь четыре свойства:
    x1 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле 
(минус). Если квадратный трехчлен не имеет корней, значением свойства должно быть значение None
    x2 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле 
(плюс). Если квадратный трехчлен не имеет корней, значением свойства должно быть значение None
    view — свойство, доступное только для чтения, возвращающее строку вида: ax^2 + bx + cб где a, b и с представляют 
коэффициенты квадратного трехчлена
    coefficients — свойство, доступное для чтения и записи, возвращающее кортеж вида: (a, b, c)б где a, b и с 
представляют коэффициенты квадратного трехчлена
Примечание 1. Если квадратный трехчлен имеет лишь один корень, значения свойств x1 и x2 должны совпадать.
Примечание 2. При изменении коэффициентов квадратного трехчлена через соответствующие атрибуты или свойство coefficients 
значения свойств x1, x2, view и coefficients также должны изменяться.
Примечание 3. Если какие-либо коэффициенты квадратного трехчлена равны нулю, они по-прежнему должны присутствовать в 
строке, возвращаемой свойством view, дополнительно их убирать не нужно.
Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 5. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.
Sample Input 1:
    polynom = QuadraticPolynomial(1, 2, -3)
    
    print(polynom.a)
    print(polynom.b)
    print(polynom.c)
Sample Output 1:
    1
    2
    -3
Sample Input 2:
    polynom = QuadraticPolynomial(1, 2, -3)
    
    print(polynom.x1)
    print(polynom.x2)
Sample Output 2:
    -3.0
    1.0
Sample Input 3:
    polynom = QuadraticPolynomial(1, 2, -3)
    
    print(polynom.view)
    print(polynom.coefficients)
Sample Output 3:
    1x^2 + 2x - 3
    (1, 2, -3)
"""


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.coefficients = a, b, c

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, value):
        self.a, self.b, self.c = value

    @property
    def view(self):
        fp = f'{str(self.a) if self.a >= 0 else "-" + str(abs(self.a))}x^2'
        sp = f'{"+ " + str(self.b) if self.b >= 0 else "- " + str(abs(self.b))}x'
        tp = f'{"+ " + str(self.c) if self.c >= 0 else "- " + str(abs(self.c))}'
        return fp + ' ' + sp + ' ' + tp

    def desc_check(func):
        def wrapper(self):
            desc = self.b ** 2 - 4 * self.a * self.c
            if desc < 0:
                return None
            return func(self, desc)

        return wrapper

    @property
    @desc_check
    def x1(self, desc):
        return (- self.b - desc ** 0.5) / (2 * self.a)

    @property
    @desc_check
    def x2(self, desc):
        return (- self.b + desc ** 0.5) / (2 * self.a)


""" Упражнение 4
Для кодирования цвета часто используется шестнадцатеричное значение цвета. Оно записывается в формате #RRGGBB, где RR 
(красный), GG (зеленый) и BB (синий) являются шестнадцатеричными целыми числами в диапазоне [00; FF] (или [0; 255] 
в десятичной системе счисления), которые указывают интенсивность соответствующих цветов. Например, #0000FF представляет 
чистый синий цвет, так как синий компонент имеет наивысшее значение (FF), а остальные — 00.
Реализуйте класс Color, описывающий цвет. При создании экземпляра класс должен принимать один аргумент:
    hexcode — шестнадцатеричное значение цвета 
Экземпляр класса Color должен иметь три атрибута:
    r — интенсивность красного компонента цвета в виде десятичного числа
    g — интенсивность зеленого компонента цвета в виде десятичного числа
    b — интенсивность синего компонента цвета в виде десятичного числа  
Класс Color должен иметь одно свойство:
    hexcode — свойство, доступное для чтения и записи, возвращающее шестнадцатеричное значение цвета
Примечание 1. При изменении шестнадцатеричного значения цвета значения атрибутов r, g и b также должны изменяться.
Примечание 2. Гарантируется, что для записи шестнадцатеричных чисел используются только заглавные латинские буквы.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса Color нет, она может быть произвольной.
Sample Input 1:
    color = Color('0000FF')
    
    print(color.hexcode)
    print(color.r)
    print(color.g)
    print(color.b)
Sample Output 1:
    0000FF
    0
    0
    255
Sample Input 2:
    color = Color('0000FF')
    
    color.hexcode = 'A782E3'
    print(color.hexcode)
    print(color.r)
    print(color.g)
    print(color.b)
Sample Output 2:
    A782E3
    167
    130
    227
"""
class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return ''.join(hex(self.__dict__[x])[2:].ljust(2, '0') for x in 'rgb').upper()

    @hexcode.setter
    def hexcode(self, hexcode):
        self.r, self.g, self.b = (int(hexcode[0 + x * 2:2 + x * 2], 16) for x in range(3))
