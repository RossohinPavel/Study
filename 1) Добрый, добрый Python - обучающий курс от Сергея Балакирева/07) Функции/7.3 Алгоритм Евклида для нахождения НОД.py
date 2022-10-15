""" Упражнение 1
Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b. В программе
необходимо объявить функцию get_nod, которая принимает два аргумента a и b (натуральные числа) и возвращает вычисленное
значение НОД(a, b).
P. S. Вызывать функцию не нужно, только задать. Постарайтесь реализовать алгоритм, не возвращаясь к материалу на видео.
Sample Input: 15 121050
Sample Output: 15
"""
def get_nod(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
