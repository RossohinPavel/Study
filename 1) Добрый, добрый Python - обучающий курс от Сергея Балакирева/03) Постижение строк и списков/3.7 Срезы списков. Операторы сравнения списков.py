""" Упражнение 1
Имеется список числа просмотров видео по дням: v = [1205, 1101, 1434, 1320, 923, 874]
Необходимо выбрать из него первые три значения (используя срезы) и вывести результат на экран.
Sample Input:
Sample Output: [1205, 1101, 1434]
"""
v = [1205, 1101, 1434, 1320, 923, 874]
print(v[:3])


""" Упражнение 2
Имеется список числа просмотров видео по дням: v = [1205, 1101, 1434, 1320, 923, 874]
Необходимо выбрать из него последние четыре значения (используя срезы) и вывести результат на экран.
Sample Input:
Sample Output: [1434, 1320, 923, 874]
"""
v = [1205, 1101, 1434, 1320, 923, 874]
print(v[-4:])


""" Упражнение 3
Имеется список городов: c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
Необходимо с помощью срезов выбрать из него города через один (начиная с первого) и результат вывести на экран.
Sample Input:
Sample Output: ['Москва', 'Самара', 'Вологда', 'Уфа']
"""
c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
print(c[::2])


""" Упражнение 4
Имеется список городов: c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
Необходимо с помощью срезов выбрать из него города через один (начиная со второго) и результат вывести на экран.
Sample Input:
Sample Output: ['Ульяновск', 'Тверь', 'Омск']
"""
c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
print(c[1::2])


""" Упражнение 5
Имеется список с оценками студента: m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
Необходимо с помощью срезов выбрать элементы с 3-го по 7-й (включительно) и вывести их на экран в обратном порядке.
Sample Input:
Sample Output: [3, 2, 2, 5, 5]
"""
m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
m = m[2:7]
print(m[::-1])


""" Упражнение 6
Имеется список с оценками студента: m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
Необходимо с помощью срезов выбрать элементы через один, начиная с последнего, и вывести результат на экран.
Sample Input:
Sample Output: [4, 5, 3, 2, 5, 3]
"""
m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[::-2])
