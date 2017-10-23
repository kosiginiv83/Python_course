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
            'Authorization': f'OAuth {self.token}'
        }
        return headers
    
    def get_counters(self):
        url = urljoin(self.management_url, 'counters')
        headers = self.get_headers()
        response = requests.get(self.management_url, headers=headers)
        return [c['id'] for c in response.json()['counters']]
    
    def get_counter_info(self, counter_id):
        url = urljoin(self.management_url, f'counter/{counter_id}')
        headers = self.get_headers()
        response = requests.get(self.management_url, headers=headers)
        return response.json()


class Counter:
    def get_visits(self):
        pass


user_1 = YMManagement(TOKEN)
counters = user_1.get_counters()
pprint(counters)
for counter_id in counters:
    counter_info = user_1.get_counter_info(counter_id)
    pprint(counter_info)

for counter_id in counters:
    params = {
        'id': counter_id,
        'metrics': 'ym:s:visits',
        'oauth_token': TOKEN
    }
    response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
    pprint(response.json())
