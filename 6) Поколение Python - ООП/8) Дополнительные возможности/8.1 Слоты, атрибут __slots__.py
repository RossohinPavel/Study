""" Упражнение 1
Реализуйте класс Shape, описывающий геометрическую фигуру. При создании экземпляра класс должен принимать три аргумента
в следующем порядке:
    name — название фигуры
    color — цвет фигуры
    area — площадь фигуры
Экземпляр класса Shape должен иметь три атрибута:
    name — название фигуры
    color — цвет фигуры
    area — площадь фигуры
Помимо приведенных выше трех атрибутов, экземпляр класса Shape не должен иметь возможности получить какие-либо другие
атрибуты.
Также экземпляр класса Shape должен иметь следующее неформальное строковое представление:
    <цвет фигуры> <название фигуры> (<площадь фигуры>)
Наконец, экземпляры класса Shape должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >,
<, >=, <=. Две фигуры считаются равными, если их площади совпадают. Фигура считается больше другой фигуры, если ее
площадь больше.
Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию,
должен вернуть константу NotImplemented.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 3. Никаких ограничений касательно реализации класса Shape нет, она может быть произвольной.
Sample Input 1:
    shape = Shape('triangle', 'red', 12)

    print(shape.name)
    print(shape.color)
    print(shape.area)
Sample Output 1:
    triangle
    red
    12
Sample Input 2:
    print(Shape('Square', 'Red', 4))
    Sample Output 2:

    Red Square (4)
Sample Input 3:
    print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
    print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))
Sample Output 3:
    True
    True
Sample Input 4:
    shape = Shape('triangle', 'red', 12)

    try:
        shape.perimeter = 9
    except AttributeError:
        print('Error')
Sample Output 4:
    Error
"""
from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = 'name', 'color', 'area'

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area < other.area
