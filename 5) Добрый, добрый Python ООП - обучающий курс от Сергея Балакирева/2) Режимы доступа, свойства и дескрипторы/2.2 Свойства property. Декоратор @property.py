""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PN3SjHz2ZG4
Подвиг 4. Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model для записи и считывания
информации о модели автомобиля из локальной приватной переменной __model.
Объект-свойство объявите с помощью декоратора @property. Также в объекте-свойстве model должны быть реализованы
проверки:
    - модель автомобиля - это строка;
    - длина строки модели должна быть в диапазоне [2; 100].
Если проверка не проходит, то локальное свойство __model остается без изменений.
Объекты класса Car предполагается создавать командой:
    car = Car()
и далее работа с объектом-свойством, например:
    car.model = "Toyota"
P.S. В программе объявить только класс. На экран ничего выводить не нужно.
"""
class Car:
    def __init__(self):
        self.__model = ''

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, car_model):
        if type(car_model) == str and 2 <= len(car_model) <= 100:
            self.__model = car_model


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/P0sI_Eb_i0c
Подвиг 5. Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:
    wnd = WindowDlg(заголовок окна, ширина, высота)
В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:
    __title - заголовок окна (строка);
    __width, __height - ширина и высота окна (числа).
В классе WindowDlg необходимо реализовать метод:
    show() - для отображения окна на экране (выводит в консоль строку в формате: "<Заголовок>: <ширина>, <высота>", 
например "Диалог 1: 100, 50").
Также в классе WindowDlg необходимо реализовать два объекта-свойства:
    width - для изменения и считывания ширины окна;
    height - для изменения и считывания высоты окна.
При изменении размеров окна необходимо выполнять проверку:
    - переданное значение является целым числом в диапазоне [0; 10000].
Если хотя бы один размер изменился (высота или ширина), то следует выполнить автоматическую перерисовку окна (вызвать 
метод show()). При начальной инициализации размеров width, height вызывать метод show() не нужно.
P.S. В программе нужно объявить только класс с требуемой функциональностью.
"""
class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 10000:
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 10000:
            self.__height = value
            self.show()


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/mg4b8nhVDKY
Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов), 
когда один объект ссылается на следующий и так по цепочке до последнего:
Для этого объявите в программе два класса: 
    StackObj - для описания объектов односвязного списка;
    Stack - для управления односвязным списком.
Объекты класса StackObj предполагается создавать командой:
    obj = StackObj(данные)
Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные 
приватные атрибуты:
    __data - ссылка на строку с данными, указанными при создании объекта;
    __next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).
Также в классе StackObj должны быть объявлены объекты-свойства:
    next - для записи и считывания информации из локального приватного свойства __next;
    data - для записи и считывания информации из локального приватного свойства __data.
При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None. 
Если проверка не проходит, то __next остается без изменений.
Класс Stack предполагается использовать следующим образом:
    st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:
    top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).
А в самом классе Stack следующие методы:
    push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
    pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
    get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого 
объекта в порядке их добавления, или пустой список, если объектов нет).
Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    st.pop()
    res = st.get_data()    # ['obj1', 'obj2']
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 
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

    def push(self, obj):
        """добавление объекта класса StackObj в конец односвязного списка"""
        def func(last_obj):
            if last_obj.next is None:
                return last_obj
            return func(last_obj.next)

        if self.top is None:
            self.top = obj
        else:
            func(self.top).next = obj

    def pop(self):
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


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/q_8BdpVWbyE
Подвиг 7. Объявите класс RadiusVector2D, объекты которого должны создаваться командами:
    v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
    v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
    v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:
    __x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).
В классе RadiusVector2D необходимо объявить два объекта-свойства:
    x - для изменения и считывания локального атрибута __x;
    y - для изменения и считывания локального атрибута __y.
При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
- значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0). 
Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.
Также в классе RadiusVector2D необходимо объявить статический метод:
norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D 
(квадратическая норма вектора: x*x + y*y).
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""
class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def check_value(self, value):
        return type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD

    def __init__(self, x=0, y=0):
        self.__x = x if self.check_value(x) else 0
        self.__y = y if self.check_value(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.check_value(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.check_value(value):
            self.__x = value

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


""" Упражнение 5 
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/5Y9qT5grunw
Большой подвиг 8. Требуется реализовать программу по работе с решающими деревьями:
Здесь в каждом узле дерева делается проверка (задается вопрос). Если проверка проходит, то осуществляется переход к 
следующему объекту по левой стрелке (с единицей), а иначе - по правой стрелке (с нулем). И так до тех пор, пока не 
дойдем до одного из листа дерева (вершины без потомков).
В качестве входных данных используется вектор (список) с бинарными значениями: 1 - да, 0 - нет. Каждый элемент этого 
списка соответствует своему вопросу (своей вершине дерева), например:
Далее, этот вектор применяется к решающему дереву, следующим образом. Корневая вершина "Любит Python" с ней связан 
первый элемент вектора x и содержит значение 1, следовательно, мы переходим по левой ветви. Попадаем в вершину "Понимает 
ООП". С ней связан второй элемент вектора x со значением 0, следовательно, мы переходим по правой ветви и попадаем 
в вершину "будет кодером". Так как эта вершина конечная (листовая), то получаем результат в виде строки "будет кодером". 
По аналогии выполняется обработка вектора x с другими наборами значений 0 и 1.
Для реализации решающих деревьев в программе следует объявить два класса:
    TreeObj - для описания вершин и листьев решающего дерева;
    DecisionTree - для работы с решающим деревом в целом.
В классе DecisionTree должны быть реализованы (по крайне мере) два метода уровня класса (@classmethod):
    def predict(cls, root, x) - для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла 
дерева root.
    def add_obj(cls, obj, node=None, left=True) - для добавления вершин в решающее дерево (метод должен возвращать 
добавленную вершину - объект класса TreeObj);
В методе add_obj параметры имеют, следующие значения:
    obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
    node - ссылка на объект дерева, к которому присоединяется вершина obj;
    left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj (True - к левой ветви; 
False - к правой).
В классе TreeObj следует объявить инициализатор:
    def __init__(self, indx, value=None): ...
где indx - проверяемый в вершине дерева индекс вектора x; value - значение, хранящееся в вершине (принимает значение 
None для вершин, у которых есть потомки - промежуточных вершин).
При этом, в каждом создаваемом объекте класса TreeObj должны автоматически появляться следующие локальные атрибуты:
    indx - проверяемый индекс (целое число);
    value - значение с данными (строка);
    __left - ссылка на следующий объект дерева по левой ветви (изначально None);
    __right - ссылка на следующий объект дерева по правой ветви (изначально None).
Для работы с локальными приватными атрибутами __left и __right необходимо объявить объекты-свойства с именами left и right.
Эти классы в дальнейшем предполагается использовать следующим образом (эти строчки в программе не писать):
    root = DecisionTree.add_obj(TreeObj(0))
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
    DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
    x = [1, 1, 0]
    res = DecisionTree.predict(root, x) # будет программистом
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 
"""
class TreeObj:
    """для описания вершин и листьев решающего дерева"""
    def __init__(self, indx, value=None):
        self.indx = indx    # проверяемый индекс(целое число);
        self.value = value    # значение с данными(строка);
        self.__left = None    # ссылка на следующий объект дерева по левой ветви (изначально None);
        self.__right = None    # ссылка на следующий объект дерева по правой ветви (изначально None).

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:
    """для работы с решающим деревом в целом"""

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """
        для добавления вершин в решающее дерево(метод должен возвращать добавленную вершину - объект TreeObj)
        :param obj: ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj)
        :param node: ссылка на объект дерева, к которому присоединяется вершина obj
        :param left: флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj
        (True - к левой ветви; False - к правой)
        :return: Объект TreeObj
        """
        if node is not None:
            if left is True:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root, x):
        """для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root"""
        curr = root
        c_v = curr.value
        while curr.value is None:
            if x[curr.indx] == 1:
                curr = curr.left
            else:
                curr = curr.right
            c_v = curr.value
        return c_v


""" Упражнение 6
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/EAt0fgLNYGg
Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных 
сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса 
будут формироваться командой:
    line = LineTo(x, y)
    где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).
В каждом объекте класса LineTo должны формироваться локальные атрибуты:
    x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).
Объекты класса PathLines должны создаваться командами:
    p = PathLines()                   # начало маршрута из точки 0, 0
    p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
где line1, line2, ... - объекты класса LineTo.
Сам же класс PathLines должен иметь следующие методы:
    get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
    get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
    add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется 
как евклидовое расстояние по формуле:
    L = sqrt((x1-x0)^2 + (y1-y0)^2)
где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.
Пример использования классов (эти строчки в программе писать не нужно):
    p = PathLines(LineTo(10, 20), LineTo(10, 30))
    p.add_line(LineTo(20, -10))
    dist = p.get_length()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 
"""
class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y


class PathLines:
    def __init__(self, *args):
        self.__lst = list(args)

    def get_path(self):
        return self.__lst

    def add_line(self, line):
        self.__lst.append(line)

    def get_length(self):
        length = 0
        for i in range(len(self.__lst)):
            x1, y1 = self.__lst[i].get()
            x0, y0 = 0, 0
            if i != 0:
                x0, y0 = self.__lst[i-1].get()
            length += ((x1-x0)**2 + (y1-y0)**2)**0.5
        return length


""" Упражнение 7
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/TMPPmryMKD0
Подвиг 10 (на закрепление). Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого 
класса создаются командой:
    p = PhoneBook()
А сам класс должен иметь следующий набор методов:
    add_phone(phone) - добавление нового номера телефона (в список);
    remove_phone(indx) - удаление номера телефона по индексу списка;
    get_phone_list() - получение списка из объектов всех телефонных номеров.
Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:
    note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера 
(строка).
В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
    number - номер телефона (число);
    fio - ФИО владельца номера телефона.
Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.
Пример использования классов (эти строчки в программе писать не нужно):
    p = PhoneBook()
    p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
    p.add_phone(PhoneNumber(21345678901, "Панда"))
    phones = p.get_phone_list()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 
"""
class PhoneBook:
    def __init__(self):
        self.__lst = []

    def add_phone(self, phone):
        self.__lst.append(phone)

    def remove_phone(self, indx):
        self.__lst.pop(indx)

    def get_phone_list(self):
        return self.__lst


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio
