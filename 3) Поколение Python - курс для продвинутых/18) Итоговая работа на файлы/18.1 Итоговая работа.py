""" Упражнение 1
На вход программе подается строка текста с именем текстового файла. Напишите программу для вывода на экран количества
строк данного файла.
Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла.
Формат выходных данных
Программа должна вывести количество строк файла.
Примечание. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
"""
with open(input(), 'r') as file:
    l = file.readlines()
print(len(l))


""" Упражнение 2
Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц. На каждой строке файла указано, сколько 
клиент заплатил за товар, в долларах (целое число):
    $47
    $100
    $60
    $12
    $8
...
Напишите программу для подсчета суммарной месячной выручки фирмы. 
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести выручку фирмы (сумму всех чисел из файла) в соответствии с примером ниже.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Если бы файл ledger.txt содержал строки:
    $37
    $44
    $19
то результатом будет:
    $100
"""
with open('ledger.txt', 'r',  encoding='UTF-8') as file:
    l = list(map(lambda x: int(x.strip('\n').lstrip('$')), file.readlines()))
print(f'${sum(l)}')


""" Упражнение 3
Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста в каждом из триместров. Строки файла 
имеют вид: фамилия оценка_1 оценка_2 оценка_3.
Напишите программу для подсчета количества студентов, сдавших все три теста. Тест считается сданным, если количество 
баллов по нему не меньше 65.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести количество студентов, сдавших все три теста.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Если бы файл grades.txt содержал строки:
    Washington 83 77 54
    Adams 86 69 90
    Jacobson 50 49 71
    MacDonald 100 99 100
    Berrington 66 67 64
то результатом будет:
    2
"""
with open('grades.txt', 'r',  encoding='UTF-8') as file:
    l = list(map(lambda x: x.strip('\n').split(), file.readlines()))
print(len(list(filter(lambda x: int(x[1]) >= 65 and int(x[2]) >= 65 and int(x[3]) >= 65, l))))


""" Упражнение 4
Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу, которая находит и выводит 
самые длинные слова этого файла, не меняя порядка их следования.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести самые длинные слова файла words.txt, каждое с новой строки, не меняя их порядка следования.
Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
Примечание 2. Словом считайте любую группу символов без пробелов, даже если она включает цифры или знаки препинания.
Примечание 3. Если бы файл words.txt содержал строки:
there are many different holidays on the first of january we celebrate new year on the seventh of january and the 
twenty-fifth of december we have christmas the twenty-third of february is the day of the defenders of the motherland 
or the army day then comes easter and radonitsa the first of may is the labour day the ninth of may is victory day 
the third of july is independence day then comes the seventh of november the day of the october revolution and so on
то результатом будет:
    twenty-fifth
    twenty-third
    independence
"""
with open('words.txt', 'r',  encoding='UTF-8') as file:
    l = file.readline().strip('\n').split()
ml = len(max(l, key=len))
print(*filter(lambda x: len(x) == ml, l), sep='\n')


""" Упражнение 5
На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран последние 
10 строк данного файла.
Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.
Формат выходных данных
Программа должна вывести последние 1010 строк этого файла.
Примечание 1. Считайте, что исполняемая программа и файл находятся в одной папке.
Примечание 2. Если количество строк в файле меньше 1010, необходимо вывести содержимое файла полностью.
Примечание 3. Если бы файл содержал строки:
    there are many different holidays
    on the first of january we
    celebrate new year on the
    seventh of january and the
    twenty-fifth of december we
    have christmas the twenty-third
    of february is the day of the
    defenders of the motherland
    or the army day then comes
    easter and radonitsa the
    first of may is the labour
    day the ninth of may is
    victory day the third of july
    is independence day then comes
    the seventh of november the day
    of the october revolution and so on
то результатом будет:
    of february is the day of the
    defenders of the motherland
    or the army day then comes
    easter and radonitsa the
    first of may is the labour
    day the ninth of may is
    victory day the third of july
    is independence day then comes
    the seventh of november the day
    of the october revolution and so on
Примечание 4. Подумайте над ситуацией, когда файл очень большой и нерационально считывать все его содержимое в память 
компьютера.
"""
with open(input(), 'r') as file:
    l = list(map(lambda x: x.strip('\n'), file.readlines()))
print(*l[-10:], sep='\n', end='')


""" Упражнение 6
На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран содержимое 
этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).
Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что все 
слова в этом файле записаны в нижнем регистре.
Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, в котором необходимо заменить 
запрещенные слова звездочками.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались, даже если они встречаются 
в середине другого слова.
Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра. Например, если файл 
forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и подобные должны быть 
заменены на ****.
Примечание 3. Если бы файл forbidden_words.txt содержал слова:
hello email python the exam wor is
а файл в котором заменяются слова имел бы вид:
Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!
то результатом будет:
*****, ***ld! ****** ** *** programming language of *** future. My ***** **....
****** ** awesome!!!!
"""
with open(r'C:\Users\DF17\Downloads\forbidden_words.txt', 'r',  encoding='UTF-8') as file:
    l = file.read().strip('\n').split()
with open(r'C:\Users\DF17\Downloads\data.txt', 'r',  encoding='UTF-8') as file:
    rep = file.read()
lrep = rep.lower()
for j in l:
    ind = lrep.find(j)
    while ind != -1:
        st1 = rep[:ind]
        st2 = rep[ind + len(j):]
        rep = st1 + '*' * len(j) + st2
        lrep = st1 + '*' * len(j) + st2
        ind = lrep.find(j)
with open('test', 'w',  encoding='UTF-8') as file:
    file.write(rep)


""" Упражнение 7
Транслитерация — передача знаков одной письменности знаками другой письменности, при которой каждый знак (или 
последовательность знаков) одной системы письма передаётся соответствующим знаком (или последовательностью знаков) 
другой системы письма.
Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для транслитерации этого файла, то есть 
замены кириллических символов на латинские в соответствии с предложенной таблицей. Все остальные символы надо оставить 
без изменений. Результат транслитерации требуется записать в файл transliteration.txt.
Кириллица 	Латиница	Кириллица	Латиница	Кириллица	Латиница
а	a	к	k	х	h
б	b	л	l	ц	c
в	v	м	m	ч	ch
г	g	н	n	ш	sh
д	d	о	o	щ	shh
е	e	п	p	ъ	*
ё	jo	р	r	ы	y
ж	zh	с	s	ь	'
з	z	т	t	э	je
и	i	у	u	ю	ju
й	j	ф	f	я	ya
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна создать файл с именем transliteration.txt в соответствии с условием задачи.
Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
Примечание 2. Обратите внимание, что заглавные буквы должны заменяться на соответствующие им заглавные же буквы, 
но если транслитерационная последовательность состоит из нескольких символов, то заглавным будет только первый из них: 
«С» на «S», а «Я» на «Ya».
Примечание 3. Если бы файл cyrillic.txt содержал текст:
Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to 
help him: they don’t want the truth to be exposed.
то содержимое файла transliteration.txt будет:
Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help 
him: they don’t want the truth to be exposed.
"""
with open('cyrillic.txt', 'r',  encoding='UTF-8') as file:
    l = file.read()
d = { 'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n',
      'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh',
      'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
      'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N',
      'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж':
          'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F',
      'Я': 'Ya' }
c = 0
while c < len(l):
    b = l[c]
    st1 = l[:c]
    st2 = l[c+1:]
    if b in d:
        b = d[b]
    l = st1 + b + st2
    c += 1
with open('transliteration.txt', 'w') as file:
    file.write(l)


""" Упражнение 8
При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и возвращаемое 
значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе забывают о них 😂.
На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите 
программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать, что 
любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит комментарий, 
если первый символ предыдущей строки - #.
Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.
Формат выходных данных
Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле), каждое на отдельной 
строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют поясняющий комментарий, 
то следует вывести: Best Programming Team.
Примечание 1. Если бы файл содержал код:
def powers(a):
    return a, a**2, a**3

# функция вычисляет сумму всех переданных чисел
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# функция возвращает количество переданных аргументов
def count_args(*args):
    return len(args)

def mean(*args):
    total = 0.0
    count = 0  
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count
    
def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# функция вычисляет факториал переданного числа
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
то результатом будет:
powers
matrix
mean
greet
Примечание 2. Гарантируется, что в файле есть хотя бы одна функция при этом вложенных функций в файле нет. 
"""
with open(input(), 'r',  encoding='UTF-8') as file:
    l = file.readlines()
l.insert(0, '')
x = []
for i in range(len(l)):
    if 'def ' in l[i] and '#' not in l[i-1]:
        st = l[i].replace('def ', '').split('(')
        x.append(st[0])
if x:
    print(*x, sep='\n')
else:
    print('Best Programming Team')

