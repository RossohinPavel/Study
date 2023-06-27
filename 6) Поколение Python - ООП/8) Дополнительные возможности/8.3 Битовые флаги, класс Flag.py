""" Упражнение 1
Реализуйте класс OrderStatus, описывающий флаг с состояниями интернет-заказов. Флаг должен иметь три элемента:
    ORDER_PLACED
    PAYMENT_RECEIVED
    SHIPPING_COMPLETE
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.
Примечание 2. Никаких ограничений касательно реализации класса OrderStatus нет, она может быть произвольной.
Sample Input:
    order_status = OrderStatus(0)
    order_status |= OrderStatus.ORDER_PLACED

    if OrderStatus.ORDER_PLACED in order_status:
        print('Заказ оформлен!')

    order_status |= OrderStatus.PAYMENT_RECEIVED

    if OrderStatus.PAYMENT_RECEIVED in order_status:
        print('Оплата получена!')

    order_status |= OrderStatus.SHIPPING_COMPLETE

    if OrderStatus.SHIPPING_COMPLETE in order_status:
        print('Доставка завершена!')
Sample Output:
    Заказ оформлен!
    Оплата получена!
    Доставка завершена!
"""
from enum import Flag


OrderStatus = Flag('OrderStatus', ['ORDER_PLACED', 'PAYMENT_RECEIVED', 'SHIPPING_COMPLETE'])


""" Упражнение 2
1. Реализуйте класс MovieGenres, описывающий флаг с жанрами кино. Флаг должен иметь пять элементов:
    ACTION
    COMEDY
    DRAMA
    FANTASY
    HORROR
2. Также реализуйте класс Movie, описывающий фильм. При создании экземпляра класс должен принимать два аргумента в 
следующем порядке:
    name — название фильма
    genres — жанр фильма (элемент флага MovieGenres)
Класс Movie должен иметь один метод экземпляра:
    in_genre() — метод, принимающий в качестве аргумента жанр и возвращающий True, если фильм принадлежит данному жанру, 
или False в противном случае
Экземпляр класса Movie должен иметь следующее неформальное строковое представление:
    <название фильма>
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы 
используются только с корректными данными.
Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
Sample Input 1:
    movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
    
    print(movie)
Sample Output 1:
    The Lord of the Rings
Sample Input 2:
    movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
    
    print(movie.in_genre(MovieGenres.FANTASY))
    print(movie.in_genre(MovieGenres.COMEDY))
    print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))
Sample Output 2:
    True
    False
    True
"""
from enum import Flag

MovieGenres = Flag('MovieGenres', ['ACTION', 'COMEDY', 'DRAMA', 'FANTASY', 'HORROR'])


class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def __str__(self):
        return self.name

    def in_genre(self, genre):
        return bool(self.genres & genre)
