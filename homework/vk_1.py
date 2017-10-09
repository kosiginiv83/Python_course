import requests
from pprint import pprint

VERSION = '5.68'

my_params = {
	'v': VERSION,
	'user_id': 251522831
}

response = requests.get('https://api.vk.com/method/friends.get', my_params)
my_friends = response.json()
# pprint(my_friends)
my_friends_id_list = my_friends['response']['items']
print('\n\tmy_friends_id_list: ', my_friends_id_list, '\n')

for friend_id in my_friends['response']['items']:
	params = {
		'v': VERSION,
		'user_id': friend_id
	}
	friend_info_raw = requests.get('https://api.vk.com/method/users.get', params)
	friend_info = friend_info_raw.json()
	# print(friend_info)

friends_friends_dict = {}
for id in my_friends_id_list:
	friend_params = {
		'v': VERSION,
		'user_id': id
	}
	friend_info_raw = requests.get('https://api.vk.com/method/users.get', friend_params)
	friend_info = friend_info_raw.json()
	friend_firstname = friend_info['response'][0]['first_name']
	friend_lastname = friend_info['response'][0]['last_name']
	fio = f"{friend_lastname} {friend_firstname}"
	# print('\n', fio)
	
	response = requests.get('https://api.vk.com/method/friends.get', friend_params)
	my_friend_friends = response.json()
	# print(my_friend_friends)
	
	friends_friends_dict[fio] = set(my_friend_friends['response']['items'])
	
print(friends_friends_dict)


print('\n\tIntersections\n')
# set.inersection(other, ...)
# int_per_pol = (set(friends_friends_dict['Перебейносов Алексей']) & 
		# set(friends_friends_dict['Пологрудов Алексей']))
int_list = list(friends_friends_dict.values())
print(int_list)
print(type(int_list))


# print(int_per_pol)
# for id in int_per_pol:
	# friend_params = {
		# 'v': VERSION,
		# 'user_id': id
	# }
	# friend_info_raw = requests.get('https://api.vk.com/method/users.get', friend_params)
	# friend_info = friend_info_raw.json()
	# friend_firstname = friend_info['response'][0]['first_name']
	# friend_lastname = friend_info['response'][0]['last_name']
	# fio = f"{friend_lastname} {friend_firstname}"
	# print('\n', fio)
	