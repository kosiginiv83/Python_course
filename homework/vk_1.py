import requests
from pprint import pprint
import itertools
import functools

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
inter = functools.reduce(int_list[0].intersection, int_list[1:])

# inter = itertools.starmap(int_list[0].intersection, range(1, len(int_list) - 1))
# inter = int_list[0].intersection(int_list[x] for x in range(1, len(int_list) - 1))
# inter = int_list[0].intersection(itertools.islice(int_list, 1, len(int_list) - 1))

print(dir(inter))
print('\n\t', inter)
print(type(inter))


for id in inter:
	friend_params = {
		'v': VERSION,
		'user_id': id
	}
	friend_info_raw = requests.get('https://api.vk.com/method/users.get', friend_params)
	friend_info = friend_info_raw.json()
	friend_firstname = friend_info['response'][0]['first_name']
	friend_lastname = friend_info['response'][0]['last_name']
	fio = f"{friend_lastname} {friend_firstname}"
	print('\n', fio)
	