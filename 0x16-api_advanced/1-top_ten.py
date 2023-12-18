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
    response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False
    )

    if response.status_code >= 300:
        print('None')
    else:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)
