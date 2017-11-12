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
            'date1': '60daysAgo',
        }
        response = requests.get(self.stat_url, params)
        print('====================Количество визитов========================')
        return response

    @property
    def get_users(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users',
            'oauth_token': self.token,
            'date1': '60daysAgo',
        }
        response = requests.get(self.stat_url, params)
        print('=============Количество уникальных посетителей================')
        return response

    @property
    def get_pageviews(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews',
            'oauth_token': self.token,
            'date1': '60daysAgo',
        }
        response = requests.get(self.stat_url, params)
        print('===============Количество просмотров страниц==================')
        return response

    @property
    def get_mobilePercentage(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:mobilePercentage',
            'oauth_token': self.token,
            'date1': '60daysAgo',
        }
        response = requests.get(self.stat_url, params)
        print('===========Процент использования мобильных устройств==========')
        return response


class Users(YMManagement, Counter):
    pass


user_1 = Users(TOKEN)
counters = user_1.get_counters()
print("ID счетчиков:", counters, '\n')

queries = ['get_visits', 'get_users', 'get_pageviews', 'get_mobilePercentage']
for counter_id in counters:
    print('\n==================Информация о счетчике=======================')
    counter_info = user_1.get_counter_info(counter_id)
    print(counter_info['counter']['site'])
    print("ID счетчика:", counter_id)
    for query in queries:
        exec (f"response = user_1.{query}")
        data = response.json()
        print(f"За период c {data['query']['date1']} по {data['query']['date2']}")
        print("Минимум:", round(data['min'][0]))
        print("Максимум:", round(data['max'][0]))
        print("Всего:", round(data['totals'][0]))
