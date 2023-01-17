""" Упражнение 1
Подвиг 4. Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception. После этого
объявите еще два класса-исключения:
    NegativeLengthString - ошибка, если длина отрицательная;
    ExceedLengthString - ошибка, если длина превышает заданное значение;
унаследованные от базового класса StringException.
Затем, в блоке try (см. программу) пропишите команду генерации исключения для перехода в блок обработки исключения
ExceedLengthString.
"""
# здесь объявляйте классы
class StringException(Exception):
    pass

class NegativeLengthString(StringException):
    pass

class ExceedLengthString(StringException):
    pass


try:
    # здесь команда для генерации исключения
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6wnJd7OrNaI
Подвиг 5. Объявите в программе класс-исключение с именем PrimaryKeyError, унаследованным от базового класса Exception. 
Объекты класса PrimaryKeyError должны создаваться командами:
    e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
    e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
    e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
В первом варианте команды должно формироваться сообщение об ошибке "Первичный ключ должен быть целым неотрицательным 
числом". При втором варианте:
    "Значение первичного ключа id = <id> недопустимо"
И при третьем:
    "Значение первичного ключа pk = <pk> недопустимо"
Эти сообщения должны формироваться при отображении объектов класса PrimaryKeyError, например:
    print(e2) # Значение первичного ключа id = abc недопустимо
Затем, сгенерируйте это исключение с аргументом id = -10.5, обработайте его и отобразите на экране объект исключения.
Sample Input:
Sample Output:
Значение первичного ключа id = -10.5 недопустимо
"""
class PrimaryKeyError(Exception):
    def __init__(self, *args, **kwargs):
        self.dct = kwargs

    def __str__(self):
        string = 'Первичный ключ должен быть целым неотрицательным числом'
        if self.dct:
            k, v = list(self.dct.items())[0]
            string = f'Значение первичного ключа {k} = {v} недопустимо'
        return string

try:
    raise PrimaryKeyError(id = -10.5)
except PrimaryKeyError as p1:
    print(p1)


""" Упражнение 3
Подвиг 6. Объявите класс DateString для представления дат, объекты которого создаются командой:
    date = DateString(date_string)
где date_string - строка с датой в формате:
    "DD.MM.YYYY"
здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12); YYYY - год (целое число от 1 до 3000).
Например:
    date = DateString("26.05.2022")
или
    date = DateString("26.5.2022") # незначащий ноль может отсутствовать
Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с помощью собственного класса:
    DateError - класс-исключения, унаследованный от класса Exception.
В самом классе DateString переопределить магический метод __str__() для формирования строки даты в формате:
    "DD.MM.YYYY"
(здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022" должна формироваться строка "26.05.2022").
Далее, в программе выполняется считывание строки из входного потока командой:
    date_string = input()
Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:
    print(date) # date - объект класса DateString
Если же произошло исключение, то вывести сообщение (без кавычек):
"Неверный формат даты"
Sample Input:
    1.2.1812
Sample Output:
    01.02.1812
"""
# здесь объявляйте классы
from datetime import datetime


class DateError(Exception):
    pass


class DateString:
    @staticmethod
    def check(string):
        try:
            string = datetime.strptime(string, '%d.%m.%Y').strftime('%d.%m.%Y')
        except ValueError:
            raise DateError
        return string

    def __init__(self, date_string):
        self.date_string = self.check(date_string)

    def __str__(self):
        string = self.date_string.split('.')
        res = string[0].rjust(2, '0') + '.' + string[1].rjust(2, '0') + '.' + string[2].rjust(4, '0')
        return res


date_string = input()

# здесь создавайте объект класса DateString и выполняйте обработку исключений
try:
    date = DateString(date_string)
    print(date)
except DateError:
    print("Неверный формат даты")


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wLaOyNN8x7E
Значимый подвиг 7. Вам поручается разработать класс TupleData, элементами которого могут являются только объекты 
классов: CellInteger, CellFloat и CellString.
Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:
    cell_1 = CellInteger(min_value, max_value)
    cell_2 = CellFloat(min_value, max_value)
    cell_3 = CellString(min_length, max_length)
где min_value, max_value - минимальное и максимальное допустимое значение в ячейке; min_length, max_length - минимальная 
и максимальная допустимая длина строки в ячейке.
В каждом объекте этих классов должны формироваться локальные атрибуты с именами _min_value, _max_value или _min_length, 
_max_length и соответствующими значениями.
Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:
    value - для записи и считывания значения в ячейке (изначально возвращает значение None).
Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или [min_length; max_length], 
то генерируется исключения командами:
    raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
    raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
    raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
Все три класса исключений должны быть унаследованы от одного общего класса:
    CellException
Далее, объявите класс TupleData, объекты которого создаются командой:
    ld = TupleData(cell_1, ..., cell_N)
где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).
Обращение к отдельной ячейке должно выполняться с помощью оператора:
    value = ld[index] # считывание значения из ячейке с индексом index
    ld[index] = value # запись нового значения в ячейку с индексом index
Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом. Если значение index выходит за диапазон 
[0; число ячеек-1], то генерировать исключение IndexError.
Также с объектами класса TupleData должны выполняться следующие функции и операторы:
    res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
    for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
        print(d)
Все эти классы в программе можно использовать следующим образом:
    ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
    
    try:
        ld[0] = 1
        ld[1] = 20
        ld[2] = -5.6
        ld[3] = "Python ООП"
    except CellIntegerException as e:
        print(e)
    except CellFloatException as e:
        print(e)
    except CellStringException as e:
        print(e)
    except CellException:
        print("Ошибка при обращении к ячейке")
    except Exception:
        print("Общая ошибка при работе с объектом TupleData")
P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно.
"""
# здесь объявляйте классы CellException, CellIntegerException, CellFloatException, CellStringException
class CellException(Exception):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string


class CellIntegerException(CellException): pass


class CellFloatException(CellException): pass


class CellStringException(CellException): pass


# здесь объявляйте классы CellInteger, CellFloat, CellString
class Cell:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._v = None

    @property
    def value(self):
        return self._v


class CellInteger(Cell):
    @property
    def value(self):
        return self._v

    @value.setter
    def value(self, val):
        if type(val) != int or not self._min_value <= val <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')
        self._v = val


class CellFloat(Cell):
    @property
    def value(self):
        return self._v

    @value.setter
    def value(self, val):
        if type(val) != float or not self._min_value <= val <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')
        self._v = val


class CellString(Cell):
    @property
    def value(self):
        return self._v

    @value.setter
    def value(self, val):
        if type(val) != str or not self._min_value <= len(val) <= self._max_value:
            raise CellStringException('длина строки выходит за допустимый диапазон')
        self._v = val


# здесь объявляйте класс TupleData
class TupleData:
    def __init__(self, *args):
        self.__lst = list(args)

    def __getitem__(self, item):
        return self.__lst[item].value

    def __setitem__(self, key, val):
        self.__lst[key].value = val

    def __len__(self):
        return len(self.__lst)


# эти строчки в программе не менять!
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
