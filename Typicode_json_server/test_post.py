# send a 'POST' request with a new user to the server db.json file

import json
import requests

def test_post():
    r = requests.post('http://localhost:3000/users', data={'id': '7', 'firstName':'Slawomir', 'lastName':'Tatinger'})
    
    print(r.json())
    
    # use '-s' while performing a pyTest to see terminal output