#!/usr/bin/python3

"""
I need to export to CSV
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""

import csv
import requests
import sys

def get_employee_todos(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    return response.json()

def get_employee_name(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()["name"]

def export_to_csv(employee_id):
    todos = get_employee_todos(employee_id)
    name = get_employee_name(employee_id)

    filename = f"{employee_id}.csv"

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            completed_status = "True" if todo["completed"] else "False"
            task_title = todo["title"]
            writer.writerow([employee_id, name, completed_status, task_title])

    print(f"Data exported to {filename} successfully.")

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
