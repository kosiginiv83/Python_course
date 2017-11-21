import json
import requests
import subprocess
import sys
from pprint import pprint


VERSION = '5.68'

with open('info.json') as f:
    data = json.load(f)
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


def get_friends_groups():
    friends_groups_list = []
    friends_info = get_data(USER_ID, 'friends')
    friends_ids = friends_info['response']['items']
    #print(friends_ids)
    i = 1
    for friend_id in friends_ids:
        #friend_info = get_data(friend_id, 'users')
        #user_fio(friend_info)
        friend_groups_raw = get_data(friend_id, 'groups')
        #print(friend_groups_raw)

        t = '|/-\\'
        sys.stdout.write('\r')
        sys.stdout.write(t[i])
        sys.stdout.flush()
        i += 1
        if i == 4:
            i = 0
        
        if 'response' in friend_groups_raw:
            friend_groups_ids = friend_groups_raw['response']['items']
            friends_groups_list += friend_groups_ids
        elif 'error' in friend_groups_raw:
            """
            'error_code': 18, 'error_msg': 'User was deleted or banned'
            'error_code': 6, 'error_msg': 'Too many requests per second'
            """
            error_code = friend_groups_raw['error']['error_code']
            error_msg = friend_groups_raw['error']['error_msg']
            #print(friend_groups_raw)
            with open('log.txt', 'a') as log:
                log.write(f'error_code: {error_code}, ')
                log.write(f'error_msg: {error_msg}\n')
        
    friends_groups_set = set(friends_groups_list)
    print('\nКоличество групп', len(friends_groups_set))
    

if __name__ == '__main__':
    try:
        get_friends_groups()
    except:
        print("\tAn Error Occured")
        raise
 
 

"""
Выводит название группы.
for group_id in friend_groups_ids:
    friend_group_info = get_group_info(group_id)
    #pprint(friend_group_info)
    #print(friend_group_info['response'][0]['name'])
"""