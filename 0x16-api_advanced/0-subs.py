#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """Return number of suscribers"""
    if subreddit:
        heads = {'User-agent': 'dagomez2530'}
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

        response = requests.get(url, headers=heads)

        data_reddit = response.json()
        return data_reddit['data']['subscribers']
    else:
        return 0
