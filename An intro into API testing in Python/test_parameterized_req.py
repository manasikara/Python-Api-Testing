import requests
import pytest

user_data = [
    (1, 'Leanne Graham'),
    (2, 'Ervin Howell'),
    (3, 'Clementine Bauch')
]
    
@pytest.mark.parametarize('user_id, expected_name', user_data)

def test_user_names(user_id, expected_name):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    body = response.json()
    assert body['name'] == expected_name
    
    
    
    # again getting errors, although the code is exactly the same as the source code
    # tbc.