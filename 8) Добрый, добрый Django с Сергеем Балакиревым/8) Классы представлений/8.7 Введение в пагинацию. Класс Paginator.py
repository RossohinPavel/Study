""" Упражнение 1
Подвиг 3. Из входного потока читается список строк с помощью следующей команды:

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять
Объявите переменную pages, которая ссылается на объект пагинатора (Paginator) для списка lst с разбиением по 4 элемента на страницу. 

Используя переменную pages и функцию print, выведите на экран в одну строчку через пробел общее число элементов в списке и общее число страниц.
 

Sample Input:
django 4; Анджелина Джоли; Дженнифер Лоуренс; Джулия Робертс; Марго Робби; Ума Турман
Sample Output:
6 2
"""
from django.core.paginator import Paginator

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять

# здесь продолжайте программу
pages = Paginator(lst, 4)
print(pages.count, pages.num_pages)


""" Упражнение 2
Подвиг 4. Из входного потока читается список строк с помощью следующей команды:

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять
Объявите переменную pages, которая ссылается на объект пагинатора (Paginator) для списка lst с разбиением по 3 элемента на страницу. 

Используя переменную pages и итератор page_range, с помощью оператора for выведите по порядку (возрастания) номера страниц в одну строчку через пробел.
 

Sample Input:
Анджелина Джоли; Дженнифер Лоуренс; Джулия Робертс; Марго Робби; Ума Турман; Ариана Гранде; Бейонсе
Sample Output:
1 2 3
"""
from django.core.paginator import Paginator

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять

# здесь продолжайте программу
pages = Paginator(lst, 3)
print(*pages.page_range, end=' ')


""" Упражнение 3
Подвиг 5. Из входного потока читается список строк с помощью следующей команды:

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять
Объявите переменную pages, которая ссылается на объект пагинатора (Paginator) для списка lst с разбиением по 4 элемента на страницу.

Используя переменную pages, получите объект второй страницы и сохраните его в переменной p. Если существует следующая страница, выведите элементы текущей страницы в одну строчку через пробел. Иначе выведите строку "NO" (без кавычек).

Sample Input:
а; б; в; г; д; е; ж; з; и; й; к; л; м; н; о; п; р; с; т; у; ф; х; ц; ч; ш; щ; ь; ъ; э; ю; я
Sample Output:
д е ж з
"""
from django.core.paginator import Paginator

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять

# здесь продолжайте программу
pages = Paginator(lst, 4)
p = pages.page(2)
if p.has_next():
    print(*p)
else:
    print('NO')


""" Упражнение 4
Подвиг 6. Из входного потока читается список строк с помощью следующей команды:

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять
Объявите переменную pages, которая ссылается на объект пагинатора (Paginator) для списка lst с разбиением по 2 элемента на страницу.

Если третья страница существует, то получите объект третьей страницы и сохраните его в переменной p. После этого в одну строчку через пробел выведите номер предыдущей страницы, текущей страницы и следующей страницы, если она существует. Если третья страница не существует, то выведите строку "NO" (без кавычек).

Sample Input:
а; б; в; г; д; е; ж; з; и; й; к; л; м; н; о; п; р; с; т; у; ф; х; ц; ч; ш; щ; ь; ъ; э; ю; я
Sample Output:
2 3 4
"""
from django.core.paginator import Paginator

lst = list(map(str.strip, input().split(";")))  # эту строчку и переменную lst не менять

# здесь продолжайте программу
pages = Paginator(lst, 2)
if pages.num_pages > 3:
    p = pages.page(3)
    print(p.previous_page_number(), p.number, end=' ')
    if p.has_next():
        print(p.next_page_number())
else:
    print('NO')
