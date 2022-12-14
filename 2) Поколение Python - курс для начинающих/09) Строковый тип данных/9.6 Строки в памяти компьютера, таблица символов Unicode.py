""" Упражнение 1
На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового значения в диапазоне
от a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.
Формат входных данных
На вход программе подается два натуральных числа, каждое на отдельное строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1:
    65
    70
Sample Output 1:
    A B C D E F
"""
a, b = int(input()), int(input())
for i in range(a, b+1):
    print(chr(i), end=' ')


""" Упражнение 2
На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему 
код из таблицы символов Unicode.
Формат входных данных 
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.
Sample Input: Hello world!
Sample Output: 72 101 108 108 111 32 119 111 114 108 100 33
"""
print(*[ord(x) for x in input()])


""" Упражнение 3
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря. 
Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного 
мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения. Напишите программу для 
декодирования этого шифра.
Формат входных данных
В первой строке дается число n (1≤ n≤ 25) – сдвиг, во второй строке даётся закодированное сообщение в виде строки со 
строчными латинскими буквами.
Формат выходных данных
Программа должна вывести одну строку – декодированное сообщение. Обратите внимание, что нужно декодировать сообщение, 
а не закодировать.
Sample Input 1:
    1
    bwfusvfupdbftbs
Sample Output 1: avetruetocaesar
"""
s = int(input())
for i in input():
    n = ord(i) - s
    if n < 97:
         n = 122 - (96 - n)
    print(chr(n), end='')
