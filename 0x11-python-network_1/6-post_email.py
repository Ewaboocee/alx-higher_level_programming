#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and finally displays the response"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")
