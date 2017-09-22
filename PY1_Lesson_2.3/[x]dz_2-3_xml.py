import xml.etree.ElementTree as ET
import chardet
# from pprint import pprint
from xml.etree.ElementTree import XMLParser


def cp_identify(file):
	with open(file, 'rb') as f:
		data = f.read()
		result = chardet.detect(data)
		cp = result['encoding']
		return cp
	

def form_data_structure(files_list, chars_more):
	data_list = list()
	
	
	for file in files_list:
		cp = cp_identify(file)
		print(cp)
		
		words_dict = dict()
		news_dscrptns = list()
		
		tree = ET.parse(file)
		root = tree.getroot()
		# root = ET.tostring(file, encoding=cp, method="xml", short_empty_elements=True)
		# root = ET.tostring(file, encoding=cp, short_empty_elements=True)
		print(tree)
		
		# news_dict = json.load(f)
		# news_desc_list = news_dict['rss']['channel']['items']
		# news_desc_list = root.find('rss').find('channel').find('item').find('description')
		# news_desc_list = root.findall('channel').find('item').find('description')
		# print(news_desc_list)
		# print(news_desc_list.text)
		
		# for i in range(len(news_desc_list)):
			# words_list = news_desc_list[i]['description'].split(' ')
			# words_list_condition = [words_list[x] for x in 
					# range(len(words_list)) if 
					# len(words_list[x]) > chars_more]
			# news_dscrptns += words_list_condition
		# words_dict['file'] = file
		# words_dict['news'] = news_dscrptns
		# data_list.append(words_dict)
			
	# top_ten_words(data_list, chars_more)
		
form_data_structure(['newsafr.xml'], 6)
		
# def top_ten_words(data_list, chars_more):
	# print("\nТоп 10 часто встречающихся слов, длиннее {} "
				# "символов:".format(chars_more))
				
	# for data in data_list:
		# top_ten_list = list()
		
		# for i in range(10):
			# words_count_list = list()
			# max_words_list = list()
			
			# words_list = data['news']
			# for word in words_list:
				# word_count = words_list.count(word)
				# words_count_list.append(word_count)
			# max_count = max(words_count_list)
			# max_word_index = words_count_list.index(max_count)
			# max_words_indexes = list(filter(lambda x: 
					# words_count_list[x] == max_count, 
					# range(len(words_list))))
			# for index in max_words_indexes:
				# max_words_list.append(words_list[index])
			# words_set = set(max_words_list)
			# for word in words_set:
				# top_ten_list.append(word)
				# while word in words_list:
					# words_list.remove(word)
	
		# print('\n\tFile: ', data['file'])
		# for num, value in enumerate(top_ten_list[:10]):
			# print(num + 1, '-', value)
	
	
# Второй аргумент - число символов в слове - в данном 
# случае поиск идет по словам длиннее шести символов 
# (начиная с семи символов).
# form_data_structure(['newsafr.xml', 'newscy.xml', 'newsfr.xml', 
		# 'newsit.xml'], 6)
# Программа работает корректно при значении данного 
# параметра не более 9.
