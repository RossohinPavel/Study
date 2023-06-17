""" Упражнение 1
Реализуйте функцию hash_function(), которая принимает один аргумент:
    obj — произвольный объект
Функция должна вычислять хеш-значение объекта obj согласно следующему алгоритму:
    вычисление значения выражения:
    ord(obj[0]) * ord(obj[-1]) + ord(obj[1]) * ord(obj[-2]) + ord(obj[2]) * ord(obj[-3]) + ...
где obj — объект, преобразованный в строку с помощью функции str(). Обратите внимание, что суммироваться должны
произведение первого и последнего элементов, второго и предпоследнего, и так далее до середины. Если obj имеет нечетное
количество символов, то серединный элемент должен прибавляться без перемножения
    вычисление значения выражения:
    ord(obj[0]) * 1 - ord(obj[1]) * 2 + ord(obj[2]) * 3 - ord(obj[3]) * 4 + ...
где obj — объект, преобразованный в строку с помощью функции str()
    вычисление значения выражения:
    (temp1 * temp2) % 123456791
где temp1 — значение, полученное в первом шаге, temp2 — значение, полученное во втором шаге
и возвращать значение, полученное в третьем шаге.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hash_function(), но не код,
вызывающий ее.
Sample Input 1: print(hash_function('python'))
Sample Output 1: 111998846
Sample Input 2: print(hash_function(12345))
Sample Output 2: 834432
Sample Input 3: print(hash_function(None))
Sample Output 3: 119077607
"""
def hash_function(obj):
    obj = str(obj)
    temp1 = 0 if len(obj) % 2 == 0 else ord(obj[len(obj)//2:len(obj)//2+1])
    temp2 = 0
    for i in range(len(obj)):
        if i < len(obj) // 2:
            temp1 += ord(obj[i]) * ord(obj[-1-i])
        temp2 += ord(obj[i]) * (1+i) if i % 2 == 0 else -ord(obj[i]) * (1+i)
    return (temp1 * temp2) % 123456791


""" Упражнение 2
Реализуйте функцию limited_hash(), которая принимает три аргумента в следующем порядке:
    left — целое число
    right — целое число
    hash_function — хеш-функция, по умолчанию равняется встроенной функции hash()
Функция должна возвращать новую функцию, которая принимает в качестве аргумента произвольный объект, вычисляет его 
хеш-значение с помощью функции hash_function(), преобразует его в число, принадлежащее диапазону [left; right], и 
возвращает полученный результат.
Если вычисленное хеш-значение уже принадлежит диапазону [left; right], то функция должна возвращать его без 
преобразования. Если вычисленное хеш-значение равняется right + 1, то функция перед возвратом должна преобразовать его 
в left, если right + 2 — в left + 1, если right + 3 — в left + 2, и так далее. Аналогичные преобразования, но в другую 
сторону, должны выполняться для хеш-значений, которые меньше left. Преобразования должны выполняться циклично при 
очередном выходе из диапазона.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию limited_hash(), но не код, 
вызывающий ее.
Sample Input 1:
    hash_function = limited_hash(10, 15)
    
    print(hash_function(10))
    print(hash_function(11))
    print(hash_function(15))
Sample Output 1:
    10
    11
    15
Sample Input 2:
    hash_function = limited_hash(10, 15)
    
    print(hash_function(16))
    print(hash_function(17))
    print(hash_function(21))
    print(hash_function(22))
    print(hash_function(23))
Sample Output 2:
    10
    11
    15
    10
    11
Sample Input 3:
    hash_function = limited_hash(10, 15)
    
    print(hash_function(9))
    print(hash_function(8))
    print(hash_function(4))
    print(hash_function(3))
    print(hash_function(2))
Sample Output 3:
    15
    14
    10
    15
    14
"""
def limited_hash(left, right, hash_function=hash):
    def inner(obj):
        temp = hash_function(obj)
        while temp > right:
            temp = left + temp - right - 1
        while temp < left:
            temp = right + temp - left + 1
        return temp
    return inner
