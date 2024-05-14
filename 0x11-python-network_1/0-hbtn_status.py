#!/usr/bin/python3
""" am module that  fetches a resurce from a url
"""
import urllib.request as urb

if __name__ == "__main__":
    """retrieve data fromma url and displays relevant information"""
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urb.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print("- Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body))
    except urb.error.HTTPError as e:
        print("Error fetching URL:", e)
    except urb.error.URLError as e:
        print("Error connecting to URL:", e)
