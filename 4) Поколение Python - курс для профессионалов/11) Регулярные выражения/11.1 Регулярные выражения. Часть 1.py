""" Упражнение 1
Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:
    7-ddd-ddd-dd-dd
    8-ddd-dddd-dddd
где d — цифра от 0 до 9.
Формат входных данных
На вход программе подается строка произвольного содержания.
Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам, указанным в условии задачи,
и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Перезвони мне, пожалуйста: 7-919-667-21-19
Sample Output 1:
    7-919-667-21-19
Sample Input 2:
    Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911
Sample Output 2:
    7-919-667-21-19
    8-917-4864-1911
"""
def is_phone_number(phone):
    groups = phone.split('-')
    chars = ''.join(groups)
    if len(groups) == 4 and len(chars) == 12 and chars.startswith('8') and len(groups[2]) == 4:
        return all(c.isdigit() for c in chars)
    elif len(groups) == 5 and len(chars) == 11 and chars.startswith('7') and len(groups[2]) == 3:
        return all(c.isdigit() for c in chars)
    else:
        return False


def get_all_numbers(text):
    for c in range(len(text)):
        chunk = text[c:c + 15]
        if is_phone_number(chunk):
            yield chunk

print(*get_all_numbers(input()), sep='\n')


""" Упражнение 2
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствует строка beegeek.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
We work really hard in Beegeek =) #python #stepik #beegeek
Sample Output 1:
beegeek
Sample Input 2:
Beegek beegeek BEEGEEK bEeGeEk beegeek
Sample Output 2:
beegeek beegeek
"""
regex = r'beegeek'


""" Упражнение 3
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют 
последовательности формата xxx.xxx, где x — любой символ.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Hello.How are you today?
Sample Output 1:
    llo.How
Sample Input 2:
    I read the letter.Stood up.Sat down.Pondered for a minute.Then reread the letter again.
Sample Output 2:
    ter.Sto  up.Sat own.Pon ute.The
"""
regex = r'...\....'


""" Упражнение 4
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют 
последовательности цифр, представляющие целые числа от 100 до 199 включительно.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    150 + 1000 = 1150
Sample Output 1:
    150 100 115
Sample Input 2:
    100 - 199
Sample Output 2:
    100 199
"""
regex = r'1\d\d'


""" Упражнение 5
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют телефонные 
номера формата xxx-xxx-xxxx, где x — произвольная цифра.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    Call me tonight: 415-441-9116, xxx-xxx-xx37
Sample Output 1:
    415-441-9116
Sample Input 2:
    www441-515-9867www
Sample Output 2:
    441-515-9867
"""
regex = r'\d{3}-\d{3}-\d{4}'
