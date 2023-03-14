"""
learning sources --> https://www.youtube.com/watch?v=tb8gHvYlCFs
                 --> https://www.youtube.com/watch?v=V7sLq7u28BA
"""
# GET status code

import requests
import json

def test_status_code():
    r = requests.get('http://localhost:3000/users')
    r.status_code

    if r.status_code == 200:
        print('Success!')
    elif r.status_code == 404:
        print('Not Found.')

# to print in pytest use '-s'  
