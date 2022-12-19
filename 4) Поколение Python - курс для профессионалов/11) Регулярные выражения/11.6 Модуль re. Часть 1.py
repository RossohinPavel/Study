""" Упражнение 1
Вам доступен набор телефонных номеров, имеющих следующие форматы:
    <код страны>-<код города>-<номер>
    <код страны> <код города> <номер>
в котором код страны и код города представлены последовательностями от одной до трех цифр включительно, а номер —
последовательностью от четырех до десяти цифр включительно. Между кодом страны, кодом города и номером используется
разделитель, которым служит либо символ дефис, либо пробел, причем одновременно оба вида разделителя в одном номере
присутствовать не могут.
Напишите программу, которая принимает произвольное количество телефонных номеров и для каждого выводит отдельно его код
страны, код города и номер.
Формат входных данных
На вход программе подается произвольное количество телефонных номеров, удовлетворяющих приведенным выше шаблонам,
каждый на отдельной строке.
Формат выходных данных
Программа должна для каждого введенного телефонного номера вывести отдельно его код страны, код города и номер в
следующем формате:
    Код страны: <код страны>, Код города: <код города>, Номер: <номер>
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    1 877 2638277
    91-011-23413627
Sample Output 1:
    Код страны: 1, Код города: 877, Номер: 2638277
    Код страны: 91, Код города: 011, Номер: 23413627
Sample Input 2:
    148-809-2561957985
    1 5 5864
    91-454-91954
Sample Output 2:
    Код страны: 148, Код города: 809, Номер: 2561957985
    Код страны: 1, Код города: 5, Номер: 5864
    Код страны: 91, Код города: 454, Номер: 91954
"""
import sys
import re

for i in sys.stdin:
    r = re.fullmatch(r'(\d{1,3})([ -])(\d{1,3})(\2)(\d{4,10})', i.strip()).groups()
    print(f'Код страны: {r[0]}, Код города: {r[2]}, Номер: {r[4]}')


""" Упражнение 2
В онлайн-школе BEEGEEK логин учетной записи определяется следующим образом:
    первым символом является символ нижнего подчеркивания _
    затем следуют одна или более цифр
    после записываются ноль или более латинских букв в произвольном регистре
логин может иметь на конце необязательный символ нижнего подчеркивания _
Напишите программу, которая принимает произвольное количество строк и определяет, какие из них представляют собой 
корректный логин онлайн-школы BEEGEEK.
Формат входных данных
На вход программе подаётся произвольное количество строк, каждая из которых содержит набор произвольных символов.
Формат выходных данных
Программа должна для каждой введенной строки вывести True, если она представляет собой корректный логин онлайн-школы 
BEEGEEK, или False в противном случае.
Примечание. Тестовые данные доступны по ссылке. 
Sample Input 1:
    _123abc_
    _1abc_
    123abc
    _abc123
Sample Output 1:
    True
    True
    False
    False
Sample Input 2:
    _1
    _1_
Sample Output 2:
    True
    True
"""
import sys
import re

for i in sys.stdin:
    print(True if re.fullmatch(r'_\d+[A-Za-z]*_*', i.strip()) else False)


""" Упражнение 3
Напишите программу, которая выводит слова, состоящие из двух одинаковых слогов.
Формат входных данных
На вход программе подается произвольное количество слов, каждое на отдельной строке.
Формат выходных данных
Программа должна из введенных слов вывести только те, которые состоят из двух одинаковых слогов. Слова должны быть 
расположены в своем исходном порядке, каждое на отдельной строке.
Примечание 1. Словом будем считать любую непрерывную последовательность из одной или нескольких символов, 
соответствующих \w.
Примечание 2. Тестовые данные доступны по ссылке. 
Sample Input 1:
    Python
    beebee
    PyPy
    portal
Sample Output 1:
    beebee
    PyPy
Sample Input 2:
    gogo
    hohoho
    XaXaXaXa
Sample Output 2:
    gogo
    XaXaXaXa
"""
import re
import sys

for i in sys.stdin:
    i = i.strip('\n')
    if re.fullmatch(r'(\w{2,})(\1)', i):
        print(i)


""" Упражнение 4
Напишите программу, определяющую:
    количество строк, в которых bee встречается в качестве подстроки не менее двух раз
    количество строк, в которых geek встречается в качестве слова хотя бы один раз
Формат входных данных
На вход программе произвольное количество строк, каждая из которых содержит набор произвольных символов.
Формат выходных данных
Программа должна вывести два числа:
    первое — количество строк, в которых bee встречается в качестве подстроки не менее двух раз
    второе — количество строк, в которых geek встречается в качестве слова хотя бы один раз
каждое на отдельной строке.
Примечание 1. Словом будем считать любую непрерывную последовательность из одной или нескольких символов, 
соответствующих \w.
Примечание 2. Строка может одновременно удовлетворять обоим условиям.
Примечание 3. В первой строке первого теста bee встречается в качестве подстроки 3 раза:
beebee bee
Во второй строке bee встречается в качестве подстроки лишь один раз, а слово geek отсутствует.
В третьей строке bee встречается в качестве подстроки 2 раза, geek в качестве слова — 1 раз:
bee geek bee
Примечание 4. Тестовые данные доступны по ссылке. 
Sample Input 1:
    beebee bee
    beegeek
    bee geek bee
Sample Output 1:
    2
    1
Sample Input 2:
    abigail alex
    clint dwarf
    emily
    gil
Sample Output 2:
    0
    0
"""
import sys
import re

bee = 0
geek = 0

for i in sys.stdin:
    i = i.strip('\n')
    if re.search(r'(bee)(.*)(bee)', i):
        bee += 1
    if re.search(r'(^geek$)|(\sgeek\s)', i):
        geek+= 1
print(bee, geek, sep='\n')


""" Упражнение 5
В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность. Для этого мы собираем публикации из 
различных соцсетей, которые содержат вхождения строки beegeek в нижнем регистре. Мы оцениваем публикацию:
    в 3 балла, если она начинается и заканчивается строкой beegeek
    в 2 балла, если она только начинается или только заканчивается строкой beegeek
    в 1 балл, если она содержит строку beegeek только внутри
    в 0 баллов, если она не содержит строку beegeek
Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования баллов всех публикаций.
Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.
Формат выходных данных
Программа должна определить, во сколько баллов оценивается каждая введенная публикация, и вывести сумму всех полученных 
баллов.
Примечание 1. Если публикация представляет собой просто строку beegeek, то она оценивается в 2 балла.
Примечание 2. Тестовые данные доступны по ссылке. 
Sample Input 1:
    hi, beegeek
    beegeek is an awesome place for programmers
    beegeek rocks, rocks beegeek
    i think beegeek is a great place to hangout
Sample Output 1:
    8
Sample Input 2:
    good morning everyone
    i am going to school
    and it is raining
Sample Output 2:
    0
"""
import sys
import re

c = 0
pat = 'beegeek'

for i in sys.stdin:
    i = i.strip('\n')
    if re.match(pat, i) and re.match(pat[::-1], i[::-1]):
        c += 3
        continue
    if re.match(pat, i) or re.match(pat[::-1], i[::-1]):
        c += 2
        continue
    if re.search(pat, i):
        c += 1

print(c)


""" Упражнение 6
На электронную почту Тимура нередко приходят письма с предложением о сотрудничестве. Тимур ценит взаимное уважение и 
считает письмо достойным внимания, если оно начинается с одного из следующих выражений:
    Здравствуйте
    Доброе утро
    Добрый день
    Добрый вечер
Напишите программу, которая определяет, является ли письмо достойным внимания Тимура.
Формат входных данных
На вход программе подается единственная строка .
Формат выходных данных
Программа должна вывести True, если введенная строка начинается с одного из представленных в условии задачи выражений 
(в произвольном регистре), или False в противном случае.
Примечание. Тестовые данные доступны по ссылке. 
Sample Input 1:
    здарова, я кирилл, хочу, чтобы ты сделал курс, суть такова...
Sample Output 1:
    False
Sample Input 2:
    Добрый день, Тимур! Предлагаем обсудить ряд курсов в сотрудничестве с нашим фондом.
Sample Output 2:
    True
Sample Input 3:
    здравствуйте, вы не заняты?
Sample Output 3:
    True
"""
import re

print(True if re.match(r'(Здравствуйте|Доброе утро|Добрый день|Добрый вечер)', input(), re.I) else False)


""" Упражнение 7
Вам доступен набор популярных публикаций из социальной сети Твиттер, которые могут иметь следующий вид:
Люблю курсы BEEGEEK!
Когда курс по ООП? @timur_guev
BEEGEEK, спасибо за курсы, вы лучшие! #python #BeeGeek
и т.д.
Напишите программу, которая определяет, в скольких публикациях содержится строка beegeek.
Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.
Формат выходных данных
Программа должна определить, в скольких введенных строках содержится строка beegeek в произвольном регистре, 
и вывести полученный результат.
Примечание. Тестовые данные доступны по ссылке. 
Sample Input 1:
    Люблю курсы BEEGEEK!
    Когда курс по ООП? @beegeek
    BEEGEEK, спасибо за курсы, вы лучшие! #python #BeeGeek
Sample Output 1:
    3
Sample Input 2:
    Нельзя быть дружелюбным соседом, если соседей нет
    @everyone, посоветуйте курсы по программированию
Sample Output 2:
    0
"""
import re
import sys

c = 0

for i in sys.stdin:
    if re.search(r'BEEGEEK', i.strip('\n'), re.I):
        c += 1

print(c)
