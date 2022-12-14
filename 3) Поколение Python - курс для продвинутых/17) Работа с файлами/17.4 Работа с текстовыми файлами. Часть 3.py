""" Упражнение 1
Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна создать файл с именем output.txt и записать в него считанную строку текста.
Примечание. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
"""
with open('output.txt', 'w') as file:
    file.write(input())


""" Упражнение 2
Напишите программу, записывающую в текстовый файл random.txt $25$ случайных чисел в диапазоне 
от 111 до 777 (включительно), каждое с новой строки.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна создать файл с именем random.txt и записать в него случайные числа в соответствии с условием задачи.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Для генерации случайных чисел используйте модуль random.
"""
import random
l = [random.randint(111, 777) for _ in range(25)]
with open('random.txt', 'w') as file:
    print(*l, sep='\n', file=file)


""" Упражнение 3
Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого 
файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел. 
Нумерация строк должна начинаться с 1.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.
Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
Примечание 2. Используйте встроенную функцию enumerate().
Примечание 3. Если бы файл input.txt содержал строки:
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
то файл output.txt имел бы вид:
    1) Beautiful is better than ugly.
    2) Explicit is better than implicit.
    3) Simple is better than complex.
    4) Complex is better than complicated.
"""
with open('input.txt', 'r') as file:
    l = file.readlines()
for i in range(1, len(l)+1):
    l[i-1] = f'{i}) {l[i-1]}'
with open('output.txt', 'w') as file:
    file.writelines(l)


""" Упражнение 4
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и 
оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.
Напишите программу для добавления 55 баллов к каждому результату теста и вывода фамилий и новых результатов тестов 
в файл new_scores.txt.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.
Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
Примечание 2. Если бы файл class_scores.txt содержал строки:
    Washington 83
    Adams 86
    Kingsman 100
    MacDonald 95
    Thomson 98
то файл new_scores.txt имел бы вид:
    Washington 88
    Adams 91
    Kingsman 100
    MacDonald 100
    Thomson 100
"""
def cr_ad(st):
    st = st.strip('\n').split()
    st[1] = int(st[1])
    if st[1] > 95:
        st[1] = st[1] + 100 - st[1]
    else:
        st[1] += 5
    return st[0] + ' ' + str(st[1])
with open('class_scores.txt', 'r',  encoding='UTF-8') as file:
    l = file.readlines()
for i in range(len(l)):
    l[i] = cr_ad(l[i])
with open('new_scores.txt', 'w', encoding='UTF-8') as file:
    print(*l, sep='\n', file=file)


""" Упражнение 5
Однажды Жака Фреско спросили:
"Если ты такой умный, почему не богатый?"
Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
"Были разноцветные козлы. Сколько?"
"Сколько чего?"
"Сколько из них составляет более 7% от общего количества козлов?"
Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех возможных 
цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов. Перечень 
козлов включает только строки из первого списка.
Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки 
от Жака Фреско.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов, 
которые удовлетворяют условию загадки Жака Фреско.
Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
Примечание 2. Если бы файл goats.txt содержал строки:
    COLOURS
    Pink goat
    Green goat
    Black goat
    GOATS
    Pink goat
    Pink goat
    Black goat
    Pink goat
    Pink goat
    Black goat
    Green goat
    Pink goat
    Black goat
    Black goat
    Pink goat
    Pink goat
    Black goat
    Black goat
    Pink goat
то файл answer.txt имел бы вид:
    Black goat
    Pink goat
"""
with open('goats.txt', 'r',  encoding='UTF-8') as file:
    l = file.readlines()
col_index = l.index('GOATS\n')
colors = dict.fromkeys([x.strip('\n') for x in l[1:col_index]], 0)
for i in l[col_index+1:]:
    colors[i.strip('\n')] += 1
sc = round(sum([v for v in colors.values()]) / 100 * 7)
answer = [v[0] for v in colors.items() if v[1] > sc]
with open('answer.txt', 'w') as file:
    print(*answer, sep='\n', file=file)


""" Упражнение 6
На вход программе подается натуральное число nn и nn строк с названиями файлов. Напишите программу, которая создает 
файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.
Формат входных данных
На вход программе подается натуральное число nn и nn строк названий существующих файлов.
Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.
Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
"""
l = []
for i in range(int(input())):
    with open(input(), 'r') as file:
        l.append(file.read())
with open('output.txt', 'a') as file:
    file.writelines(l)
""" Упражнение 7
Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее. 
Каждая строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа, 
время выхода, где время указано в 2424-часовом формате.
Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей 
(не меняя порядка следования), которые были в сети не менее часа.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.
Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
Примечание 2. Считайте, что каждый пользователь был только раз в системе, то есть в файле нет двух строк с одинаковым 
пользователем.
Примечание 3. Если бы файл logfile.txt содержал строки:
    Тимур Гуев, 14:10, 15:50
    Руслан Гриценко, 12:00, 12:59
    Роман Гацалов, 09:10, 17:45
    Габолаев Георгий, 11:10, 12:10
то файл output.txt имел бы вид:
    Тимур Гуев
    Роман Гацалов
    Габолаев Георгий
"""

