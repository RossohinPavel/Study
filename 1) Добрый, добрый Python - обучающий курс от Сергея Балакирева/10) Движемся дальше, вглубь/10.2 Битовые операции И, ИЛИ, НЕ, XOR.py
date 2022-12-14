""" Упражнение 1
На вход программы подается целое десятичное число. Используя битовые операции, включите третий бит введенного числа.
Выведите на экран полученное числовое значение.
P. S. Распределение номеров бит представлено на следующем рисунке.
Sample Input: 100
Sample Output: 108
"""
a = int(input())
b = 8
print(a | b)


""" Упражнение 2
На вход программы подается целое десятичное число. Используя битовые операции, выключите 4-й и 1-й биты введенного 
числа. Выведите на экран полученное числовое значение.
P. S. Распределение номеров бит представлено на следующем рисунке.
Sample Input: 153
Sample Output: 137
"""
a = int(input())
res = a & 0b11101101
print(res)


""" Упражнение 3
На вход программы подается целое десятичное число. Используя битовые операции, переключите 3-й и 0-й биты введенного 
числа. Выведите на экран полученное числовое значение.
P. S. Распределение номеров бит представлено на следующем рисунке.
Sample Input: 58
Sample Output: 51
"""
a = int(input())
print(a ^ 0b001001)


""" Упражнение 4
На вход программы подается целое десятичное число. Используя битовые операции, выполните умножение введенного числа 
на 4. Результат отобразите на экране.
Sample Input: 40
Sample Output: 160
"""
a = int(input())
print(a << 2)


""" Упражнение 5
На вход программы подается целое десятичное число. Используя битовые операции, выполните целочисленное деление 
введенного числа на 2. Результат отобразите на экране.
Sample Input: 22
Sample Output: 11
"""
a = int(input())
print(a >> 1)


""" Упражнение 6
Вводится зашифрованное слово. Шифрование кодов символов этого слова было проведено с помощью битовой операции XOR с 
ключом key=123. То есть, каждый символ был преобразован по алгоритму: x = ord(x) ^ key
Здесь ord - функция, возвращающая код символа x. Расшифруйте введенное слово и выведите его на экран.
P. S. Подсказка: для преобразования кода в символ используйте функцию chr.
Sample Input: ѩкю[щюлцхZ
Sample Output: Все верно!
"""
a = input()
key = 123
print(''.join([chr(ord(x) ^ key) for x in a]))


""" Упражнение 7
На вход программы подается целое десятичное число. Используя битовые операции, проверьте, включен ли 6-й и 3-й биты 
введенного числа. Если они оба включены, то выведите слово ДА, иначе - слово НЕТ.
P. S. Распределение номеров бит представлено на следующем рисунке.
Sample Input: 106
Sample Output: ДА
"""
a = int(input())
b = 0b1001000
print('ДА' if a & b == b else 'НЕТ')


""" Упражнение 8
На вход программы подается целое десятичное число. Используя битовые операции, проверьте, включен ли 5-й или 1-й биты 
введенного числа. Если включен хотя бы один из этих битов, то выведите слово ДА, иначе - слово НЕТ.
P. S. Распределение номеров бит представлено на следующем рисунке.
Sample Input: 74
Sample Output: ДА
"""
a = int(input())
b = 0b0100000
c = 0b0000010
print('ДА' if a & b == b or a & c == c else 'НЕТ')
