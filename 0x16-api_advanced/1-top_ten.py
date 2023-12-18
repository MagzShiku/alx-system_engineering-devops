#!/usr/bin/python3
"""
    this function goes to reddit, prints:
         - Titles of the first 10 hosts
            listed in a given subreddit
    if not a valid subreddit, it prints none
"""

import requests


def top_ten(subreddit):
    """
    this actions the requirements
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
