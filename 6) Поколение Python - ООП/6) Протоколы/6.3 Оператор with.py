""" Упражнение 1
Реализуйте функцию print_file_content(), которая принимает один аргумент:
    filename — имя текстового файла
Функция должна выводить содержимое файла с именем filename. Если файла с данным именем нет в папке с программой, функция
должна вывести текст: Файл не найден
Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.
Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_file_content(), но не
код, вызывающий ее.
Sample Input 1:
    with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
        file.write('Сражения и путешествия берут своё')

    print_file_content('Precepts_of_Zote.txt')
Sample Output 1:
    Сражения и путешествия берут своё
Sample Input 2:
    print_file_content('Precepts_of_Zote2.txt')
Sample Output 2:
    Файл не найден
"""
def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            print(*(x.strip() for x in file.readlines()), sep='\n')
    except:
        print('Файл не найден')


""" Упражнение 2
Реализуйте функцию non_closed_files(), которая принимает один аргумент:
    files — список файловых объектов
Функция должна возвращать список, элементами которого являются открытые файловые объекты из списка files.
Примечание 1. Файловые объекты в возвращаемом функцией списке должны располагаться в своем исходном порядке
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию non_closed_files(), но не 
код, вызывающий ее.
Sample Input:
    with (
        open('file1.txt', 'w', encoding='utf-8') as file1,
        open('file2.txt', 'w', encoding='utf-8') as file2,
        open('file3.txt', 'w', encoding='utf-8') as file3
    ):
        file1.write('i am the first file')
        file2.write('i am the second file')
        file3.write('i am the third file')
    
    file1 = open('file1.txt', encoding='utf-8')
    file3 = open('file3.txt', encoding='utf-8')
    
    
    for file in non_closed_files([file1, file2, file3]):
        print(file.read())
Sample Output:
    i am the first file
    i am the third file
"""
def non_closed_files(files):
    return [x for x in files if not x.closed]


""" Упражнение 3
Лог-файл — это текстовый файл, в который автоматически записывается важная информация о работе системы или программы. 
Форматов лог-файла довольно много, однако в рамках этой задачи будем считать, что все лог-файлы имеют следующий единый 
формат:
    2022-01-01 INFO: User logged in
    2022-01-01 ERROR: Invalid input data
    2022-01-01 WARNING: File not found
    2022-01-02 INFO: User logged out
    2022-01-03 INFO: User registered
То есть каждая строка лог-файла описывает некоторое событие, которое характеризуется датой в формате YYYY-MM-DD, типом 
и кратким описанием.
Реализуйте функцию log_for(), которая принимает два аргумента в следующем порядке:
    logfile — имя лог-файла
    date_str — строковая дата в формате YYYY-MM-DD
Функция должна создавать текстовый файл с именем:
    log_for_<date_str>.txt
и записывать в него все события из файла logfile, которые произошли в дату date_str. События должны записываться без 
указания даты, а также располагаться в своем исходном порядке.
Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.
Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию log_for(), но не код, 
вызывающий ее.
Sample Input:
    with open('log.txt', 'w', encoding='utf-8') as file:
        print('2022-01-01 INFO: User logged in', file=file)
        print('2022-01-01 ERROR: Invalid input data', file=file)
        print('2022-01-02 INFO: User logged out', file=file)
        print('2022-01-03 INFO: User registered', file=file)
    
    log_for('log.txt', '2022-01-01')
    
    with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
        print(file.read())
Sample Output:
    INFO: User logged in
    ERROR: Invalid input data
"""
def log_for(logfile, date_str):
    with open(logfile, 'r', encoding='UTF-8') as source, open(f'log_for_{date_str}.txt', 'w', encoding='UTF-8') as output:
        output.writelines(line[11:] for line in source.readlines() if line.startswith(date_str))
