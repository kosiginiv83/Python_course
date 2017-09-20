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
				news_dscrptns.append(words_list)
				# news_dscrptns.append(news_desc_list[i]['description'])
			words_dict['file'] = file
			words_dict['news'] = news_dscrptns
			data_list.append(words_dict)
			
	top_ten_words(data_list, chars_more)
		

def top_ten_words(data_list, chars_more):		
	pprint(data_list)
	print(type(data_list[0]))
	print(len(data_list))
	print(len(data_list[3]['news']))

	
form_data_structure(['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json'], 6)