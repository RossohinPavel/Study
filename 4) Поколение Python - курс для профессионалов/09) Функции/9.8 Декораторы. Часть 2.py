""" Упражнение 1
Реализуйте декоратор square, который возводит возвращаемое значение декорируемой функции во вторую степень.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа int или float.
Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
 а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор square, но не код,
вызывающий его.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    @square
    def add(a, b):
        return a + b

    print(add(3, 7))
Sample Output 1:
    100
Sample Input 2:
    @square
    def add(a, b):
        '''прекрасная функция'''
        return a + b

    print(add(1, 1))
    print(add.__name__)
    print(add.__doc__)
Sample Output 2:
    4
    add
    прекрасная функция
"""
import functools
def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper


""" Упражнение 2
Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции принадлежит 
типу str. Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение 
TypeError.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор returns_string, но не код, 
вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @returns_string
    def beegeek():
        return 'beegeek'
        
    print(beegeek())
Sample Output 1:
    beegeek
Sample Input 2:
    @returns_string
    def add(a, b):
        return a + b
    
    try:
        print(add(3, 7))
    except TypeError as e:
        print(type(e))
Sample Output 2:
    <class 'TypeError'>
"""
import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not isinstance(res, str):
            raise TypeError
        return res
    return wrapper


""" Упражнение 3
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения, 
а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:
    TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
    TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор trace, но не код, 
вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @trace
    def say(name, line):
        return f'{name}: {line}'
        
    say('Jane', 'Hello, World')
Sample Output 1:
    TRACE: вызов say() с аргументами: ('Jane', 'Hello, World'), {}
    TRACE: возвращаемое значение say(): 'Jane: Hello, World'
Sample Input 2:
    @trace
    def sub(a, b, c):
        '''прекрасная функция'''
        return a - b + c
        
    print(sub.__name__)
    print(sub.__doc__)
    sub(20, 5, c=10)
Sample Output 2:
    sub
    прекрасная функция
    TRACE: вызов sub() с аргументами: (20, 5), {'c': 10}
    TRACE: возвращаемое значение sub(): 25
"""
# Применяем функцию repr для вывода машинного представления возвращаемого значения декорируемой функции.
# Поможет понять, какой тип значения выводит декорируемая функция.
import functools
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(res)}')
        return res
    return wrapper


""" Упражнение 4
Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:
    string — произвольная строка
    to_the_end — булево значение, по умолчанию равное False
Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. Если to_the_end имеет значение 
True, строка string добавляется в конец, если False — в начало.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор prefix, но не код, 
вызывающий его.
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    @prefix('€')
    def get_bonus():
        return '2000'
        
    print(get_bonus())
Sample Output 1:
    €2000
Sample Input 2:
    @prefix('$$$', to_the_end=True)
    def get_bonus():
        return '2000'
           
    print(get_bonus())
Sample Output 2:
    2000$$$
"""
import functools
def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res + string if to_the_end else string + res
        return wrapper
    return decorator


""" Упражнение 5
Тег — элемент языка разметки, используемый для форматирования текста. Например, текст, заключённый между начальным 
тегом <small> и конечным тегом </small>, отображается с меньшим размером, чем основной текст, а текст между тегами 
<big> и </big> отображается с большим размером.
Реализуйте декоратор make_html(), который принимает один аргумент:
    tag — HTML-тег, например, del
Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор make_html, 
но не код, вызывающий его. 
Примечание 4. Тестовые данные доступны по ссылке.
Sample Input 1:
    @make_html('del')
    def get_text(text):
        return text
        
    print(get_text('Python'))
Sample Output 1:
    <del>Python</del>
Sample Input 2:
    @make_html('i')
    @make_html('del')
    def get_text(text):
        return text
        
    print(get_text(text='decorators are so cool!'))
Sample Output 2:
    <i><del>decorators are so cool!</del></i>
"""
import functools
def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return decorator


""" Упражнение 6
Реализуйте декоратор repeat, который принимает один аргумент:
times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор repeat, но не код, 
вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @repeat(3)
    def say_beegeek():
        '''documentation'''
        print('beegeek')
        
    say_beegeek()
Sample Output 1:
    beegeek
    beegeek
    beegeek
Sample Input 2:
    @repeat(4)
    def say_beegeek():
        '''documentation'''
        print('beegeek')
        
    print(say_beegeek.__name__)
    print(say_beegeek.__doc__)
Sample Output 2:
    say_beegeek
documentation
"""
import functools
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator


""" Упражнение 7
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:
    start — неотрицательное целое число
    end — неотрицательное целое число
    char — одиночный символ, по умолчанию равный точке .
Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все символы в диапазоне индексов 
от start (включительно) до end (не включительно) на символ char.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
Примечание 2. Гарантируется, что start < end.
Примечание 3. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимый декоратор strip_range, 
но не код, вызывающий его.
Примечание 5. Тестовые данные доступны по ссылке.
Sample Input 1:
    @strip_range(3, 5)
    def beegeek():
        return 'beegeek'
        
    print(beegeek())
Sample Output 1:
    bee..ek
Sample Input 2:
    @strip_range(3, 20, '_')
    def beegeek():
        return 'beegeek'
        
    print(beegeek())
Sample Output 2:
    bee____
Sample Input 3:
    @strip_range(20, 30)
    def beegeek():
        return 'beegeek'
        
    print(beegeek())
Sample Output 3:
    beegeek
"""
import functools
def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return ''.join([char if i in range(start, end) else v for i, v in enumerate(func(*args, **kwargs))])
        return wrapper
    return decorator


""" Упражнение 8
Реализуйте декоратор returns, который принимает один аргумент:
datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. Если возвращаемое 
значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор returns, но не код, 
вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @returns(int)
    def add(a, b):
        return a + b
    
    print(add(10, 5))
Sample Output 1:
    15
Sample Input 2:
    @returns(int)
    def add(a, b):
        return a + b
    
    try:
        print(add('199', '1'))
    except TypeError as e:
        print(type(e))
Sample Output 2:
    <class 'TypeError'>
Sample Input 3:
    @returns(list)
    def beegeek():
        '''beegeek docs'''
        return 'beegeek'
    
    print(beegeek.__name__)
    print(beegeek.__doc__)
    
    try:
        print(beegeek())
    except TypeError as e:
        print(type(e))
Sample Output 3:
    beegeek
    beegeek docs
    <class 'TypeError'>
Sample Input 4:
    @returns(list)
    def append_this(li, elem):
        '''append_this docs'''
        return li + [elem]
    
    print(append_this.__name__)
    print(append_this.__doc__)
    print(append_this([1, 2, 3], elem=4))
Sample Output 4:
    append_this
    append_this docs
    [1, 2, 3, 4]
"""
import functools
def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, datatype):
                return res
            else:
                raise TypeError
        return wrapper
    return decorator


""" Упражнение 9
Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов, каждый из которых 
является типом данных.
Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат одному из этих типов. 
Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes, но не код, 
вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @takes(int, str)
    def repeat_string(string, times):
        return string * times
    
    print(repeat_string('bee', 3))
Sample Output 1:
    beebeebee
Sample Input 2:
    @takes(list, bool, float, int)
    def repeat_string(string, times):
        return string * times
    
    try:
        print(repeat_string('bee', 4))
    except TypeError as e:
        print(type(e))
Sample Output 2:
    <class 'TypeError'>
"""
import functools
def takes(*typeargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in (*args, *kwargs.values()):
                if type(i) not in typeargs:
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator


""" Упражнение 10
Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов и устанавливает их 
в качестве атрибутов декорируемой функции. Названием атрибута должно являться имя аргумента, значением атрибута — 
значение аргумента.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Вспомните про атрибут функции __dict__.
Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор add_attrs, 
но не код, вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @add_attrs(attr1='bee', attr2='geek')
    def beegeek():
        return 'beegeek'
        
    print(beegeek.attr1)
    print(beegeek.attr2)
Sample Output 1:
    bee
    geek
Sample Input 2:
    @add_attrs(attr2='geek')
    @add_attrs(attr1='bee')
    def beegeek():
        return 'beegeek'
        
    print(beegeek.attr1)
    print(beegeek.attr2)
    print(beegeek.__name__)
Sample Output 2:
    bee
    geek
    beegeek
"""
# Да, атрибуты функции доступны изнутри неё.
# Да, изменение wrapper.__dict__ внутри него самого - приводит к положительному результату.
# * Только для этого надо его заставить отработать хотя бы один раз, для чего вызвать декорируемую функцию, чего тесты,
# конечно же, не делают.
# А вот если изменить его атрибуты извне, то они изменятся в процессе декорирования, а не в процессе вызова.
# А нам это и надо.
import functools
def add_attrs(**kwargs_attr):
    def decorator(func):
        for k, v in kwargs_attr.items():
            func.__dict__[k] = v
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


""" Упражнение 11
Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных аргументов — типов 
исключений, и выводит текст:
Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.
Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор ignore_exception, 
но не код, вызывающий его.
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @ignore_exception(ZeroDivisionError, TypeError, ValueError)
    def f(x):
        return 1 / x
        
    f(0)
Sample Output 1:
    Исключение ZeroDivisionError обработано
Sample Input 2:
    min = ignore_exception(ZeroDivisionError)(min)
    
    try:
        print(min(1, '2', 3, [4, 5]))
    except Exception as e:
        print(type(e))
Sample Output 2:
    <class 'TypeError'>
"""
# Для получения имени исключения, которое было передано в декоратор, используем следующую конструкцию. Альтернативный
# способ - через модуль sys. Остальные исключения ловим через BaseException.

#from sys import exc_info
#try:
#    х = 1 / 0
# except Exception as err:
#     print(exc_info())
# -- (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001BEEF80E840>)
import functools
def ignore_exception(*err_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except err_args as decl_err:
                print(f'Исключение {type(decl_err).__name__} обработано')
            except BaseException as non_decl_err:
                raise non_decl_err
        return wrapper
    return decorator


""" Упражнение 12
Реализуйте декоратор retry, который принимает один аргумент:
    times — натуральное число
Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка. 
Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, после чего должен возбуждать 
исключение MaxRetriesException.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор retry, но не код, 
вызывающий его. 
Примечание 3. Тестовые данные доступны по ссылке.
Sample Input 1:
    @retry(3)
    def no_way():
        raise ValueError
       
    try:
        no_way()
    except Exception as e:
        print(type(e))
Sample Output 1:
<class '__main__.MaxRetriesException'>
Sample Input 2:
    @retry(8)
    def beegeek():
        beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
        if beegeek.calls < 5:
            raise ValueError
        print('beegeek')
        
    beegeek()
Sample Output 2:
    beegeek
"""
import functools
class MaxRetriesException(Exception):
    pass
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator