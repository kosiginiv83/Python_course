import requests
from functools import reduce


VERSION = '5.68'


def get_data(user_id, query):
    params = {
        'v': VERSION,
        'user_id': user_id
    }
    response = requests.get(f"https://api.vk.com/method/{query}.get", params)
    return response.json()


def user_fio(friend_info):
    user_firstname = friend_info['response'][0]['first_name']
    user_lastname = friend_info['response'][0]['last_name']
    fio = f"{user_lastname} {user_firstname}"
    print(fio)


if __name__ == '__main__':
    my_friends = get_data(251522831, 'friends')
    my_friends_id_list = my_friends['response']['items']
    print('\n\tmy_friends_id_list: ', my_friends_id_list)
    
    friends_friends_list = []
    print("\n\tFriends names:")
    for friend_id in my_friends_id_list:
        friend_info = get_data(friend_id, 'users')
        my_friend_friends = get_data(friend_id, 'friends')
        user_fio(friend_info)
        friends_friends_list.append(set(my_friend_friends['response']['items']))
    
    print('\n\tFriends intersection')
    """
    Ищется пересечение только среди друзей друзей, чтобы для проверки
    правильности работы кода выводился как минимум я.
    """
    inter = reduce(friends_friends_list[0].intersection, friends_friends_list[1:])
    print('\tUsers id', inter)
    for user_id in inter:
        user = get_data(user_id, 'users')
        user_fio(user)
