""" Упражнение 1
Реализуйте функцию get_digits() c использованием аннотаций типов, которая принимает один аргумент:
    number — положительное целое или вещественное число
Функция должна возвращать список, состоящий из цифр числа number.
Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing.
Также используйте нотацию |, а не тип Union из модуля typing.
Примечание 2. Порядок следования цифр в списке должен совпадать с порядком следования их в исходном числе.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_digits(),
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    print(get_digits(16733))
Sample Output 1:
    [1, 6, 7, 3, 3]
Sample Input 2:
    print(get_digits(13.909934))
Sample Output 2:
    [1, 3, 9, 0, 9, 9, 3, 4]
Sample Input 3:
    annotations = get_digits.__annotations__

    print(annotations['return'])
Sample Output 3:
    list[int]
"""
def get_digits(number: int | float) -> list[int]:
    return list(map(int, [x for x in str(number) if x.isdigit()]))


""" Упражнение 2
Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:
grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список оценок по ключу grades
Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую высокую оценку по ключу top_grade.
Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. 
Также используйте нотацию |, а не тип Union из модуля typing.
Примечание 2. В возвращаемом функцией словаре сначала должно следовать имя, а затем — самая высокая оценка.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию top_grade(), но не код, 
вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    info = {'name': 'Timur', 'grades': [30, 57, 99]}
    
    print(top_grade(info))
Sample Output 1:
    {'name': 'Timur', 'top_grade': 99}
Sample Input 2:
    print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))
Sample Output 2:
    {'name': 'Ruslan', 'top_grade': 86}
Sample Input 3:
    annotations = top_grade.__annotations__
    
    print(annotations['grades'])
Sample Output 3:
    dict[str, str | list[int]]
"""
def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


""" Упражнение 3
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:
    numbers — список целых или вещественных чисел
    step — целое число
Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None. 
Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. 
Также используйте нотацию |, а не тип Union из модуля typing.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию cyclic_shift(), 
но не код, вызывающий ее. 
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    numbers = [1, 2, 3, 4, 5]
    cyclic_shift(numbers, 1)
    
    print(numbers)
Sample Output 1:
    [5, 1, 2, 3, 4]
Sample Input 2:
    numbers = [1, 2, 3, 4, 5]
    cyclic_shift(numbers, -2)
    
    print(numbers)
Sample Output 2:
    [3, 4, 5, 1, 2]
"""
def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step >= 0:
        while step > 0:
            numbers.insert(0, numbers.pop())
            step -= 1
    elif step < 0:
        while step < 0:
            numbers.append(numbers.pop(0))
            step += 1


""" Упражнение 4
Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, которая принимает один аргумент:
matrix — матрица произвольной размерности, элементами которой являются целые или вещественные числа
Функция должна возвращать словарь, ключом в котором является номер строки матрицы, а значением — список элементов этой строки.
Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. 
Также используйте нотацию |, а не тип Union из модуля typing.
Примечание 2. Под матрицей подразумеваются исключительно вложенные списки.
Примечание 3. Нумерация строк матрицы в возвращаемом функцией словаре должна начинаться с единицы.
Примечание 4. Элементы матрицы в списке должны располагаться в своем исходном порядке.
Примечание 5. В тестирующую систему сдайте программу, содержащую только необходимую функцию matrix_to_dict(), 
но не код, вызывающий ее.
Примечание 6. Тестовые данные доступны по ссылке.
Sample Input 1:
    matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
    
    print(matrix_to_dict(matrix))
Sample Output 1:
    {1: [5, 6, 7], 2: [8, 3, 2], 3: [4, 9, 8]}
Sample Input 2:
    matrix = [[5.1, 6, 7.94]]
    
    print(matrix_to_dict(matrix))
Sample Output 2:
    {1: [5.1, 6, 7.94]}
Sample Input 3:
    annotations = matrix_to_dict.__annotations__
    
    print(annotations['return'])
Sample Output 3:
    dict[int, list[int | float]]
"""
def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i: v for i, v in enumerate(matrix, 1)}
