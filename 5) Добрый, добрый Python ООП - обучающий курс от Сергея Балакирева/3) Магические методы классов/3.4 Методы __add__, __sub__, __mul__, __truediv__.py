""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/tkjqkiCSnqM
Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:
    lst = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это
показано в примере:
    lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен
сохраняться)
Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого
создаются командами:
    lst = NewList() # пустой список
    lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять
следующие действия:
    lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
    lst2 = NewList([0, 1, 2, 3, True])
    res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
    lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
    res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
    res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
    a = NewList([2, 3])
    res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:
get_list() - для возвращения результирующего списка объекта класса NewList
Например:
    lst = res_2.get_list() # [1, 2, 3]
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.
"""
class NewList:
    def __init__(self, lst=None):
        self.__lst = lst if lst else []

    def get_list(self):
        return self.__lst

    @staticmethod
    def func(left, right):
        dct = {list: lambda x: [(type(y), y) for y in x], NewList: lambda x: [(type(y), y) for y in x.get_list()]}
        left = dct[type(left)](left)
        right = dct[type(right)](right)
        for i in right:
            if i in left:
                left.remove(i)
        return NewList([x[-1] for x in left])

    def __rsub__(self, other):
        return self.func(other, self)

    def __sub__(self, other):
        return self.func(self, other)


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0Poea079PSs
Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:
    lst1 = ListMath() # пустой список
    lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа, 
остальные игнорировать (если указываются в списке). Например:
    lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть публичный атрибут:
lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).
Также с объектами класса ListMath должны работать следующие операторы:
    lst = lst + 76 # сложение каждого числа списка с определенным числом
    lst = 6.5 + lst # сложение каждого числа списка с определенным числом
    lst += 76.7  # сложение каждого числа списка с определенным числом
    lst = lst - 76 # вычитание из каждого числа списка определенного числа
    lst = 7.0 - lst # вычитание из числа каждого числа списка
    lst -= 76.3
    lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
    lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
    lst *= 5.54
    lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
    lst = 3 / lst # деление числа на каждый элемент списка
    lst /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками, 
прежние списки не меняются.
При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта (новый объект не создается).
P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.
"""
class ListMath:
    def __init__(self, lst_math=None):
        self.lst_math = [x for x in lst_math if type(x) in (int, float)] if lst_math else []

    @staticmethod
    def __func(left, right, operand):
        if operand == '+':
            return [x + right for x in left.lst_math]
        if operand == 'l-':
            return [x - right for x in left.lst_math]
        if operand == 'r-':
            return [right - x for x in left.lst_math]
        if operand == '*':
            return [x*right for x in left.lst_math]
        if operand == 'l/':
            return [x / right for x in left.lst_math]
        if operand == 'r/':
            return [right/x for x in left.lst_math]

    def __add__(self, other):
        return ListMath(self.__func(self, other, '+'))

    def __radd__(self, other):
        return ListMath(self.__func(self, other, '+'))

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.lst_math = [x+other for x in self.lst_math]
        return self

    def __sub__(self, other):
        return ListMath(self.__func(self, other, 'l-'))

    def __rsub__(self, other):
        return ListMath(self.__func(self, other, 'r-'))

    def __isub__(self, other):
        if type(other) in (int, float):
            self.lst_math = [x-other for x in self.lst_math]
        return self

    def __mul__(self, other):
        return ListMath(self.__func(self, other, '*'))

    def __rmul__(self, other):
        return ListMath(self.__func(self, other, '*'))

    def __imul__(self, other):
        if type(other) in (int, float):
            self.lst_math = [x*other for x in self.lst_math]
        return self

    def __truediv__(self, other):
        return ListMath(self.__func(self, other, 'l/'))

    def __rtruediv__(self, other):
        return ListMath(self.__func(self, other, 'r/'))

    def __itruediv__(self, other):
        if type(other) in (int, float):
            self.lst_math = [x/other for x in self.lst_math]
        return self


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PY-E4OSh1gM
Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один 
объект ссылается на следующий и так далее):
Давайте снова создадим такую структуру данных. Для этого объявим два класса:
    Stack - для управления односвязным списком в целом;
    StackObj - для представления отдельных объектов в односвязным списком.
Объекты класса StackObj должны создаваться командой:
    obj = StackObj(data)
    где data - строка с некоторыми данными.
Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
    __data - ссылка на строку с переданными данными;
    __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).
Объекты класса Stack создаются командой:
    st = Stack()
и каждый из них должен содержать локальный атрибут:
    top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).
Также в классе Stack следует объявить следующие методы:
    push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
    pop_back(self) - удаление последнего объекта из односвязного списка.
Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):
# добавление нового объекта класса StackObj в конец односвязного списка st
    st = st + obj 
    st += obj
# добавление нескольких объектов в конец односвязного списка
    st = st * ['data_1', 'data_2', ..., 'data_N']
    st *= ['data_1', 'data_2', ..., 'data_N']
В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка 
(каждый элемент списка для очередного добавляемого объекта).
P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.
"""
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if value is None or type(value) == StackObj:
            self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        """добавление объекта класса StackObj в конец односвязного списка"""
        def func(last_obj):
            if last_obj.next is None:
                return last_obj
            return func(last_obj.next)

        if self.top is None:
            self.top = obj
        else:
            func(self.top).next = obj

    def pop_back(self):
        """извлечение последнего объекта с его удалением из односвязного списка"""
        def func(last_obj):
            if last_obj.next.next is None:
                obj = last_obj.next
                last_obj.next = None
                return obj
            return func(last_obj.next)

        if self.top is None:
            return None
        if self.top.next is None:
            obj = self.top
            self.top = None
            return obj
        return func(self.top)

    def get_data(self):
        """получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого
        объекта в порядке их добавления, или пустой список, если объектов нет)
        """
        def func(last_obj):
            lst.append(last_obj.data)
            if last_obj.next is None:
                return
            func(last_obj.next)

        lst = []
        if self.top is not None:
            func(self.top)

        return lst

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in other:
            self.push_back(StackObj(i))
        return self


""" Упражнение 4
Подвиг 7. Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:
    Lib - для представления библиотеки в целом;
    Book - для описания отдельной книги.
Объекты класса Book должны создаваться командой:
    book = Book(title, author, year)
где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).
Объекты класса Lib создаются командой:
    lib = Lib()
Каждый объект должен содержать локальный публичный атрибут:
    book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.
Также объекты класса Lib должны работать со следующими операторами:
lib = lib + book # добавление новой книги в библиотеку
lib += book
lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book
lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx
При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.
Также с объектами класса Lib должна работать функция:
    n = len(lib) # n - число книг
которая возвращает число книг в библиотеке.
P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.
"""
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == int:
            self.book_list.pop(other)
        if type(other) == Book:
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        return self - other

    def __len__(self):
        return len(self.book_list)


""" Упражнение 5
Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите два 
класса с именами:
    Budget - для управления семейным бюджетом;
    Item - пункт расходов бюджета.
Объекты класса Item должны создаваться командой:
    it = Item(name, money)
где name - название статьи расхода; money - сумма расходов (вещественное или целое число).
Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с переданными 
значениями. Также с объектами класса Item должны выполняться следующие операторы:
    s = it1 + it2 # сумма для двух статей расходов
и в общем случае:
    s = it1 + it2 + ... + itN # сумма N статей расходов
При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих объектов 
класса Item.
Объекты класса Budget создаются командой:
    my_budget = Budget()
А сам класс Budget должен иметь следующие методы:
    add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
    remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
    get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).
Пример использования классов (эти строчки в программе писать не нужно):
    my_budget = Budget()
    my_budget.add_item(Item("Курс по Python ООП", 2000))
    my_budget.add_item(Item("Курс по Django", 5000.01))
    my_budget.add_item(Item("Курс по NumPy", 0))
    my_budget.add_item(Item("Курс по C++", 1500.10))
# вычисление общих расходов
    s = 0
    for x in my_budget.get_items():
        s = s + x
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.
"""
class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other.money

    def __radd__(self, other):
        return self.money + other


class Budget:
    def __init__(self):
        self.__lst = []

    def add_item(self, it):
        self.__lst.append(it)

    def remove_item(self, indx):
        self.__lst.pop(indx)

    def get_items(self):
        return self.__lst


""" Упражнение 6
Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска), объекты которого создаются 
командой:
    box = Box3D(width, height, depth)
где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)
В каждом объекте класса Box3D должны создаваться публичные атрибуты:
    width, height, depth - ширина, высота и глубина соответственно.
С объектами класса Box3D должны выполняться следующие операторы:
box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.
P.S. В программе достаточно только объявить класс Box3D. На экран ничего выводить не нужно.
"""
class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get(self):
        return self.width, self.height, self.depth

    def __add__(self, other):
        cur = self.get()
        other = other.get()
        return Box3D(*(cur[i] + other[i] for i in range(3)))

    def __sub__(self, other):
        cur = self.get()
        other = other.get()
        return Box3D(*(cur[i] - other[i] for i in range(3)))

    def __mul__(self, other):
        return Box3D(*(i*other for i in self.get()))

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        return Box3D(*(i // other for i in self.get()))

    def __mod__(self, other):
        return Box3D(*(i % other for i in self.get()))


""" Упражнение 7
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9wNoWmEHdfo
Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в 
сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора 
наибольшего значения в пределах этого окна:
Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):
Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого 
создаются командой:
    mp = MaxPooling(step=(2, 2), size=(2,2))
где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.
Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).
Для выполнения операции Max Pooling используется команда:
    res = mp(matrix)
где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая 
таблица чисел.
Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за 
ее пределы, то эти данные отбрасывать (не учитывать все окно).
Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться 
исключение командой:
    raise ValueError("Неверный формат для первого параметра matrix.")
Пример использования класса (эти строчки в программе писать не нужно):
    mp = MaxPooling(step=(2, 2), size=(2,2))
    res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
Результатом будет таблица чисел:
6 8
9 7
P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно.
"""
class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    @staticmethod
    def __is_matrix(matrix):
        flag = True
        for i in matrix:
            if len(i) != len(matrix):
                flag = False
            for j in i:
                if type(j) not in (int, float):
                    flag = False
            if flag is False:
                break
        return flag

    def calc(self, matrix):
        lst = []
        for i in range(0, len(matrix), self.step[-1]):
            sub_lst = []
            for j in range(0, len(matrix), self.step[0]):
                if i + self.size[-1] <= len(matrix) and j + self.size[0] <= len(matrix):
                    sub_sub_lst = []
                    for x in range(0+i, i+self.size[-1]):
                        for y in range(0+j, j+self.size[0]):
                            sub_sub_lst.append(matrix[x][y])
                    sub_lst.append(max(sub_sub_lst))
            if sub_lst:
                lst.append(sub_lst)
        return lst

    def __call__(self, matrix, *args, **kwargs):
        if not self.__is_matrix(matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")
        return self.calc(matrix)
