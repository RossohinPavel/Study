""" Упражнение 1
Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел). Необходимо выбрать и
отобразить на экране уникальные числа, присутствующие и в первом и во втором списках одновременно. Результат выведите
на экран в виде строки чисел, записанных по возрастанию через пробел, используя команду (здесь s - это множество):
print(*sorted(s))
P. S. О функции sorted мы еще будем говорить, а также об операторе *. Пока просто запомните такую возможность
сортировки и вывода произвольных коллекций на экран.
Sample Input:
    8 11 12 15 -2
    4 11 10 15 -5 1 -2
Sample Output: -2 11 15
"""
a = set(input().split())
b = set(input().split())
s = a & b
print(*sorted(s))


""" Упражнение 2
Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел). Необходимо выбрать и 
отобразить на экране уникальные числа, присутствующие в первом списке, но отсутствующие во втором. Результат выведите на 
экран в виде строки чисел, записанных по возрастанию через пробел.
Sample Input:
    8 5 3 5 -3 1
    1 2 3 4
Sample Output:
    -3 5 8
"""
a = set(map(int, input().split()))
b = set(map(int, input().split()))
a -= b
print(*sorted(a))


""" Упражнение 3
Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел). Необходимо выбрать и 
отобразить на экране уникальные числа, присутствующие в первом или втором списках, но отсутствующие одновременно в 
обоих. Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел.
Sample Input:
    1 2 3 4 5
    4 5 6 7 8
Sample Output:
    1 2 3 6 7 8
"""
a = set(map(int, input().split()))
b = set(map(int, input().split()))
s = a ^ b
print(*sorted(s))


""" Упражнение 4
Вводятся два списка городов каждый с новой строки (в строке названия через пробел). Необходимо сравнить их между собой 
на равенство по уникальным (не повторяющимся) городам. Если списки содержат одни и те же уникальные города, то вывести 
на экран ДА, иначе - НЕТ.
Sample Input:
    Москва Тверь Уфа Казань Уфа Москва
    Уфа Тверь Москва Казань
Sample Output:
    ДА
"""
a = set(input().split())
b = set(input().split())
print("ДА" if a == b else 'НЕТ')


""" Упражнение 5
Вводится список оценок студента - его ответов у доски по предмету "Информатика" в виде чисел от 2 до 5 в одну строку 
через пробел. Если студент имеет хотя бы одну двойку, то он не допускается до экзамена. Определить на основе введенного 
списка, допущен ли студент. Если допущен, то вывести слово ДОПУЩЕН, иначе - НЕ ДОПУЩЕН. При реализации задачи 
используйте множество для определения наличия двойки.
Sample Input: 3 4 4 5 2 3
Sample Output: НЕ ДОПУЩЕН
"""
a = set(map(int, input().split()))
print('ДОПУЩЕН' if 2 not in a else 'НЕ ДОПУЩЕН')


""" Упражнение 6
Вводятся два списка городов каждый с новой строки (в строке названия через пробел), которые объехал Сергей в 1-й и 2-й 
годы своего путешествия по России. Требуется определить, включал ли его маршрут во 2-й год все города 1-го года 
путешествия? Если это так, то вывести ДА, иначе - НЕТ.
Sample Input:
    Москва Казань Самара Москва
    Москва Владимир Новгород Казань Самара Москва
Sample Output: ДА
"""
a = set(input().split())
b = set(input().split())
print('ДА' if a < b else 'НЕТ')


""" Упражнение 7
Вводится натуральное число, которое может быть определено простыми множителями 1, 2, 3, 5 и 7. Необходимо разложить 
введенное число на указанные простые множители и проверить, содержит ли оно множители 2, 3 и 5 
(все указанные множители)? Если это так, то вывести ДА, иначе - НЕТ.
Sample Input: 210
Sample Output: ДА
"""
a = int(input())
m = (2, 3, 5, 7)
mm = set()
while a != 1:
    for i in m:
        while a % i == 0:
            a /= i
            mm.add(i)
print('ДА' if {2, 3, 5} <= mm else 'НЕТ')
