#!/usr/bin/python3
"""
    recursive function(that calls itself) that goes to reddit
        - Returns a list containing the titles of all hot articles
          of a given subreddit
        - If no results are found for the given subreddit,
          the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
        thr action
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]

        if after is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
