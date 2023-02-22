#learning source --> https://youtu.be/59vD5iyRdXI
#API --> https://jsonplaceholder.typicode.com/users/1
#invocing the API; sending the request throug API; capturing the response; writing some characteristics of that response - status code, what are response headers, what are response body. Its usefull for exploratory testing

import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users/1')
print(f'Status code: {response.status_code}')
print(f'Status code: {response.headers}')
print(json.dumps(response.json(), indent=4))
