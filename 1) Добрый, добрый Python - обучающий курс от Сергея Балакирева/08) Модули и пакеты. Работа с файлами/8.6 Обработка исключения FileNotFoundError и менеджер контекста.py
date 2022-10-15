""" Упражнение 1
 Имеется фрагмент программы (см. листинг ниже). При его выполнении возникает ошибка FileNotFoundError. Запишите
 конструкцию try / except, чтобы отображалось сообщение "File Not Found", если файл не удается открыть.
"""
try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")
