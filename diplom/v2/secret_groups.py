import json
import requests
import sys
import time
from typing import Iterable


VERSION = '5.68'

with open('info.json', encoding='utf-8') as f:
    data = json.load(f)
    TOKEN = data[0]['token']
    USER_ID = data[0]['user_id']


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


class Users:
    
    def __init__(self, user_id):
        self.user_id = user_id
        params = {
            'v': VERSION,
            'user_id': user_id,
            'access_token': TOKEN,
        }
        response = requests.get("https://api.vk.com/method/groups.get",
                                        params)
        data = response.json()
        self.user_groups = data['response']['items']
        self.groups_count = len(self.user_groups)
        
        if user_id == USER_ID:
            response = requests.get("https://api.vk.com/method/friends.get",
                                            params)
            data = response.json()
            self.user_friends = data['response']['items']
            self.friends_count = len(self.user_friends)


#class Groups:



def main():
    user = Users(USER_ID)
    user_friends = LinkedList(user.user_friends)
    #user_groups = LinkedList(user.user_groups)
    
    
    """
    print(dir(user))
    print(user.user_id)
    print(user.user_groups)
    print(user.groups_count)
    print(user.user_friends)
    print(user.friends_count)
    
    for unit in friends:
        print(unit)
    print('====================================')
    
    for unit in groups:
        print(unit)
    """


if __name__ == '__main__':
    try:
        main()
    except:
        print("\tAn Error Occured")
        raise
