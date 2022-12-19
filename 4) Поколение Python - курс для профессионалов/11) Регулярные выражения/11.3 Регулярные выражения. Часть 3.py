""" Упражнение 1
PAN (Permanent Account Number) – это уникальный номер, который присваивается всем налогоплательщикам в Индии.
Он имеет следующий формат:
    <letter><letter><letter><letter><letter><digit><digit><digit><digit><letter>
PAN всегда состоит из 1010 символов, в котором letter — заглавная латинская буква, а digit — цифра.
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют PAN номера.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    The PAN (or PAN number) is a ten-character long alpha-numeric unique identifier. Example: AAAPZ1234C
Sample Output 1:
    AAAPZ1234C
Sample Input 2:
    first number is ABCD EZZPA1234ZaPMQ0000O, check thusEZZPA1234ZAPMQ0000O,
Sample Output 2:
    EZZPA1234Z EZZPA1234Z
"""
regex = r'[A-Z]{5}\d{4}[A-Z]'


""" Упражнение 2
HTML-элементы — основа языка HTML. Каждый парный HTML-элемент обозначается начальным (открывающим) и конечным 
(закрывающим) тегами. Открывающий и закрывающий теги содержат имя элемента. Комментарии в страницах HTML помещаются 
между тегами <!-- и -->.
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют 
комментарии HTML.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Hi, your tags <!-bee-> and <--geek--> are incorrect. Correct tags look like <!--beegeek-->
Sample Output 1:
    <!--beegeek-->
Sample Input 2:
    <!-- header of page --> <-- incorrect header of page !-->
Sample Output 2:
    <!-- header of page -->
"""
regex = r'<!--.*?-->'


""" Упражнение 3
Каждому гражданину страны Утопия выдается идентификационный номер, который имеет следующий формат:
    номер начинается с 00—33 строчных латинских букв включительно
    далее следует последовательность цифр, длина которой должна быть от 2 до 8 включительно
    после цифр указываются 33 или более заглавные латинские буквы
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют 
идентификационные номера граждан Утопии.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Dear citizen! Your old ID: tba44891AHH, your new ID: 781AHHGYT
Sample Output 1:
    tba44891AHH 781AHHGYT
Sample Input 2:
    1. name Tobot id: 234AZXR, 2. name Alph id: a6578ALPH, 3. name Teta id: abra0909CADABRA 4. name Alph up id: A6578ALPH
Sample Output 2:
    234AZXR a6578ALPH bra0909CADABRA 6578ALPH
"""
regex = r'[a-z]{0,3}\d{2,8}?[A-Z]{3,}'


""" Упражнение 4
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют почтовые 
индексы Великобритании, удовлетворяющие следующим условиям:
почтовый индекс начинается с одной или двух заглавных латинских букв, за которыми следует одна цифра. После цифры 
может следовать один необязательный символ — цифра или заглавная латинская буква
далее через пробел указываются одна цифра и любые две заглавные латинские буквы, кроме C, I, K, M, O, V
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Our postcodes. Arthur: NW11 8AB, Timur: P01 3AX, Anri: H7Z9T4 Dima: N16 6PS
Sample Output 1:
    NW11 8AB P01 3AX N16 6PS
Sample Input 2:
    my postcode is: 1 1PR, but it's not correct, my another postcode P0Z 9AU, it's correct, Artur's postcode CI0 0GG, 
    it's correct, Timur's postcode CIK7O 8JH, it's not correct
Sample Output 2:
    P0Z 9AU CI0 0GG IK7O 8JH
"""
regex = r'[A-Z]{1,2}\d[0-9A-Z]? \d[ABDEFGHJLNPQRSTWYXUZ]{2}'
