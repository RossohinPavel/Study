import random


digits = '23456789'
lc_letters = 'abcdefghjmnpqrstuvwxyz'
uc_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
nsym = 'il1Lo0O'

chars = ''

print('Программа для генерации пароля. ')
c = input('Количество паролей для генерации? Введите целое число\n')
l = input('Длину одного пароля. Введите целое число\n')
d = input('Включать ли цифры 0123456789? (y/n)\n')
uc = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)\n')
lc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)\n')
sym = input('Включать ли символы !#$%&*+-=?@^_? (y/n)\n')
ns = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)\n')

if d == 'y':
    chars = chars + digits
if uc == 'y':
    chars = chars + uc_letters
if lc == 'y':
    chars = chars + lc_letters
if sym == 'y':
    chars = chars + punctuation
if ns == 'n':
    chars = chars + nsym


def generate_rassword(length, chars):
    pw = ''
    for i in range(int(length)):
        pw = pw + random.choice(chars)
    return pw


for i in range(int(c)):
    print(generate_rassword(int(l), chars))
