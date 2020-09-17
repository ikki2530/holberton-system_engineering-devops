#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def new_recurse(subreddit, hot_list=[], page=''):
    """Adding new recursion"""
    titles = []
    if page is None:
        return hot_list
    if subreddit:
        try:
            heads = {'User-agent': 'dagomez2530'}
            url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, page)

            response = requests.get(url, headers=heads)

            data_reddit = response.json()
            i = 0
            lista_hot = data_reddit['data']['children']
            lg = len(lista_hot)
            for i in range(lg):
                hot_list.append(lista_hot[i]['data']['title'])

            after = data_reddit['data']['after']

            titles = new_recurse(subreddit, hot_list, after)
            return titles
        except:
            return None


def recurse(subreddit, hot_list=[]):
    """top ten subreddits titles"""
    titles = new_recurse(subreddit, hot_list, '')
    return titles
