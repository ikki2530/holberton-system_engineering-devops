#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """top ten subreddits titles"""
    if subreddit:
        try:
            heads = {'User-agent': 'dagomez2530'}
            url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

            response = requests.get(url, headers=heads)

            data_reddit = response.json()
            i = 0
            for i in range(10):
                print(data_reddit['data']['children'][i]['data']['title'])
        except:
            print(None)
