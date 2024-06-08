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

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId="\
        f"{employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    with open("USER_ID.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
            ])

        for task in todos_data:
            writer.writerow(
                [employee_id, employee_name, task["completed"], task["title"]]
            )
