""" Упражнение 1
Дополните приведенный код, используя генератор, так чтобы получить словарь result , в котором ключом будет позиция числа
в списке numbers (начиная с 00), а значением – его квадрат.
Примечание. Выводить содержимое словаря result не нужно.
"""
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {i: v ** 2 for i, v in enumerate(numbers)}

""" Упражнение 2
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
colors, кроме тех, у которых значением является None.
Примечание. Выводить содержимое словаря result не нужно.
"""
colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange',
          'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber',
          'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None,
          'c22': 'Sand', 'c23': None}
result = {key: value for key, value in colors.items() if value is not None}

""" Упражнение 3
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
favorite_numbers , значения которых являются двузначными числами.
Примечание. Выводить содержимое словаря result не нужно.
"""
favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
                    'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
                    'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
                    'anna': 55, 'madlen': 876}
result = {k: v for k, v in favorite_numbers.items() if len(str(v)) == 2}

""" Упражнение 4
Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов словаря 
months , в которых ключ и значение поменялись местами.
Примечание. Выводить содержимое словаря result не нужно.
"""
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9:
          'September', 10: 'October', 11: 'November', 12: 'December'}
result = {v: k for k, v in months.items()}


""" Упражнение 5
В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить словарь 
result , в котором числа будут ключами, а слова – значениями.
Примечание 1. Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).
Примечание 2. Выводить содержимое словаря result не нужно.
"""
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(i.split(':')[0]): i.split(':')[1] for i in s.split()}


""" Упражнение 6
Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка numbers, 
а значением – отсортированный по возрастанию список всех его делителей начиная с 1.
Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь
result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}
Примечание 2. Выводить содержимое словаря result не нужно. 
"""
numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {i: [x for x in range(1, i+1) if i % x == 0] for i in numbers}


""" Упражнение 7
Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет строка – 
элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.
Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь
result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}
Примечание 2. Для получения ASCII кода символа используйте функцию ord().
Примечание 3. Выводить содержимое словаря result не нужно.
"""
words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
result = {x: [ord(i) for i in x] for x in words}


""" Упражнение 8
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
letters , за исключением тех, ключи которых есть в списке remove_keys.
Примечание. Выводить содержимое словаря result не нужно.
"""
letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
           13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
           26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = {x: letters[x] for x in letters if x not in remove_keys}


""" Упражнение 9
В переменной students хранится словарь, содержащий информацию о росте (в см) и весе (в кг) студентов.
Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря 
students , где указан рост больше 167167 см, а вес меньше 7575 кг.
Примечание. Выводить содержимое словаря result не нужно.
"""
students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
            'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
            'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
            'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}


""" Упражнение 10
Список tuples содержит кортежи, состоящие из трех чисел.
Дополните приведенный код, используя генератор, чтобы получить словарь result, в котором ключом является первый 
элемент каждого кортежа, а значением – кортеж из оставшихся двух элементов.
Примечание. Выводить содержимое словаря result не нужно.
"""
tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
          (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
result = {x[0]:x[1:] for x in tuples}


""" Упражнение 11
Даны три списка student_ids, student_names, student_grades, содержащие информацию о студентах.

Дополните приведенный код, используя генератор, так чтобы получить список result, содержащий вложенные словари в 
соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].
Примечание 1. Для параллельной итерации по всем трем спискам одновременно можно использовать встроенную функцию zip().
Примечание 2. Выводить содержимое списка result не нужно.
"""
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
                 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman',
                 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
result = [{a: {b:c}} for a, b, c in zip(student_ids, student_names, student_grades)]
