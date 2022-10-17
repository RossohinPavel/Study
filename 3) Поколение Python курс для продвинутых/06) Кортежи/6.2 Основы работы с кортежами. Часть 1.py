""" Упражнение 1
Дополните приведенный код, используя индексацию кортежа, чтобы переменная last, содержала последний элемент
кортежа countries.
"""
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
last = countries[-1]
print(last)


""" Упражнение 2
Дополните приведенный код, используя срезы, так чтобы он вывел первые 66 элементов кортежа primes.
Примечание. Результатом вывода должна быть строка (2, 3, 5, 7, 11, 13).
"""
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
print(primes[:6])


""" Упражнение 3
Дополните приведенный код, используя срезы, так чтобы он вывел элементы кортежа countries, кроме первых двух.
Примечание. Результатом вывода должна быть строка ('Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 
'Chile', 'Cameroon').
"""
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[2:])


""" Упражнение 4
Дополните приведенный код, используя срезы, чтобы он вывел все элементы кортежа countries, кроме последних трех.
"""
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:-3])


""" Упражнение 5
Дополните приведенный код, используя срезы, чтобы он вывел все элементы кортежа countries, кроме двух последних 
и трех первых.
"""
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])


""" Упражнение 6
Дополните приведенный код так, чтобы переменная number содержала количество элементов кортежа countries.
"""
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
number = len(countries)
print(number)


""" Упражнение 7
Дополните приведенный код так, чтобы он вывел сумму минимального и максимального элементов кортежа numbers.
"""
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
print(min(numbers) + max(numbers))


""" Упражнение 8
Дополните приведенный код так, чтобы переменная index содержала индекс элемента «Slovenia» в кортеже countries.
"""
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index('Slovenia')
print(index)


""" Упражнение 9
Дополните приведенный код так, чтобы переменная number, содержала количество вхождений «Spain» в кортеж countries.
"""
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count('Spain')
print(number)


""" Упражнение 10
Дополните приведенный код, используя операторы конкатенации (+) и умножения кортежа на число (*), чтобы он вывел кортеж:
 (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13).
"""
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
print(numbers1 * 2 + numbers2 * 9 + numbers3)


""" Упражнение 11
В переменную city_name вводится название города (например, Москва), а в переменную city_year – год его основания 
(например, 1147). Заполните пропущенную строку таким образом, чтобы в переменной city оказался кортеж из значений 
этих двух переменных (сначала название города, затем год основания).
"""
city_name = input()
city_year = int(input())
city = city_name, city_year
print(city)


""" Упражнение 12
Дополните приведенный код, так чтобы получить список, содержащий только непустые кортежи исходного списка tuples, 
не меняя порядка их следования.
"""
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [x for x in tuples if x]
print(non_empty_tuples)


""" Упражнение 13
Дополните приведенный код так, чтобы переменная new_tuples, содержала список кортежей на основе списка tuples с 
последним элементом каждого кортежа, замененным на численное значение 100100.
"""
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [x[:-1] + (100,) for x in tuples]
print(new_tuples)
