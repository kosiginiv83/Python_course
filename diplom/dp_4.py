import json
import requests
import subprocess
import sys
import math
from pprint import pprint


VERSION = '5.68'

with open('info.json') as f:
    data = json.load(f)
    TOKEN = data[1]['token']
    USER_ID = data[1]['user_id']


def get_data(user_id, query):
    params = {
        'v': VERSION,
        'user_id': user_id,
        'access_token': TOKEN,
    }
    response = requests.get(f"https://api.vk.com/method/{query}.get", params)
    return response.json()


def console_output(i):
    sys.stdout.write('\r')
    if isinstance(i, int):
        t = '|/-\\'
        i = 0 if i == 4 else i
        out = t[i]
        i += 1
    else:
        out = i
    sys.stdout.write(out)
    sys.stdout.flush()
    return i


def get_friends_groups():
    friends_groups_list = []
    friends_info = get_data(USER_ID, 'friends')
    friends_ids = friends_info['response']['items']
    count = 1
    for friend_id in friends_ids:
        friend_groups_raw = get_data(friend_id, 'groups')
        count = console_output(count)
        
        if 'response' in friend_groups_raw:
            friend_groups_ids = friend_groups_raw['response']['items']
            friends_groups_list += friend_groups_ids
        elif 'error' in friend_groups_raw:
            error_code = friend_groups_raw['error']['error_code']
            error_msg = friend_groups_raw['error']['error_msg']
            with open('log.txt', 'a') as log:
                log.write(f'error_code: {error_code}, ')
                log.write(f'error_msg: {error_msg}\n')
    
    friends_groups_set = set(friends_groups_list)
    #print('\nСуммарное количество уникальных групп друзей:',
    #      len(friends_groups_set))
    return friends_groups_set


def get_group_info(group_id):
    params = {
        'v': VERSION,
        'access_token': TOKEN,
        'group_id': group_id,
        'fields': 'members_count',
    }
    response = requests.get("https://api.vk.com/method/groups.getById", params)
    return response.json()


if __name__ == '__main__':
    try:
        groups_list = []
        user_groups_raw = get_data(USER_ID, 'groups')
        user_groups_set = set(user_groups_raw['response']['items'])
        #print('\nКоличество групп пользователя:', len(user_groups_set))
        #print(user_groups_ids)
        friends_groups_set = get_friends_groups()
        user_groups_set.difference_update(friends_groups_set)
        console_output('Done\n')
        #print('\nКоличество секретных групп:', len(user_groups_set))
        #print(user_groups_set)
        for group_id in user_groups_set:
            group_dict = {}
            group_info = get_group_info(group_id)
            #pprint(group_info)
            group_dict['gid'] = group_info['response'][0]['id']
            group_dict['name'] = group_info['response'][0]['name']
            group_dict['members_count'] = group_info['response'][0]['members_count']
            groups_list.append(group_dict)
        #pprint(groups_list)
        with open('groups.json', 'w') as f:
            json.dump(groups_list, f, sort_keys = True,
                      indent = 2, ensure_ascii=False)
    except:
        print("\tAn Error Occured")
        raise
 
 


"""
Выводит имя пользователя.
def user_fio(friend_info):
    user_firstname = friend_info['response'][0]['first_name']
    user_lastname = friend_info['response'][0]['last_name']
    fio = f"{user_lastname} {user_firstname}"
    print(fio)
    #print(friend_info)
"""

"""
Выводит название группы.
for group_id in friend_groups_ids:
    friend_group_info = get_group_info(group_id)
    #pprint(friend_group_info)
    #print(friend_group_info['response'][0]['name'])
    
def get_group_info(group_id):
    params = {
        'v': VERSION,
        'access_token': TOKEN,
        'group_id': group_id,
    }
    response = requests.get("https://api.vk.com/method/groups.getById", params)
    return response.json()
"""