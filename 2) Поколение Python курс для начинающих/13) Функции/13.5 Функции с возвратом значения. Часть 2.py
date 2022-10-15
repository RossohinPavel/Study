""" Упражнение 1
апишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа,
и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в
противном случае.
Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.
Примечание 2. Следующий программный код:
    print(is_valid_triangle(2, 2, 2))
    print(is_valid_triangle(2, 3, 10))
    print(is_valid_triangle(3, 4, 5))
должен выводить:
    True
    False
    True
"""
def is_valid_triangle(side1, side2, side3):
    return side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2
a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))


""" Упражнение 2
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True 
если число является простым и False в противном случае.
Примечание. Следующий программный код:
    print(is_prime(1))
    print(is_prime(10))
    print(is_prime(17))
должен выводить:
    False
    False
    True
"""
def is_prime(num):
    return len([x for x in range(1, num+1) if num % x == 0]) == 2
n = int(input())
print(is_prime(n))


""" Упражнение 3
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое 
простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
Примечание 2. Следующий программный код:
    print(get_next_prime(6))
    print(get_next_prime(7))
    print(get_next_prime(14))
должен выводить:
    7
    11
    17
"""
def is_prime(num):
    return len([x for x in range(1, num+1) if num % x == 0]) == 2
def get_next_prime(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        else:
            num+= 1
n = int(input())
# вызываем функцию
print(get_next_prime(n))


""" Упражнение 4
апишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и 
возвращает значение True если пароль является надежным и False в противном случае.
Пароль является надежным если:
    его длина не менее 88 символов; 
    он содержит как минимум одну заглавную букву (верхний регистр); 
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.
Примечание. Следующий программный код:
    print(is_password_good('aabbCC11OP'))
    print(is_password_good('abC1pu'))
должен выводить:
    True
    False
"""
def is_password_good(password):
    c = 0
    if len(password) >= 8:
        c += 1
    if password != password.upper():
        c += 1
    if password != password.lower():
        c += 1
    for i in password:
        if i.isdigit():
            c += 1
            break
    return 4 == c
txt = input()
print(is_password_good(txt))


""" Упражнение 5
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает 
значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.
Примечание. Следующий программный код:
    print(is_one_away('bike', 'hike'))
    print(is_one_away('water', 'wafer'))
    print(is_one_away('abcd', 'abpo'))
    print(is_one_away('abcd', 'abcde'))
должен выводить:
    True
    True
    False
    False
"""
def is_one_away(word1, word2):
    result = False
    if len(word1) == len(word2):
        c = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                c += 1
        if c+1 == len(word1):
            result = True
    return result
txt1 = input()
txt2 = input()
print(is_one_away(txt1, txt2))


""" Упражнение 6
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True 
если указанный текст является палиндромом и False в противном случае.
Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, 
а также символы , . ! ? -.
Примечание 3. Следующий программный код:
    print(is_palindrome('А роза упала на лапу Азора.'))
    print(is_palindrome('Gabler Ruby - burrel bag!'))
    print(is_palindrome('BEEGEEK'))
должен выводить:
    True
    True
    False
"""
def is_palindrome(text):
    text = [x.lower() for x in text if x.isalpha()]
    return text == text[::-1]
txt = input()
print(is_palindrome(txt))


""" Упражнение 7
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK 
фанатеет от математики, то он решил:
    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password 
и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
Примечание. Следующий программный код:
    print(is_valid_password('1221:101:22'))
    print(is_valid_password('565:30:50'))
    print(is_valid_password('112:7:9'))
    print(is_valid_password('1221:101:22:22'))
должен выводить:
    True
    False
    False
    False
"""
def is_valid_password(password):
    result = False
    password = password.split(':')
    if len(password) == 3:
        c = 0
        if password[0] == password[0][::-1]:
            c += 1
        temp = int(password[1])
        if len([x for x in range(1, temp+1) if temp % x == 0]) == 2:
            c += 1
        if int(password[2]) % 2 == 0:
            c += 1
        if c == 3:
            result = True
    return result
psw = input()
print(is_valid_password(psw))


""" Упражнение 8
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из 
символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной 
последовательностью и False в противном случае.
Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), 
где каждой открывающей скобке найдется парная закрывающая скобка.
Примечание 2. Следующий программный код:
    print(is_correct_bracket('()(()())'))
    print(is_correct_bracket(')(())('))
должен выводить:
    True
    False
"""
def is_correct_bracket(text):
    c = 0
    for i in text:
        if c < 0:
            return False
        if i == '(':
            c += 1
        if i == ')':
            c -= 1
    return c == 0
txt = input()
print(is_correct_bracket(txt))


""" Упражнение 9
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и 
преобразует его в «змеиный регистр».
Примечание 1. Почитать подробнее о стилях именования можно тут.
Примечание 2. Следующий программный код:
    print(convert_to_python_case('ThisIsCamelCased'))
    print(convert_to_python_case('IsPrimeNumber'))
должен выводить:
    this_is_camel_cased
    is_prime_number
"""
def convert_to_python_case(text):
    a = text[0].lower()
    for i in text[1:]:
        if i.isupper():
            a = f'{a}_{i.lower()}'
        else:
            a = a + i
    return a
txt = input()
print(convert_to_python_case(txt))
