n = input("Шифровка 'c' или дешифровка 'd'?\n")
lan = input('На коком языке написана фраза? "en" или "ru"\n')
q = 26
if lan == 'ru':
    q = 32
step = int(input(f'Задайте шаг сдвига. Целое цисло от 1 до {q}\n'))
if n == 'd':
    step = - step
ph = input('Введите фразу для анализа\n')
rp = ''
if lan == 'en':
    uc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lc = list('abcdefghijklmnopqrstuvwxyz')
    for i in ph:
        if i.isalpha():
            s = ord(i)
            if i.islower():
                n = s - 97 + step
                if n > len(lc) - 1:
                    n = 0 + (n - 26)
                rp = rp + lc[n]
            else:
                n = s - 65 + step
                if n > len(uc) - 1:
                    n = 0 + (n - 26)
                rp = rp + uc[n]
        else:
            rp = rp + i
else:
    uc = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    lc = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
    for i in ph:
        if i.isalpha():
            s = ord(i)
            if i.islower():
                n = s - 1072 + step
                if n > len(lc) - 1:
                    n = 0 + (n - 32)
                rp = rp + lc[n]
            else:
                n = s - 1040 + step
                if n > len(uc) - 1:
                    n = 0 + (n - 32)
                rp = rp + uc[n]
        else:
            rp = rp + i
print(rp)

""" Упражнение 1
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово 
строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом 
остаются строчными, а прописные – прописными.
Формат входных данных 
На вход программе подается строка текста на английском языке.
Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.
Примечание. Символы, не являющиеся английскими буквами, не изменяются.
Sample Input 1: Day, mice. "Year" is a mistake!
Sample Output 1: Gdb, qmgi. "Ciev" ku b tpzahrl!
Sample Input 2: my name is Python!
Sample Output 2: oa reqi ku Veznut!
"""
def ces_cod(st, step):
    rp = ''
    uc = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lc = list('abcdefghijklmnopqrstuvwxyz')
    for i in st:
        s = ord(i)
        if i.islower():
            n = s - 97 + step
            if n > len(lc) - 1:
                n = 0 + (n - 26)
            rp = rp + lc[n]
        else:
            n = s - 65 + step
            if n > len(uc) - 1:
                n = 0 + (n - 26)
            rp = rp + uc[n]
    return rp


count = 0
temp = ''
res = ''
a = input()
for i in a:
    if i.isalpha():
        temp = temp + i
        count += 1
    else:
        if temp:
            res = res + ces_cod(temp, count)
        count = 0
        temp = ''
        res = res + i
if temp:
    res = res + ces_cod(temp, count)
print(res)
