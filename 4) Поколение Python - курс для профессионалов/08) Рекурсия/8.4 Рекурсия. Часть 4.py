""" Упражнение 1
Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:
nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат. Если список nested_lists
пуст, функция должна вернуть число 0.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(),
но не код, вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    my_list = [1, [4, 4], 2, [1, [2, 10]]]

    print(recursive_sum(my_list))
Sample Output 1:
    24
Sample Input 2:
    my_list = []

    print(recursive_sum(my_list))
Sample Output 2:
    0
"""
def recursive_sum(my_list):
    total = 0
    if not my_list:
        return 0
    if isinstance(my_list, int):
        return my_list
    if isinstance(my_list, list):
        for name in my_list:
            total += recursive_sum(name)
    return total


""" Упражнение 2
Линеаризация — это процесс преобразования списка, который может содержать несколько уровней вложенных списков, в список, 
содержащий все те же элементы без какой-либо вложенности.
Например, список:
    [1, [2, 3], [4, [5, 6, [7, 8, 9]]]]
после линеаризации будет иметь вид:
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:
nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, 
также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна возвращать новый список, представляющий собой линеаризованный список nested_lists.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию linear(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    my_list = [3, [4], [5, [6, [7, 8]]]]
    
    print(linear(my_list))
Sample Output 1:
    [3, 4, 5, 6, 7, 8]
Sample Input 2:
    my_list = [10, 20, 30, 40, 50]
    
    print(linear(my_list))
Sample Output 2:
    [10, 20, 30, 40, 50]
"""

""" Упражнение 3
Реализуйте функцию get_value(), которая принимает два аргумента в следующем порядке:
nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь, 
так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
    key — хешируемый объект
Функция должна определять значение, которое соответствует ключу key в словаре nested_dicts или в одном из его вложенных 
словарей, и возвращать полученный результат.
Примечание 1. Гарантируется, что ключ key присутствует в словаре nested_dicts или в одном из его вложенных словарей, 
причем в единственном экземпляре.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_value(), но не код, 
вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 
        'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 
        'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))
Sample Output 1:
    Москва
Sample Input 2:
    data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}
    
    print(get_value(data, 'birthday'))
Sample Output 2:
    {'day': 24, 'month': 'March', 'year': 1974}
"""
def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]
    for k, v in nested_dicts.items():
        if isinstance(v, dict):
            value = get_value(v, key)
            if value is not None:
                return value


""" Упражнение 4
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:
    nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь, 
    так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
    key — хешируемый объект
Функция должна определять все значения, которые соответствуют ключу key в словаре nested_dicts и всех его вложенных 
словарях, и возвращать их в виде множества. Если ключа key нет ни в одном словаре, функция должна вернуть пустое 
множество.
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_values(), но не код, 
вызывающий ее.
Примечание 2. Тестовые данные доступны по ссылке.
Sample Input 1:
    my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
    result = get_all_values(my_dict, 'top_grade')
    
    print(*sorted(result))
Sample Output 1:
    4 5
Sample Input 2:
    my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
    result = get_all_values(my_dict, 'hobby')
    
    print(*sorted(result))
Sample Output 2:
    math videogames
Sample Input 3:
    my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
    result = get_all_values(my_dict, 'top_grade')
    
    print(len(sorted(result)))
Sample Output 3:
    0
"""
def get_all_values(nested_dicts, key):
    mn = set()
    def get_value(dicts, ks):
        if ks in dicts:
            mn.add(dicts[ks])
        for k, v in dicts.items():
            if isinstance(v, dict):
                value = get_value(v, key)
                if value is not None:
                    mn.add(value)
    get_value(nested_dicts, key)
    return mn


""" Упражнение 5
Реализуйте функцию dict_travel(), которая принимает один аргумент:
nested_dicts — словарь, содержащий в качестве значений числа, строки или словари, которые, в свою очередь, так же 
содержат в качестве значений числа, строки или словари; вложенность может быть произвольной
Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей. 
При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня, 
разделяя их точками.
Например, в словаре:
{'name': 'Arthur', 'grades': {'math': [4, 4], 'chemistry': [3, 4]}}
    значение [4, 4] должно быть выведено в следующем формате:
    grades.math: [4, 4]
Все пары ключ-значение должны быть расположены в лексикографическом порядке, каждая на отдельной строке.
Примечание 1. Гарантируется, что ключами в подаваемом в функцию словаре являются строки, содержащие только латинские 
буквы в нижнем регистре.
Примечание 2. Гарантируется, что ни один ключ в подаваемом в функцию словаре не является последовательностью других 
ключей. Другими словами, словарь не может иметь, например, следующий вид:
    {'b.c': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию dict_travel(), 
но не код, вызывающий ее.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
Sample Output 1:
    a: 1
    b.a: 10
    b.b: 20
    b.c: 30
Sample Input 2:
    data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
    
    dict_travel(data)
Sample Output 2:
    a: 100
    b.a: 10
    b.b: 20
    b.c: 30
    d: 1
Sample Input 3:
    data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}
    
    dict_travel(data)
Sample Output 3:
    b.a: 10
    b.b.d: 40
    b.b.e: 50
    b.c: 30
"""
def dict_travel(nested_dicts):
    def linear(dct, name):
        for k, v in sorted(dct.items()):
            if not isinstance(v, dict):
                print(f'{name}.{k}: {v}' if name else f'{k}: {v}')
            if isinstance(v, dict):
                linear(v, f'{name}.{k}' if name else f'{k}')
    linear(nested_dicts, '')
