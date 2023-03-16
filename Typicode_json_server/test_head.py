# Send a HEAD request to receive only the response headers (not the body)

import requests

def test_response():
        response = requests.head('http://localhost:3000')

        # Get response headers
        print(response.headers)

