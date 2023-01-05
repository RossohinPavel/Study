""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/fiYiJWXv-5I
Подвиг 2. Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться
командой:
    rnd = RandomPassword(psw_chars, min_length, max_length)
где psw_chars - строка из разрешенных в пароле символов; min_length, max_length - минимальная и максимальная длина
генерируемых паролей.
Непосредственная генерация одного пароля должна выполняться командой:
psw = rnd()
где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из случайно выбранных символов строки psw_chars.
С помощью генератора списка (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом rnd
класса RandomPassword, созданного с параметрами:
    min_length = 5
    max_length = 20
    psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
P.S. Выводить на экран ничего не нужно, только создать список из паролей.
P.P.S. Дополнительное домашнее задание: попробуйте реализовать этот же функционал с использованием замыканий функций.
"""
from random import randint  # функция для генерации целых случайных значений в диапазоне [a; b]


# здесь объявляйте класс RandomPassword
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self):
        return ''.join(
            self.psw_chars[randint(0, len(self.psw_chars) - 1)] for _ in range(randint(self.min_length, self.max_length)))


mn_length = 5
mx_length = 20
chars = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%"
rnd = RandomPassword(chars, mn_length, mx_length)

lst_pass = [rnd() for _ in range(3)]


# Closure realization
from random import randint  # функция для генерации целых случайных значений в диапазоне [a; b]


def pass_gen(chars, mn, mx):
    def inner():
        return ''.join(chars[randint(0, len(chars)-1)] for _ in range(randint(mn, mx)))
    return inner

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&"

psw = pass_gen(psw_chars, min_length, max_length)

print(*[psw() for _ in range(3)])


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/JIQhCEqb4rU
Подвиг 3. Для последовательной обработки файлов из некоторого списка, например:
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", 
    "my.html", "data.shtml"]
Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с указанными расширениями.
Для этого предполагается создавать объекты класса командой:
    acceptor = ImageFileAcceptor(extensions)
где extensions - кортеж с допустимыми расширениями файлов, например: extensions = ('jpg', 'bmp', 'jpeg').
А, затем, использовать объект acceptor в стандартной функции filter языка Python следующим образом:
    image_filenames = filter(acceptor, filenames)
Пример использования класса (эти строчки в программе писать не нужно):
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
    acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
    image_filenames = filter(acceptor, filenames)
    print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
P.S. Ваша задача только объявить класс ImageFileAcceptor. На экран ничего выводить не нужно. 
"""
class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename):
        return filename.split('.')[-1] in self.extensions


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/e1U6SoX1ChI
Подвиг 4. Предположим, мы разрабатываем класс для обработки формы авторизации на стороне сервера. Для этого был создан 
следующий класс с именем LoginForm:
class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
        
    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")
        
    def is_validate(self):
        if not self.validators:
            return True
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
            
        return True
Здесь name - это заголовок формы (строка); validators - список из валидаторов для проверки корректности поля. В методе 
post параметр request - это словарь с ключами 'login' и 'password' и значениями (строками) для логина и пароля 
соответственно.
Пример использования класса LoginForm (в программе не писать):
    from string import ascii_lowercase, digits
    
    lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
    lg.post({"login": "root", "password": "panda"})
    if lg.is_validate():
        print("Дальнейшая обработка данных формы")
Вам необходимо в программе объявить классы валидаторов:
    LengthValidator - для проверки длины данных в диапазоне [min_length; max_length];
    CharsValidator - для проверки допустимых символов в строке.
Объекты этих классов должны создаваться командами:
    lv = LengthValidator(min_length, max_length) # min_length - минимально допустимая длина; max_length - максимально 
допустимая длина
    cv = CharsValidator(chars) # chars - строка из допустимых символов
Для проверки корректности данных каждый валидатор должен вызываться как функция:
    res = lv(string)
    res = cv(string)
и возвращать True, если string удовлетворяет условиям валидатора и False - в противном случае.
P.S. В программе следует только объявить два класса валидаторов, на экран выводить ничего не нужно.
"""
# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string):
        return self.min_length <= len(string) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return all(True if x in self.chars else False for x in string)


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YYUPa-0IeQU
Подвиг 5. Объявите класс DigitRetrieve для преобразования данных из строки в числа. Объекты этого класса создаются 
командой:
    dg = DigitRetrieve()
Затем, их предполагается использовать, например следующим образом:
    d1 = dg("123")   # 123 (целое число)
    d2 = dg("45.54")   # None (не целое число)
    d3 = dg("-56")   # -56 (целое число)
    d4 = dg("12fg")  # None (не целое число)
    d5 = dg("abc")   # None (не целое число)
То есть, целые числа в строке следует приводить к целочисленному типу данных, а все остальные - к значению None.
С помощью объектов класса DigitRetrieve должно выполняться преобразование чисел из списка строк следующим образом:
    st = ["123", "abc", "-56.4", "0", "-5"]
    digits = list(map(dg, st))  # [123, None, None, 0, -5]
P.S. На экран ничего выводить не нужно. 
"""
import re


class DigitRetrieve:
    def __call__(self, string):
        return int(string) if re.fullmatch(r'-?\d+', string) else None


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wp4CyhdXcbY
Подвиг 6. Предположим, вам необходимо создать программу по преобразованию списка строк, например:
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить не нужно):
    '''<ul>
    <li>Пункт меню 1</li>
    <li>Пункт меню 2</li>
    <li>Пункт меню 3</li>
    </ul>'''
Для этого необходимо объявить класс RenderList, объекты которого создаются командой:
render = RenderList(type_list)
где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>). 
Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.
Затем, предполагается использовать объект render следующим образом:
h   tml = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
Пример использования класса (эти строчки в программе писать не нужно):
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
    render = RenderList("ol")
    html = render(lst)
P.S. На экран ничего выводить не нужно. 
"""
class RenderList:
    def __init__(self, type_list):
        self.t_l = type_list if type_list in ('ul', 'ol') else 'ul'

    def __call__(self, lst):
        return f'<{self.t_l}>\n<li>' + '</li>\n<li>'.join(lst) + f'</li>\n</{self.t_l}>'


""" Упражнение 6
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Ac0s64-XEdE
Подвиг 7. Необходимо объявить класс-декоратор с именем HandlerGET, который будет имитировать обработку GET-запросов на 
стороне сервера. Для этого сам класс HandlerGET нужно оформить так, чтобы его можно было применять к любой функции как 
декоратор. Например:
    @HandlerGET
    def contact(request):
        return "Сергей Балакирев"
Здесь request - это произвольный словарь с данными текущего запроса, например, такой: {"method": "GET", "url": 
"contact.html"}. А функция должна возвращать строку.
Затем, при вызове декорированной функции:
    res = contact({"method": "GET", "url": "contact.html"})
должна возвращаться строка в формате:
    "GET: <данные из функции>"
В нашем примере - это будет:
    "GET: Сергей Балакирев"
Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если же ключ method 
принимает другое значение, например, "POST", то декорированная функция contact должна возвращать значение None.
Для реализации имитации GET-запроса в классе HandlerGET следует объявить вспомогательный метод со следующей сигнатурой:
    def get(self, func, request, *args, **kwargs): ...
Здесь func - ссылка на декорируемую функцию; request - словарь с переданными данными при вызове декорированной функции. 
Именно в этом методе следует формировать возвращаемую строку в указанном формате:
    "GET: Сергей Балакирев"
P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.
"""
# Зачем эта "вспомогательная" функция get не понятно.
class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        return self.get(self.func, request)

    def get(self, func, request, *args, **kwargs):
        if request.get('method') in ("GET", None):
            return f'GET: {func(request)}'


""" Упражнение 7
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/FyL9RyFGGCo
Подвиг 8 (развитие подвига 7). Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к 
функциям следующим образом:
    @Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
    def contact(request):
        return "Сергей Балакирев"
Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки. Сама декорированная 
функция вызывается по аналогии с предыдущим подвигом:
    res = contact({"method": "POST", "url": "contact.html"})
В результате функция contact должна возвращать строку в формате:
"<метод>: <данные из функции>"
В нашем примере - это будет:
"POST: Сергей Балакирев"
Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если ключ method принимает 
значение отсутствующее в списке methods декоратора Handler, например, "PUT", то декорированная функция contact должна 
возвращать значение None.
Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:
    def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
    def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса
В зависимости от типа запроса должен вызываться соответствующий метод (его выбор в классе можно реализовать методом 
__getattribute__()). На выходе эти методы должны формировать строки в заданном формате.
P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.
Небольшая справка
Для реализации декоратора с параметрами на уровне класса в инициализаторе __init__(self, methods) прописываем параметр 
для декоратора, а магический метод __call__() объявляем как полноценный декоратор на уровне функции, например:
    
    class Handler:
        def __init__(self, methods):
            # здесь нужные строчки
    
        def __call__(self, func):
            def wrapper(request, *args, **kwargs):
                # здесь нужные строчки
            return wrapper
"""
class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            r_g = request.get('method')
            if r_g is None:
                return f'GET: {func(request)}'
            if r_g in self.methods:
                return f'{r_g}: {func(request)}'

        return wrapper

    def get(self, func, request, *args, **kwargs):
        pass

    def post(self, func, request, *args, **kwargs):
        pass


""" Упражнение 8
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/EEzEodYvoXc
Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе строки 
из целых чисел, записанных через пробел, например:
    "12 -5 10 83"
на выходе возвращался список из целых чисел:
    [12, -5, 10, 83]
Назовите декорированную функцию input_dg и вызовите ее командой:
res = input_dg()
P.S. На экран ничего выводить не нужно.
"""
class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return list(map(int, self.func().split()))


input_dg = InputDigits(input)
res = input_dg()


""" Упражнение 9
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/H4cJ0fBVHpc
Подвиг 10 (развитие подвига 9). Объявите класс-декоратор InputValues с параметром render - функция или объект для 
преобразования данных из строк в другой тип данных. Чтобы реализовать такой декоратор в инициализаторе __init__() 
следует указать параметр render, а магический метод __call__() определяется как функция-декоратор:
    class InputValues:
        def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
            # здесь строчки программы
    
        def __call__(self, func):     # func - ссылка на декорируемую функцию
            def wrapper(*args, **kwargs):
                # здесь строчки программы
            return wrapper
В качестве рендера объявите класс с именем RenderDigit, который бы преобразовывал строковые данные в целые числа. 
Объекты этого класса создаются командой:
    render = RenderDigit()
и применяются следующим образом:
    d1 = render("123")   # 123 (целое число)
    d2 = render("45.54")   # None (не целое число)
    d3 = render("-56")   # -56 (целое число)
    d4 = render("12fg")  # None (не целое число)
    d5 = render("abc")   # None (не целое число)
Декорируйте стандартную функцию input декоратором InputValues и объектом рендера класса RenderDigit так, чтобы на 
выходе при вводе целых чисел через пробел возвращался список из введенных значений. А на месте не целочисленных 
данных - значение None.
Например, при вводе строки:
    "1 -5.3 0.34 abc 45f -5"
должен возвращаться список:
    [1, None, None, None, None, -5]
Назовите декорированную функцию input_dg и вызовите ее командой:
    res = input_dg()
Выведите результат res на экран.
"""
import re


class RenderDigit:
    def __call__(self, string):
        return int(string) if re.fullmatch(r'-?\d+', string) else None


class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.render, func().split()))

        return wrapper


input_dg = InputValues(RenderDigit())
res = input_dg(input)
print(res())
