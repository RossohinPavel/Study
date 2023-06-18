""" Упражнение 1
Реализуйте класс ReversedSequence, описывающий объект, который реализует доступ к элементам некоторой последовательности
в обратном порядке. При создании экземпляра класс должен принимать один аргумент:
    sequence — последовательность
При передаче экземпляра класса ReversedSequence в функцию len() должна возвращаться его длина, представленная
количеством элементов в исходной последовательности.
Также экземпляр класса ReversedSequence должен быть итерируемым объектом, элементами которого являются элементы исходной
последовательности в обратном порядке.
Наконец, экземпляр класса ReversedSequence должен позволять получать значения элементов исходной последовательности с
помощью индексов, при этом индексация должна производиться в обратном порядке, то есть по индексу 0 должен быть доступен
последний элемент исходной последовательности, по индексу 1 — предпоследний элемент, по индексу 2 — предпредпоследний
элемент, и так далее.
Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
Примечание 2. Экземпляр класса ReversedSequence должен зависеть от последовательности, на основе которой он был создан.
Другими словами, если исходная последовательность изменится, то должен измениться и экземпляр класса ReversedSequence.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса ReversedSequence нет, она может быть произвольной.
Sample Input 1:
    reversed_list = ReversedSequence([1, 2, 3, 4, 5])

    print(reversed_list[0])
    print(reversed_list[1])
    print(reversed_list[2])
Sample Output 1:
    5
    4
    3
Sample Input 2:
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = ReversedSequence(numbers)

    print(reversed_numbers[0])
    numbers.append(6)
    print(reversed_numbers[0])
Sample Output 2:
    5
    6
Sample Input 3:
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = ReversedSequence(numbers)
    print(len(reversed_numbers))

    numbers.append(6)
    numbers.append(7)
    print(len(reversed_numbers))
Sample Output 3:
    5
    7
"""
class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        yield from reversed(self.sequence)

    def __getitem__(self, key):
        return self.sequence[-1 - key]


""" Упражнение 2
Разреженный массив (список) — абстрактное представление обычного массива (списка), в котором данные представлены не 
непрерывно, а фрагментарно: большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None. 
В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение 
по умолчанию.
Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один 
аргумент:
    default — значение по умолчанию для неопределенных элементов разреженного массива
Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов. При 
попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.
Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса SparseArray нет, она может быть произвольной.
Sample Input 1:
    array = SparseArray(0)
    
    array[5] = 1000
    array[12] = 1001
    
    print(array[5])
    print(array[12])
    print(array[13])
Sample Output 1:
    1000
    1001
    0
Sample Input 2:
    array = SparseArray(None)
    
    array[0] = 'Timur'
    array[1] = 'Arthur'
    
    print(array[0])
    print(array[1])
    print(array[2])
Sample Output 2:
    Timur
    Arthur
    None
"""
class SparseArray:
    def __init__(self, default):
        self.default = default
        self.__dct = {}

    def __getitem__(self, key):
        return self.__dct.get(key, self.default)

    def __setitem__(self, key, value):
        self.__dct[key] = value


""" Упражнение 3
Реализуйте класс CyclicList, описывающий циклический список. При создании экземпляра класс должен принимать один 
аргумент:
    iterable — итерируемый объект, определяющий начальный набор элементов циклического списка. Если не передан, 
    начальный набор элементов считается пустым
Класс CyclicList должен иметь два метода экземпляра:
    append() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец циклического списка
    pop() — метод, который принимает в качестве аргумента индекс элемента циклического списка, возвращает его значение и 
удаляет из циклического списка элемент с данным индексом. Если аргумент не передан, возвращаемым и удаляемым элементом 
считаесяя последний элемент циклического списка 
При передаче экземпляра класса CyclicList в функцию len() должно возвращаться количество элементов в нем.
Также экземпляр класса CyclicList должен быть зацикленным итерируемым объектом. Другими словами, итерация по нему должна 
происходить бесконечно, и при каждом достижении его последнего элемента она должна начинаться сначала.
Наконец, экземпляр класса CyclicList должен позволять получать значения своих элементов с помощью индексов, при этом 
индексы должны работать циклически. Например, в циклическом списке [1, 2, 3] элементом с индексом 4 должно являться 
число 2.
Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
Примечание 2. Экземпляр класса CyclicList не должен зависеть от итерируемого объекта, на основе которого он был создан. 
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса CyclicList измениться  не должен.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса CyclicList нет, она может быть произвольной.
Sample Input 1:
    cyclic_list = CyclicList([1, 2, 3])
    
    for index, elem in enumerate(cyclic_list):
        if index > 6:
            break
        print(elem, end=' ')
    Sample Output 1:
    
    1 2 3 1 2 3 1
Sample Input 2:
    cyclic_list = CyclicList([1, 2, 3])
    
    cyclic_list.append(4)
    print(cyclic_list.pop())
    print(len(cyclic_list))
    print(cyclic_list.pop(0))
    print(len(cyclic_list))
Sample Output 2:
    4
    3
    1
    2
"""
class CyclicList:
    def __init__(self, iterable=None):
        self.__lst = list(iterable) if iterable else []
        self.__ind = -1

    def append(self, value):
        self.__lst.append(value)

    def pop(self, ind=None):
        return self.__lst.pop(ind) if ind is not None else self.__lst.pop()

    def __len__(self):
        return len(self.__lst)

    def __iter__(self):
        return self

    def __next__(self):
        self.__ind += 1
        return self[self.__ind]

    def __getitem__(self, key):
        return self.__lst[key % len(self)]


""" Упражнение 4
Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных 
аргументов, каждый из которых является итерируемым объектом. Класс SequenceZip должен описывать последовательность, 
элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи. Объединение 
должно происходить аналогично тому, как это делает функция zip().
При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.
Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, 
например, с помощью цикла for.
Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.
Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
Примечание 2. Экземпляр класса SequenceZip не должен зависеть от итерируемых объектов, на основе которых он был создан. 
Другими словами, если исходные итерируемые объекты изменятся, то экземпляр класса SequenceZip измениться  не должен.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.
Sample Input 1:
    sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
    
    print(list(sequencezip))
    print(tuple(sequencezip))
Sample Output 1:
    [('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3)]
    (('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3))
Sample Input 2:
    sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])
    
    print(len(sequencezip))
    print(sequencezip[1])
    print(sequencezip[2])
Sample Output 2:
    3
    ('B', 'geek', 2)
    ('C', 'python', 3)
"""
import copy


class SequenceZip:
    def __init__(self, *args):
        self.__args = copy.deepcopy(args)

    def __len__(self):
        return len(min(self.__args, key=len)) if self.__args else 0

    def __iter__(self):
        yield from zip(*self.__args)

    def __getitem__(self, key):
        for i in self:
            if key == 0:
                return i
            key -= 1


""" Упражнение 5
Реализуйте класс OrderedSet, описывающий упорядоченное множество. При создании экземпляра класс должен принимать один 
аргумент:
iterable — итерируемый объект, определяющий начальный набор элементов упорядоченного множества. Если не передан, 
начальный набор элементов считается пустым
Класс OrderedSet должен иметь два метода экземпляра:
    add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец упорядоченного 
множества
    discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий его из упорядоченного множества, 
если он в нем присутствует
При передаче экземпляра класса OrderedSet в функцию len() должно возвращаться количество элементов в нем.
Помимо этого, экземпляр класса OrderedSet должен быть итерируемым объектом, то есть позволять перебирать свои элементы, 
например, с помощью цикла for.
Также экземпляр класса OrderedSet должен поддерживать операцию проверки на принадлежность с помощью оператора in.
Наконец, экземпляры класса OrderedSet должны поддерживать операции сравнения с помощью операторов == и !=. Методы, 
реализующие операции сравнения, должны уметь сравнивать как два экземпляра класса OrderedSet между собой, так и 
экземпляр класса OrderedSet с экземпляром класса set. Если упорядоченное множество сравнивается с упорядоченным 
множеством, они считаются равными в том случае, если они имеют равную длину и содержат равные элементы на равных 
позициях. Если упорядоченное множество сравнивается с обычным множеством, они считаются равными в том случае, если имеют 
равную длину и содержат равные элементы без учета их расположения.
Примечание 1. Экземпляр класса OrderedSet не должен зависеть от итерируемого объекта, на основе которого он был создан. 
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса OrderedSet измениться  не должен.
Примечание 2. Если объект, с которыми происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен 
вернуть константу NotImplemented.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса OrderedSet нет, она может быть произвольной.
Sample Input 1:
    orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])
    
    print(*orderedset)
    print(len(orderedset))
Sample Output 1:
    bee python stepik geek
    4
Sample Input 2:
    orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])
    
    print('python' in orderedset)
    print('C++' in orderedset)
Sample Output 2:
    True
    False
Sample Input 3:
    orderedset = OrderedSet()
    
    orderedset.add('green')
    orderedset.add('green')
    orderedset.add('blue')
    orderedset.add('red')
    print(*orderedset)
    orderedset.discard('blue')
    orderedset.discard('white')
    print(*orderedset)
Sample Output 3:
    green blue red
    green red
"""
class OrderedSet:
    def __init__(self, iterable=tuple()):
        self._lst = []
        for value in iterable:
            self.add(value)

    def add(self, value):
        if value not in self._lst:
            self._lst.append(value)

    def discard(self, value):
        if value in self._lst:
            del self._lst[self._lst.index(value)]

    def __len__(self):
        return len(self._lst)

    def __iter__(self):
        return iter(self._lst)

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self._lst == other._lst
        if isinstance(other, set):
            return set(self._lst) == other
        return NotImplemented


""" Упражнение 6
Реализуйте класс AttrDict, описывающий упрощенный словарь, значения элементов которого можно получать как по ключам 
([key]), так и по одноименным атрибутам (.key). При создании экземпляра класс должен принимать один аргумент:
data — словарь, определяющий начальный набор элементов упрощенного словаря. Если не передан, начальный набор элементов 
считается пустым
При передаче экземпляра класса AttrDict в функцию len() должно возвращаться количество элементов в нем.
Также экземпляр класса AttrDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, 
с помощью цикла for.
Наконец, экземпляр класса AttrDict должен позволять получать значения своих элементов как по их ключам, так и 
по одноименным атрибутам. Реализовывать добавление элементов и изменение их значений по одноименным атрибутам не нужно.
Примечание 1. Экземпляр класса AttrDict не должен зависеть от словаря, на основе которого он был создан. Другими 
словами, если исходный словарь изменится, то экземпляр класса AttrDict измениться  не должен.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс 
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса AttrDict нет, она может быть произвольной.
Sample Input 1:
    attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})
    
    print(attrdict['name'])
    print(attrdict.father)
    print(len(attrdict))
Sample Output 1:
    X Æ A-12
    Elon Musk
    2
Sample Input 2:
    attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})
    
    attrdict['city'] = 'Dubai'
    attrdict['age'] = 31
    print(attrdict.city)
    print(attrdict.age)
Sample Output 2:
    Dubai
    31
Sample Input 3:
    attrdict = AttrDict()
    
    attrdict['school_name'] = 'BEEGEEK'
    print(attrdict['school_name'])
    print(attrdict.school_name)
Sample Output 3:
    BEEGEEK
    BEEGEEK
"""
class AttrDict:
    def __init__(self, data=None):
        self.__dict__ |= data if data else {}

    def __len__(self):
        return len(self.__dict__)

    def __setattr__(self, key, value):
        pass

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __iter__(self):
        yield from self.__dict__


""" Упражнение 7
Реализуйте класс PermaDict, описывающий словарь, который позволяет добавлять и удалять пары (<ключ>, <значение>), но не 
позволяет изменять значения по уже имеющимся ключам. При создании экземпляра класс должен принимать один аргумент:
    data — словарь, определяющий начальный набор элементов экземпляра класса PermaDict. Если не передан, начальный набор 
элементов считается пустым
Класс PermaDict должен иметь три метода экземпляра:
    keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса PermaDict
    values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса 
PermaDict
    items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса PermaDict 
в виде кортежей (<ключ>, <значение>)
При передаче экземпляра класса PermaDict в функцию len() должно возвращаться количество элементов в нем.
Также экземпляр класса PermaDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, 
с помощью цикла for.
Наконец, экземпляр класса PermaDict должен позволять получать значения своих элементов по их ключам, добавлять новые 
пары (ключ, значение) и удалять уже имеющиеся с помощью оператора del. При этом изменение значений по уже имеющимся 
ключам должно быть недоступно, и при попытке выполнения такой операции должно возбуждаться исключение KeyError 
с текстом: Изменение значения по ключу невозможно
Примечание 1. Экземпляр класса PermaDict не должен зависеть от словаря, на основе которого он был создан. Другими 
словами, если исходный словарь изменится, то экземпляр класса PermaDict измениться  не должен.
Примечание 2. Реализация класса PermaDict может быть произвольной, то есть требований к наличию определенных атрибутов 
нет.
Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный 
класс используется только с корректными данными.
Sample Input 1:
    permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})
    
    print(permadict['name'])
    print(len(permadict))
Sample Output 1:
    Timur
    2
Sample Input 2:
    permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})
    
    print(*permadict)
    print(*permadict.keys())
    print(*permadict.values())
    print(*permadict.items())
Sample Output 2:
    name city age
    name city age
    Timur Moscow 30
    ('name', 'Timur') ('city', 'Moscow') ('age', 30)
Sample Input 3:
    permadict = PermaDict()
    
    permadict['name'] = 'Timur'
    permadict['age'] = 30
    del permadict['name']
    print(permadict['age'])
    print(len(permadict))
Sample Output 3:
    30
    1
Sample Input 4:
    permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})
    
    try:
        permadict['name'] = 'Arthur'
    except KeyError as e:
        print(e)
Sample Output 4:
    'Изменение значения по ключу невозможно'
"""
# Схитрим и наследуем от dict
class PermaDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('Изменение значения по ключу невозможно')
        super().__setitem__(key, value)


""" Упражнение 8
Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании 
экземпляра класс должен принимать один аргумент:
    data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный 
набор элементов считается пустым
Класс HistoryDict должен иметь пять методов экземпляра:
    keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
    values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса 
HistoryDict
    items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict 
в виде кортежей (<ключ>, <значение>)
    history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются 
все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу. Если данный ключ не 
содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
    all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, 
а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам
При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.
Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, 
с помощью цикла for.
Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам, 
добавлять новые пары (ключ, значение) и удалять уже имеющиеся.
Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан. Другими 
словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.
Примечание 2. Реализация класса HistoryDict может быть произвольной, то есть требований к наличию определенных атрибутов 
нет.
Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный 
класс используется только с корректными данными.
Sample Input 1:
    historydict = HistoryDict({'ducks': 99, 'cats': 1})
    
    print(historydict['ducks'])
    print(historydict['cats'])
    print(len(historydict))
Sample Output 1:
    99
    1
    2
Sample Input 2:
    historydict = HistoryDict({'ducks': 99, 'cats': 1})
    
    print(*historydict)
    print(*historydict.keys())
    print(*historydict.values())
    print(*historydict.items())
Sample Output 2:
    ducks cats
    ducks cats
    99 1
    ('ducks', 99) ('cats', 1)
Sample Input 3:
    historydict = HistoryDict({'ducks': 99, 'cats': 1})
    
    historydict['ducks'] = 100
    print(historydict.history('ducks'))
    print(historydict.history('cats'))
    print(historydict.history('dogs'))
Sample Output 3:
    [99, 100]
    [1]
    []
Sample Input 4:
    historydict = HistoryDict({'ducks': 99, 'cats': 1})
    
    print(historydict.all_history())
    historydict['ducks'] = 100
    historydict['ducks'] = 101
    historydict['cats'] = 2
    print(historydict.all_history())
Sample Output 4:
    {'ducks': [99], 'cats': [1]}
    {'ducks': [99, 100, 101], 'cats': [1, 2]}
Sample Input 5:
    historydict = HistoryDict({'ducks': 99, 'cats': 1})
    
    historydict['dogs'] = 1
    print(len(historydict))
    del historydict['ducks']
    del historydict['cats']
    print(len(historydict))
Sample Output 5:
    3
    1
"""
# Продолжаем хитрить с наследованием во избежание лишней писанины
class HistoryDict(dict):
    def __init__(self, data=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if data:
            self.update({k: [v] for k, v in data.items()})

    def __getitem__(self, key):
        return super().__getitem__(key)[-1]

    def values(self):
        return list(x[-1] for x in super().values())

    def items(self):
        return list(zip(self.keys(), self.values()))

    def history(self, key):
        return self.get(key, [])

    def __setitem__(self, key, value):
        self.setdefault(key, []).append(value)

    def all_history(self):
        return self


""" Упражнение 9
Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один 
аргумент:
    string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
Класс MutableString должен иметь два метода экземпляра:
    lower() — метод, переводящий все символы изменяемой строки в нижний регистр
    upper() — метод, переводящий все символы изменяемой строки в верхний регистр
Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:
    <текущее значение изменяемой строки>
Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:
    MutableString('<текущее значение изменяемой строки>')
При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.
Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои 
символы, например, с помощью цикла for.
Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью 
индексов, причем как как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать 
полноценные срезы, результатами которых должны быть новые изменяемые строки.
Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +, 
результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.
Примечание 1. Реализация класса MutableString может быть произвольной, то есть требований к наличию определенных 
атрибутов нет.
Примечание 2. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный 
класс используется только с корректными данными.
Sample Input 1:
    mutablestring = MutableString('beegeek')
    
    print(*mutablestring)
    print(str(mutablestring))
    print(repr(mutablestring))
Sample Output 1:
    b e e g e e k
    beegeek
    MutableString('beegeek')
Sample Input 2:
    mutablestring = MutableString('Beegeek')
    
    mutablestring.lower()
    print(mutablestring)
    mutablestring.upper()
    print(mutablestring)
Sample Output 2:
    beegeek
    BEEGEEK
Sample Input 3:
    mutablestring1 = MutableString('bee')
    mutablestring2 = MutableString('geek')
    
    print(mutablestring1 + mutablestring2)
    print(mutablestring2 + mutablestring1)
Sample Output 3:
    beegeek
    geekbee
Sample Input 4:
    mutablestring = MutableString('beegeek')
    
    print(mutablestring)
    mutablestring[0] = 'B'
    mutablestring[-4] = 'G'
    print(mutablestring)
Sample Output 4:
    beegeek
    BeeGeek
"""
class MutableString:
    def __init__(self, string=None):
        self.__lst = []
        if string:
            self.__lst = list(string)

    def lower(self):
        self.__lst = [x.lower() for x in self.__lst]

    def upper(self):
        self.__lst = [x.upper() for x in self.__lst]

    def __str__(self):
        return ''.join(self.__lst)

    def __repr__(self):
        return f'MutableString(\'{str(self)}\')'

    def __len__(self):
        return len(self.__lst)

    def __iter__(self):
        yield from self.__lst

    def __getitem__(self, key):
        return MutableString(''.join(self.__lst[key]))

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            self.__lst[key] = list(value)
        else:
            self.__lst[key] = value[0]
            for i in value[1:]:
                self.__lst.insert(key, i)

    def __delitem__(self, key):
        del self.__lst[key]

    def __add__(self, other):
        return MutableString(str(self) + str(other))


""" Упражнение 10
Нередко нам приходится группировать объекты по определенному признаку. Например, строки можно сгруппировать по их длине 
или первому символу. Реализуйте класс Grouper, описывающий объект, который группирует элементы некоторого итерируемого 
объекта на основе ключевой функции. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
    iterable — итерируемый объект
    key — ключевая функция
Элементы попадают в одну группу, если при их передаче в ключевую функцию она возвращает один и тот же результат.  
Например, elem1 и elem2 попадают в одну группу, если key(elem1) == key(elem2). Значение key(elem1) будем называть ключом 
группы, а elem1 и elem2 — элементами группы по этому ключу.
Класс Grouper должен иметь два метода экземпляра:
    add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в нужную группу экземпляра 
класса Grouper
    group_for() — метод, принимающий в качестве аргумента произвольный объект, определяющий, в какую группу экземпляра 
класса Grouper попадет этот объект, и возвращающий ключ этой группы
При передаче экземпляра класса Grouper в функцию len() должно возвращаться количество групп в нем.
Помимо этого, экземпляр класса Grouper должен быть итерируемым объектом, то есть позволять перебирать свои группы, 
например, с помощью цикла for. В данном случае группа — это кортеж, первым элементом которого является ключ группы, 
вторым — список элементов группы. Группы при итерировании могут располагаться в произвольном порядке.
Также экземпляр класса Grouper должен поддерживать операцию проверки на принадлежность с помощью оператора in, в которой 
проверяется наличие в экземпляре класса Grouper группы с искомым ключом.
Наконец, экземпляр класса Grouper должен позволять получать элементы группы по ключу. В данном случае элементы группы 
должны быть представлены в виде списка, при этом элементы в списке должны располагаться в том порядке, в котором они 
были добавлены.
Примечание 1. Экземпляр класса Grouper не должен зависеть от итерируемого объекта, на основе которого он был создан. 
Другими словами, если исходный итерируемый объект изменится, то экземпляр класса Grouper измениться  не должен.
Примечание 2. Реализация класса может быть произвольной, то есть требований к наличию определенных атрибутов нет.
Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный 
класс используется только с корректными данными.
Sample Input 1:
    grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)
    
    print(grouper[2])
    print(grouper[3])
    print(grouper[4])
Sample Output 1:
    ['hi']
    ['bee', 'one', 'two']
    ['geek', 'five']
Sample Input 2:
    grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)
    
    print(3 in grouper)
    print('bee' in grouper)
Sample Output 2:
    True
    False
Sample Input 3:
    grouper = Grouper(['hi'], key=lambda s: s[0])
    
    grouper.add('hello')
    grouper.add('bee')
    grouper.add('big')
    grouper.add('geek')
    print(grouper['h'])
    print(grouper['b'])
    print(grouper['g'])
Sample Output 3:
    ['hi', 'hello']
    ['bee', 'big']
    ['geek']
Sample Input 4:
    grouper = Grouper(['hi'], key=lambda s: s[0])
    
    print(grouper.group_for('hello'))
    print(grouper.group_for('bee'))
    print(grouper['h'])
    print('b' in grouper)
Sample Output 4:
    h
    b
    ['hi']
    False
"""
class Grouper:
    def __init__(self, iterable, key):
        self.key = key
        self.__dct = {}
        for x in iterable:
            self.add(x)

    def add(self, obj):
        self.__dct.setdefault(self.key(obj), []).append(obj)

    def __getitem__(self, key):
        return self.__dct[key]

    def __iter__(self):
        yield from self.__dct.items()

    def group_for(self, obj):
        return self.key(obj)

    def __len__(self):
        return len(self.__dct)

    def __contains__(self, item):
        return item in self.__dct
