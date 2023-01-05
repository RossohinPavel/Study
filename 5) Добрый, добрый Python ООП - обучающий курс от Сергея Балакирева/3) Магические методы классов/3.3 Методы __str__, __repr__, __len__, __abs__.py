""" Упражнение 1
Подвиг 2. Объявите класс с именем Book (книга), объекты которого создаются командой:
    book = Book(title, author, pages)
где title - название книги (строка); author - автор книги (строка); pages - число страниц в книге (целое число).
Также при выводе информации об объекте на экран командой:
    print(book)
должна отображаться строчка в формате:
    "Книга: {title}; {author}; {pages}"
Например:
    "Книга: Муму; Тургенев; 123"
Прочитайте из входного потока строки с информацией по книге командой:
    lst_in = list(map(str.strip, sys.stdin.readlines()))
(строки идут в порядке: title, author, pages). Создайте объект класса Book и выведите его строковое представление в консоль.
Sample Input:
    Python ООП
    Балакирев С.М.
    1024
Sample Output:
    Книга: Python ООП; Балакирев С.М.; 1024
"""
import sys


# здесь пишите программу
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка из входного потока (эту строчку не менять)

print(Book(*lst_in))


""" Упражнение 2
Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:
    model = Model()
Объявите в этом классе метод query() для формирования записи базы данных. Использоваться этот метод должен следующим образом:
    model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)
Например:
    model.query(id=1, fio='Sergey', old=33)
Все эти переданные данные должны сохраняться внутри объекта model класса Model. Затем, при выполнении команды:
    print(model)
В консоль должна выводиться информация об объекте в формате:
    "Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"
Например:
    "Model: id = 1, fio = Sergey, old = 33"
Если метод query() не вызывался, то в консоль выводится строка:
    "Model"
P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.
"""
class Model:
    def __init__(self):
        self.dct = {}

    def query(self, **kwargs):
        self.dct.update(kwargs)

    def __str__(self):
        string = "Model"
        if self.dct:
            string = string + ': ' + ', '.join([f'{k} = {v}' for k, v in self.dct.items()])
        return string


""" Упражнение 3
Подвиг 4. Объявите класс WordString, объекты которого создаются командами:
    w1 = WordString()
    w2 = WordString(string)
где string - передаваемая строка. Например:
    words = WordString("Курс по Python ООП")
Реализовать следующий функционал для объектов этого класса:
    len(words) - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
    words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).
Также в классе WordString реализовать объект-свойство (property):
    string - для передачи и считывания строки.
Пример пользования классом WordString (эти строчки в программе писать не нужно):
    words = WordString()
    words.string = "Курс по Python ООП"
    n = len(words)
    first = "" if n == 0 else words(0)
    print(words.string)
    print(f"Число слов: {n}; первое слово: {first}")
P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.
"""
class WordString:
    def __init__(self, string=None):
        self.__string = string
        self.__st_lst = [x for x in string.split()] if string else None

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        if type(value) == str:
            self.__string = value
            self.__st_lst = [x for x in value.split()]

    def __len__(self):
        if self.__st_lst is None:
            return 0
        return len(self.__st_lst)

    def __call__(self, indx, *args, **kwargs):
        if self.__st_lst is None:
            return -1
        return self.__st_lst[indx]


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6-xKuQp9b7Y
Теория по двусвязным спискам (при необходимости): https://youtu.be/0sTH9EwXT1I
Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:
Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:
    obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:
    __data - ссылка на строку с данными;
    __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
    __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).
В свою очередь, объекты класса LinkedList должны создаваться командой:
    linked_lst = LinkedList()
и содержать локальные атрибуты:
    head - ссылка на первый объект связного списка (если список пуст, то head = None);
    tail - ссылка на последний объект связного списка (если список пуст, то tail = None).
А сам класс содержать следующие методы:
    add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
    remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); 
индекс отсчитывается с нуля.
Также с объектами класса LinkedList должны поддерживаться следующие операции:
    len(linked_lst) - возвращает число объектов в связном списке;
    linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx 
(в связном списке).
Пример использования классов (эти строчки в программе писать не нужно):
    linked_lst = LinkedList()
    linked_lst.add_obj(ObjList("Sergey"))
    linked_lst.add_obj(ObjList("Balakirev"))
    linked_lst.add_obj(ObjList("Python"))
    linked_lst.remove_obj(2)
    linked_lst.add_obj(ObjList("Python ООП"))
    n = len(linked_lst)  # n = 3
    s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно. 
"""
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__lst = []

    def refresh(self):
        if self.__lst:
            self.head = self.__lst[0]
            self.tail = self.__lst[-1]
            for i in range(1, len(self.__lst)):
                self.__lst[i-1].next = self.__lst[i]
                self.__lst[i].prev = self.__lst[i-1]

    def add_obj(self, obj):
        self.__lst.append(obj)
        self.refresh()

    def remove_obj(self, indx):
        self.__lst.pop(indx)
        self.refresh()
        if not self.__lst:
            self.head = self.tail = None

    def __len__(self):
        return len(self.__lst)

    def __call__(self, indx):
        return self.__lst[indx].data


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/t8KuHjY71-o
Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами. Объекты этого класса должны 
создаваться командой:
    cm = Complex(real, img)
где real - действительная часть комплексного числа (целое или вещественное значение); img - мнимая часть комплексного 
числа (целое или вещественное значение).
Объявите в этом классе следующие объекты-свойства (property):
    real - для записи и считывания действительного значения;
    img - для записи и считывания мнимого значения.
При записи новых значений необходимо проверять тип передаваемых данных. Если тип не соответствует целому или 
вещественному числу, то генерировать исключение командой:
    raise ValueError("Неверный тип данных.")
Также с объектами класса Complex должна поддерживаться функция:
    res = abs(cm)
возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img) - корень квадратный от суммы 
квадратов действительной и мнимой частей комплексного числа).
Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8. Затем, через объекты-свойства 
real и img измените эти значения на real = 3 и img = 4. Вычислите модуль полученного комплексного числа 
(сохраните результат в переменной c_abs).
P.S. На экран ничего выводить не нужно.
"""
class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__img = value

    def __abs__(self):
        return (self.__real ** 2 + self.__img ** 2) ** 0.5


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)


""" Упражнение 6
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/lCYllyv9nVM
Подвиг 7. Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат). 
Объекты этого класса должны создаваться командами:
# создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
    vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0
# создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
    vector = RadiusVector(1, -5, 3.4, 10)
То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора. Если же передается 
более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.
Класс RadiusVector должен содержать методы:
    set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат радиус-вектора;
    get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).
Также с объектами класса RadiusVector должны поддерживаться следующие функции:
    len(vector) - возвращает число координат радиус-вектора (его размерность);
    abs(vector) - возвращает длину радиус-вектора (вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ... 
+ coord_N*coord_N) - корень квадратный из суммы квадратов координат).
Пример использования класса RadiusVector (эти строчки в программе писать не нужно):
    vector3D = RadiusVector(3)
    vector3D.set_coords(3, -5.6, 8)
    a, b, c = vector3D.get_coords()
    vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
    vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
    res_len = len(vector3D) # res_len = 3
    res_abs = abs(vector3D)
P.S. На экран ничего выводить не нужно, только объявить класс RadiusVector.
"""
class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.__lst = [0 for _ in range(args[0])]
        else:
            self.__lst = list(args)

    def set_coords(self, *args):
        for i in range(len(self.__lst)):
            if i >= len(args):
                break
            self.__lst[i] = args[i]

    def get_coords(self):
        return tuple(self.__lst)

    def __len__(self):
        return len(self.__lst)

    def __abs__(self):
        return sum(x ** 2 for x in self.__lst) ** 0.5


""" Упражнение 7
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/V7SV1pOWyEY
Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:
    dt = DeltaClock(clock1, clock2)
где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:
    clock = Clock(hours, minutes, seconds)
где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).
В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):
    get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
После создания объекта dt класса DeltaClock, с ним должны выполняться команды:
    str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
    len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
    print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
Если разность получается отрицательной, то разницу времен считать нулевой.
Пример использования классов (эти строчки в программе писать не нужно):
    dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
    print(dt) # 01: 30: 00
    len_dt = len(dt) # 5400
Обратите внимание, добавляется незначащий ноль, если число меньше 10.
P.S. На экран ничего выводить не нужно, только объявить классы.
"""
from datetime import timedelta


class Clock:
    def __init__(self, h, m, s):
        self.__time = timedelta(hours=h, minutes=m, seconds=s)

    def get_time(self):
        return self.__time.total_seconds()


class DeltaClock:
    def __init__(self, c1, c2):
        self.clock1 = c1
        self.clock2 = c2

    def __len__(self):
        if self.clock2.get_time() >= self.clock1.get_time():
            return 0
        return int(self.clock1.get_time() - self.clock2.get_time())

    def __str__(self):
        if self.clock2.get_time() >= self.clock1.get_time():
            return '00: 00: 00'
        res = int(self.clock1.get_time() - self.clock2.get_time())
        hour = str(res // 3600).rjust(2, "0")
        minute = str(res // 60 % 60).rjust(2, "0")
        second = str(res % 60).rjust(2, "0")
        return f'{hour}: {minute}: {second}'


""" Упражнение 8
Подвиг 9. Объявите класс Recipe для представления рецептов. Отдельные ингредиенты рецепта должны определяться классом 
Ingredient. Объекты этих классов должны создаваться командами:
    ing = Ingredient(name, volume, measure)
    recipe = Recipe()
    recipe = Recipe(ing_1, ing_2,..., ing_N)
где ing_1, ing_2,..., ing_N - объекты класса Ingredient.
В каждом объекте класса Ingredient должны создаваться локальные атрибуты:
    name - название ингредиента (строка);
    volume - объем ингредиента в рецепте (вещественное число);
    measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;
С объектами класса Ingredient должна работать функция:
    str(ing)  # название: объем, ед. изм.
и возвращать строковое представление объекта в формате:
    "название: объем, ед. изм."
Например:
    ing = Ingredient("Соль", 1, "столовая ложка")
    s = str(ing) # Соль: 1, столовая ложка
Класс Recipe должен иметь следующие методы:
    add_ingredient(ing) - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
    remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
    get_ingredients() - получение кортежа из объектов класса Ingredient текущего рецепта.
Также с объектами класса Recipe должна поддерживаться функция:
    len(recipe) - возвращает число ингредиентов в рецепте.
Пример использования классов (эти строчки в программе писать не нужно):
    recipe = Recipe()
    recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
    recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
    recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
    ings = recipe.get_ingredients()
    n = len(recipe) # n = 3
P.S. На экран ничего выводить не нужно, только объявить классы.
"""
class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        self.__lst = list(args)

    def add_ingredient(self, ing):
        self.__lst.append(ing)

    def remove_ingredient(self, ing):
        self.__lst.remove(ing)

    def get_ingredients(self):
        return tuple(self.__lst)

    def __len__(self):
        return len(self.__lst)


""" Упражнение 9
Подвиг 10 (на повторение). Объявите класс PolyLine (полилиния) для представления линии из последовательности 
прямолинейных сегментов. Объекты этого класса должны создаваться командой:
    poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3, ... - последующие 
координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.
Например:
    poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
В классе PolyLine должны быть объявлены следующие методы:
    add_coord(x, y) - добавление новой координаты (в конец);
    remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
    get_coords() - получение списка координат (в виде списка из кортежей).
P.S. На экран ничего выводить не нужно, только объявить класс.
"""
class PolyLine:
    def __init__(self, *args):
        self.__lst = list(args)

    def add_coord(self, x, y):
        self.__lst.append((x, y))

    def remove_coord(self, indx):
        self.__lst.pop(indx)

    def get_coords(self):
        return self.__lst
