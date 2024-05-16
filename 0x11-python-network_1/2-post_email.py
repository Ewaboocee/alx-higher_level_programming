#!/usr/bin/python3
"""a module that sends a POST request to the passed
URL with the email as a parameter"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    """send an email to a url and show response"""
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error connecting to URL:", e)
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e)
