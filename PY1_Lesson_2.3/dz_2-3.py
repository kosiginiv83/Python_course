import json
import chardet
from pprint import pprint


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
		with open(file, encoding=cp) as f:
			words_dict = dict()
			news_dscrptns = list()
			
			news_dict = json.load(f)
			news_desc_list = news_dict['rss']['channel']['items']
			for i in range(len(news_desc_list)):
				words_list = news_desc_list[i]['description'].split(' ')
				words_list_condition = [words_list[x] for x in 
						range(len(words_list)) if 
						len(words_list[x]) > chars_more]
				news_dscrptns += words_list_condition
			words_dict['file'] = file
			words_dict['news'] = news_dscrptns
			data_list.append(words_dict)
			
	top_ten_words(data_list)
		

def top_ten_words(data_list):		
	for data in data_list:
		# words_count_list = list()
		# max_words_list = list()
		top_ten_list = list()
		
		for i in range(10):
			
			words_count_list = list()
			max_words_list = list()
			# top_ten_list = list()
			
			words_list = data['news']
			for word in words_list:
				word_count = words_list.count(word)
				words_count_list.append(word_count)
			# print(sorted(words_count_list))
			max_count = max(words_count_list)
			# print('\n\tMax count: ', max_count)
			max_word_index = words_count_list.index(max_count)
			# print('Word: ', words_list[max_word_index])
			
			max_words_indexes = list(filter(lambda x: 
					words_count_list[x] == max_count, 
					range(len(words_list))))
			for index in max_words_indexes:
				# print(words_list[index])
				max_words_list.append(words_list[index])
			
			# print(max_words_indexes)
			words_set = set(max_words_list)
			# print(words_set)
			
			for word in words_set:
				top_ten_list.append(word)
				while word in words_list:
					words_list.remove(word)
				# print(word in words_list)
	
		print('\n\tFile: ', data['file'])
		print('Top ten words: ', top_ten_list[:10])
	
	
# Второй аргумент - число символов в слове - в данном случае поиск идет
# по словам длиннее шести символов (начиная с семи символов).
form_data_structure(['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json'], 6)
