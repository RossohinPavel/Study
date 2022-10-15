""" Упражнение 1
Напишите программу ввода двух строк (каждая вводится с новой строки) и их объединения в одну строку через пробел.
Результат выведите на экран.
Sample Input:
    hello python
    i love you
Sample Output: hello python i love you
"""
a = input()
b = input()
print(f'{a} {b}')


""" Упражнение 2
Напишите программу ввода двух слов через пробел. Сформируйте новую строку, 
продублировав первое слово дважды, а второе - трижды (все слова в результирующей строке должны идти через пробел). 
Результат выведите на экран.
Программу следует реализовать без использования F-строк, а с применением оператора дублирования строк.
Sample Input: hello python
Sample Output: hello hello python python python
"""
a, b = map(str, input().split())
a = a + ' ' + a
b = b + ' '
print(a, b*3)


""" Упражнение 3
Выполняется считывание двух целочисленных значений в переменные a и b (вводятся в одну строчку через пробел). 
Необходимо сформировать строку вида: "Переменная a = <значение>, переменная b = <значение>", 
используя оператор конкатенации (соединения) строк. Результат выведите на экран.
P. S. F-строки в программе не использовать.
Sample Input: 2 -5
Sample Output: Переменная a = 2, переменная b = -5
"""
a, b = map(str, input().split())
print("Переменная a = " + a + ", переменная b = " + b)


""" Упражнение 4
Написать программу ввода строки и формирования новой строчки вида: 
"Строка: <введенная строка>. Длина: <длина строки>". 
Результат сформированной строки вывести на экран.
P. S. В программе F-строки не использовать.
Sample Input: hello Balakirev
Sample Output: Строка: hello Balakirev. Длина: 15
"""
a = input()
print("Строка: " + a + ". Длина: " + str(len(a)))


""" Упражнение 5
Написать программу ввода двух слов (через пробел в одну строчку).
Определить булевы значения для оператора in проверки вхождения первого слова во второе. 
А также для операторов ==, >, <. Все булевы значения объединить в одну строку через пробел и вывести на экран.
Sample Input: hello python
Sample Output: False False False True
"""
a, b = map(str, input().split())
print(a in b, a == b, a > b, a < b)


""" Упражнение 6
С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
"Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"
Sample Input: a z
Sample Output: Коды: a = 97, z = 122
"""
w1, w2 = map(str, input().split())
print(f'Коды: {w1} = {ord(w1)}, {w2} = {ord(w2)}')
