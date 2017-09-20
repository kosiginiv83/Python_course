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
				# words_list_indexes = list(filter(lambda x: len(words_list[x]) > chars_more, 
						# range(len(words_list))))
				words_list_condition = [words_list[x] for x in range(len(words_list)) if 
						len(words_list[x]) > chars_more]
				news_dscrptns += words_list_condition
			words_dict['file'] = file
			words_dict['news'] = news_dscrptns
			data_list.append(words_dict)
			
	top_ten_words(data_list)
		

def top_ten_words(data_list):		
	# pprint(data_list)
	# print(type(data_list[0]))
	# print(len(data_list))
	# print(len(data_list[3]['news']))
	
	for data in data_list:
		words_count_list = list()
		
		for word in data['news']:
			word_count = data['news'].count(word)
			words_count_list.append(word_count)
		# print(sorted(words_count_list))
		max_count = max(words_count_list)
		print('\n\tMax count: ', max_count)
		max_word_index = words_count_list.index(max_count)
		print('Word: ', data['news'][max_word_index])
		# print(max_word)
		# count_max_count = words_count_list.count(max_count)
		# print('\tCount max count: ', count_max_count)

	
form_data_structure(['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json'], 6)