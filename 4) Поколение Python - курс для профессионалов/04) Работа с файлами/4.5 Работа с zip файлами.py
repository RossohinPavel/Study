""" Упражнение 1
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное
число — количество файлов в этом архиве.
Примечание 1. Обратите внимание, что папка не считается файлом.
Примечание 2. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
"""
from zipfile import ZipFile
with ZipFile('workbook.zip') as zfile:
    a = zfile.infolist()
    print(sum([1 for x in a if not x.is_dir()]))


""" Упражнение 2
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит суммарный 
объем файлов этого архива в сжатом и не сжатом видах в байтах, в следующем формате:
    Объем исходных файлов: <объем до сжатия> байт(а)
    Объем сжатых файлов: <объем после сжатия> байт(а)
Примечание 1. Вывод на примере архива test.zip из конспекта:
    Объем исходных файлов: 7810260 байт(а)
    Объем сжатых файлов: 7798267 байт(а)
"""
from zipfile import ZipFile
un = 0
c = 0
with ZipFile('workbook.zip') as zfile:
    a = zfile.infolist()
    for name in a:
        un += name.file_size
        c += name.compress_size
print(f'Объем исходных файлов: {un} байт(а)', f'Объем сжатых файлов: {c} байт(а)', sep='\n')


""" Упражнение 3
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит название 
файла из этого архива, который имеет наилучший показатель степени сжатия.
Примечание 1. Если файл находится в папке, вывести следует только название без пути.
Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.
Примечание 3. Степень сжатия файла характеризуется коэффициентом KK, определяемым как отношение объема сжатого файла 
к объему исходного файла, выраженным в процентах.
"""
from zipfile import ZipFile
with ZipFile('workbook.zip') as zfile:
    a = zfile.infolist()
    comp = min(a, key=lambda x: x.compress_size/x.file_size*100 if not x.is_dir() else 100)
    print(comp.filename.split('/')[-1])


""" Упражнение 4
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия 
файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть 
расположены в лексикографическом порядке, каждое на отдельной строке.
Примечание 1. Если файл находится в папке, вывести следует только название без пути.
Примечание 2. Начальная часть ответа выглядит так:
    countries.json
    data_sample.csv
    ...
"""
from zipfile import ZipFile
with ZipFile('workbook.zip') as zfile:
    archive = zfile.infolist()
    lst = [name.filename.split('/')[-1] for name in archive if not name.is_dir() and name.date_time > (2021, 11, 30, 14, 22, 0)]
print(*sorted(lst), sep='\n')


""" Упражнение 5
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия всех 
файлов из этого архива в лексикографическом порядке, указывая для каждого его дату изменения, а также объем до и после 
сжатия, в следующем формате:
<название файла>
  Дата модификации файла: <дата изменения>
  Объем исходного файла: <объем до сжатия> байт(а)
  Объем сжатого файла: <объем после сжатия> байт(а)
Между данными о двух файлах должна располагаться пустая строка.
Примечание 1. Если файл находится в папке, вывести следует только название без пути.
Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):
Alexandra Savior – Crying All the Time.mp3
  Дата модификации файла: 2021-11-30 13:27:02
  Объем исходного файла: 5057559 байт(а)
  Объем сжатого файла: 5051745 байт(а)
  
Hollow Knight Silksong.exe
  Дата модификации файла: 2013-08-22 08:20:06
  Объем исходного файла: 805992 байт(а)
  Объем сжатого файла: 494930 байт(а)

...
"""
from zipfile import ZipFile
with ZipFile('workbook.zip') as zfile:
    archive = zfile.infolist()
    lst = list(sorted(filter(lambda x: not x.is_dir(), archive), key=lambda x: x.filename.split('/')[-1]))
    for name in lst:
        n = name.filename.split('/')[-1]
        x = [str(name.date_time[0])] + [str(x).rjust(2, '0') for x in name.date_time[1:]]
        md = f'  Дата модификации файла: {x[0]}-{x[1]}-{x[2]} {x[3]}:{x[4]}:{x[5]}'
        s = f'  Объем исходного файла: {name.file_size} байт(а)'
        c = f'  Объем сжатого файла: {name.compress_size} байт(а)'
        print(n, md, s, c, sep='\n')
        if lst.index(name) != len(lst) - 1:
            print()


""" Упражнение 6
Вам доступен набор различных файлов, названия которых представлены в списке file_names. Дополните приведенный ниже код, 
чтобы он создал архив files.zip и добавил в него все файлы из данного списка.
Примечание. Считайте, что файлы из списка file_names находятся в папке с программой.
"""
from zipfile import ZipFile
file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']
with ZipFile('files.zip', mode='w') as file:
    for name in file_names:
        file.write(name)


""" Упражнение 7
Вам доступен набор различных файлов, названия которых представлены в списке file_names. Также вам доступен архив 
files.zip. Дополните приведенный ниже код, чтобы он добавил в архив files.zip только те файлы из списка file_names, 
объем которых не превышает 100 байт.
Примечание 1. Получить объем файла в байтах позволяет функция getsize() из модуля os.path. Данная функция принимает в 
качестве аргумента путь к файлу и возвращает размер указанного файла в байтах.
Например, вычислить объем архива files.zip в байтах и сохранить его в переменную size можно следующим образом:
import os.path
size = os.path.getsize('files.zip')
Примечание 2. Вычислить объем файла в байтах можно и вручную, не прибегая к использованию сторонних модулей. 
Подумайте, как 😉. (Открыть файл в режиме чтения байт и посчитать их)
Примечание 3. Считайте, что файлы из списка file_names и архив files.zip находятся в папке с программой.
"""
from zipfile import ZipFile
import os
file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']
with ZipFile('files.zip', mode='w') as zfile:
    for name in file_names:
        if os.path.getsize(name) <= 100:
            zfile.write(name)


""" Упражнение 8
Реализуйте функцию extract_this(), которая принимает один или более аргументов в следующем порядке:
    zip_name — название zip архива, например, data.zip
    *args — переменное количество позиционных аргументов, каждый из которых является названием некоторого файла
Функция должна извлекать файлы *args из архива zip_name в папку с программой. Если в функцию не передано ни одного 
названия файла для извлечения, то функция должна извлечь все файлы из архива.
Примечание 1. Например, следующий вызов функции
    extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
должен извлечь из архива workbook.zip файлы earth.jpg и exam.txt в папку с программой.
Вызов функции
    extract_this('workbook.zip')
должен извлечь из архива workbook.zip все файлы в папку с программой.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию extract_this(), но не код, 
вызывающий ее.
"""
from zipfile import ZipFile
def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zfile:
        if args:
            for name in args:
                zfile.extract(name)
        else:
            zfile.extractall()


""" Упражнение 9
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из 
которых содержит информацию о каком-либо футболисте:
    {
       "first_name": "Gary",
       "last_name": "Cahill",
       "team": "Chelsea",
       "position": "Defender"
    }
У футболиста имеются следующие атрибуты: 
    first_name — имя
    last_name — фамилия
    team — название футбольного клуба
    position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих
за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — 
в лексикографическом порядке фамилий, каждый на отдельной строке.
Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным 
текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, 
воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.
Примечание 2. Начальная часть ответа выглядит так:
    Alex Iwobi
    Alexis Sanchez
    ...
"""
from zipfile import ZipFile
import json
def is_correct_json(string):
    try:
        return json.loads(string)
    except:
        return False
lst = []
with ZipFile('data.zip') as zip_file:
    files = [x.filename for x in zip_file.infolist() if not x.is_dir()]
    for name in files:
        with zip_file.open(name) as file:
            try:
                js = file.read().decode('utf-8')
            except:
                continue
            conv = is_correct_json(js)
            if conv and conv['team'] == 'Arsenal':
                lst.append([conv['first_name'], conv['last_name']])
for name in sorted(lst):
    print(*name)


""" Упражнение 10
Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его файловую 
структуру и объем каждого файла.
Формат входных данных
На вход программе ничего не подается.
Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде. Так как архив 
имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.
Примечание 1. Вывод на примере архива test.zip из конспекта:
test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B
Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.
Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:
1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 4. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
"""
from zipfile import ZipFile
def convert_bytes(size):
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'
with ZipFile('desktop.zip') as zip_file:
    for name in zip_file.infolist():
        fn = name.filename.split('/')
        indent = '  ' * (len(fn) - 2)
        if fn[-1] == '':
            print(f'{indent}{fn[-2]}')
        else:
            filesize = name.file_size
            if len(fn) > 1:
                indent = indent + '  '
            print(f'{indent}{fn[-1]} {convert_bytes(filesize)}')
