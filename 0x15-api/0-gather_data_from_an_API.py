#!/usr/bin/python3
"""returns information about an employee, TO DO list progress."""
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
    name = user_info.get("name")

    # completed tasks
    c = 0
    for task in todo_list:
        completed_status = task.get('completed')
        if completed_status:
            c += 1

    print("Employee {} is done with tasks({}/{}):".format(name, c, total_todo))
    for task in todo_list:
        completed_status = task.get('completed')
        if completed_status:
            title = task.get("title")
            print("\t {}".format(title))
