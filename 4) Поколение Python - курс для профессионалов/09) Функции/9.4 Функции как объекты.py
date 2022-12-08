""" Упражнение 1
Реализуйте функцию numbers_sum(), которая принимает один аргумент:
elems — список произвольных объектов
Функция должна возвращать сумму чисел (типы int и float), находящихся в списке elems, игнорируя все нечисловые объекты.
Если в списке elems нет чисел, функция должна вернуть число 0.
Также функция должна иметь следующую строку документации:
    Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию numbers_sum(), но не код,
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(numbers_sum([1, '2', 3, 4, 'five']))
Sample Output 1:
    8
Sample Input 2:
    print(numbers_sum(['beegeek', 'stepik', '100']))
Sample Output 2:
    0
Sample Input 3:
    print(numbers_sum.__doc__)
Sample Output 3:
    Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
"""
def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """
    return sum(filter(lambda x: isinstance(x, int | float), elems))


""" Упражнение 2
Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные строковые 
аргументы в верхнем регистре.
Примечание 1. Значения sep и end также должны переводиться в верхний регистр.
Примечание 2. В тестирующую систему сдайте программу, содержащую только переопределенную функцию print(), но не код, 
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Задача представлена исключительно в учебных целях, на практике применять подобное, конечно, не следует.
Sample Input 1:
    print('beegeek', [1, 2, 3], 4)
Sample Output 1:
    BEEGEEK [1, 2, 3] 4
Sample Input 2:
    print('bee', 'geek', sep=' and ', end=' wow')
Sample Output 2:
    BEE AND GEEK WOW
Sample Input 3:
    words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
    print(*words, sep=' to ', end=' LOVE')
Sample Output 3:
    BLACK TO WHITE TO GREY TO BLACK-1 TO WHITE-1 TO PYTHON LOVE
"""
old_print = print
def print(*args, **kwargs):
    kwargs['sep'] = kwargs.get('sep', ' ').upper()
    kwargs['end'] = kwargs.get('end', '\n').upper()
    old_print(*[x.upper() if isinstance(x, str) else x for x in args], **kwargs)


""" Упражнение 3
Реализуйте функцию polynom(), которая принимает один аргумент:
x — вещественное число
Функция должна возвращать значение выражения x^2 + 1
Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции, которые уже 
были вычислены.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию polynom(), но не код, 
вызывающий ее. 
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(polynom(5))
    print(polynom.values)
Sample Output 1:
    26
    {26}
Sample Input 2:
    polynom(1)
    polynom(2)
    polynom(3)
    
    print(*sorted(polynom.values))
Sample Output 2:
    2 5 10
Sample Input 3:
    for _ in range(10):
        polynom(10)
        
    print(polynom.values)
Sample Output 3:
    {101}
"""
def polynom(x):
    x = x**2 + 1
    polynom.__dict__.setdefault('values', set()).add(x)
    return x


""" Упражнение 4
Функция remove_marks()
Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:
    text — произвольная строка
    marks — набор символов
Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.
Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию remove_marks(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    text = 'Hi! Will we go together?'
    
    print(remove_marks(text, '!?'))
    print(remove_marks.count)
Sample Output 1:
    Hi Will we go together
    1
Sample Input 2:
    marks = '.,!?'
    text = 'Are you listening? Meet my family! There are my parents, my brother and me.'
    
    for mark in marks:
        print(remove_marks(text, mark))
        
    print(remove_marks.count)
Sample Output 2:
    Are you listening? Meet my family! There are my parents, my brother and me
    Are you listening? Meet my family! There are my parents my brother and me.
    Are you listening? Meet my family There are my parents, my brother and me.
    Are you listening Meet my family! There are my parents, my brother and me.
    4
"""
# Не совсем понятно, зачем обнулять строчку... Но это было необходимо для теста.
def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('call', []).append(text)
    remove_marks.count = len(remove_marks.call)
    return ''.join(x for x in text if x not in marks)

remove_marks.count = 0
