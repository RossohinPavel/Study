""" Упражнение 1
Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*).
Примечание. Высота и ширина прямоугольника равны 4 и 17 звёздочкам соответственно.
Sample Input:
Sample Output:
*****************
*               *
*               *
*****************
"""
# Вариант 1
print('*'*17, '*' + ' '*15 + '*', '*' + ' '*15 + '*', '*'*17, sep='\n')
#Вариант 2
print(*(a := ['*'*17, '*' + ' '*15 + '*']), *(reversed(a)), sep='\n')


""" Упражнение 2
Напишите программу, которая считывает два целых числа aa и bb и выводит на экран квадрат суммы (a+b)^2
и сумму квадратов a^2+b^2 этих чисел.
Формат входных данных
На вход программе подаётся два целых числа, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием.
Sample Input 1: 
    3 
    2
Sample Output 1:
    Квадрат суммы 3 и 2 равен 25
    Сумма квадратов 3 и 2 равна 13
Sample Input 2:
    -5
    1
Sample Output 2:
    Квадрат суммы -5 и 1 равен 16
    Сумма квадратов -5 и 1 равна 26
Sample Input 3:
    17
    0
Sample Output 3:
    Квадрат суммы 17 и 0 равен 289
    Сумма квадратов 17 и 0 равна 289
"""
a, b = list(map(lambda x: input(), range(2)))
print(f'Квадрат суммы {a} и {b} равен {(a+b)**2}', f'Сумма квадратов {a} и {b} равна {a**2+b**2}', sep='\n')


""" Упражнение 3
Как известно, целые числа в языке Python не имеют ограничений, которые встречаются в других языках программирования. 
Напишите программу, которая считывает четыре целых положительных числа a, \, b, \, ca,b,c и dd и выводит на экран 
значение выражения a^b + c^da 
Формат входных данных
На вход программе подаётся четыре целых положительных числа a, b, c, d, каждое на отдельной строке в указанном порядке.
Формат выходных данных
Программа должна вывести значение a^b + c^da 
Sample Input:
    9
    29
    7
    27
Sample Output:
    4710194409608608369201743232
"""
a, b, c, d = list(map(lambda x: input(), range(4)))
print(a**b + c**d)


""" Упражнение 4
Напишите программу, которая считывает целое положительное число n, n,n∈[1;9] (в диапозоне) и выводит значение 
числа n + nn + nnn.
Формат входных данных
На вход программе подаётся одно целое положительное число n, n∈[1;9].
Формат выходных данных
Программа должна вывести число n + nn + nnn 
Примечание. Для первого теста 1 + 11 + 111 = 123
Sample Input 1: 1
Sample Output 1: 123
Sample Input 2: 2
Sample Output 2: 246
Sample Input 3: 3
Sample Output 3: 369
Sample Input 4: 9
Sample Output 4: 1107
"""
print(int(a := input()) + int(a + a) + int(a + a + a))
