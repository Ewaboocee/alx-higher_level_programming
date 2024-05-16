#!/usr/bin/python3
"""takes your GitHub credentials and uses the GitHub API to display your id"""
import sys
import requests


def get_github_user_id(username, token):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    data = response.json()
    user_id = data.get("id")
    return user_id


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    user_id = get_github_user_id(username, token)
    print(user_id)
