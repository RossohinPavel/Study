""" Упражнение 1
На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит  его содержимое.
Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.
Формат выходных данных
Программа должна вывести содержимое указанного файла.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Не забудьте закрыть файл.
"""
file = open(input())
print(file.read())
file.close()


""" Упражнение 2
На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его 
предпоследнюю строку.
Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.
Формат выходных данных
Программа должна вывести предпоследнюю строку указанного файла.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Гарантируется, что файл содержит хотя бы две строки.
Примечание 3. Не забудьте закрыть файл 🙂.
"""
file = open(input())
print(file.readlines()[-2])
file.close()


""" Упражнение 3
Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную 
строку из этого файла.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести случайную строку указанного файла.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Гарантируется, что файл содержит хотя бы одну строку.
Примечание 3. Не забудьте закрыть файл 🙂.
Примечание 4. Указанный файл можно скачать по ссылке.
"""
import random
file = open('lines.txt')
print(random.choice(file.readlines()))
file.close()


""" Упражнение 4
Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. Напишите программу, 
выводящую на экран сумму этих чисел.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести сумму чисел из указанного файла.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Не забудьте закрыть файл .
Примечание 3. Указанный файл можно скачать по ссылке.
"""
file = open('numbers.txt')
print(sum(map(int, file.readlines())))
file.close()


""" Упражнение 5
Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела и 
конца строки. Напишите программу, выводящую на экран сумму этих чисел.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести сумму чисел из указанного файла.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Не забудьте закрыть файл 🙂.
Примечание 3. Указанный файл можно скачать по ссылке.
"""
file = open('nums.txt')
print(sum(map(int, file.read().split())))
file.close()


""" Упражнение 6
Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью 
символа табуляции (\t) разделена на три колонки:
наименование товара;
количество товара (целое число);
цена (в рублях) товара за 11 шт (целое число).
Напишите программу, выводящую на экран общую стоимость заказа.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести общую стоимость заказа.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Не забудьте закрыть файл 🙂.
Примечание 3. Указанный файл можно скачать по ссылке.
"""
file = open('prices.txt')
l = map(lambda x: x.split('\t'), file.readlines())
file.close()
print(sum([int(x[1]) * int(x[2].rstrip('\n')) for x in l]))
