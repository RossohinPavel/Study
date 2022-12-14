""" Упражнение 1
Необходимо задать строку со следующим содержимым: Тема занятия "спецсимволы".
И отобразить ее на экране (кавычки у слова спецсимволы также должны быть отображены).
Sample Input:
Sample Output: Тема занятия "спецсимволы"
"""
s = r'Тема занятия "спецсимволы"'
print(s)


""" Упражнение 2
Вводится два слова в одну строку через пробел. Поставьте между этими словами символ обратного слеша (вместо пробела). 
Результирующую строку отобразите на экране.
P. S. Задачу реализовать без применения F-строк.
Sample Input: Hello Balakirev!
Sample Output: Hello\\Balakirev!
"""
s = input()
print(s.replace(' ', '\\'))


""" Упражнение 3
Вводится строка со словами, разделенными пробелом. Необходимо первый пробел заменить на одинарную кавычку, 
а все остальные - на двойные. Результирующую строку отобразить на экране.
Sample Input: My best friend is Python!
Sample Output: My'best"friend"is"Python!
"""
s = input()
print(s.replace(' ', '\"').replace('\"', '\'', 1))


""" Упражнение 4
Используя raw-строки, задайте строку, содержащую этот путь к файлу: C:\\WINDOWS\\System32\\drivers\\etc\\hosts. 
Результат отобразите на экране.
Sample Input:
Sample Output: C:\\WINDOWS\\System32\\drivers\\etc\\hosts
"""
s = r'C:\WINDOWS\System32\drivers\etc\hosts'
print(s)


""" Упражнение 5
Вводится слово. Необходимо сформировать новую строку, где введенное слово будет заключено в двойные кавычки. 
Результат выведите на экран.
Sample Input: language
Sample Output: "language"
"""
s = input()
s2 = '\"' + s + '\"'
print(s2)
