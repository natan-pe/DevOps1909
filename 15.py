import requests

response = requests.get('https://app.valimail.com/')
if response.status_code == 200:
    print('Valimail is online')
