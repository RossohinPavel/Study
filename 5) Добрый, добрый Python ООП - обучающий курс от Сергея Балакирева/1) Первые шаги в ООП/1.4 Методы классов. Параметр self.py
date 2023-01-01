""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/AbMOpQSt1fA
Подвиг 4. Объявите класс с именем MediaPlayer с двумя методами:
open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со значением аргумента file
в объекте класса MediaPlayer)
play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")
Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод open() с аргументом "filemedia1"
для объекта media1 и "filemedia2" для объекта media2. После этого вызовите через объекты метод play(). При этом,
на экране должно отобразиться две строки (без кавычек):
"Воспроизведение filemedia1"
"Воспроизведение filemedia2"
"""
class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print('Воспроизведение ' + self.filename)


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open('filemedia1')
media2.open('filemedia2')

media1.play()
media2.play()


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/XNbphw3bYAI
Подвиг 5. Объявите класс с именем Graph и методами:
    set_data(data) - передача набора данных data для последующего отображения (data - список числовых данных);
    draw() - отображение данных (в том же порядке, что и в списке data)
и атрибутом:
    LIMIT_Y = [0, 10]
Метод set_data() должен формировать локальное свойство data объекта класса Graph. Атрибут data должен ссылаться на 
переданный в метод список. Метод draw() должен выводить на экран список в виде строки из чисел, разделенных пробелами и 
принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).
Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и передайте список:
[10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с соответствующим набором чисел, 
записанных через пробел. Например (вывод без кавычек):
"10 0 2 5 7"
"""
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print(*(x for x in self.data if x in range(self.LIMIT_Y[0], self.LIMIT_Y[1] + 1)))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/IxXtZXrnnDY
Подвиг 7. Имеется следующий класс для считывания информации из входного потока:
import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
Которым, затем, можно воспользоваться следующим образом:
    sr = StreamReader()
    data, result = sr.readlines()
Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
    def create(self, fields, lst_values): ...
который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields) и список строк 
lst_in (передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с именами 
полей из fields и соответствующими значениями из lst_values.
Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. Если число полей и 
число строк не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.
P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.
Пример входной информации (Sample Input):
    10
    Питон - основы мастерства
    512
"""
import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for i in range(len(fields)):
                setattr(self, fields[i], lst_values[i])
            return True
        # Можно else не писать и сразу после блока иф поставить return. Но явное лучше неявного.
        else:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ljahVEppmxM
Подвиг 9. Из входного потока читаются строки данных с помощью команды:
    lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:
    1 Сергей 35 120000
    2 Федор 23 12000
    3 Иван 13 1200
    ...
То есть, каждая строка - это элемент списка lst_in.
Необходимо в класс DataBase:
    class DataBase:
        lst_data = []
        FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода:
    select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их 
индексам (не id, а индексам списка); также учесть, что граница b может превышать длину списка.
    insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
Каждая запись в списке lst_data должна быть представлена словарем в формате:
{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}
Например:
{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции 
FIELDS.
P. S. Ваша задача только добавить два метода в класс DataBase.
Sample Input:
    1 Сергей 35 120000
    2 Федор 23 12000
    3 Иван 13 1200
"""
import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))

    def select(self, a, b):
        return self.lst_data[a:b+1]


db = DataBase()
db.insert(lst_in)


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/butyKEUntK0
Подвиг 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует, 
то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать); если связка eng-rus 
уже существует, то второй раз ее добавлять не нужно, например:  add('go', 'идти'), add('go', 'идти');
remove(self, eng) - для удаления связки по указанному английскому слову;
translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов, 
соответствующих переводу английского слова, даже если в списке всего одно слово).
Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator, т.е. 
связки хранить локально внутри экземпляров классов класса Translator.
Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
    tree - дерево
    car - машина
    car - автомобиль
    leaf - лист
    river - река
    go - идти
    go - ехать
    go - ходить
    milk - молоко
Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go. 
Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
Вывод в формате: идти ехать ходить
"""
class Translator:
    def add(self, eng, rus):
        current = getattr(self, eng, False)
        if current is False:
            setattr(self, eng, [rus])
        if current and rus not in current:
            current.append(rus)

    def remove(self, eng):
        delattr(self, eng)

    def translate(self, eng):
        return getattr(self, eng)


tr = Translator()

for i in ('tree - дерево', 'car - машина', 'car - автомобиль', 'leaf - лист', 'river - река', 'go - идти',
          'go - ехать', 'go - ходить', 'milk - молоко'):
    tr.add(*i.split(' - '))

tr.remove('car')

print(*tr.translate('go'))
