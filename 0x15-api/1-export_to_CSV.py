#!/usr/bin/python3
""" A script that:
- using this REST API, for a given employee ID,
- returns information about his/her TODO list progress.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]
    employee_username = user_data["username"]

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId="\
        f"{employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    # print(todos_data)
    # print(str(employee_id))
    # print(employee_name)
    # print(user_data["username"])

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    with open("USER_ID.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([
                employee_id,
                employee_username,
                task["completed"],
                task["title"]
            ])
