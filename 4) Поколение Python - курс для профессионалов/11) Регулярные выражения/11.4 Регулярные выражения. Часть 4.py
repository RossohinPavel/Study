""" Упражнение 1
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют слова
a, A, an и An.
Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами,
соответствующими \W
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    A cow is an animal.
Sample Output 1:
    A an
Sample Input 2:
    I have been reading this text for aN hour. Сan you give me this book? AN or an apple
Sample Output 2:
    an
Sample Input 3:
    An acle, a Ancle, A antarktida, an Any
Sample Output 3:
    An a A an
"""
regex = r'\b[aA]n?\b'


""" Упражнение 2
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют слова, 
написанные строго заглавными латинскими буквами.
Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, 
соответствующими \W
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    Why isn’t my progress in the APP synchrONized with my progress in the WEB version?
Sample Output 1:
    APP WEB
Sample Input 2:
    OOO 'BEEGEEK'
Sample Output 2:
    OOO BEEGEEK
Sample Input 3:
    I will go to the shop aNd you stay At home
Sample Output 3:
    I
"""
regex = r'\b[A-Z]+\b'


""" Упражнение 3
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют слова, 
начинающиеся с латинской заглавной буквы.
Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, 
соответствующими \W
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    I signed up in the app using my Apple ID. How can I sign in to the web version?
Sample Output 1:
    I Apple ID How I
Sample Input 2:
    I can Do it MYSELF
Sample Output 2:
    I Do MYSELF
Sample Input 3:
    How are --U--
Sample Output 3:
    How U
"""
regex = r'\b[A-Z]\w*\b'


""" Упражнение 4
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки, 
содержащие открывающую круглую скобку, а за ней когда-нибудь закрывающую круглую скобку.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    (41 + 9) * 2 = ?
Sample Output 1:
    (41 + 9) * 2 = ?
Sample Input 2:
    A synthesizer (also spelled synthesiser) is an electronic musical instrument that generates audio signals.
Sample Output 2:
    A synthesizer (also spelled synthesiser) is an electronic musical instrument that generates audio signals.
Sample Input 3:
    It was to be both a technical and surprisingly emotional challenge!))
Sample Output 3:
"""
regex = r'.*\(.*\).*'


""" Упражнение 5
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки, 
удовлетворяющие следующим условиям:
    строка начинается с двух или более цифр
    после следуют ноль или более букв латинского алфавита в нижнем регистре
    строка оканчивается нулем или более букв латинского алфавита в верхнем регистр
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    51tePIK
Sample Output 1:
    51tePIK
Sample Input 2:
    79
Sample Output 2:
    79
Sample Input 3:
    stePIK
Sample Output 3:
"""
regex = r'\b\d{2,}[a-z]*[A-Z]*\b'


""" Упражнение 6
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки, 
удовлетворяющие следующим условиям:
    строка содержит исключительно буквы латинского алфавита в произвольном регистре
    строка оканчивается латинской буквой s в нижнем регистре
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Chess
Sample Output 1:
    Chess
Sample Input 2:
    exodus
Sample Output 2:
    exodus
Sample Input 3:
    Diablo
Sample Output 3:
"""
regex = r'^[A-Za-z]*s$'


""" Упражнение 7
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки 
длины 45, удовлетворяющие следующим условиям:
    первые 40 символов являются либо латинскими буквами произвольного регистра, либо четными цифрами
    последние 55 символов являются либо нечетными цифрами, либо символами пробела
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    BpOBNpqKg4EgPKxWn8wavcQMOP06nbCwvOdu6CPj11111
Sample Output 1:
    BpOBNpqKg4EgPKxWn8wavcQMOP06nbCwvOdu6CPj11111
Sample Input 2:
    BTJubHCvbwTQEN2BqQJsgAIDW4bcyFyUp4COdUO4 3791
Sample Output 2:
    BTJubHCvbwTQEN2BqQJsgAIDW4bcyFyUp4COdUO4 3791
Sample Input 3:
    Sufk6dm7ECNGRlJ7VsIB7HvBOvSgAoN9gIUOqwy4
Sample Output 3:
"""
regex = r'[A-Za-z02468]{40}[ 13579]{5}'


""" Упражнение 8
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки, 
удовлетворяющие следующим условиям:
строка начинается с Mr., Mrs., Ms., Dr. или Er.
оставшаяся часть строки состоит только из одной или более букв латинского алфавита в произвольном регистре
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Mr.Guev
Sample Output 1:
    Mr.Guev
Sample Input 2:
    Ms.Jones
Sample Output 2:
    Ms.Jones
Sample Input 3:
    Dr. Guev
Sample Output 3:
Sample Input 4:
    MRS.Traveler
"""
regex = r'^Mr\.[A-Za-z]+$|^Mrs\.[A-Za-z]+$|^Ms\.[A-Za-z]+$|^Dr\.[A-Za-z]+$|^Er\.[A-Za-z]+$'


""" Упражнение 9
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют строки, 
удовлетворяющие следующим условиям:
    строка начинается с одной или двух цифр
    после следуют три или более буквы латинского алфавита в произвольном регистре
    оставшаяся часть строки содержит от 0 до 3 точек включительно
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    71mur...
Sample Output 1:
    71mur...
Sample Input 2:
    4rTur
Sample Output 2:
    4rTur
Sample Input 3:
    Python...
Sample Output 3:
"""
regex = r'^\d{1,2}[A-Za-z]{3,}\.{,3}$'
