""" Упражнение 1
Напишите программу с использованием рекурсии, которая принимает на вход число и выводит количество цифр в этом числе.
Формат входных данных
На вход программе подается неотрицательное целое число.
Формат выходных данных
Программа должна определить количество цифр в введенном числе и вывести полученный результат.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    50
Sample Output 1:
    2
Sample Input 2:
    17488
Sample Output 2:
    5
Sample Input 3:
    7
Sample Output 3:
    1
"""

""" Упражнение 2
Напишите программу с использованием рекурсии, которая принимает на вход число и выводит сумму цифр этого числа.
Формат входных данных
На вход программе подается неотрицательное целое число.
Формат выходных данных
Программа должна определить сумму цифр введенного числа и вывести полученный результат.
Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
    25
Sample Output 1:
    7
Sample Input 2:
    10000
Sample Output 2:
    1
Sample Input 3:
    12345
Sample Output 3:
    15
"""
sum_num = lambda x: 0 if x == 0 else x % 10 + sum_num(x // 10)
print(sum_num(int(input())))


""" Упражнение 3
В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек, а оставшиеся размножаются, и их 
становится в три раза больше. Так, количество лягушек k-й год  может быть описано формулой:
F_k = 3(F{k-1} - 30)
Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:
    year — натуральное число
Функция должна возвращать единственное число — количество лягушек в пруду в году year.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию number_of_frogs(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(number_of_frogs(2))
Sample Output 1:
    141
Sample Input 2:
    print(number_of_frogs(10))
Sample Output 2:
    629901
Sample Input 3:
    print(number_of_frogs(1))
Sample Output 3:
    77
"""
def number_of_frogs(year):
    if year == 1:
        return 77
    return (number_of_frogs(year-1) - 30)*3


""" Упражнение 4
Реализуйте функцию range_sum() с использованием рекурсии, которая принимает три аргумента в следующем порядке:
    numbers — список целых чисел
    start — целое неотрицательное число
    end — целое неотрицательное число
Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end] включительно и возвращать 
полученный результат.
Примечание 1. Рассмотрим первый тест. Диапазону индексов [3;7][3;7] в переданном списке принадлежат числа 4,5,6,7,8, 
сумма которых равна: 4+ 5+ 6+ 7+ 8 = 30
Примечание 2. Гарантируется, что start <= end.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию range_sum(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
Sample Output 1:
    30
Sample Input 2:
    print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
Sample Output 2:
    45
Sample Input 3:
    print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
Sample Output 3:
    1
"""
def range_sum(lst, st, end):
    if st == end:
        return lst[end]
    return lst[end] + range_sum(lst, st, end-1)


""" Упражнение 5
Реализуйте функцию get_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
    a — положительное целое число
    n — неотрицательное целое число
Функция должна вычислять значение a в степени n и возвращать полученный результат.
Примечание 1. При решении не используйте оператор возведения в степень **.
Примечание 2. Для построения рекурсивного алгоритма воспользуйтесь следующим рекуррентным соотношением:
a^n = a * a^{n - 1}
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_pow(), но не код,
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(get_pow(5, 2))
Sample Output 1:
    25
Sample Input 2:
    print(get_pow(99, 0))
Sample Output 2:
    1
Sample Input 3:
    print(get_pow(2, 10))
Sample Output 3:
    1024
"""
def get_pow(a, n):
    if n == 0:
        return 1
    return a * get_pow(a, n-1)


""" Упражнение 6
Возводить в степень можно гораздо быстрее, чем за n умножений. Для этого нужно воспользоваться следующими рекуррентными 
соотношениями:
a^n = (a^2)^{n/2}, при четном n 
a^n = a * a^{n - 1}, при нечетном 
Реализуйте функцию get_fast_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
    a — положительное целое число
    n — неотрицательное целое число
Функция должна вычислять значение a в степени n, используя алгоритм быстрого возведения в степень, и возвращать 
полученный результат.
Примечание 1. При решении не используйте оператор возведения в степень **.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_fast_pow(), но не код, 
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(get_fast_pow(2, 10))
Sample Output 1:
    1024
Sample Input 2:
    print(get_fast_pow(5, 2))
Sample Output 2:
    25
Sample Input 3:
    print(get_fast_pow(2, 100))
Sample Output 3:
    1267650600228229401496703205376
"""
def get_fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return get_fast_pow(a*a, n // 2)
    else:
        return a * get_fast_pow(a, n - 1)


""" Упражнение 7
Реализуйте функцию recursive_sum() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
    a — неотрицательное целое число
    b — неотрицательное целое число
Функция должна возвращать сумму чисел a и b. При вычислении суммы функция:
    не должна использовать циклы
    из всех арифметических операций должна использовать только +1 и -1
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(recursive_sum(10, 22))
Sample Output 1:
    32
Sample Input 2:
    print(recursive_sum(99, 0))
Sample Output 2:
    99
Sample Input 3:
    print(recursive_sum(0, 0))
Sample Output 3:
    0
"""
def recursive_sum(a, b):
    if b == 0:
        return a
    return 1 + recursive_sum(a, b-1)


""" Упражнение 8
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
    number — натуральное число
Функция должна возвращать значение True, если number является степенью числа 2, или False в противном случае.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_power(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(is_power(512))
Sample Output 1:
    True
Sample Input 2:
    print(is_power(15))
Sample Output 2:
    `False
Sample Input 3:
    print(is_power(1))
Sample Output 3:
    True
"""
def is_power(num):
    if num == 1:
        return True
    elif num % 2 == 1:
        return False
    return is_power(num // 2)


""" Упражнение 9
Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех 
предыдущих: 1,1, 1, 3, 5, 9, 17, 31, 57, 105 …
Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:
    n — натуральное число
Функция должна возвращать n-й член последовательности Трибоначчи.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию tribonacci(), 
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(tribonacci(1))
Sample Output 1:
    1
Sample Input 2:
    print(tribonacci(7))
Sample Output 2:
    17
Sample Input 3:
    print(tribonacci(4))
Sample Output 3:
    3
"""
cache = {1:1, 2:1, 3:1}

def tribonacci(n):
    result = cache.get(n)
    if result is None:
        result = tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
        cache[n] = result
    return result


""" Упражнение 10
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:
    string — произвольная строка
Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.
Примечание 1. Палиндром — текст, одинаково читающийся в обоих направлениях.
Примечание 2. Пустая строка является палиндромом, как и строка, состоящая из одного символа.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_palindrome(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(is_palindrome('stepik'))
Sample Output 1:
    False
Sample Input 2:
    print(is_palindrome('level'))
Sample Output 2:
    True
Sample Input 3:
    print(is_palindrome('122333221'))
Sample Output 3:
    True
"""
def is_palindrome(string):
    if not string:
        return True
    elif string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


""" Упражнение 11
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:
number — неотрицательное целое число
Функция должна возвращать строковое представление числа number в двоичной системе счисления.
Примечание 1. Вспомнить алгоритм перевода числа из десятичной системы счисления в двоичную можно по ссылке.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(to_binary(15))
Sample Output 1:
    1111
Sample Input 2:
    print(to_binary(0))
Sample Output 2:
    0
Sample Input 3:
    print(to_binary(1))
Sample Output 3:
    1
"""
def to_binary(number):
    if number == 1:
        return '1'
    elif number == 0:
        return '0'
    return to_binary(number // 2) + str(number % 2)


""" Упражнение 12
Выберем натуральное число n = 16 и будем вычитать из него число 5, пока оно не перестанет быть положительным:
16 - 5 = 11
11 - 5 = 6
6 - 5 = 1
1 - 5 = -4
Исходное число nn после четырех вычитаний перестало быть положительным и стало равным −4. Теперь будем прибавлять к 
нему число 5, пока оно снова не станет равным n:
-4 + 5 = 1
1 + 5 = 6
6 + 5 = 11
11 + 5 = 16
Напишите программу с использованием рекурсии, которая принимает на вход число n и вычитает из него число 5, 
пока оно не перестанет быть положительным, а затем прибавляет к нему число 55, пока оно снова не станет равным n.
Формат входных данных
На вход программе подается натуральное число.
Формат выходных данных
Программа должна выполнить алгоритм, представленный в условии задачи, и вывести все результаты арифметических операций, 
произведенных с введенным числом, каждый на отдельной строке.
Примечание 1. Обратите внимание, что в начале и в конце выводится исходное число n.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    16
Sample Output 1:
    16
    11
    6
    1
    -4
    1
    6
    11
    16
Sample Input 2:
    10
Sample Output 2:
    10
    5
    0
    5
    10
Sample Input 3:
    1
Sample Output 3:
    1
    -4
    1
"""
def perversion(num):
    print(num)
    if num <= 0:
        return num
    perversion(num-5)
    print(num)

perversion(int(input()))
