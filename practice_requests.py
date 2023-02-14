import requests
import json

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get')
print(r.text)