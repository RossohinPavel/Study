""" Упражнение 1
Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение переданного параметра на 5 и
возвращала бы вычисленный результат. При этом внешняя функция должна иметь следующую сигнатуру: def counter_add(): ...
Вызовите функцию counter_add и результат ее работы присвойте переменной с именем cnt. Вызовите внутреннюю функцию через
переменную cnt со значением k, введенным с клавиатуры: k = int(input()) Выведите результат на экран.
Sample Input: 7
Sample Output: 12
"""
k = int(input())
def counter_add(n=0):
    def plus():
        nonlocal n
        n += 5
        return n
    return plus
cnt = counter_add(k)
print(cnt())


""" Упражнение 2
Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего аргумента на некоторую 
величину n - параметр внешней функции с сигнатурой: def counter_add(n): ...
Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt. Вызовите внутреннюю 
функцию через переменную cnt со значением k, введенным с клавиатуры: k = int(input()) Выведите результат на экран.
Sample Input: 5
Sample Output: 7
"""
def counter_add(n=0):
    def plus(k):
        k += n
        return k
    return plus
k = int(input())
cnt = counter_add(2)
print(cnt(k))


""" Упражнение 3
Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s (s - строка, параметр 
внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного 
замыкания. Результат выведите на экран. P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
Sample Input: Balakirev
Sample Output: <h1>Balakirev</h1>
"""
def set_tag(tag='h1'):
    def proc(s):
        return f'<{tag}>{s}</{tag}>'
    return proc
a = input()
tt = set_tag()
print(tt(a))


""" Упражнение 4
Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s (s - строка, параметр внутренней 
функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции. 
Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым. Вторую строку нужно 
поместить в тег из первой строки с помощью реализованного замыкания. Результат выведите на экран.
P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
Sample Input: div Сергей Балакирев
Sample Output: <div>Сергей Балакирев</div>
"""
def set_tag(tag='h1'):
    def proc(s):
        return f'<{tag}>{s}</{tag}>'
    return proc
atag = input()
aname = input()
tt = set_tag(tag=atag)
print(tt(aname))


""" Упражнение 5
Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел, записанных 
через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции. Если tp = 'list', 
то используется список, иначе (при другом значении) - кортеж. Далее, на вход программы поступают две строки: 
первая - это значение для параметра tp; вторая - список целых чисел, записанных через пробел. С помощью реализованного 
замыкания преобразовать эти данные в соответствующую коллекцию. Результат вывести на экран командой 
(lst - ссылка на коллекцию): print(lst)
Sample Input:
    list
    -5 6 8 11 0 111 -456 3
Sample Output:
    [-5, 6, 8, 11, 0, 111, -456, 3]
"""
def ret_type(tp='tuple'):
    def set_type(col):
        col = list(map(int, col.split()))
        return col if tp=='list' else tuple(col)
    return set_type
at = input()
al = input()
lst = ret_type(at)
print(lst(al))
