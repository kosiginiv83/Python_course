# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции


import os
from pprint import pprint


migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
	sql_files_list = list()
	user_input = ''
	
	files_dir = os.path.join(current_dir, migrations)
	files_list = os.listdir(files_dir)
	for file in files_list:
		file_name, file_extension = os.path.splitext(file)
		if file_extension == '.sql':
			sql_files_list.append(file)
	# pprint(sql_files_list)
	
	while user_input != 'exit' and len(sql_files_list) != 0:
		user_input = input("Введите слово для поиска (exit для выхода):")
		for file in sql_files_list:
			
		
	# break
	
	pass
	

# -----------------------------------------
# import os
 
# path = r'C:\Python27\Tools'
 
# for root, dirs, files in os.walk(path):
    # print(root)

# -----------------------------------------
# import os

# for root, dirs, files in os.walk(path):
    # print(root)
    # for _dir in dirs:
        # print(_dir)

    # for _file in files:
        # print(_file)
# -----------------------------------------

	# n_file = os.path.join(current_dir, 'n.txt')
	# print(n_file)
	
	# dirname, fname = os.path.split(n_file)
	# print(dirname, fname)
	
	# file_name, file_extension = os.path.splitext('n.txt')
	# print(file_name, '***', file_extension)