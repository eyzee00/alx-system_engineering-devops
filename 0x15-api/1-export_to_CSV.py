#!/usr/bin/python3
"""Exports todo list information for a given employee ID to CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                         format(user_id)).json()

    with open("{}.csv".format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user.get('username'),
                             task.get('completed'), task.get('title')])
