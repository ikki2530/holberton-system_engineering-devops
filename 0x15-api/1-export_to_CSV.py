#!/usr/bin/python3
"""export data in the CSV format."""
import csv
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

    with open("2.csv", "w") as f:
        csv_write = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        lista = []
        for task in todo_list:
            lista.append(u_id)
            lista.append(username)
            status = task.get("completed")
            title = task.get("title")
            lista.append(status)
            lista.append(title)
            csv_write.writerow(lista)
            lista = []
