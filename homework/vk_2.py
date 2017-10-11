import requests
from functools import reduce


VERSION = '5.68'


def get_data(user_id, query):
    params = {
        'v': VERSION,
        'user_id': user_id
    }
    response = requests.get(f'https://api.vk.com/method/{query}.get', params)
    return response.json()


def get_friends(user_id):
    params = {
        'v': VERSION,
        'user_id': user_id
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()


def get_user(user_id):
    params = {
        'v': VERSION,
        'user_id': user_id
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    return response.json()


def user_fio(friend_info):
    user_firstname = friend_info['response'][0]['first_name']
    user_lastname = friend_info['response'][0]['last_name']
    fio = f"{user_lastname} {user_firstname}"
    print(fio)
    return fio


if __name__ == '__main__':
    my_friends = get_friends(251522831)
    my_friends_id_list = my_friends['response']['items']
    print('\n\tmy_friends_id_list: ', my_friends_id_list)
    
    friends_friends_dict = {}
    print("\n\tFriends names:")
    for friend_id in my_friends_id_list:
        friend_info = get_user(friend_id)
        my_friend_friends = get_friends(friend_id)
        fio = user_fio(friend_info)
        friends_friends_dict[fio] = set(my_friend_friends['response']['items'])
    
    print('\n\tFriends intersection')
    # Ищется пересечение только среди друзей друзей, чтобы для проверки
    # правильности работы кода выводился как минимум я.
    ids_list = list(friends_friends_dict.values())
    inter = reduce(ids_list[0].intersection, ids_list[1:])
    print('\tUsers id', inter)
    for user_id in inter:
        user = get_user(user_id)
        user_fio(user)
