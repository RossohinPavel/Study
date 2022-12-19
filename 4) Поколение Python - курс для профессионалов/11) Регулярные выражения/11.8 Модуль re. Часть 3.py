""" Упражнение 1
Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:
filename — название файла, имеющее расширение jpeg или jpg, которое может быть записано буквами произвольного регистра
Функция должна возвращать новое название файла с нормализованным расширением — jpg.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию normalize_jpeg(),
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(normalize_jpeg('stepik.jPeG'))
Sample Output 1:
    stepik.jpg
Sample Input 2:
    print(normalize_jpeg('mountains.JPG'))
Sample Output 2:
    mountains.jpg
Sample Input 3:
    print(normalize_jpeg('windows11.jpg'))
Sample Output 3:
    windows11.jpg
"""
import re

def normalize_jpeg(m):
    return re.sub(r'.+?\.', r'gpj.', m[::-1], count=1)[::-1]


""" Упражнение 2
Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:
string — произвольная строка
Функция должна заменять все множественные пробелы в строке string на единственный пробел и возвращать полученный 
результат.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию normalize_whitespace(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(normalize_whitespace('AAAA                A                AAAA'))
Sample Output 1:
    AAAA A AAAA
Sample Input 2:
    print(normalize_whitespace('Тут нет лишних пробелов'))
Sample Output 2:
    Тут нет лишних пробелов
Sample Input 3:
    print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
Sample Output 3:
    Тут н е т л и шних пробелов 
"""
import re

def normalize_whitespace(m):
    return re.sub(r' +', r' ', m)


""" Упражнение 3
В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов. Для 
получения списка всех ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword.
Приведенный ниже код:
    import keyword
    
    print(keyword.kwlist)
выводит:
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
    'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
    'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.
Формат входных данных
На вход программе подается строка.
Формат выходных данных
Программа должна в введенном тексте заменить все ключевые слова (в любом регистре) на строку <kw> и вывести полученный 
результат.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    True, assert, as, false, or, Import
Sample Output 1:
    <kw>, <kw>, <kw>, <kw>, <kw>, <kw>
Sample Input 2:
    True or False - that's the question
Sample Output 2:
    <kw> <kw> <kw> - that's the question
Sample Input 3:
    True and False - that is the question
Sample Output 3:
    <kw> <kw> <kw> - that <kw> the question
"""
import re
import keyword

kwl = [x.lower() for x in keyword.kwlist]

def replace(m):
    return '<kw>' if m.group().lower() in kwl else m.group()

print(re.sub(r'\w+', replace, input()))


""" Упражнение 4
Напишите программу, которая меняет местами первые две буквы в каждом слове, состоящем из двух или более букв.
Формат входных данных
На вход программе подается строка, содержащая слова.
Формат выходных данных
Программа должна в введенной строке заменить первые две буквы в каждом слове, состоящем из двух или более букв, 
и вывести полученный результат.
Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, 
соответствующими \W.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    This is Python
Sample Output 1:
    hTis si yPthon
Sample Input 2:
    Hi, everyone. Lets start a lesson!
Sample Output 2:
    iH, veeryone. eLts tsart a elsson!
"""
import re

print(re.sub(r'(\w)(\w)(\w*)', r'\2\1\3', input()))


""" Упражнение 5
Назовем умножением строки на число запись в формате n(string), где n — неотрицательное целое число, а string — строка, 
которая должна быть записана n раз. Раскрытием умножения будем считать развернутый вариант данной записи, например, 
строка ti2(Be)3(Ge) после раскрытия в ней всех умножений будет иметь вид tiBeBeGeGeGe.
Напишите программу, которая раскрывает все умножения в тексте и выводит полученный результат.
Формат входных данных
На вход программе подается одна строка, содержащая строчные латинские буквы, числа и скобки.
Формат выходных данных
Программа должна вывести строку, в которой раскрыты все умножения с учетом приоритетности операций.
Примечание 1. Гарантируется, что умножение в подаваемой строке всегда записано корректно, то есть строго в формате 
n(string). Записи вида 4(2), 3q, (fg)7 не корректны.
Примечание 2. Рассмотрим третий тест. С учетом приоритетности операций сначала раскрываем умножение 2(a) и получаем 
промежуточную строку bbbb10(aa)bbb, далее раскрываем умножение 10(aa) и получаем конечный результат в виде строки 
bbbbaaaaaaaaaaaaaaaaaaaabbb.
Примечание 3. Строка, в которой раскрыты все умножения, всегда содержит исключительно строчные латинские буквы.
Примечание 4. Максимальная длина результирующей строки не превосходит 450000450000 символов.
Примечание 5. Тестовые данные доступны по ссылке.
Sample Input 1:
    hello3(world)hi
Sample Output 1:
    helloworldworldworldhi
Sample Input 2:
    0(s)he0(be)lie0(ve)d
Sample Output 2:
    helied
Sample Input 3:
    bbbb10(2(a))bbb
Sample Output 3:
    bbbbaaaaaaaaaaaaaaaaaaaabbb
Sample Input 4:
    hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd
Sample Output 4:
    hiprivdiiidddiiidddiiiddqqprivdiiidddiiidddiiiddqqbqwqdd
Sample Input 5:
    hhhhhh
Sample Output 5:
    hhhhhh
"""
import re

string = input()

def replace(m):
    digit = int(*re.findall(r'\d+', m.group()))
    alpha = ''.join(re.findall(r'\((\w+)\)', m.group()))
    return alpha * digit

while '(' in string:
    string = re.sub(r'\d+\(\w+\)', replace, string)

print(string)


""" Упражнение 6
Напишите программу, которая заменяет все повторяющиеся рядом стоящие слова на одно слово.
Формат входных данных
На вход программе подается строка, содержащая слова.
Формат выходных данных
Программа должна в введенной строке заменить все повторяющиеся рядом стоящие слова на одно слово и вывести полученный 
результат.
Примечание 1. Программа должна быть чувствительной к регистру, то есть, например, слова python и Python считаются 
различными.
Примечание 2. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, 
соответствующими \W.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik
Sample Output 1:
    beegeek! python.. Python.. stepik
Sample Input 2:
    hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!
Sample Output 2:
    hi, hello, HELLO, hello!
Sample Input 3:
    wow Wow wow WOW
Sample Output 3:
    wow Wow wow WOW
"""
import re

string = input()

def replace(m):
    return re.findall(r'\w+', m.group())[-1]

while re.subn(r'\b(\w+?)\W+(\1)\b', replace,  string)[1] != 0:
    string = re.sub(r'\b(\w+?)\W+(\1)\b', replace,  string)

print(string)


""" Упражнение 7
При написании программ мы нередко оставляем комментарии или строки-документации к функциям. Определим три вида 
комментариев:

однострочные комментарии — строки кода, начинающиеся с символа решетки #. Однострочные комментарии могут находиться на 
любом уровне вложенности. Например: 
# это однострочный комментарий

def func(a, b):
    # это однострочный комментарий
    return a + b
комментарии, следующие непосредственно за строкой кода. Другими словами, это строка кода, за которой следуют 2 пробела, 
символ решетки #, пробел и сам комментарий, например:
numbers = [1, 2, 3]  # это комментарий
многострочные комментарии — одна или несколько строк кода, которые начинаются и заканчиваются тремя кавычками . 
Многострочные комментарии могут находиться на любом уровне вложенности. Например:
то многострочный комментарий
def func(a, b):
    это
    многострочный
    комментарий
    return a + b
Напишите программу, которая удаляет все комментарии из Python кода.
Формат входных данных
На вход программе подается произвольное число строк, представляющих собой Python код.
Формат выходных данных
Программе должна удалить все комментарии из введенного кода согласно условию задачи и вывести полученный результат.
Примечание 1. Пустые строки в начале и конце всего Python кода, а также пробелы в конце строк кода при сравнении 
ответов не учитываются. Другими словами, записи:
a = int(input())
a = int(input())
a = int(input())
считаются одинаковыми.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input:
hello everyone
welcome to my project

import math  # importing a useful math module

# let's take a look at some functions

def circle_area(radius):
    coming soon
    return math.pi * r ** 2  # my favorite formula

def triangle_area(base, height):
    ""\"the function takes
    the base and height
    of a triangle and
    returns its area\"""
    return 0.5 * base * height
Sample Output:


import math


def circle_area(radius):
    return math.pi * r ** 2

def triangle_area(base, height):
    return 0.5 * base * height
"""
import re
import sys

code = sys.stdin.read()
code = re.sub(r'^ *#.*?\n', r'', code, count=0, flags=re.M | re.S)
code = re.sub(r' *#( .+)+', r'', code)
code = re.sub(r' *""".+"""\n', r'', code)
code = re.sub(r'^""".+?"""\n', r'', code, count=0, flags=re.M | re.S)
code = re.sub(r'""".+?"""\n *', r'', code, count=0, flags=re.M | re.S)
print(code)
