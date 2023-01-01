""" Упражнение 1
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/KV8T8JDtxW4
Подвиг 6. В программе предполагается реализовать парсер (обработчик) строки с данными string в определенный выходной
формат. Для этого объявлен следующий класс:
class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq
И предполагается его использовать следующим образом:
    res = Loader.parse_format("4, 5, -6", Factory)
На выходе (в переменной res) ожидается получать список из набора целых чисел. Например, для заданной строки, должно
получиться:
[4, 5, -6]
Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:
build_sequence() - для создания пустого списка (метод возвращает пустой список);
build_number(string) - для преобразования строки (string) в целое число (метод возвращает полученное целочисленное
значение).
Объявите класс с именем Factory, чтобы получать на выходе искомый результат.
P.S. В программе на экран ничего выводить не нужно.
"""
# Здесь объявляется класс Factory
class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)


""" Упражнение 2
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/D02X5B6zLi8
Подвиг 7. В программе объявлен следующий класс для работы с формами ввода логин/пароль:
class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
Который предполагается использовать следующим образом:
    login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
    html = login.render_template()
Необходимо прописать классы TextInput и PasswordInput, объекты которых формируются командами:
    login = TextInput(name, size)
    psw = PasswordInput(name, size)
В каждом объекте этих классов должны быть следующие локальные свойства:
    name - название для поля (сохраняет передаваемое имя, например, "Логин" или "Пароль");
    size - размер поля ввода (целое число, по умолчанию 10).
Также классы TextInput и PasswordInput должны иметь метод:
get_html(self) - возвращает сформированную HTML-строку в формате (1-я строка для класса TextInput; 
2-я - для класса PasswordInput):
        <p class='login'><имя поля>: <input type='text' size=<размер поля> />
        <p class='password'><имя поля>: <input type='text' size=<размер поля> />
Например, для поля login:
    <p class='login'>Логин: <input type='text' size=10 />
Также классы TextInput и PasswordInput должны иметь метод класса (@classmethod):
check_name(cls, name) - для проверки корректности переданного имя поля (следует вызывать в инициализаторе) по следующим критериям:
- длина имени не менее 3 символов и не более 50;
- в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
Если проверка не проходит, то генерировать исключение командой:
    raise ValueError("некорректное поле name")
Для проверки допустимых символов в каждом классе должен быть прописан атрибут CHARS_CORRECT:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
По заданию нужно объявить только классы TextInput и PasswordInput с соответствующим функционалом. Более ничего.
P. S. В данном задании получится дублирование кода в классах TextInput и PasswordInput. На данном этапе - это нормально.
"""
from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if not 3 <= len(name) <= 50:
            raise ValueError("некорректное поле name")
        for x in name:
            if x not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")
        return name

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size}/>"


class PasswordInput(TextInput):
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size}/>"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()


""" Упражнение 3
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9766M0dS1qc
Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен иметь 
следующие методы:
check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True, если номер в верном 
формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано 
верно и False - в противном случае.
Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например, 
SERGEI BALAKIREV.
Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):
    is_number = CardCheck.check_card_number("1234-5678-9012-0000")
    is_name = CardCheck.check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).
P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""
from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + ' '

    @staticmethod
    def check_card_number(number):
        return True if re.fullmatch(r'\d{4}(-\d{4}){3}', number) else False

# Можно было и этот метод забить регуляркой. Ради разнообразия и использования @classmethod напишем вручную
    @classmethod
    def check_name(cls, name):
        for x in name:
            if x not in cls.CHARS_FOR_NAME:
                return False
        if len(name.split()) != 2:
            return False
        return True


""" Упражнение 4
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YkDq9p8n17A
Подвиг 9. Объявите в программе класс Video с двумя методами:
    create(self, name) - для задания имени name текущего видео 
    (метод сохраняет имя name в локальном атрибуте name объекта класса Video);
    play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").
Объявите еще один класс с именем YouTube, в котором объявите два метода (с декоратором @classmethod):
    add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
    play(cls, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).
(здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):
videos - для хранения добавленных объектов класса Video (изначально список пуст).
Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем, 
вызывать метод play() класса Video.
Методы add_video и play вызывайте напрямую из класса YouTube. Создавать экземпляр этого класса не нужно.
Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП". 
После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите (с помощью метода 
play класса YouTube) сначала первое, а затем, второе видео.
Sample Input:
Sample Output:
воспроизведение видео Python
воспроизведение видео Python ООП
"""
class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1, v2 = Video(), Video()
v1.create('Python')
v2.create('Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)


""" Упражнение 5
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Y4Hvpg4FuKs
Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS. В этом классе 
должны быть реализованы следующие методы:
    add_application(self, app) - добавление нового приложения app в магазин;
    remove_application(self, app) - удаление приложения app из магазина;
    block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в 
        значение True);
    total_apps(self) - возвращает общее число приложений в магазине.
Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
    store = AppStore()
    app_youtube = Application("Youtube")
    store.add_application(app_youtube)
    store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса Application 
должен содержать локальные свойства:
    name - наименование приложения (строка);
    blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).
Как хранить список приложений в объектах класса AppStore решите сами.
P.S. В программе нужно только объявить классы с указанным функционалом.
"""
class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


class AppStore:
    collections = []

    @classmethod
    def add_application(cls, app):
        """добавление нового приложения app в магазин"""
        cls.collections.append(app)

    @classmethod
    def remove_application(cls, app):
        """удаление приложения app из магазина"""
        cls.collections.remove(app)

    @classmethod
    def block_application(cls, app):
        """блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True)"""
        cls.collections[cls.collections.index(app)].blocked = True

    @classmethod
    def total_apps(cls):
        """возвращает общее число приложений в магазине"""
        return len(cls.collections)


""" Упражнение 6
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/38QoBSpQqnM
Подвиг 11 (на повторение). Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:
    add_message(msg) - добавление нового сообщения в список сообщений;
    remove_message(msg) - удаление сообщения из списка;
    set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет 
        то он ставится, если уже есть, то убирается);
    show_last_message(число) - отображение последних сообщений;
    total_messages() - возвращает общее число сообщений.
Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):
    msg = Message("Всем привет!")
    Viber.add_message(msg)
    Viber.add_message(Message("Это курс по Python ООП."))
    Viber.add_message(Message("Что вы о нем думаете?"))
    Viber.set_like(msg)
    Viber.remove_message(msg)
Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения 
        (булево значение True - если лайк есть и False - в противном случае, изначально False);
P.S. Как хранить список сообщений, решите самостоятельно.
"""
class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    m_list = []

    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений"""
        cls.m_list.append(msg)

    @classmethod
    def remove_message(cls, msg):
        """удаление сообщения из списка"""
        cls.m_list.remove(msg)

    @classmethod
    def set_like(cls, msg):
        """поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg:
        если лайка нет то он ставится, если уже есть, то убирается)"""
        obj = cls.m_list[cls.m_list.index(msg)]
        obj.fl_like = not obj.fl_like

    @classmethod
    def show_last_message(cls, num):
        """отображение последних сообщений"""
        print(cls.m_list[-num:])

    @classmethod
    def total_messages(cls):
        """возвращает общее число сообщений."""
        return len(cls.m_list)
