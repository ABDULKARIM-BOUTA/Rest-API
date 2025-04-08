import requests

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
username = input('Username:')
password = input('Password:')

auth_response = requests.post(auth_endpoint, json={'username':username, 'password':password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = { 'Authorization': f'token {token}'}

    endpoint = 'http://127.0.0.1:8000/api/product/list-create/'
    data = {
        'name': 'I9-11700',
        'price': '275'
    }
    response = requests.post(endpoint, data=data, headers=headers)
    print(response.json())

