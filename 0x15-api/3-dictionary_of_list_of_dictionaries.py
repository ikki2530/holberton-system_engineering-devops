#!/usr/bin/python3
"""export data of all employees to JSON format."""
import json
import requests
import sys
import time


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/"

    response_users = requests.get(url_user)

    users_info = response_users.json()
    filename = "todo_all_employees.json"
    dictionary = {}
    for user in users_info:
        u_id = user['id']
        url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
                u_id)
        response_todo = requests.get(url)
        todo_list = response_todo.json()
        total_todo = len(todo_list)
        username = user.get("username")
        dictionary[u_id] = []
        dict_task = {}
        # wait 10 seconds
        # time.sleep(1)
        for task in todo_list:
            status = task.get("completed")
            title = task.get("title")
            dict_task["username"] = username
            dict_task["task"] = title
            dict_task["completed"] = status
            dictionary[u_id].append(dict_task)
            dict_task = {}

    with open(filename, "w") as f:
        json.dump(dictionary, f)
