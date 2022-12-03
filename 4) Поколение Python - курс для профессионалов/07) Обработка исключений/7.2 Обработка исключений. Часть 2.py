""" Упражнение 1
Вам доступна программа, которая находит сумму всех значений по ключу Likes из всех словарей списка blog_posts. Если
словарь не содержит ключа Likes, его значение считается равным минус единице. Дополните приведенный ниже код
конструкцией try-except, чтобы он выполнился без ошибок.
"""
blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
              {'Likes': 13, 'Comments': 2, 'Shares': 1},
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
              {'Comments': 4, 'Shares': 2},
              {'Photos': 8, 'Comments': 1, 'Shares': 1},
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]
total_likes = 0
for post in blog_posts:
    try:
        total_likes += post['Likes']
    except:
        total_likes -= 1

print(total_likes)


""" Упражнение 2
Вам доступна программа, которая добавляет в список fifth пятую букву каждого слова из списка food. Если слово не имеет 
пятой буквы, этой буквой считается символ _. Дополните приведенный ниже код конструкцией try-except, чтобы он выполнился 
без ошибок.
"""
food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except:
        fifth.append('_')

print(fifth)


""" Упражнение 3
Вам доступна программа, которая добавляет в список remainders остаток от деления 3636 на каждое число из списка numbers. 
Если число равно нулю, оно игнорируется. Дополните приведенный ниже код конструкцией try-except, чтобы он выполнился без 
ошибок.
"""
numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
remainders = []
for number in numbers:
    try:
        remainders.append(36 % number)
    except:
        pass
print(remainders)


""" Упражнение 4
На вход программе подается неопределенное количество строк, каждая из которых содержит произвольное значение. Напишите 
программу с использованием конструкции try-except, которая выводит сумму всех введенных чисел, а затем — количество 
введенных нечисловых значений.
Формат входных данных
На вход программе подается неопределенное количество строк (хотя бы одна), каждая из которых содержит произвольное 
значение.
Формат выходных данных
Программа должна вывести сумму всех введенных чисел (тип int и float), а затем на следующей строке — количество 
введенных нечисловых значений.
Примечание 1. Если ни одно число введено не было, то сумма равна 0.
Примечание 2. Рассмотрим первый тест. Имеем три введенных числа, сумма которых равна:
100 + 10 + 1.1 = 111.1
Также три нечисловых значения, а именно: i'm number!, [1, 99], {'math', 'physics'}.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    100
    i'm number!
    10
    [1, 99]
    1.1
    {'math', 'physics'}
Sample Output 1:
    111.1
    3
Sample Input 2:
    10
    10
Sample Output 2:
    20
    0
Sample Input 3:
    abc
    cda
    xyz
Sample Output 3:
    0
    3
"""
import sys

total = 0
count = 0

for line in sys.stdin:
    im = 0
    try:
        im = float(line)
        try:
            im = int(line)
        except:
            pass
    except:
        count += 1
    total += im

print(total, count, sep='\n')
