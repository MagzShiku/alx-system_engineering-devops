#!/usr/bin/python3
"""
    recursive function
     parses the title of all hot articles
     prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    couts an assortment
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Invalid subreddit or no posts found.")
        return

    data = response.json()
    children = data["data"]["children"]

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                if word.lower() in counts:
                    counts[word.lower()] += 1
                else:
                    counts[word.lower()] = 1

    after = data["data"]["after"]
    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
