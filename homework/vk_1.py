import requests
import functools


VERSION = '5.68'


def get_friends(user_id):
    params = {
        'v': VERSION,
        'user_id': user_id
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()


my_friends = get_friends(251522831)
my_friends_id_list = my_friends['response']['items']
print('\n\tmy_friends_id_list: ', my_friends_id_list)


def get_user(user_id):
    params = {
        'v': VERSION,
        'user_id': user_id
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    return response.json()


friends_friends_dict = {}
print("\n\tFriends names:")
for friend_id in my_friends_id_list:
    friend_info = get_user(friend_id)
    friend_firstname = friend_info['response'][0]['first_name']
    friend_lastname = friend_info['response'][0]['last_name']
    fio = f"{friend_lastname} {friend_firstname}"
    print(fio)
    my_friend_friends = get_friends(friend_id)
    friends_friends_dict[fio] = set(my_friend_friends['response']['items'])


print('\n\tFriends intersection')
# Ищется пересечение только среди друзей друзей, чтобы для проверки
# правильности работы кода выводился как минимум я.
ids_list = list(friends_friends_dict.values())
inter = functools.reduce(ids_list[0].intersection, ids_list[1:])
print('\tUsers id', inter)
for user_id in inter:
    print(get_user(user_id))
