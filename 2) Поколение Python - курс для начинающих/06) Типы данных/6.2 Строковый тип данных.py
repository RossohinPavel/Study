""" Упражнение 1
Напишите программу, которая выводит текст:
"Python is a great language!", said Fred. "I don't ever remember having this much fun before."
Примечание. Используйте конкатенацию строк.
Sample Input:
Sample Output:
"Python is a great language!", said Fred. "I don't ever remember having this much fun before."
"""
print('"Python is a great language!", ' + 'said Fred. ' + '"I don\'t ever remember having this much fun before."')


""" Упражнение 2
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
«Hello [введенное имя] [введенная фамилия]! You just delved into Python».
Формат входных данных
На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Между firstname lastname вставьте пробел =)
Sample Input 1:
    Anthony
    Joshua
Sample Output 1:
    Hello Anthony Joshua! You just delved into Python
Sample Input 2:
    Michael
    Jordan
Sample Output 2:
    Hello Michael Jordan! You just delved into Python
Sample Input 3:
    Leonardo
    DiCaprio
Sample Output 3:
    Hello Leonardo DiCaprio! You just delved into Python
"""
n, f = input(), input()
print(f'Hello {n} {f}! You just delved into Python')


""" Упражнение 3
Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».
Формат входных данных
На вход программе подаётся строка – название футбольной команды.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1: Barcelona
Sample Output 1: Футбольная команда Barcelona имеет длину 9 символов
Sample Input 2: Real Madrid
Sample Output 2: Футбольная команда Real Madrid имеет длину 11 символов
Sample Input 3: Manchester United
Sample Output 3: Футбольная команда Manchester United имеет длину 17 символов
Sample Input 4: Milan
Sample Output 4: Футбольная команда Milan имеет длину 5 символов
"""
a = input()
print(f'Футбольная команда {a} имеет длину {len(a)} символов')


""" Упражнение 4
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
Примечание. Гарантируется, что длины названий всех трех городов различны.
Sample Input 1:
    Москва
    Санкт-Петербург
    Екатеринбург
Sample Output 1:
    Москва
    Санкт-Петербург
Sample Input 2:
    Нью-Йорк
    Вашингтон
    Чикаго
Sample Output 2:
    Чикаго
    Вашингтон
Sample Input 3:
    Париж
    Марсель
    Лион
Sample Output 3:
    Лион
    Марсель
"""
a = sorted(map(lambda x: input(), range(3)), key=len)
print(*a[::2], sep='\n')


""" Упражнение 5
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить 
возрастающую арифметическую прогрессию.
Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.
Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.
Sample Input 1:
    abc
    a
    abcde
Sample Output 1:
    YES
Sample Input 2:
    2434
    90099
    21
Sample Output 2:
    NO
Sample Input 3:
    aaaaaaaaaa10
    1111111Nm
    22222r
Sample Output 3:
    YES
"""
a, b, c = sorted(map(lambda x: len(input()), range(3)))
print('YES' if b-a == c-b else 'NO')


""" Упражнение 6
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока 
«синий» и «NO» в противном случае.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1: Какой хороший день!
Sample Output 1: NO
Sample Input 2: Как называется этот красивый синий камень в Вашем кольце?
Sample Output 2: YES
Sample Input 3: Разглядите синий густой цвет.
Sample Output 3: YES
"""
a = input()
print('YES' if 'синий' in a else 'NO')


""" Упражнение 7
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока 
«суббота» или «воскресенье», и «NO» в противном случае.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1: Какой сегодня день недели?
Sample Output 1: NO
Sample Input 2: Была суббота, и ему хотелось поскорее уехать домой.
Sample Output 2: YES
Sample Input 3: День в воскресенье выдался тёплым и солнечным.
Sample Output 3: YES
"""
s = input()
print('YES' if 'суббота' in s or 'воскресенье' in s else 'NO')


""" Упражнение 8
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую 
корректность email адреса.
Формат входных данных
На вход программе подаётся одна строка – email адрес.
Формат выходных данных
Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.
Примечание. Наличие символов @ и . недостаточно для корректности email адреса, однако их отсутствие гарантировано влечёт 
за собой неверный email.
Sample Input 1: aaaa@bbb.com
Sample Output 1: YES
Sample Input 2: aaaa@bbbcom
Sample Output 2: NO
Sample Input 3: qwerty.com
Sample Output 3: NO
"""
s = input()
print('YES' if '@' in s and '.' in s else 'NO')
