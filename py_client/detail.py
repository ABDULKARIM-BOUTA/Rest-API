import requests

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
username = input('Username:')
password = input('Password:')

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {'Authorization': f'token {token}'}

    item_pk = 9
    endpoint = f'http://127.0.0.1:8000/api/product/{item_pk}/detail'

    response = requests.get(endpoint, headers=headers)
    print(response.json())
