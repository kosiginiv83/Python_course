import requests
from pprint import pprint


VERSION = '5.68'
TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'


def get_data(user_id, query):
    params = {
        'v': VERSION,
        'user_id': user_id,
        'access_token': TOKEN,
    }
    response = requests.get(f"https://api.vk.com/method/{query}.get", params)
    return response.json()


def get_group_info(group_id):
    params = {
        'v': VERSION,
        'access_token': TOKEN,
        'group_id': group_id,
    }
    response = requests.get("https://api.vk.com/method/groups.getById", params)
    return response.json()


def user_fio(friend_info):
    user_firstname = friend_info['response'][0]['first_name']
    user_lastname = friend_info['response'][0]['last_name']
    fio = f"{user_lastname} {user_firstname}"
    print(fio)
    #print(friend_info)


if __name__ == '__main__':
    user_info = get_data(251522831, 'users')
    print(user_info)
    friends_ids = get_data(251522831, 'friends')
    #print(friends_ids)

    x = friends_ids['response']['items']
    #x.remove(29185587) #remove clown
    for friend_id in x:
        friend_info = get_data(friend_id, 'users')
        user_fio(friend_info)

        friend_groups_raw = get_data(friend_id, 'groups')
        #print(friend_groups_raw)
        
        friend_groups_ids = friend_groups_raw['response']['items']
        for group_id in friend_groups_ids:
            friend_group_info = get_group_info(group_id)
            #pprint(friend_group_info)
            print(friend_group_info['response'][0]['name'])
        print('==================================')
