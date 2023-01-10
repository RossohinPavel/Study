""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/-ZvYUtWMUFw
Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:
    p = Person(fio, job, old, salary, year_job)
где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); salary -
зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).
В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old,
salary, year_job и соответствующими значениями.
Также с объектами класса Person должны поддерживаться следующие команды:
    data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job
и начинается с нуля)
    p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
    for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
        print(v)
При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. Иначе,
генерировать исключение командой:
    raise IndexError('неверный индекс')
Пример использования класса (эти строчки в программе не писать):
    pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
    pers[0] = 'Балакирев С.М.'
    for v in pers:
        print(v)
    pers[5] = 123 # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        if not 0 <= item <= 4:
            raise IndexError('неверный индекс')
        return self.__dict__[list(self.__dict__.keys())[item]]

    def __setitem__(self, key, value):
        if not 0 <= key <= 4:
            raise IndexError('неверный индекс')
        self.__dict__[list(self.__dict__.keys())[key]] = value


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wfy7UyTSN_Y
Подвиг 6. Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных) списков 
следующей структуры:
    lst = [[x00],
           [x10, x11],
           [x20, x21, x22],
           [x30, x31, x32, x33],
           ...
          ]
Для этого необходимо в программе объявить класс с именем TriangleListIterator, объекты которого создаются командой:
    it = TriangleListIterator(lst)
где lst - ссылка на перебираемый список.
Затем, с объектами класса TriangleListIterator должны быть доступны следующие операции:
    for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
        print(x)
    
    it_iter = iter(it)
    x = next(it_iter)
Итератор должен перебирать элементы списка по указанной треугольной форме. Даже если итератору на вход будет передан 
прямоугольная таблица (вложенный список), то ее перебор все равно должен осуществляться по треугольнику. Если же это 
невозможно (из-за структуры списка), то естественным образом должна возникать ошибка IndexError: index out of range 
(выход индекса за допустимый диапазон).
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""
class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
        self.j = 0

    def __iter__(self):
        self.i = 0
        self.j = 0
        return self

    def __next__(self):
        if self.i == len(self.lst) or self.j >= len(self.lst[self.i]):
            raise StopIteration
        res = self.lst[self.i][self.j]
        self.j += 1
        if self.j > self.i:
            self.i += 1
            self.j = 0
        return res


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kxCAnaAqdOk
Подвиг 7. Теперь, вам необходимо разработать итератор, который бы перебирал указанные столбцы двумерного списка. Список 
представляет собой двумерную таблицу из данных:
    lst = [[x11, x12, ..., x1N],
           [x21, x22, ..., x2N],
           ...
           [xM1, xM2, ..., xMN]
          ]
Для этого в программе необходимо объявить класс с именем IterColumn, объекты которого создаются командой:
    it = IterColumn(lst, column)
где lst - ссылка на двумерный список; column - индекс перебираемого столбца (отсчитывается от 0).
Затем, с объектами класса IterColumn должны быть доступны следующие операции:
    it = IterColumn(lst, 1)
    for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
        print(x)
    
    it_iter = iter(it)
    x = next(it_iter)
P.S. В программе нужно объявить только класс итератора. Выводить на экран ничего не нужно.
"""
class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.i = 0
        self.column = column

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i == len(self.lst):
            raise StopIteration
        res = self.lst[self.i][self.column]
        self.i += 1
        return res


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/WrZ1TMwuvis
Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:
Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:
    Stack - для представления стека в целом;
    StackObj - для представления отдельных объектов стека.
В классе Stack должны быть методы:
    push_back(obj) - для добавления нового объекта obj в конец стека;
    push_front(obj) - для добавления нового объекта obj в начало стека.
В каждом объекте класса Stack должен быть публичный атрибут:
    top - ссылка на первый объект стека (при пустом стеке top = None).
Объекты класса StackObj создаются командой:
    obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).
Также в каждом объекте класса StackObj должны быть публичные атрибуты:
    data - ссылка на данные объекта;
    next - ссылка на следующий объект стека (если его нет, то next = None).
Наконец, с объектами класса Stack должны выполняться следующие команды:
    st = Stack()
    
    st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
    data = st[indx]  # получение данных из объекта стека по индексу
    n = len(st) # получение общего числа объектов стека
    
    for obj in st: # перебор объектов стека (с начала и до конца)
        print(obj.data)  # отображение данных в консоль
При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число 
объектов в стеке. Иначе, генерировать исключение командой:
    raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def __len__(self):
        indx = 0
        if self.top is None:
            return indx
        obj = self.top
        indx += 1
        while obj.next is not None:
            obj = obj.next
            indx += 1
        return indx

    def push_back(self, obj):
        """для добавления нового объекта obj в конец стека;"""
        if self.top is None:
            self.top = obj
        else:
            prev = self.top
            while prev.next is not None:
                prev = prev.next
            prev.next = obj

    def push_front(self, obj):
        """для добавления нового объекта obj в начало стека."""
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __getitem__(self, item):
        if not 0 <= item < len(self):
            raise IndexError('неверный индекс')
        item = item
        obj = self.top
        while item > 0:
            obj = obj.next
            item -= 1
        return obj.data

    def __setitem__(self, key, value):
        if not 0 <= key < len(self):
            raise IndexError('неверный индекс')
        item = key
        obj = self.top
        while item > 0:
            obj = obj.next
            item -= 1
        obj.data = value

    def __iter__(self):
        lst = []
        if self.top is None:
            return lst
        lst.append(self.top)
        obj = self.top
        while obj.next is not None:
            obj = obj.next
            lst.append(obj)
        return iter(lst)


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kmmvxZWxaAY
Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:
Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:
    cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с 
соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):
    data - для записи и считывания информации из атрибута __data.
Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:
    table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и 
т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).
С объектами класса TableValues должны выполняться следующие команды:
    table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
    value = table[row, col] # считывание значения из ячейки с индексами row, col
    
    for row in table:  # перебор по строкам
        for value in row: # перебор по столбцам
            print(value, end=' ')  # вывод значений ячеек в консоль
        print()
При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data объекта 
класса TableValues), должно генерироваться исключение командой:
    raise TypeError('неверный тип присваиваемых данных')
При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за 
диапазон размера таблицы, то генерировать исключение командой:
    raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.indx = 0
        self.__dumb_lst = tuple(tuple(Cell(0) for _ in range(cols)) for _ in range(rows))

    def __check_index(self, item):
        i, j = item
        if type(i) != int or not 0 <= i < self.rows or type(j) != int or not 0 <= j < self.cols:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        i, j = item
        return self.__dumb_lst[i][j].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        i, j = key
        self.__dumb_lst[i][j].data = value

    def __iter__(self):
        self.indx = 0
        return self

    def __next__(self):
        if self.indx == len(self.__dumb_lst):
            raise StopIteration
        res = iter(x.data for x in self.__dumb_lst[self.indx])
        self.indx += 1
        return res


""" Упражнение 6
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/yX9qxE8X1OA
Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны 
создаваться командой:
    m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы (должно 
быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:
    raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
Также объекты можно создавать командой:
    m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не 
прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:
    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
Для объектов класса Matrix должны выполняться следующие команды:
    matrix = Matrix(4, 5, 0)
    res = matrix[0, 0] # возвращается первый элемент матрицы
    matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:
    raise TypeError('значения матрицы должны быть числами')
Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать 
исключение:
    raise IndexError('недопустимые значения индексов')
Также с объектами класса Matrix должны выполняться операторы:
    matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
    matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
    matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
    matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не 
совпадают (разные хотя бы по одной оси), то генерировать исключение командой:
    raise ValueError('операции возможны только с матрицами равных размеров')
Пример для понимания использования индексов (эти строчки в программе писать не нужно):
    mt = Matrix([[1, 2], [3, 4]])
    res = mt[0, 0] # 1
    res = mt[0, 1] # 2
    res = mt[1, 0] # 3
    res = mt[1, 1] # 4
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""
class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            self.__check_list(*args)
            self.matrix = args[0]
            self.rows = len(args[0])
            self.cols = len(args[0][0])
        if len(args) == 3:
            self.matrix = self.__check_values(*args)
            self.rows = args[0]
            self.cols = args[1]

    @staticmethod
    def __check_list(lst):
        flag = True
        if len(set([len(x) for x in lst])) != 1:
            flag = False
        for i in lst:
            for j in i:
                if type(j) not in (int, float):
                    flag = False
        if flag is False:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    @staticmethod
    def __check_values(rows, cols, fill_value):
        if type(rows) != int or type(cols) != int or type(fill_value) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        return [[fill_value for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, item):
        i, j = item
        if type(i) != int or not 0 <= i < self.rows or type(j) != int or not 0 <= j < self.cols:
            raise IndexError('недопустимые значения индексов')
        return self.matrix[i][j]

    def __setitem__(self, key, value):
        i, j = key
        if type(i) != int or not 0 <= i < self.rows or type(j) != int or not 0 <= j < self.cols:
            raise IndexError('недопустимые значения индексов')
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.matrix[i][j] = value

    def comp(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if type(other) == int:
            other = Matrix([[other for _ in range(self.cols)] for _ in range(self.rows)])
        if self.comp() != other.comp():
            raise ValueError('операции возможны только с матрицами равных размеров')
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(other) == int:
            other = Matrix([[other for _ in range(self.cols)] for _ in range(self.rows)])
        if self.comp() != other.comp():
            raise ValueError('операции возможны только с матрицами равных размеров')
        return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])
