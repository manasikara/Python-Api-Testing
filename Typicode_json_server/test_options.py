# An OPTIONS API call will return the allowed HTTP methods for the specified endpoint. We are then printing the available HTTP methods to the console using the response.headers['allow'] property.

import requests

def test_options():
    response = requests.options('http://localhost:3000/posts')

    # Get the available HTTP methods for the endpoint
    print(response.headers)
