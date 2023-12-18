#!/usr/bin/python3
"""
goes to REDDIT asks it for:
    no. of subscribers
if an invalid subredit is given return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    our prototype:
    url - returns the suvscribers in .json format
    headers - gets compatibility with various search engines
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; \
            Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        """checks for error"""
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
