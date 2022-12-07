""" Упражнение 1
Назовем пароль хорошим, если
    его длина равна 9 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра
Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_good_password(),
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(is_good_password('41157082'))
Sample Output 1:
    False
Sample Input 2:
    print(is_good_password('мойпарольсамыйлучший'))
Sample Output 2:
    False
Sample Input 3:
    print(is_good_password('МойПарольСамыйЛучший111'))
Sample Output 3:
    True
"""

""" Упражнение 2
Назовем пароль хорошим, если
    его длина равна 99 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра
Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:
    string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:
    LengthError, если его длина меньше 99 символов
    LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
    DigitError, если в нем нет ни одной цифры
Примечание 1. Исключения LengthError, LetterError и DigitError уже определены и доступны.
Примечание 2. Приоритет возбуждения исключений в случае невыполнения нескольких условий: LengthError, затем LetterError, 
а уже после DigitError.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_good_password(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке. 
Sample Input 1:
    try:
        print(is_good_password('Short7'))
    except Exception as err:
        print(type(err))
Sample Output 1:
    <class '__main__.LengthError'>
Sample Input 2:
    print(is_good_password('еПQSНгиfУЙ70qE'))
Sample Output 2:
    True
Sample Input 3:
    try:
        print(is_good_password('41157081231232'))
    except Exception as err:
        print(type(err))
Sample Output 3:
    <class '__main__.LetterError'>
"""
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    let, num = '', ''
    for symb in string:
        if symb.isalpha():
            let += symb
        elif symb.isdigit():
            num += symb
    if let == let.upper() or let == let.lower():
        raise LetterError
    if not num:
        raise DigitError
    return True


""" Упражнение 3
Назовем пароль хорошим, если
    его длина равна 9 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра
Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
Формат входных данных
На вход программе подается произвольное количество паролей, каждая на отдельной строке. Гарантируется, что среди них 
присутствует хороший.
Формат выходных данных
Для каждого введенного пароля программа должна вывести текст:
    LengthError, если длина введенного пароля меньше 9 символов
    LetterError, если в нем все буквы имеют одинаковый регистр
    DigitError, если в нем нет ни одной цифры
    Success!, если введенный пароль хороший
После ввода хорошего пароля все последующие пароли должны игнорироваться.
Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий: LengthError, затем 
LetterError, а уже после DigitError.
Примечание 2. Воспользуйтесь функцией is_good_password() из предыдущей задачи.
Примечание 3. Тестовые данные доступны по ссылке. 
Sample Input 1:
    arr1
    Arrrrrrrrrrr
    arrrrrrrrrrrrrrr1
    Arrrrrrr1
Sample Output 1:
    LengthError
    DigitError
    LetterError
    Success!
Sample Input 2:
    beegeek
    Beegeek123
    Beegeek2022
    Beegeek2023
    Beegeek2024
Sample Output 2:
    LengthError
    Success!
"""
import sys

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    let, num = '', ''
    for symb in string:
        if symb.isalpha():
            let += symb
        elif symb.isdigit():
            num += symb
    if let == let.upper() or let == let.lower():
        raise LetterError
    if not num:
        raise DigitError
    return True

for line in sys.stdin:
    try:
        is_good_password(line.strip())
        print('Success!')
        break
    except LengthError:
        print('LengthError')
    except LetterError:
        print('LetterError')
    except DigitError:
        print('DigitError')
