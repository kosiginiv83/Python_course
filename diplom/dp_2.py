import requests
import json
from pprint import pprint


VERSION = '5.68'

with open('inf0.json') as f:
    data = json.load(f)
    pprint(data)
    TOKEN = data[0]['token']
    USER_ID = data[0]['user_id']


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
    user_info = get_data(USER_ID, 'users')
    print(user_info)
    friends_info = get_data(USER_ID, 'friends')
    #print(friends_ids)
    groups_dict = {}
    friends_ids = friends_info['response']['items']
    for friend_id in friends_ids:
        friend_info = get_data(friend_id, 'users')
        user_fio(friend_info)
        friend_groups_raw = get_data(friend_id, 'groups')
        #print(friend_groups_raw)
        friend_groups_ids = friend_groups_raw['response']['items']
        for group_id in friend_groups_ids:
            friend_group_info = get_group_info(group_id)
            #pprint(friend_group_info)
            #print(friend_group_info['response'][0]['name'])
        print('==================================')
