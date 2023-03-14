# PUT - change values in json file

import requests

def test_put():
    # /products/'1' is the input id number
    website = 'http://localhost:3000/products/1'
    r = requests.put(website, data={
        
        "id": "1",
        "title": "VALUE CHANGED BY THE 'PUT' METHOD"
        
    })

print('ok')                     
                           
                     
                     
                     
                