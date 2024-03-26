#!/usr/bin/python3
"""Exports todo list information for a given employee ID to JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id)).json()

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump({user_id: [{
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user.get('username')
        } for todo in todos]}, file)
