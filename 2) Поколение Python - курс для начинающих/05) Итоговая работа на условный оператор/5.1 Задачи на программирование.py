""" Упражнение 1
Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается,
то выведите «YES», иначе выведите «NO».
Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1: 2000
Sample Output 1: YES
Sample Input 2: 1999
Sample Output 2: NO
Sample Input 3: 3000
Sample Output 3: YES
"""
a = input()
print('YES' if a[-2:] == '00' else 'NO')


""" Упражнение 2
Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. 
Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой 
клетки, потом для второй клетки.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1:
    1
    1
    2
    6
Sample Output 1:
    YES
Sample Input 2:
    2
    2
    2
    5
Sample Output 2:
    NO
"""
a, b, c, d = map(lambda x: int(input()), range(4))
print('YES' if (a+b)%2 == (c+d)%2 else 'NO')


""" Упражнение 3
Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу, которая запрашивает возраст и пол 
претендента, используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) и определяет подходит ли 
претендент для вступления в команду или нет. Если претендент подходит, то выведите «YES», иначе выведите «NO».
Формат входных данных
На вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f (женщина).
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1:
    10
    f
Sample Output 1:
    YES
Sample Input 2:
    11
    m
Sample Output 2:
    NO
"""
y, s = int(input()), input()
print('YES' if s == 'f' and 10 <= y <= 15 else 'NO')


""" Упражнение 4
Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне 
диапазона 1-10, то программа должна вывести текст «ошибка».
В таблице приведены римские цифры для чисел от 1 до 10
Формат входных данных
На вход программе подаётся целое число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1: 7
Sample Output 1: VII
Sample Input 2: 12
Sample Output 2: ошибка
"""
rome = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
a = int(input())
print(rome[a-1] if 1 <= a <= 10 else 'ошибка')


""" Упражнение 5
Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
Условия:
    если число нечётное, то вывести «YES»;
    если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
    если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
    если число чётное и больше 20, то вывести «NO».
Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1: 1
Sample Output 1: YES
Sample Input 2: 2
Sample Output 2: NO
"""
a = int(input())
if a % 2 == 1 or (a % 2 == 0 and 6 <= a <= 20):
    print('YES')
else:
    print('NO')


""" Упражнение 6
Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с первой клетки 
на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки 
сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом слона 
можно попасть во вторую или «NO» в противном случае.
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Шахматный слон ходит по диагоналям.
Sample Input 1:
    4
    4
    5
    5
Sample Output 1: YES
Sample Input 2:
    4
    4
    5
    4
Sample Output 2:
    NO
Sample Input 3:
    4
    4
    5
    3
Sample Output 3:
    YES
"""
a, b, c, d = map(lambda x: int(input()), range(4))
if abs(a-c) == abs(b-d):
    print('YES')
else:
    print('NO')


""" Упражнение 7
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь попасть с первой 
клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер 
строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом 
коня можно попасть во вторую или «NO» в противном случае.
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Шахматный конь ходит буквой «Г».
Sample Input 1:
    1
    1
    8
    8
Sample Output 1:
    NO
Sample Input 2:
    2
    4
    3
    2
Sample Output 2:
    YES
"""
a, b, c, d = map(lambda x: int(input()), range(4))
if (abs(a-c) == 1 and abs(b-d) == 2) or (abs(a-c) == 2 and abs(b-d) == 1):
    print('YES')
else:
    print('NO')


""" Упражнение 8
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли ферзь попасть с первой 
клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер 
строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом 
ферзя можно попасть во вторую или «NO» в противном случае.
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
Sample Input:
    1
    1
    2
    2
Sample Output:
    YES
"""
a, b, c, d = map(lambda x: int(input()), range(4))
if (abs(a-c) == abs(b-d)) or (a == c or b == d):
    print('YES')
else:
    print('NO')
