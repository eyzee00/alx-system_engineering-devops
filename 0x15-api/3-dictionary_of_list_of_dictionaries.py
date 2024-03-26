#!/usr/bin/python3
"""Exports todo list information of all employees to JSON format"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()
    users_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/todos'
        todos = requests.get(url, params={'userId': user_id}).json()
        users_dict[user_id] = []
        for todo in todos:
            users_dict[user_id].append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
