import requests
from pprint import pprint

TOKEN = 'AQAAAAAazgOnAASYKJ4J3j8TvUnVmJ-pENTHj6Y'

params = {
    'oauth_token': TOKEN
}

response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', params)
print(response.status_code)
pprint(response.headers)
pprint(response.json())
