#!/usr/bin/python3
"""a module that sends a request to the URL and
displays the value of the X-Request-Id variable
found in the header of the response
"""

import urllib.request
import sys

if __name__ == "__main__":
    """displays the id of a request"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            header = response.getheader('X-Request-Id')
            if header:
                print(header)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error connecting to URL:", e)
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e)
