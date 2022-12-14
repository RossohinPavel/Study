""" Упражнение 1
Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы
неравенств:
"""
import random
n = 10**6
s0 = 3.5*4
k = 0
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    q = x**3 + y**4 + 2
    z = 3*x + x**2
    if q >= 0 and z <= 2:
        k += 1
print((k/n)*s0)


""" Упражнение 2

"""

