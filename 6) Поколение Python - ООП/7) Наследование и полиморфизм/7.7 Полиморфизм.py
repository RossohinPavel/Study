""" Упражнение 1
1. Реализуйте класс USADate, описывающий дату в американском формате. При создании экземпляра класс должен принимать три
аргумента в следующем порядке:
    year — год
    month — месяц
    day — день
Класс USADate должен иметь два метода экземпляра:
    format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
    iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате, конструктор которого принимает три
аргумента:
    year — год
    month — месяц
    day — день
Класс ItalianDate должен иметь два метода экземпляра:
    format() — который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
    iso_format() — который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы
используются только с корректными данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    usadate = USADate(2023, 4, 6)

    print(usadate.format())
    print(usadate.iso_format())
Sample Output 1:
    04-06-2023
    2023-04-06
Sample Input 2:
    italiandate = ItalianDate(2023, 4, 6)

    print(italiandate.format())
    print(italiandate.iso_format())
Sample Output 2:
    06/04/2023
    2023-04-06
"""
from datetime import date


class Date:
    def __init__(self, year, month, day):
        self._date = date(year, month, day)

    def iso_format(self):
        return self._date.strftime(r'%Y-%m-%d')


class USADate(Date):
    def format(self):
        return self._date.strftime(r'%m-%d-%Y')


class ItalianDate(Date):
    def format(self):
        return self._date.strftime(r'%d/%m/%Y')


""" Упражнение 2
1. Реализуйте класс MinStat, описывающий объект, который находит минимальное значение среди определенного набора чисел. 
При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс MinStat должен иметь три метода экземпляра:
    add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
    result() — метод, возвращающий минимальное число из набора. Если набор пуст, метод должен вернуть значение None
    clear() — метод, удаляющий из набора все числа
2. Также реализуйте класс MaxStat, описывающий объект, который находит максимальное значение среди определенного набора 
чисел. При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс MaxStat должен иметь три метода экземпляра:
    add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
    result() — метод, возвращающий максимальное число из набора. Если набор пуст, метод должен вернуть значение None
    clear() — метод, удаляющий из набора все числа
3. Наконец, реализуйте класс AverageStat, описывающий объект, который находит среднее арифметическое определенного 
набора чисел. При создании экземпляра класс должен принимать один аргумент:
    iterable — итерируемый объект, определяющий начальный набор чисел. Если не передан, начальный набор считается пустым
Класс AverageStat должен иметь три метода экземпляра:
    add() — метод, принимающий в качестве аргумента число и добавляющий его в набор
    result() — метод, возвращающий среднее арифметическое набора чисел. Если набор пуст, метод должен вернуть значение 
None
    clear() — метод, удаляющий из набора все числа
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используются только с корректными данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    minstat = MinStat([1, 2, 4])
    maxstat = MaxStat([1, 2, 4])
    averagestat = AverageStat([1, 2, 4])
    
    minstat.add(5)
    maxstat.add(5)
    averagestat.add(5)
    
    print(minstat.result())
    print(maxstat.result())
    print(averagestat.result())
Sample Output 1:
    1
    5
    3.0
Sample Input 2:
    minstat = MinStat()
    maxstat = MaxStat()
    averagestat = AverageStat()
    
    for i in range(1, 6):
        minstat.add(i)
        maxstat.add(i)
        averagestat.add(i)
    
    print(minstat.result())
    print(maxstat.result())
    print(averagestat.result())
Sample Output 2:
    1
    5
    3.0
Sample Input 3:
    minstat = MinStat()
    maxstat = MaxStat()
    averagestat = AverageStat()
    
    print(minstat.result())
    print(maxstat.result())
    print(averagestat.result())
Sample Output 3:
    None
    None
    None
"""


class Stat:
    def __init__(self, iterable=None):
        self._lst = []
        if iterable:
            self._lst.extend(list(iterable))

    def add(self, n):
        self._lst.append(n)

    def clear(self):
        self._lst.clear()

    @staticmethod
    def result(func):
        def inner(obj):
            if obj._lst:
                return func(obj._lst)
        return inner


class MinStat(Stat):
    result = Stat.result(min)


class MaxStat(Stat):
    result = Stat.result(max)


class AverageStat(Stat):
    result = Stat.result(lambda x: sum(x) / len(x))


""" Упражнение 3
Будем называть словом любую последовательность из одной или более латинских букв.
1. Реализуйте класс LeftParagraph, описывающий абзац, выровненный по левому краю. При создании экземпляра класс должен 
принимать один аргумент:
    length — длина строки абзаца
Класс LeftParagraph должен иметь два метода экземпляра:
    add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в 
текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен 
автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
    end() — метод, печатающий текущий абзац, выровненный по левому краю. После вызова метода текущий абзац считается 
пустым, то есть начинается формирование нового
2. Также реализуйте класс RightParagraph, описывающий абзац, выровненный по правому краю. При создании экземпляра класс 
должен принимать один аргумент:
    length — длина строки абзаца
Класс RightParagraph должен иметь два метода экземпляра:
    add() — метод, принимающий в качестве аргумента слово или несколько слов, разделенных пробелом, и добавляющий их в 
текущий абзац. Если слово не помещается на текущей строке, оно переносится на следующую. Также метод должен 
автоматически добавлять один пробел после каждого добавленного слова (кроме последнего)
    end() — метод, печатающий текущий абзац, выровненный по правому краю с учетом длины строки. После вызова метода 
текущий абзац считается пустым, то есть начинается формирование нового
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используются только с корректными данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    leftparagraph = LeftParagraph(10)
    
    leftparagraph.add('death')
    leftparagraph.add('can have me')
    leftparagraph.add('when it earns me')
    leftparagraph.end()
Sample Output 1:
    death can
    have me
    when it
    earns me
Sample Input 2:
    rightparagraph = RightParagraph(10)
    
    rightparagraph.add('death')
    rightparagraph.add('can have me')
    rightparagraph.add('when it earns me')
    rightparagraph.end()
Sample Output 2:
     death can
       have me
       when it
      earns me
"""
class LeftParagraph:
    def __init__(self, length):
        self.length = length
        self._lst = []

    def add(self, string):
        self._lst.extend(string.split())

    def end(self, rindent=False):
        while self._lst:
            line = self._lst.pop(0)
            while self._lst and len(line) + 1 + len(self._lst[0]) <= self.length:
                line = line + ' ' + self._lst.pop(0)
            if rindent:
                line = line.rjust(self.length, ' ')
            print(line)


class RightParagraph(LeftParagraph):
    def end(self):
        super().end(True)
