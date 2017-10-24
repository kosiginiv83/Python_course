import requests
from pprint import pprint
from urllib.parse import urljoin


TOKEN = 'AQAAAAAPYnwKAASbhoBg63II10TDllSpWCdhF-4'


class YMManagement:
    management_url = 'https://api-metrika.yandex.ru/management/v1/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/x-yametrika+json',
        }
        # print(headers)
        return headers

    def get_counters(self):
        url = urljoin(self.management_url, 'counters')
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        # print('response', response.content)
        return [c['id'] for c in response.json()['counters']]

    def get_counter_info(self, counter_id):
        url = urljoin(self.management_url, f'counter/{counter_id}')
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()


class Counter:
    stat_url = 'https://api-metrika.yandex.ru/stat/v1/data'

    @property
    def get_visits(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data',
                                params)
        return response

    @property
    def get_users(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data',
                                params)
        return response


class Users(YMManagement, Counter):
    pass


user_1 = Users(TOKEN)
counters = user_1.get_counters()
pprint(counters)

for counter_id in counters:
    counter_info = user_1.get_counter_info(counter_id)
    print('==================================================================')
    print('+++counter_info+++')
    pprint(counter_info)

for counter_id in counters:
    response = user_1.get_visits
    print('======================Количество визитов==========================')
    print('+++response.json()+++')
    pprint(response.json())

for counter_id in counters:
    response = user_1.get_users
    print('==============Количество уникальных посетителей===================')
    print('+++response.json()+++')
    pprint(response.json())
