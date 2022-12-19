""" Упражнение 1
Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:
obj — произвольный объект
Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Repeater.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    bee = Repeater('bee')

    print(next(bee))
Sample Output 1:
    bee
Sample Input 2:
    geek = Repeater('geek')

    print(next(geek))
    print(next(geek))
    print(next(geek))
Sample Output 2:
    geek
    geek
    geek
"""
class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


""" Упражнение 2
Реализуйте класс BoundedRepeater, порождающий итераторы, конструктор которого принимает два аргумента в следующем 
порядке:
    obj — произвольный объект
    times — натуральное число
Итератор класса BoundedRepeater должен генерировать значение obj times раз, а затем возбуждать исключение StopIteration.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс BoundedRepeater.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    bee = BoundedRepeater('bee', 2)
    
    print(next(bee))
    print(next(bee))
Sample Output 1:
    bee
    bee
Sample Input 2:
    geek = BoundedRepeater('geek', 3)
    
    print(next(geek))
    print(next(geek))
    print(next(geek))
    
    try:
        print(next(geek))
    except StopIteration:
        print('Error')
Sample Output 2:
    geek
    geek
    geek
    Error
"""
class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times > 0:
            self.times -= 1
            return self.obj
        else:
            raise StopIteration


""" Упражнение 3
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:
n — натуральное число,
Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых является квадратом 
очередного натурального числа, а затем возбуждать исключение StopIteration.
Примечание 1. Последовательность квадратов натуральных чисел начинается с квадрата числа 11.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Square.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    squares = Square(2)
    
    print(next(squares))
    print(next(squares))
Sample Output 1:
    1
    4
Sample Input 2:
    squares = Square(10)
    
    print(list(squares))
Sample Output 2:
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Sample Input 3:
    squares = Square(1)
    
    print(list(squares))
Sample Output 3:
    [1]
"""


class Square:
    def __init__(self, n):
        self.n = n
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= self.n:
            res = self.x ** 2
            self.x += 1
            return res
        else:
            raise StopIteration


""" Упражнение 4
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.
Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 11.
Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, где каждое последующее число 
является суммой двух предыдущих:
1, 1, 2, 3, 5, 8, 13, 21, 34
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Fibonacci.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    fibonacci = Fibonacci()
    
    print(next(fibonacci))
Sample Output 1:
    1
Sample Input 2:
    fibonacci = Fibonacci()
    
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
Sample Output 2:
    1
    1
    2
    3
"""


class Fibonacci:
    def __init__(self):
        self.st, self.ed = 1, 1
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.ind += 1
        if self.ind <= 2:
            return 1
        else:
            res = self.st + self.ed
            self.st, self.ed = self.ed, res
            return res


""" Упражнение 5
Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:
    number — ненулевое число
Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных степеней числа number 
в порядке возрастания, начиная с нулевой степени.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс PowerOf.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input:
    power_of_two = PowerOf(2)
    
    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))
    print(next(power_of_two))
Sample Output:
    1
    2
    4
    8
"""

""" Упражнение 6
Как известно, во время итерации по словарю мы получаем ключи, а не значения или пары ключ-значение.
Приведенный ниже код:
    info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}
    
    print(*info)
выводит:
    name age gender
Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:
data — словарь
Итератор класса DictItemsIterator должен генерировать последовательность кортежей, представляющих собой 
пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.
Примечание 1. При решении задачи не используйте словарные методы keys(), values() и items().
Примечание 2. Пары ключ-значение в возвращаемом функцией итераторе должны располагаться в своем изначальном порядке.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс DictItemsIterator.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
    
    print(*pairs)
Sample Output 1:
    (1, 'A') (2, 'B') (3, 'C')
Sample Input 2:
    data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
    
    pairs = DictItemsIterator(data)
    
    print(*pairs)
Sample Output 2:
    (1, 1) (2, 4) (3, 9) (4, 16) (5, 25) (6, 36) (7, 49)
"""
class DictItemsIterator:
    def __init__(self, dct):
        self.dct = dct
        self.dct_name = list(reversed([(x, dct[x]) for x in dct]))

    def __iter__(self):
        return self

    def __next__(self):
        if self.dct_name:
            return self.dct_name.pop()
        else:
            raise StopIteration


""" Упражнение 7
Реализуйте класс CardDeck, порождающий итераторы, конструктор которого не принимает никаких аргументов.
Итератор класса CardDeck должен генерировать последовательность из 5252 игральных карт, а после возбуждать исключение 
StopIteration. Каждая карта должна представлять собой строку в следующем формате:
<номинал> <масть>
Например, 7 пик, валет треф, дама бубен, король червей, туз пик.
Примечание 1. Карты, генерируемые итератором, должны располагаться сначала по величине номинала, затем масти.
Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы. Старшинство карт в масти по возрастанию: 
двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.
Примечание 3. Масти не требуют склонения и независимо от номинала должны сохранять следующее написание: пик, треф, 
бубен, червей.
Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимый класс CardDeck.
Примечание 5. Тестовые данные доступны по ссылке.
Sample Input 1:
    cards = CardDeck()
    
    print(next(cards))
    print(next(cards))
Sample Output 1:
    2 пик
    3 пик
Sample Input 2:
    cards = list(CardDeck())
    
    print(cards[9])
    print(cards[23])
    print(cards[37])
    print(cards[51])
Sample Output 2:
    валет пик
    дама треф
    король бубен
    туз червей
"""
class CardDeck:
    def __init__(self):
        self.mark = ("пик", "треф", "бубен", "червей")
        self.mark_ind = 0
        self.values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.values_ind = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.mark_ind == len(self.mark):
            raise StopIteration
        self.values_ind += 1
        card = f'{self.values[self.values_ind]} {self.mark[self.mark_ind]}'
        if self.values_ind == len(self.values) - 1:
            self.mark_ind += 1
            self.values_ind = -1
        return card


""" Упражнение 8
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:
iterable — итерируемый объект
Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.
Примечание 1. Гарантируется, что итерируемый объект, передаваемый в конструктор класса, не является множеством и 
итератором.
Примечание 2. Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс Cycle.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    cycle = Cycle('be')
    
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
    print(next(cycle))
Sample Output 1:
    b
    e
    b
    e
Sample Input 2:
    cycle = Cycle([1])
    
    print(next(cycle) + next(cycle) + next(cycle))
Sample Output 2:
    3
Sample Input 3:
    cycle = Cycle(range(100_000_000))
    
    print(next(cycle))
    print(next(cycle))
Sample Output 3:
    0
    1
"""
class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.et_iter = iter(self.iterable)
        self.et_iter_len = len(iterable)
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.x == self.et_iter_len:
            self.et_iter = iter(self.iterable)
            self.x = 0
        self.x += 1
        return next(self.et_iter)


""" Упражнение 9
Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
left — целое число
right — целое число
n — натуральное число
Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел от left до right включительно, 
а затем возбуждать исключение StopIteration.
Примечание 1. Гарантируется, что left <= right.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс RandomNumbers.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    iterator = RandomNumbers(1, 1, 3)
    
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
Sample Output 1:
    1
    1
    1
Sample Input 2:
    iterator = RandomNumbers(1, 10, 2)
    
    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))
Sample Output 2:
    True
    True
"""
import random
class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return random.randint(self.left, self.right)
        else:
            raise StopIteration


""" Упражнение 10
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность букв:
    русского алфавита, если language имеет значение ru
    английского алфавита, если language имеет значение en
Примечание 1. Буква ё в русском алфавите не учитывается.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    ru_alpha = Alphabet('ru')
    
    print(next(ru_alpha))
    print(next(ru_alpha))
    print(next(ru_alpha))
Sample Output 1:
    а
    б
    в
Sample Input 2:
    en_alpha = Alphabet('en')
    
    letters = [next(en_alpha) for _ in range(28)]
    
    print(*letters)
Sample Output 2:
    a b c d e f g h i j k l m n o p q r s t u v w x y z a b
"""
from string import ascii_lowercase
class Alphabet:
    def __init__(self, language):
        self.ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.letters = ascii_lowercase if language == 'en' else self.ru
        self.i = 0
        self.let_len = len(self.letters)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.let_len:
            self.i = 0
        val = self.letters[self.i]
        self.i += 1
        return val


""" Упражнение 11
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
    start — целое или вещественное число
    end — целое или вещественное число
    step — целое или вещественное число, по умолчанию имеет значение 1
Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end, 
включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Xrange.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    evens = Xrange(0, 10, 2)
    
    print(*evens)
Sample Output 1:
    0 2 4 6 8
Sample Input 2:
    xrange = Xrange(0, 3, 0.5)
    
    print(*xrange, sep='; ')
Sample Output 2:
    0.0; 0.5; 1.0; 1.5; 2.0; 2.5
Sample Input 3:
    xrange = Xrange(10, 1, -1)
    
    print(*xrange)
Sample Output 3:
    10 9 8 7 6 5 4 3 2
Sample Input 4:
    xrange = Xrange(5, 10)
    
    print(*xrange)
Sample Output 4:
    5 6 7 8 9
"""
class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if abs(self.step) == self.step and self.start >= self.end:
            raise StopIteration
        elif abs(self.step) == -self.step and self.start <= self.end:
            raise StopIteration
        return self.start
