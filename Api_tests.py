#API --> https://jsonplaceholder.typicode.com/users/1

import requests

def test_statu_code():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    assert response.status_code == 200
    body = response.json()
    assert body['username'] == 'Bret'
    assert body['address']['geo']['lng'] == '81.1496'
