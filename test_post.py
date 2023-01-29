#API--> https://jsonplaceholder.typicode.com/posts

import requests


my_new_post = {
    'userID' : 1,
    'title' : 'My new post title',
    'body' : 'Content of my new post here'
}

def test_create_new_post():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=my_new_post)
    print(response.request.body)
    assert response.status_code == 201

