""" Упражнение 1
Вводится слово. Необходимо первую букву этого слова сделать заглавной, а остальные - малыми.
Результат отобразить на экране.
Sample Input: HELLO
Sample Output: Hello
"""
w = input()
# Вариант 1
print(w[0].upper() + w[1:].lower())
# Вариант 2 (из ответов)
print(w.capitalize())


""" Упражнение 2 ('-')
Вводится строка. Необходимо определить число вхождений дефисов (-) в этой строке. На экране отобразить полученное число.
Sample Input: osnovnye-metody-strok
Sample Output: 2
"""
s = input()
print(s.count('-'))


""" Упражнение 3
Вводится строка. С помощью метода String.find найдите в этой строке индекс первого вхождения фрагмента "ra". 
Полученное число выведите на экран.
Sample Input: abrakadabra
Sample Output: 2
"""
s = input()
print(s.find('ra'))


""" Упражнение 4
Вводится строка (слаг). Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные (-). 
Подумайте, в какой последовательности следует выполнять эти замены. Результат преобразования выведите на экран.
Sample Input: dobavlyaem---slagi--slug-k--url---adresam
Sample Output: dobavlyaem-slagi-slug-k-url-adresam
"""
s = input()
print(s.replace('---', '-').replace('--', '-'))


""" Упражнение 5
Вводятся три целых положительных числа (максимум трехзначные) через пробел в одну строчку. 
Для двухзначных и однозначных чисел нужно добавить слева незначащие нули так, чтобы все числа содержали по три цифры. 
Вывести на экран полученные числа в столбик.
Sample Input: 8 11 123
Sample Output: 008 / 011 / 123
"""
s1, s2, s3 = map(str, input().split())
print(s1.rjust(3, '0'), s2.rjust(3, '0'), s3.rjust(3, '0'), sep='\n')


""" Упражнение 6
Вводится строка, состоящая из слов, разделенных пробелом. 
Необходимо подсчитать число слов в этой строке и результат (число) отобразить на экране.
Sample Input: I love Python
Sample Output: 3
"""
a = map(str, input().split())
print(len(list(a)))


""" Упражнение 7
Вводится строка, состоящая из названий городов, разделенных пробелом. 
Необходимо преобразовать эту строку, чтобы названия городов шли через точку с запятой. Результат отобразить на экране.
Sample Input: Москва Тверь Казань
Sample Output: Москва;Тверь;Казань
"""
a = input()
print(a.replace(" ", ";"))
