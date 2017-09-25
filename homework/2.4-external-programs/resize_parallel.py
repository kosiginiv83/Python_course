import os
import subprocess


def resize_imgs(prog_dir, files_dir, files_list, result_dir):
	for file in files_list:
		orig_file = os.path.join(files_dir, file)
		new_file = os.path.join(result_dir, file)
		command = 'convert {} -resize 200 {}'.format(orig_file, new_file)
		subprocess.Popen(command, stdin = subprocess.PIPE)
		print("\nФайл %s с измененным размером создан." % file)
	

if __name__ == '__main__':
	prog_dir = os.path.dirname(os.path.abspath(__file__))
	result_dir = os.path.join(prog_dir, 'Result')
	files_dir = os.path.join(prog_dir, 'Source')
	files_list = os.listdir(files_dir)
	
	if not(os.path.exists('Result')):
		os.mkdir('Result')
		print("\nПапка 'Result' создана.")
		result_list = []
	else:
		result_list = os.listdir(result_dir)

	func_a = 'resize_imgs(prog_dir, files_dir, files_list, result_dir)'
	
	if len(result_list) != 0:
		print("\nПапка 'Result' содержит файлы, дальнейшее "
			"выполнение программы заменит файлы с "
			"одинаковыми именами. "
			"Введите 'y', чтобы продолжить, 'n' - чтобы выйти.")
		choise = None
		while choise != 'y' and choise != 'n':
			choise = input('Выбор: ')
			if choise == 'y':
				exec(func_a)
			elif choise == 'n':
				break
			else:
				print("\nВведите 'y', чтобы продолжить, "
						"'n' - чтобы выйти.")
	else:
		exec(func_a)
	
	input()  # Нужна для того, чтобы окно консоли не закрылось 
	# сразу после выполнения программы в случае запуска 
	# файла с проводника или файлового менеджера.
