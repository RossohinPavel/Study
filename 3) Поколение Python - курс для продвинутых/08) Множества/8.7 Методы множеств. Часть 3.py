""" Упражнение 1
На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.
Формат входных данных
На вход программе подаются два натуральных числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести YES, если в записи данных чисел есть одинаковые цифры и NO если нет.
Sample Input 1:
    114
    223
Sample Output 1:
    NO
Sample Input 2:
    1523
    3678
Sample Output 2:
    YES
"""
print('NO' if set(input()).isdisjoint(set(input())) else 'YES')


""" Упражнение 2
На вход программе подаются два числа. Напишите программу, которая определяет, входят ли в запись первого числа все 
цифры, содержащиеся в записи второго (независимо от повтора, то есть количества цифр) числа или нет.
Формат входных данных
На вход программе подаются два натуральных числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести YES, если в запись первого числа входят все цифры, содержащиеся в записи второго числа и 
NO в противном случае.
Тестовые данные 🟢
Sample Input 1:
    123456789
    657
Sample Output 1:
    YES
Sample Input 2:
    1254
    1243
Sample Output 2:
    NO
"""
print('YES' if set(input()).issuperset(set(input())) else 'NO')


""" Упражнение 3
Даны по 10-балльной шкале оценки по информатике трех учеников. Напишите программу, которая выводит множество оценок, 
которые есть и у первого и у второго учеников, но которых нет у третьего ученика.
Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого  на отдельной строке).
Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, 
в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.
Sample Input 1:
    1 5 4 2 5 6 6 2 3 3 5 2
    2 3 5 1 2 1 2 6 7 1 1 6
    1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:
    5 3 2
Sample Input 2:
    2 9 3 4 6 10
    2 3 4 5 2 10
    2 3 4 5 3 9
Sample Output 2:
    10
"""
a, b, c = [map(int, input().split()) for _ in range(3)]
print(*sorted(set(a) & set(b) - set(c), reverse=True))


""" Упражнение 4
Даны по 10-балльной шкале оценки по математике трех учеников. Напишите программу, которая выводит множество оценок, 
имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.
Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого на отдельной строке).
Формат выходных данных
Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, 
в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.
Sample Input 1:
    1 5 4 2 5 6 6 2 3 3 5 2
    2 3 5 10 2 10 2 6 7 10 10 6
    1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:
    0 1 2 3 4 5 7 8 9 10
Sample Input 2:
    2 9 3 4 6 9
    2 3 4 5 2 10
    2 3 4 5 3 10
Sample Output 2:
    5 6 9 10
"""
a, b, c = [set(map(int, input().split())) for _ in range(3)]
print(*sorted((a | b | c) - (a & b & c)))


""" Упражнение 5
Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок 
третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого на отдельной строке).
Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, 
в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.
Sample Input 1:
    1 5 4 2 5 6 6 2 3 3 5 2
    2 3 5 1 2 1 2 6 7 1 1 6
    1 4 6 9 8 7 0 9 0 9 8 10
Sample Output 1:
    10 9 8 0
Sample Input 2:
    2 9 2 4 6 10
    2 2 4 5 2 10
    2 3 4 5 3 9
Sample Output 2:
    3
"""
a, b, c = [set(map(int, input().split())) for _ in range(3)]
print(*sorted(c - (a | b), reverse=True))


""" Упражнение 6
Даны по 10-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок,
не встречающихся ни у одного из трех учеников.
Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого на отдельной строке).
Формат выходных данных
Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, 
в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.
Sample Input 1:
    1 5 4 2 5 6 6 2 3 3 5 2
    2 3 5 1 2 1 2 6 7 1 1 6
    1 4 6 8 8 7 0 6 0 3 8 1
Sample Output 1:
    9 10
Sample Input 2:
    2 9 3 4 6 10
    2 3 4 5 2 10
    2 3 4 5 3 9
Sample Output 2:
    0 1 7 8
"""
a, b, c = [set(map(int, input().split())) for _ in range(3)]
x = {*range(0, 11)}
print(*sorted(x-(a | b | c)))
