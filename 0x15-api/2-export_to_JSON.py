#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    u_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(u_id)
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)

    response_todo = requests.get(url)
    response_user = requests.get(url_user)

    todo_list = response_todo.json()
    user_info = response_user.json()

    total_todo = len(todo_list)
    username = user_info.get("username")
    filename = u_id + ".json"
    dictionary = {}
    dictionary[u_id] = []
    dict_task = {}
    for task in todo_list:
        status = task.get("completed")
        title = task.get("title")
        dict_task["task"] = title
        dict_task["completed"] = status
        dict_task["username"] = username
        dictionary[u_id].append(dict_task)
        dict_task = {}

    with open(filename, "w") as f:
        json.dump(dictionary, f)
