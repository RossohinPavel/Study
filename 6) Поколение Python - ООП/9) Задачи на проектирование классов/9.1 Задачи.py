""" Упражнение 1
Реализуйте функцию anything(), которая возвращает такой объект, результат сравнения с которым c помощью операторов ==,
!=, >, <, >= и <= всегда равен True.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию anything(), но не код,
вызывающий ее.
Sample Input:
    import math, re

    print(anything() != [])
    print(anything() < 'World')
    print(anything() > 81)
    print(anything() >= re)
    print(anything() <= math)
    print(anything() == ord)
Sample Output:
    True
    True
    True
    True
    True
    True
"""
class Anything:
    def __call__(self):
        return self

    def __ne__(self, other):
        return True

    __ge__ = __le__ = __gt__ = __lt__ = __eq__ = __ne__


anything = Anything()


""" Упражнение 2
Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector 
должен создаваться на основе собственных координат:
    a = Vector(1, 2, 3)
    b = Vector(3, 4, 5)
    c = Vector(5, 6, 7, 8)
В качестве неформального строкового представления вектор должен иметь собственные координаты, заключенные в круглые 
скобки:
    print(a)                       # (1, 2, 3)
    print(b)                       # (3, 4, 5)
    print(c)                       # (5, 6, 7, 8)
Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:
    print(a + b)                   # (4, 6, 8)
    print(a - b)                   # (-2, -2, -2)
    print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
    print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292
а также операции сравнения на равенство и неравенство:
    print(a == Vector(1, 2, 3))    # True
    print(a == Vector(4, 5, 6))    # False
При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено исключение ValueError 
с текстом:
Векторы должны иметь равную длину
"""
class Vector(tuple):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, args)

    def check(self, other):
        if len(self) != len(other):
            raise ValueError('Векторы должны иметь равную длину')

    def __add__(self, other):
        self.check(other)
        return Vector(*(self[i] + other[i] for i in range(len(self))))

    def __sub__(self, other):
        self.check(other)
        return Vector(*(self[i] - other[i] for i in range(len(self))))

    def __mul__(self, other):
        self.check(other)
        return sum(self[i] * other[i] for i in range(len(self)))

    def norm(self):
        return (self * self) ** 0.5

    def __eq__(self, other):
        self.check(other)
        return super().__eq__(other)

    def __ne__(self, other):
        self.check(other)
        return super().__eq__(other)


""" Упражнение 3
Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса 
CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования 
должен отвечать метод encode(), за операцию дешифрования — decode():
    cipher = CaesarCipher(5)
    print(cipher.encode('Beegeek'))      # Gjjljjp
    print(cipher.decode('Gjjljjp'))      # Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и 
дешифровке должен сохраняться.
Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они 
присутствуют, должны оставаться неизменными:
    print(cipher.encode('Биgeek123'))    # Биljjp123
    print(cipher.decode('Биljjp123'))    # Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26].
"""
class CaesarCipher:
    __chars_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __chars_l = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, shift):
        self.shift = shift

    def get_word(self, s, chars):
        flag = False
        count = -1
        while True:
            for c in chars:
                if c == s:
                    flag = True
                if flag:
                     count += 1
                if count == self.shift:
                    return c

    def encode(self, string):
        new_word = ''
        for w in string:
            if w in self.__chars_u:
                w = self.get_word(w, self.__chars_u)
            if w in self.__chars_l:
                w = self.get_word(w, self.__chars_l)
            new_word += w
        return new_word

    def decode(self, word):
        old_shift = self.shift
        self.shift = 26 - old_shift
        res = self.encode(word)
        self.shift = old_shift
        return res


""" Упражнение 4
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса 
ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:
    progression = ArithmeticProgression(0, 1)
    
    for elem in progression:
        if elem > 10:
            break
        print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.
Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании 
экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:
    progression = GeometricProgression(1, 2)
    
    for elem in progression:
        if elem > 10:
            break
        print(elem, end=' ')    # 1 2 4 8
Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.
"""
class ArithmeticProgression:
    _operation = lambda obj, x, y: x + y

    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            self.current = self.start
            return self.current
        self.current = self._operation(self.current, self.step)
        return self.current


class GeometricProgression(ArithmeticProgression):
    _operation = lambda obj, x, y: x * y


""" Упражнение 5
Реализуйте класс исключений DomainException. Также реализуйте класс Domain для работы с доменами. Класс Domain должен 
поддерживать три способа создания своего экземпляра: напрямую через вызов класса, а также с помощью двух методов класса 
from_url() и from_email():
    domain1 = Domain('pygen.ru')                       # непосредственно на основе домена
    domain2 = Domain.from_url('https://pygen.ru')      # на основе url-адреса
    domain3 = Domain.from_email('support@pygen.ru')    # на основе адреса электронной почты
При попытке создания экземпляра класса Domain на основе некорректных домена, url-адреса или адреса электронной почты 
должно быть возбуждено исключение DomainException с текстом:
    Недопустимый домен, url или email
В качестве неформального строкового представления экземпляр класса Domain должен иметь собственный домен:
    print(str(domain1))                                # pygen.ru
    print(str(domain2))                                # pygen.ru
    print(str(domain3))                                # pygen.ru
Примечание 1. Будем считать домен корректным, если он представляет собой последовательность из одной или более латинских 
букв, за которой следует точка, а затем снова одна или более латинских букв.
Примечание 2. Будем считать url-адрес корректным, если он представляет собой строку http:// или https://, за которой 
следует корректный домен. 
Примечание 3. Будем считать адрес электронной почты корректным, если он представляет собой последовательность из одной
или более латинских букв, за которой следует собачка (@), а затем корректный домен.
"""
import re


class DomainException(Exception):
    pass


def domain_check(func):
    def wrapper(obj, domain):
        if not re.fullmatch(r'(https?://|[a-zA-Z]+@)?[a-zA-Z]+\.[a-zA-Z]+', domain):
            raise DomainException('Недопустимый домен, url или email')
        return func(obj, re.sub(r'(https?://|[a-zA-Z]+@)?', '', domain))
    return wrapper


class Domain:
    @domain_check
    def __init__(self, domain):
        self.domain = domain

    @classmethod
    def from_url(cls, url):
        return cls(url)

    @classmethod
    def from_email(cls, email):
        return cls(email)

    def __str__(self):
        return self.domain


""" Упражнение 6
Предположим, что у нас имеется некоторая игра. За каждую игровую сессию игрок получает определенное количество баллов в 
зависимости от своего результата. Вашей задачей является реализация класса HighScoreTable — таблицы рекордов, которую 
можно будет обновлять с учетом итоговых результатов игрока.
Изначально таблица рекордов является пустой. Максимальное количество рекордов указывается при создании таблицы:
    high_score_table = HighScoreTable(3)
Таблица должна позволять просматривать текущие рекорды и добавлять новые результаты:
    print(high_score_table.scores)    # []
    high_score_table.update(10)
    high_score_table.update(8)
    high_score_table.update(12)
    print(high_score_table.scores)    # [12, 10, 8]
Текущие рекорды всегда должны располагаться в порядке убывания. Так как таблица содержит именно рекорды, то после 
заполнения таблицы добавляться должны только те результаты, которые лучше текущих:
    high_score_table.update(6)
    high_score_table.update(7)
    print(high_score_table.scores)    # [12, 10, 8]
    high_score_table.update(9)
    print(high_score_table.scores)    # [12, 10, 9]
Таблица должна поддерживать сброс всех результатов:
    high_score_table.reset()
    print(high_score_table.scores)    # []
"""
class HighScoreTable:
    def __init__(self, length):
        self.length = length
        self._scores = []

    @property
    def scores(self):
        return self._scores[:]

    def reset(self):
        self._scores.clear()

    def update(self, value):
        self._scores.append(value)
        self._scores.sort(reverse=True)
        self._scores = self._scores[:self.length]


""" Упражнение 7
Реализуйте класс Pagination для обработки данных с разбивкой по страницам. Разбивка по страницам используется для 
разделения большого количества данных на части. Экземпляр класса Pagination должен создаваться на основе двух значений:
    исходные данные, представленные в виде списка с произвольными элементами
    размер страницы, то есть количество элементов, отображаемых на каждой странице
alphabet = list('abcdefghijklmnopqrstuvwxyz')
pagination = Pagination(alphabet, 4)
Для получения содержимого страницы должен использоваться метод get_visible_items():
    print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']
Обратите внимание, содержимое страницы должно быть представлено в виде списка. Перемещение по страницам должно 
происходить с помощью следующих методов:
    prev_page() — вернуться к предыдущей странице
    next_page() — перейти к следующей странице
    first_page() — вернуться к первой странице
    last_page() — перейти к последней странице
    go_to_page() — перейти к странице с указанным номером (1 — первая страница, 2 — вторая страница, и так далее)
    pagination.next_page()
    print(pagination.get_visible_items())    # ['e', 'f', 'g', 'h']
    pagination.last_page()
    print(pagination.get_visible_items())    # ['y', 'z']
Методы для перемещения по страницам должны быть применимы друг за другом:
    pagination.first_page()
    pagination.next_page().next_page()   
    print(pagination.get_visible_items())    # ['i', 'j', 'k', 'l']
С помощью атрибутов total_pages и current_page должна быть возможность получить общее количество страниц и текущую 
страницу соответственно:
    print(pagination.total_pages)            # 7
    print(pagination.current_page)           # 3
При нахождении на первой странице и перемещении к предыдущей странице, текущей страницей должна остаться первая 
страница. Аналогично при нахождении на последней странице и перемещении к следующей странице, текущей страницей должна 
остаться последняя страница:
    pagination.first_page()
    pagination.prev_page()
    print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']
    
    pagination.last_page()
    pagination.next_page()
    print(pagination.get_visible_items())    # ['y', 'z']
При перемещении к нулевой или менее странице, текущей страницей должна стать первая страница. Аналогично при перемещении 
к странице, номер которой превышает общее количество страниц, текущей страницей должна стать последняя страница:
    pagination.go_to_page(-100)
    print(pagination.get_visible_items())    # ['a', 'b', 'c', 'd']
    
    pagination.go_to_page(100)
    print(pagination.get_visible_items())    # ['y', 'z']
"""
class Pagination:
    def __init__(self, iterable, length):
        self._matrix = [iterable[i:i+length] for i in range(0, len(iterable), length)]
        self.page = 0

    @property
    def total_pages(self):
        return len(self._matrix)

    @property
    def current_page(self):
        return self.page + 1

    def get_visible_items(self):
        return self._matrix[self.page]

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
        return self

    def next_page(self):
        if self.page < len(self._matrix) - 1:
            self.page += 1
        return self

    def first_page(self):
        self.page = 0

    def last_page(self):
        self.page = len(self._matrix) - 1

    def go_to_page(self, num):
        if num >= 0:
            res = -1 + num
            if res > len(self._matrix) - 1:
                res = len(self._matrix) - 1
        if num < 0:
            res = len(self._matrix) - 1 + num
            if res < 0:
                res = 0
        self.page = res


""" Упражнение 8
В этой задаче вам необходимо реализовать класс Testpaper, который позволит составлять экзаменационные тесты. Каждый тест 
должен создаваться на основе темы, схемы верных ответов и минимального процента верных решений:
    testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
    testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
    testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
Созданные тесты должны сдаваться студентом — экземпляром класса Student. Он должен иметь метод take_test(), который 
принимает в качестве аргументов тест и ответы студента на этот тест:
    student1 = Student()
    student2 = Student()
    
    student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
    student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
    student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
Результаты тестов должны быть доступны в виде словаря, ключом в котором является тема теста, а значением — результат 
теста (сдан или не сдан), а также процент верных решений:
    print(student1.tests_taken)    # {'Maths' : 'Passed! (80%)'}
    print(student2.tests_taken)    # {'Chemistry' : 'Failed! (25%)', 'Computing' : 'Failed! (43%)'}
Если студент еще не сдал ни одного теста, атрибут tests_taken должен содержать строку No tests taken:
    student3 = Student()
    
    print(student3.tests_taken)    # No tests taken
Примечание 1. Округление процента верных решений должно происходить до ближайшего целого числа
"""
class Testpaper:
    def __init__(self, name, answers, percent):
        self.name = name
        self.answers = answers
        self.percent = int(percent[:2])


class Student:
    def __init__(self):
        self._tests_taken = {}

    @property
    def tests_taken(self):
        if self._tests_taken:
            return self._tests_taken
        return 'No tests taken'

    def take_test(self, test, answers):
        balls = round(sum(test.answers[x] == answers[x] for x in range(len(answers))) / len(test.answers) * 100)
        res = 'Passed!' if balls >= test.percent else 'Failed!'
        self._tests_taken[test.name] = f'{res} ({balls}%)'


""" Упражнение 9
Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр класса TicTacToe должен представлять собой игровое поле 
из трех строк и трех столбцов, на котором игроки по очереди могут помечать свободные клетки. Первый ход делает игрок, 
ставящий крестики:
    tictactoe = TicTacToe()
    
    tictactoe.mark(1, 1)         # помечаем крестиком клетку с координатами (1; 1)
    tictactoe.mark(3, 1)         # помечаем ноликом клетку с координатами (3; 1)
Помечать уже помеченные клетки нельзя. При попытке сделать это должен быть выведен текст Недоступная клетка:
    tictactoe.mark(1, 1)         # Недоступная клетка
    
    tictactoe.mark(1, 3)         # помечаем крестиком клетку с координатами (1; 3)
    tictactoe.mark(1, 2)         # помечаем ноликом клетку с координатами (1; 2)
    tictactoe.mark(3, 3)         # помечаем крестиком клетку с координатами (3; 3)
    tictactoe.mark(2, 2)         # помечаем ноликом клетку с координатами (2; 2)
    tictactoe.mark(2, 3)         # помечаем крестиком клетку с координатами (2; 3)
С помощью метода winner() должна быть возможность узнать победителя игры. Метод должен вернуть:
    символ X, если победил игрок, ставящий крестики
    символ O, если победил игрок, ставящий нолики
    строку Ничья, если произошла ничья
    значение None, если победитель еще не определен
    print(tictactoe.winner())    # X
Помечать клетки после завершения игры нельзя. При попытке сделать это должен быть выведен текст Игра окончена:
    tictactoe.mark(2, 1)         # Игра окончена
С помощью метода show() должна быть возможность посмотреть текущее состояние игрового поля. Оно должно быть построено из 
символов | и -, а также X и O, если игроками были сделаны какие-либо ходы. Для приведенного выше поля tictactoe вызов 
tictactoe.show() должен вывести следующее:
    X|O|X
    -----
     |O|X
    -----
    O| |X
"""
class TicTacToe:
    def __init__(self):
        self._field = [['' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self._winner = None

    def check(self):
        x_winner = ['X', 'X', 'X']
        o_winner = ['O', 'O', 'O']
        if all([y for x in self._field for y in x]):
            self._winner = 'Ничья'
        for l in self._field:
            if l == x_winner or l == o_winner:
                self._winner = l[0]
        for i in range(3):
            lst = [self._field[j][i] for j in range(3)]
            if lst == x_winner or lst == o_winner:
                self._winner = lst[0]
        lst = [self._field[j][j] for j in range(3)]
        if lst == x_winner or lst == o_winner:
            self._winner = lst[0]
        lst = [self._field[j][2-j] for j in range(3)]
        if lst == x_winner or lst == o_winner:
            self._winner = lst[0]

    def mark(self, x, y):
        if self._winner:
            print('Игра окончена')
            return
        if self._field[x - 1][y - 1] == '' and self._winner is None:
            self._field[x - 1][y - 1] = self.player
            self.player = {'X': 'O', 'O': 'X'}[self.player]
        else:
            print('Недоступная клетка')
        self.check()

    def winner(self):
        return self._winner

    def show(self):
        for i in range(len(self._field)):
            print('|'.join(x if x else ' ' for x in self._field[i]))
            if i < len(self._field)-1:
                print('-'*5)


""" Упражнение 10
В этой задаче вам необходимо реализовать поле для игры в Сапера в виде двух классов Game и Cell. Экземпляр первого 
класса будет описывать само игровое поле, экземпляр класса Cell — одну его ячейку. Экземпляр класса Game должен 
создаваться на основе трех значений: количество строк (длина поля), количество столбцов (ширина поля) и общее количество 
мин на поле:
    game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин
Количество строк и столбцов, а также общее количество мин должны быть доступны по соответствующим атрибутам:
    print(game.rows)           # 14
    print(game.cols)           # 18
    print(game.mines)          # 40
Также экземпляр класса Game должен иметь атрибут board, представляющий игровое поле в виде двумерного списка. Количество 
подсписков в этом списке должно совпадать с количеством строк, количество элементов в подсписках — с количеством 
столбцов. Каждый элемент подсписка должен представлять собой экземпляр класса Cell и иметь соответствующий набор 
атрибутов:
    cell = game.board[0][0]
    
    print(cell.row)            # 0; строка ячейки
    print(cell.col)            # 0; столбец ячейки
    print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
    print(cell.open)           # True или False в зависимости от того, открыта ячейка или нет, по умолчанию закрыта
    print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках
Игровое поле при создании должно заполняться минами случайным образом.
Примечание 1. Для проверки того, что в экземпляре класса Cell хранится верное количество мин в соседних ячейках, в одном 
из тестов мы используем собственную функцию get_neighbours_count(), которая которая считает это количество.
"""
import random


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.open = False
        self.neighbours = 0


class Game:
    def __init__(self, rows, cols, mine):
        self.rows = rows
        self.cols = cols
        self.mine = mine
        self.board = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.mine_plant()
        self.update_cell_info()

    def mine_plant(self):
        for cell in random.sample([y for x in self.board for y in x], self.mine):
            cell.mine = True

    def update_neighbours(self, i, j):
        for i_i in range(-1, 2):
            for j_j in range(-1, 2):
                nei_i, nei_j = i + i_i, j + j_j
                if 0 <= nei_i < self.rows and 0 <= nei_j < self.cols:
                    self.board[nei_i][nei_j].neighbours += 1

    def update_cell_info(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].mine is True:
                    self.update_neighbours(i, j)

    def show(self):
        for row in self.board:
            lst = []
            for el in row:
                sym = ' '
                if el.neighbours > 0:
                    sym = str(el.neighbours)
                if el.mine is True:
                    sym = '*'
                lst.append(sym)
            print(lst)


""" Упражнение 11
Реализуйте класс Currency для работы со значениями в различных валютах. Экземпляр класса Currency должен создаваться на 
основе числового значения и валюты:
    money1 = Currency(10, 'EUR')
    money2 = Currency(20, 'USD')
Поддерживаемые валюты: EUR (евро), USD (доллар) и RUB (рубль).
В качестве неформального строкового представления экземпляр класса Currency должен иметь собственное числовое значение и 
валюту:
    print(money1)                                      # 10 EUR
    print(money2)                                      # 20 USD
Экземпляр класса Currency должен поддерживать операцию конвертации в другую валюту с помощью метода change_to():
    money1.change_to('RUB')
    print(money1)                                      # 900 RUB
Экземпляры класса Currency должны поддерживать между собой операции сложения, вычитания, умножения и деления с помощью 
операторов +, -, * и / соответственно:
    print(Currency(5, 'EUR') + Currency(5, 'EUR'))     # 10 EUR
    print(Currency(5, 'EUR') + Currency(11, 'USD'))    # 15.0 EUR
    print(Currency(5, 'RUB') + Currency(11, 'USD'))    # 905.0 RUB
    print(Currency(5, 'USD') * Currency(5, 'EUR'))     # 27.5 USD
Обратите внимание, результирующую валюту должен определять левый операнд. 
Примечание. Таблица курсов валют:
    1 EUR	90 RUB
    1 EUR	1.1 USD
"""
class Currency:
    __RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1, 'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
    }

    def __init__(self, value, valute):
        self.value = value
        self.valute = valute

    def __str__(self):
        return str(round(self.value, 2)) + ' ' + self.valute

    def change_to(self, new_valute):
        self.value = self.value * self.__RATE[self.valute][new_valute]
        self.valute = new_valute

    def __add__(self, other):
        if other.valute != self.valute:
            other.change_to(self.valute)
        return Currency(self.value + other.value, self.valute)

    def __sub__(self, other):
        if other.valute != self.valute:
            other.change_to(self.valute)
        return Currency(self.value - other.value, self.valute)

    def __mul__(self, other):
        if other.valute != self.valute:
            other.change_to(self.valute)
        return Currency(self.value * other.value, self.valute)

    def __truediv__(self, other):
        if other.valute != self.valute:
            other.change_to(self.valute)
        return Currency(round(self.value / other.value, 2), self.valute)


""" Упражнение 12
Реализуйте класс Selfie, экземпляры которого запоминают свои предыдущие состояния и умеют восстанавливаться до тех 
состояний, в которых они были раньше. Под состоянием объекта понимается определенный набор атрибутов и соответствующих 
значений. Во время жизни экземпляр класса Selfie может различными способами изменять свое состояние, например, получать 
новые атрибуты или изменять значения имеющихся:
    obj = Selfie()
    
    obj.x = 1
    obj.y = 2
Для фиксации текущего состояния экземпляра класса Selfie должен использоваться метод save_state(): 
    obj.save_state()              # фиксируем состояние: x=1, y=2
    obj.x = 0                     # изменяем состояние
    obj.y = 0                     # изменяем состояние
Зафиксированные состояния экземпляра класса Selfie должны индексироваться: первое зафиксированное состояние должно иметь 
индекс 0, второе — 1, третье — 2, и так далее. По этим же индексам должна быть возможность возвращаться к необходимым 
состояниям:
    print(obj.x)                  # 0
    print(obj.y)                  # 0
    obj = obj.recover_state(0)    # возвращаемся к первому состоянию
    print(obj.x)                  # 1
    print(obj.y)                  # 2
Обратите внимание, что при возвращении к одному из предыдущих состояний с помощью метода recover_state() должен 
возвращаться новый экземпляр класса Selfie, имеющий необходимое состояние. Если в метод recover_state() передан индекс, 
по которому экземпляр класса Selfie не имеет состояние, должен быть возвращен текущий экземпляр:
    obj = obj.recover_state(7)
    print(obj.x)                  # 1
    print(obj.y)                  # 2
Каждый экземпляр класса Selfie должен знать, сколько состояний он зафиксировал:
    obj = Selfie()
    
    print(obj.n_states())         # 0
    obj.x = 0
    obj.save_state()
    obj.x = 1
    obj.save_state()
    obj.x = 2
    obj.save_state()
    print(obj.n_states())         # 3
"""
class Selfie:
    def __init__(self):
        self._states = []

    def save_state(self):
        self._states.append({k: v for k, v in self.__dict__.items() if k != '_states'})

    def n_states(self):
        return len(self._states)

    def recover_state(self, n):
        if 0 <= n < len(self._states):
            res = Selfie()
            res.__dict__.update(self._states[n])
            res._states = self._states[:n]
            return res
        return self


""" Упражнение 13
Реализуйте класс MultiKeyDict, который практически во всем повторяет класс dict. Создание экземпляра класса MultiKeyDict
должно происходить аналогично созданию экземпляра класса dict:
    multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
    multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])
    print(multikeydict1['x'])        # 1
    print(multikeydict2['z'])        # 3
Особенностью класса MultiKeyDict должен являться метод alias(), который должен позволять давать имеющимся ключам 
псевдонимы. Обращение по созданному псевдониму не должно ничем отличаться от обращения по оригинальному ключу, то есть 
с момента создания псевдонима у значения становится два ключа (или больше, если псевдонимов несколько):
    multikeydict = MultiKeyDict(x=100, y=[10, 20])
    multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
    multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
    print(multikeydict['z'])         # 100
    multikeydict['t'] += 1
    print(multikeydict['x'])         # 101
    multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
    multikeydict['z'] += [30]
    print(multikeydict['y'])         # [10, 20, 30]
Значение должно оставаться доступным по псевдониму даже в том случае, если оригинальный ключ был удален:
    multikeydict = MultiKeyDict(x=100)
    multikeydict.alias('x', 'z')
    del multikeydict['x']
    print(multikeydict['z'])         # 100
Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним совпадают, то все операции при обращении 
к ним должны выполняться именно с ключом:
    multikeydict = MultiKeyDict(x=100, y=[10, 20])
    multikeydict.alias('x', 'y')
    print(multikeydict['y'])         # [10, 20]
"""
from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.psevdonim = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, psevdo):
        self.psevdonim[psevdo] = key

    def __getitem__(self, item):
        if item in self.psevdonim and item not in self:
            item = self.psevdonim[item]
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if key in self.psevdonim and key not in self:
            key = self.psevdonim[key]
        super().__setitem__(key, value)

    def __delitem__(self, key):
        if key in self.psevdonim and key not in self:
            key = self.psevdonim[key]
        res = self[key]
        psevdo_keys = tuple(k for k, v in self.psevdonim.items() if v == key)
        self.psevdonim = {k: v for k, v in self.psevdonim.items() if v != key}
        for k in psevdo_keys:
            self[k] = res
        super().__delitem__(key)


""" Упражнение 14
Предикат — это функция, которая возвращает True или False в зависимости от переданных аргументов.
Реализуйте декоратор @predicate, который будет позволять удобно комбинировать предикаты с помощью операторов &, | и ~:
    @predicate
    def is_even(num):
        return num % 2 == 0
    
    @predicate
    def is_positive(num):
        return num > 0
    
    print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
    print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
    print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
    print((~is_even & is_positive)(3))            # True; равнозначно not is_even(4) and is_positive(4)
Декоратор должен уметь работать с любыми предикатами, независимо от того, сколько аргументов они принимают:
    @predicate
    def to_be():
        return True
    
    print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()
    
    @predicate
    def is_equal(a, b):
        return a == b
    
    @predicate
    def is_less_than(a, b):
        return a < b
    
    print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)
Также должны поддерживаться как позиционные аргументы, так и именованные:
    print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
    print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)
Задекорированная функция должна быть доступна вне комбинаций с другими функциями и вести себя как исходная функция:
    @predicate
    def is_less_than(a, b):
        return a < b
    
    print(is_less_than(1, 2))                     # True
    print(is_less_than(2, 2))                     # False
    print(is_less_than(3, 2))                     # False
Примечание 1. Гарантируется, что комбинируемые функции имеют одинаковые сигнатуры. 
"""
class predicate:
    def __init__(self, func):
        self.func = func

    def __invert__(self):
        def inner(*args, **kwargs):
            return not self.func(*args, **kwargs)
        return predicate(inner)

    def __or__(self, other):
        def inner(*args, **kwargs):
            return self.func(*args, **kwargs) | other.func(*args, **kwargs)
        return inner

    def __and__(self, other):
        def inner(*args, **kwargs):
            return self.func(*args, **kwargs) & other.func(*args, **kwargs)
        return inner

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
