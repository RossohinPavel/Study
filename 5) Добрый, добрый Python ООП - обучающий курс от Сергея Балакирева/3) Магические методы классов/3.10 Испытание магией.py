""" Упражнение
Испытание магией
Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/1dSxnEFfDu8
Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и решило дать вам испытание для подтверждения
уровня полученных навыков. Вам выпала великая честь создать полноценную программу игры в "Крестики-нолики". И вот перед
вами текст с заданием самого испытания.
Техническое задание
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты этого класса
будут создаваться командой:
    game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:
    pole - двумерный кортеж, размером 3x3.
Каждый элемент кортежа pole является объектом класса Cell:
    cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:
    value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.
Также с объектами класса Cell должна выполняться функция:
    bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.
К каждой клетке игрового поля должен быть доступ через операторы:
    res = game[i, j] # получение значения из клетки с индексами i, j
    game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать
исключение командой:
    raise IndexError('некорректно указанные индексы')
Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны
быть три публичных атрибута (атрибуты класса):
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
    init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
    show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
    human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
    computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).
Также в классе TicTacToe должны быть следующие объекты-свойства (property):
    is_human_win - возвращает True, если победил человек, иначе - False;
    is_computer_win - возвращает True, если победил компьютер, иначе - False;
    is_draw - возвращает True, если ничья, иначе - False.
Наконец, с объектами класса TicTacToe должна выполняться функция:
    bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в
противном случае.
Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):
    game = TicTacToe()
    game.init()
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1


    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем")
    else:
        print("Ничья.")
Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть в
"Крестики-нолики" между человеком и компьютером.
P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.
P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.
"""
from random import randint as rint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    WINNER = None

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def __getitem__(self, item):
        i, j = item
        if type(i) != int or not 0 <= i < 3 or type(j) != int or not 0 <= j < 3:
            raise IndexError('некорректно указанные индексы')
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        i, j = key
        if type(i) != int or not 0 <= i < 3 or type(j) != int or not 0 <= j < 3:
            raise IndexError('некорректно указанные индексы')
        self.pole[i][j].value = value
        self.__check_winner_()

    def init(self):
        self.WINNER = None
        for i in self.pole:
            for j in i:
                j.value = self.FREE_CELL

    def show(self):
        for i in self.pole:
            for j in i:
                string = '*'
                if j.value == 1:
                    string = 'X'
                if j.value == 2:
                    string = 'O'
                print(string, end=' ')
            print()

    def computer_go(self):
        i = rint(0, 2)
        j = rint(0, 2)
        while self[i, j] != 0:
            i = rint(0, 2)
            j = rint(0, 2)
        self[i, j] = self.COMPUTER_O

    def human_go(self):
        while True:
            i, j = map(int, input('Please input coords: ').split())
            if self[i, j] == 0:
                self[i, j] = self.HUMAN_X
                break

    def __check_winner_(self):
        def func(lst):
            lst = lst
            if lst == [1, 1, 1] and self.WINNER is None:
                self.WINNER = 'h'
            if lst == [2, 2, 2] and self.WINNER is None:
                self.WINNER = 'c'

        for i in self.pole:
            func([x.value for x in i])
        for i in zip(*self.pole):
            func([x.value for x in i])
        func([self[i, i] for i in range(3)])
        func([self[i, 3 - 1 - i] for i in range(3)])

    def __bool__(self):
        flag = False
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    flag = True
        if self.WINNER is not None:
            flag = False
        return flag

    @property
    def is_human_win(self):
        return True if self.WINNER == 'h' else False

    @property
    def is_computer_win(self):
        return True if self.WINNER == 'c' else False

    @property
    def is_draw(self):
        return not bool(self) and self.WINNER is None
