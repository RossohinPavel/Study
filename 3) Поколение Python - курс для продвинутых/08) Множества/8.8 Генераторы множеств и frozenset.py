""" Упражнение 1
Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные значения
списка items. Результат вывести на одной строке, в упорядоченном виде, разделяя элементы одним символом пробела.
Примечание 1. Обратите внимание, некоторые элементы списка – числа, а некоторые – строки, при этом строки необходимо
трактовать как числа.
"""
items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
myset = {int(x) for x in items}
print(*sorted(myset))


""" Упражнение 2
Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее первую букву каждого 
слова (в нижнем регистре) списка words. Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним 
символом пробела.
"""
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
         'tangerine', 'Watermelon', 'currant', 'Almond']
myset = {x.lower()[0] for x in words}
print(*sorted(myset))


""" Упражнение 3
Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова 
(в нижнем регистре) строки sentence. Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним 
символом пробела.
Примечание. Учтите, что знаки пунктуации не относятся к словам.
"""
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a 
              pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, 
              over which, if you can still stand my style (I am writing under observation), the sun of my infancy had 
              set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge 
              in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; 
              a furry warmth, golden midges.'''
myset = {x.lower().strip('(,):;.') for x in sentence.split()}
print(*sorted(myset))


""" Упражнение 4
Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова  
строки sentence длиною меньше 44 символов. Результат вывести на одной строке (в нижнем регистре) в алфавитном порядке, 
разделяя элементы одним символом пробела.
Примечание. Учтите, что знаки пунктуации не относятся к словам.
"""
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a 
              pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, 
              over which, if you can still stand my style (I am writing under observation), the sun of my infancy had 
              set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge 
              in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; 
              a furry warmth, golden midges.'''
myset = {x.lower().strip('(,):;.') for x in sentence.split() if len(x.lower().strip('(,):;.')) < 4}
print(*sorted(myset))


""" Упражнение 5
Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные имена файлов 
c расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением, все на одной 
строке, в нижнем регистре, в алфавитном порядке через пробел.
Примечание. Если бы список files содержал следующие имена файлов:
files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 
'github.git', 'ZeBrA.PnG']
то ответом был бы:
apple.png python.png zebra.png
"""
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']
myset = {x.lower() for x in files if x.lower().endswith('png')}
print(*sorted(myset))
