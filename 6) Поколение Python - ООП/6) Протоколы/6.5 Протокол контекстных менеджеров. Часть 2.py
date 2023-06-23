""" Упражнение 1
Требовалось реализовать класс SuppressAll. При создании экземпляра класс не должен был принимать никаких аргументов.
Предполагалось, что экземпляр класса SuppressAll будет являться контекстным менеджером, подавляющим любое исключение,
которое возбуждается во время выполнения кода внутри блока with.
Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте класс SuppressAll
правильно.
Примечание 1. Наглядные примеры использования класса SuppressAll продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 3. Класс SuppressAll должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__()
и __exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    print('start')

    with SuppressAll():
        print('Python generation!')
        raise ValueError

    print('end')
Sample Output 1:
    start
    Python generation!
    end
Sample Input 2:
    print('start')

    with SuppressAll():
        print('Python generation!')

    print('end')
Sample Output 2:
    start
    Python generation!
    end
"""
class SuppressAll:
    def __enter__(self):
        return None

    def __exit__(self, *args, **kwargs):
        return True

    
""" Упражнение 2
Реализуйте класс Greeter. При создании экземпляра класс должен принимать один аргумент:
    name — имя пользователя
Экземпляр класса Greeter должен иметь один атрибут:
    name — имя пользователя
Экземпляр класса Greeter должен являться контекстным менеджером, который приветствует пользователя с именем name перед 
выполнением блока with и выводит текст:
    Приветствую, <имя пользователя>!
а также прощается с ним после выполнения блока with и выводит текст:
    До встречи, <имя пользователя>!
Примечание 1. Наглядные примеры использования класса Greeter продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс Greeter должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и
__exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    with Greeter('Кейв'):
        print('...')
Sample Output 1:
    Приветствую, Кейв!
    ...
    До встречи, Кейв!
Sample Input 2:
    with Greeter('Кейв') as greeter:
        print(greeter.name)
Sample Output 2:
    Приветствую, Кейв!
    Кейв
    До встречи, Кейв!
"""
class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, *args, **kwargs):
        print(f'До встречи, {self.name}!')


""" Упражнение 3
Реализуйте класс Closer. При создании экземпляра класс должен принимать один аргумент:
    obj — произвольный объект
Экземпляр класса Closer должен являться контекстным менеджером, который закрывает используемый объект obj с помощью 
метода close() после выполнения кода внутри блока with. Если объект не поддерживает операцию закрытия, контекстный 
менеджер должен вывести:
    Незакрываемый объект
Примечание 1. Наглядные примеры использования класса Closer продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс Closer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и 
__exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    output = open('output.txt', 'w', encoding='utf-8')
    
    with Closer(output) as file:
        print(file.closed)
        
    print(file.closed)
Sample Output 1:
    False
    True
Sample Input 2:
    with Closer(5) as i:
        i += 1
        
    print(i)
Sample Output 2:
    Незакрываемый объект
    6
"""
class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, *args, **kwargs):
        try:
            self.obj.close()
        except:
            print('Незакрываемый объект')


""" Упражнение 4
Реализуйте класс ReadableTextFile. При создании экземпляра класс должен принимать один аргумент:
    filename — имя текстового файла
Экземпляр класса ReadableTextFile должен являться контекстным менеджером, который открывает файл с именем filename на 
чтение в кодировке UTF-8 и позволяет получать его строки без символа переноса строки \n на конце. Также контекстный 
менеджер должен закрывать открытый им файл после выполнения кода внутри блока with.
Примечание 1. Наглядные примеры использования класса ReadableTextFile продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс ReadableTextFile должен удовлетворять протоколу контекстного менеджера, то есть иметь методы 
__enter__() и __exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
        print('Только посмотрите!', file=file)
        print('Как величаво она парит в воздухе', file=file)
        print('Как орел', file=file)
        print('На воздушном шаре', file=file)
    
    with ReadableTextFile('glados_quotes.txt') as file:
        for line in file:
            print(line)
Sample Output 1:
    Только посмотрите!
    Как величаво она парит в воздухе
    Как орел
    На воздушном шаре
Sample Input 2:
    with open('poem.txt', 'w', encoding='utf-8') as file:
        print('Я кашлянул в звенящей тишине,', file=file)
        print('И от шального эха стало жутко…', file=file)
        print('Расскажет ли утятам обо мне', file=file)
        print('под утро мной испуганная утка?', file=file)
    
    with ReadableTextFile('poem.txt') as file:
        for line in file:
            print(line)
Sample Output 2:
    Я кашлянул в звенящей тишине,
    И от шального эха стало жутко…
    Расскажет ли утятам обо мне
    под утро мной испуганная утка?
"""
class ReadableTextFile:
    def __init__(self, filename):
        self.name = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.name, 'r', encoding='UTF-8')
        return (x.strip() for x in self.file.readlines())

    def __exit__(self, *args, **kwargs):
        self.file.close()


""" Упражнение 5
Реализуйте класс Reloopable. При создании экземпляра класс должен принимать один аргумент:
    file — открытый на чтение файловый объект
Экземпляр класса Reloopable должен являться контекстным менеджером, который позволяет многократно итерироваться 
по файловому объекту file внутри блока with. Также контекстный менеджер должен закрывать используемый им файловый объект 
после выполнения кода внутри блока with.
Примечание 1. Наглядные примеры использования класса Reloopable продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс Reloopable должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() 
и __exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    with open('file.txt', 'w') as file:
        file.write('Evil is evil\n')
        file.write('Lesser, greater, middling\n')
        file.write('Makes no difference\n')
        
    with Reloopable(open('file.txt')) as reloopable:
        for line in reloopable:
            print(line.strip())
        for line in reloopable:
            print(line.strip())
Sample Output 1:
    Evil is evil
    Lesser, greater, middling
    Makes no difference
    Evil is evil
    Lesser, greater, middling
    Makes no difference
Sample Input 2:
    with open('file.txt', 'w') as file:
        pass
        
    file = open('file.txt')
    print(file.closed)
    
    with Reloopable(file) as reloopable:
        pass
    
    print(file.closed)
Sample Output 2:
    False
    True
"""
class Reloopable:
    def __init__(self, file):
        self.file = file
        self.lst = list(file)

    def __enter__(self):
        return self

    def __iter__(self):
        return iter(self.lst)

    def __exit__(self, *args, **kwargs):
        self.file.close()


""" Упражнение 6
Реализуйте класс UpperPrint. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса UpperPrint должен являться контекстным менеджером, который внутри блока with позволяет выполнять все 
операции записи в стандартный поток вывода sys.stdout в верхнем регистре.
Примечание 1. Наглядные примеры использования класса UpperPrint продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс UpperPrint должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() 
и __exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    print('Если жизнь одаривает вас лимонами — не делайте лимонад')
    print('Заставьте жизнь забрать их обратно!')
    
    with UpperPrint():
        print('Мне не нужны твои проклятые лимоны!')
        print('Что мне с ними делать?')
    
    print('Требуйте встречи с менеджером, отвечающим за жизнь!')
Sample Output 1:
    Если жизнь одаривает вас лимонами — не делайте лимонад
    Заставьте жизнь забрать их обратно!
    МНЕ НЕ НУЖНЫ ТВОИ ПРОКЛЯТЫЕ ЛИМОНЫ!
    ЧТО МНЕ С НИМИ ДЕЛАТЬ?
    Требуйте встречи с менеджером, отвечающим за жизнь!
Sample Input 2:
    with UpperPrint():
        print('Bee', 'Geek', 'Love', sep=' one ', end=' end')
    Sample Output 2:
    
    BEE ONE GEEK ONE LOVE END
"""
import sys


class UpperPrint:
    def __init__(self):
        self.standart = sys.stdout.write
        sys.stdout.write = self.upper

    def upper(self, line):
        self.standart(line.upper())

    def __enter__(self):
        pass

    def __exit__(self, *args, **kwargs):
        sys.stdout.write = self.standart


""" Упражнение 7
Реализуйте класс Suppress. При создании экземпляра класс должен принимать произвольное количество позиционных 
аргументов, каждый из которых представляет собой тип исключения.
Экземпляр класса Suppress должен являться контекстным менеджером, подавляющим исключение, если оно возбуждается во время 
выполнения кода внутри блока with. Подавляться должны исключения тех типов, которые были перечислены при создании 
контекстного менеджера.
Также экземпляр класса Suppress должен иметь один атрибут:
exception — исключение, которое было подавлено контекстным менеджером. Если исключение не было подавлено или код был 
выполнен без исключений, атрибут должен иметь значение None
Примечание 1. Наглядные примеры использования класса Suppress продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс Suppress должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и 
__exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    with Suppress(NameError):
        print('Этой переменной не существует -->', variable)
        
    print('Завершение программы')
Sample Output 1:
    Завершение программы
Sample Input 2:
    with Suppress(TypeError, ValueError) as context:
        number = int('я число')
    
    print(context.exception)
    print(type(context.exception))
Sample Output 2:
    invalid literal for int() with base 10: 'я число'
    <class 'ValueError'>
Sample Input 3:
    with Suppress() as context:
        print('All success!')
    
    print(context.exception)
Sample Output 3:
    All success!
    None
"""
class Suppress:
    def __init__(self, *args):
        self._exceptions = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self._exceptions:
            self.exception = exc_value
            return True
        return False


""" Упражнение 8
Реализуйте класс WriteSpy. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    file1 — файловый объект
    file2 — файловый объект
    to_close — булево значение, по умолчанию равняется False
Экземпляр класса WriteSpy должен являться контекстным менеджером, который выполняет операцию записи сразу в оба файловых 
объекта file1 и file2. Параметр to_close должен определять состояние файловых объектов file1 и file2 после завершения 
блока with. Если он имеет значение True, после завершения блока with контекстный менеджер должен закрыть оба файловых 
объекта, если False — оставить открытыми.
Класс WriteSpy должен иметь четыре метода экземпляра:
    write() — метод, принимающий в качестве аргумента текст и записывающий его в оба файловых объекта. Если хотя бы один 
из файловых объектов закрыт или недоступен для записи, должно быть возбуждено исключение ValueError с текстом: Файл 
закрыт или недоступен для записи
    close() — метод, немедленно закрывающий оба файловых объекта
    writable() — метод, возвращающий True, если оба файловых объекта доступны для записи, или False в противном случае
    closed() — метод, возвращающий True, если оба файловых объекта закрыты, или False в противном случае
Примечание 1. Наглядные примеры использования класса WriteSpy продемонстрированы в тестовых данных.
Примечание 2. Для проверки того, является ли файловый объект доступным для записи, используйте метод writable(). Данный 
метод возвращает True, если файловый объект доступен для записи, или False в противном случае. При попытке применить 
метод на закрытом файловом объекте будет возбуждено исключение.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Класс WriteSpy должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и 
__exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    f1 = open('file1.txt', mode='w')
    f2 = open('file2.txt', mode='w')
    
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('You shall seal the blinding light that plagues their dreams\n')
        combined.write('You are the Vessel\n')
        combined.write('You are the Hollow Knight')
    
    print(f1.closed, f2.closed)
    
    with open('file1.txt') as file1, open('file2.txt') as file2:
        print(file1.read())
        print(file2.read())
Sample Output 1:
    True True
    You shall seal the blinding light that plagues their dreams
    You are the Vessel
    You are the Hollow Knight
    You shall seal the blinding light that plagues their dreams
    You are the Vessel
    You are the Hollow Knight
Sample Input 2:
    f1 = open('file1.txt', mode='w')
    f2 = open('file2.txt', mode='w')
    
    with WriteSpy(f1, f2, to_close=True) as combined:
        print(combined.writable())
        
    f1 = open('file1.txt')
    f2 = open('file2.txt')
    
    with WriteSpy(f1, f2, to_close=True) as combined:
        print(combined.writable())
Sample Output 2:
    True
    False
Sample Input 3:
    f1 = open('file1.txt', mode='w')
    f2 = open('file2.txt', mode='w')
    
    with WriteSpy(f1, f2, to_close=True) as combined:
        print(combined.closed())
        f1.close()
        print(combined.closed())
        f2.close()
        print(combined.closed())
Sample Output 3:
    False
    False
    True
"""
class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self.to_close:
            self.close()

    def write(self, text):
        if not self.writable():
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file1.write(text)
        self.file2.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def closed(self):
        return self.file1.closed and self.file2.closed

    def writable(self):
        return not (self.file1.closed or self.file2.closed) and self.file1.writable() and self.file2.writable()


""" Упражнение 9
Реализуйте класс Atomic. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    data — произвольный список, множество или словарь
    deep — булево значение, по умолчанию равняется False
Экземпляр класса Atomic должен являться контекстным менеджером, который позволяет выполнять операции над коллекцией data 
внутри блока with в атомарном режиме, то есть либо все операции должны быть выполнены, либо ни одна из них. Если все 
операции корректны (не приводят к возбуждению исключения), они должны быть применены к коллекции data. Если какая-либо 
операция некорректна, все ранее выполненные операции должны быть отменены, а коллекция data должна быть возвращена 
в исходное состояние.
Параметр deep должен определять состояние вложенных структур коллекции data после завершения блока with. Если он имеет 
значение False, контекстный менеджер должен возвращать в исходное состояние только саму коллекцию data, не затрагивая ее 
вложенные структуры. Например, если data является двумерным списком и внутри блока with произошло изменение одного из 
его вложенных списков, то этот вложенный список должен сохранить свое новое состояние, даже если последующие операции 
внутри блока with приведут к возбуждению исключения и возврату коллекции data в исходное состояние. Если же параметр 
deep имеет значение True, контекстный менеджер должен возвращать в исходное состояние не только саму коллекцию data, 
но и ее вложенные структуры.
Примечание 1. Наглядные примеры использования класса Atomic продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс Atomic должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и 
__exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    numbers = [1, 2, 3, 4, 5]
    
    with Atomic(numbers) as atomic:
        atomic.append(6)
        atomic[2] = 0
        del atomic[1]
    
    print(numbers)
Sample Output 1:
    [1, 0, 4, 5, 6]
Sample Input 2:
    numbers = [1, 2, 3, 4, 5]
    
    with Atomic(numbers) as atomic:
        atomic.append(6)
        atomic[2] = 0
        del atomic[100]           # обращение по несуществующему индексу
    
    print(numbers)
Sample Output 2:
    [1, 2, 3, 4, 5]
Sample Input 3:
    matrix = [[1, 2], [3, 4]]
    
    with Atomic(matrix) as atomic:
        atomic[1].append(0)       # изменение вложенной структуры
        atomic.append([5, 6])
        del atomic[100]           # обращение по несуществующему индексу
    
    print(matrix)
Sample Output 3:
    [[1, 2], [3, 4, 0]]
Sample Input 4:
    matrix = [[1, 2], [3, 4]]
    
    with Atomic(matrix, True) as atomic:
        atomic[1].append(0)       # изменение вложенной структуры
        atomic.append([5, 6])
        del atomic[100]           # обращение по несуществующему индексу
    
    print(matrix)
Sample Output 4:
    [[1, 2], [3, 4]]
"""
import copy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = copy.deepcopy(data) if deep else copy.copy(data)
        self._bkp = data

    def __enter__(self):
        return self.data

    def __exit__(self, exc_type, exc_value, trecaback):
        if exc_type is not None:
            return True
        self._bkp.clear()
        method = {dict: 'update', list: 'extend', set: 'update'}[type(self._bkp)]
        eval(f'self._bkp.{method}(self.data)', {}, {'self': self})


""" Упражнение 10
Реализуйте класс AdvancedTimer. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса AdvancedTimer должен являться многоразовым контекстным менеджером, который замеряет время выполнение 
кода внутри каждого блока with.
Также экземпляр класса AdvancedTimer должен иметь четыре атрибута:
    last_run — число, представляющее время выполнения кода внутри последнего блока with
    runs — список чисел, каждое из которых представляет время выполнения какого-либо кода внутри блока with. Первый 
элемент списка должен представлять собой время выполнения кода внутри первого блока with, второй элемент — внутри 
второго блока with, и так далее
    min — число, представляющее минимальное время выполнения кода внутри блока with среди всех замеров
    max — число, представляющее максимальное время выполнения кода внутри блока with среди всех замеров
Если экземпляр класса AdvancedTimer ни разу не использовался для замера скорости выполнения какого-либо блока кода, 
значения атрибутов last_run, min и max должны равняться None.
Примечание 1. Наглядные примеры использования класса AdvancedTimer продемонстрированы в тестовых данных.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Класс AdvancedTimer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы 
__enter__() и __exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    timer = AdvancedTimer()
    
    print(timer.runs)
    print(timer.last_run)
    print(timer.min)
    print(timer.max)
Sample Output 1:
    []
    None
    None
    None
Sample Input 2:
    from time import sleep
    
    timer = AdvancedTimer()
    
    with timer:
        sleep(1.5)
    print(round(timer.last_run, 1))
    
    with timer:
        sleep(0.7)
    print(round(timer.last_run, 1))
    
    with timer:
        sleep(1)
    print(round(timer.last_run, 1))
Sample Output 2:
    1.5
    0.7
    1.0
Sample Input 3:
    from time import sleep
    
    timer = AdvancedTimer()
    
    with timer:
        sleep(1.5)
    
    with timer:
        sleep(0.7)
    
    with timer:
        sleep(1)
    
    print([round(runtime, 1) for runtime in timer.runs])
    print(round(timer.min, 1))
    print(round(timer.max, 1))
Sample Output 3:
    [1.5, 0.7, 1.0]
    0.7
    1.5
"""
import time


class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = None
        self.min = None
        self.max = None

    def __enter__(self):
        self.last_run = time.time()

    def __exit__(self, *args):
        self.last_run = time.time() - self.last_run
        self.runs.append(self.last_run)
        self.min = min(self.runs)
        self.max = max(self.runs)


""" Упражнение 11
HTML — это язык разметки, используемый для определения структуры веб-страниц, посещаемых пользователями. HTML 
предоставляет средства для создания заголовков, абзацев, ссылок, цитат и других элементов. Каждый HTML-элемент 
обозначается открывающим и закрывающим тегами:
    <p>Если в ходе теста нет угрозы жизни, разве это вообще наука?</p>
Теги заключаются в угловые скобки. Они определяют, где элемент начинается и где он заканчивается. Единственным различием 
между открывающим и закрывающим тегами является косая черта, которая предшествует имени тега.
Открывающий и закрывающий теги, а также заключенное в них содержимое, могут располагаться как на одной строке (пример 
выше), так и на разных. Если теги и содержимое располагаются на разных строках, то сперва указывается открывающий тег, 
затем на следующий строке с отступом в два пробела указывается содержимое, а после на следующей строке указывается 
закрывающий тег, который располагается на том же уровне отступов, что и открывающий тег:
    <p>
      Наука не решает вопрос Почему?, она решает вопрос А почему бы и нет?
    </p>
Реализуйте класс HtmlTag. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    tag — HTML тег
    inline — булево значение, по умолчанию равняется False
Экземпляр класса HtmlTag должен являться реентерабельным контекстным менеджером, который позволяет генерировать HTML-код 
с правильными отступами и глубиной вложенности тегов. Параметр inline должен определять положение тегов и их 
содержимого. Если он имеет значение True, теги и содержимое должны располагаться на одной строке, если False — на разных 
строках.
Класс HtmlTag должен иметь один метод экземпляра:
    print() — метод, принимающий в качестве аргумента содержимое тега и выводящий его в рамках этого тега
Примечание 1. Наглядные примеры использования класса HtmlTag продемонстрированы в тестовых данных.
Примечание 2. В качестве отступов для каждого уровня используйте два пробела.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Класс HtmlTag должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и 
__exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    with HtmlTag('body') as _:
        with HtmlTag('h1') as header:
            header.print('Поколение Python')
        with HtmlTag('p') as section:
            section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
Sample Output 1:
    <body>
      <h1>
        Поколение Python
      </h1>
      <p>
        Cерия курсов по языку программирования Python от команды BEEGEEK
      </p>
    </body>
Sample Input 2:
    with HtmlTag('body') as _:
        with HtmlTag('h1', True) as header:
            header.print('Поколение Python')
        with HtmlTag('p', True) as section:
            section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
Sample Output 2:
    <body>
      <h1>Поколение Python</h1>
      <p>Cерия курсов по языку программирования Python от команды BEEGEEK</p>
    </body>
Sample Input 3:
    with HtmlTag('body') as _:
        with HtmlTag('h1', True) as header:
            header.print('Здесь есть что-то интересное')
        with HtmlTag('a', True) as section:
            section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')
Sample Output 3:
    <body>
      <h1>Здесь есть что-то интересное</h1>
      <a>https://stepik.org/media/attachments/course/98974/watch_me.mp4</a>
    </body>
"""
class HtmlTag:
    _indent = -2

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        HtmlTag._indent += 2
        if HtmlTag._indent > 0:
            print()
        print(' ' * self._indent + f'<{self.tag}>', end='')
        return self

    def __exit__(self, *args, **kwargs):
        print(self.get_indent() + f'</{self.tag}>', end='')
        HtmlTag._indent -= 2

    def print(self, text):
        indent = '' if self.inline else '  '
        print(self.get_indent() + indent + text, end='')

    def get_indent(self):
        return '' if self.inline else '\n' + ' ' * self._indent


""" Упражнение 12
Дерево — одна из наиболее широко распространённых структур данных в информатике, эмулирующая древовидную структуру в 
виде набора связанных узлов.
Элементы дерева называются узлами. На рисунке выше узлами являются значения 8, 3, 1, 6, 4, 7, 10, 14 и 13. Узлы без 
потомков называются листьями. На рисунке выше листьями являются значения 1, 4, 7 и 13.
Реализуйте класс TreeBuilder. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса TreeBuilder должен являться реентерабельным контекстным менеджером, который позволяет пошагово строить 
древовидную структуру данных (дерево).
Класса TreeBuilder должен иметь два метода экземпляра:
    add() — метод, принимающий в качестве аргумента произвольный объект (лист) и добавляющий его в текущий узел дерева
    structure() — метод, возвращающий структуру дерева в виде вложенных списков
Добавление узлов в дерево должно происходить с помощью оператора with. Узел считается текущим в рамках своего блока 
with. Если в узел не было добавлено ни одного листа, то этот узел не должен появляться в структуре дерева, возвращаемой 
методом structure().
Примечание 1. Структура дерева может быть произвольной, то есть узел может содержать другой узел, тот, в свою очередь, 
другой, и так далее.
Примечание 2. Гарантируется, что структура дерева не выводится внутри блоков with, то есть структура дерева выводится 
лишь после ее построения.
Примечание 3. Наглядные примеры использования класса TreeBuilder продемонстрированы в тестовых данных.
Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 5. Класс TreeBuilder должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() 
и __exit__(). Реализация же протокола может быть произвольной.
Sample Input 1:
    tree = TreeBuilder()
    print(tree.structure())
    
    tree.add('1st')
    print(tree.structure())
    
    with tree:
        tree.add('2nd')
        with tree:
            tree.add('3rd')
        tree.add('4th')
        with tree:
            pass
            
    print(tree.structure())
Sample Output 1:
    []
    ['1st']
    ['1st', ['2nd', ['3rd'], '4th']]
Sample Input 2:
    tree = TreeBuilder()
    
    tree.add('1st')
    
    with tree:
        tree.add('2nd')
        with tree:
            tree.add('3rd')
            with tree:
                tree.add('4th')
                with tree:
                    tree.add('5th')
        with tree:
            pass
    
    tree.add('6th')
    print(tree.structure())
Sample Output 2:
    ['1st', ['2nd', ['3rd', ['4th', ['5th']]]], '6th']
Sample Input 3:
    tree = TreeBuilder()
    
    with tree:
        tree.add(1)
        tree.add(2)
        with tree:
            tree.add(3)
            with tree:
                tree.add(4)
        with tree:
            tree.add(5)
    
    print(tree.structure())
Sample Output 3:
    [[1, 2, [3, [4]], [5]]]
"""
class TreeBuilder:
    def __init__(self):
        self._main = []
        self._lst = [self._main]
        self._current = self._main

    def structure(self):
        return self._main

    def add(self, value):
        self._current.append(value)

    def __enter__(self):
        self._lst.append([])
        self._current.append(self._lst[-1])
        self._current = self._lst[-1]

    def __exit__(self, *args):
        self._lst.pop()
        self._current = self._lst[-1]
        for i in range(len(self._current)):
            if isinstance(self._current[i], list) and not self._current[i]:
                self._current.pop(i)
