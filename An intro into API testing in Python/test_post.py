#learning source --> https://youtu.be/59vD5iyRdXI
#API--> https://jsonplaceholder.typicode.com/posts

import requests
import pytest


my_new_post = {
    'userID' : 1,
    'title' : 'Some content',
    'body' : '123123123123123123123123'
}

def test_create_new_post():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=my_new_post)
    print(response.request.body)
    assert response.status_code == 201

