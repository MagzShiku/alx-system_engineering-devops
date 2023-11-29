#!/usr/bin/python3

"""
   Python script that uses REST API (https://jsonplaceholder.typicode.com/)
   to return TODO list progress for a given employee ID

   Requirements:
   - Use urllib module
   - Accept integer parameter (employee ID)
   - Display progress in specified format
"""

import json
import sys
import urllib.request


def get_employee_todo_list(employee_id):
    """
       Retrieves TODO list by appending ID to URL
       Reads and parses JSON response
    """

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    todos = json.loads(response.read())
    return todos


def display_employee_progress(employee_id):
    """
       Takes employee ID, calls get_employee_todo_list()
       Displays progress in desired format using formatting
       and loop to display completed tasks
    """

    todos = get_employee_todo_list(employee_id)

    # Get employee name
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"  
    employee_response = urllib.request.urlopen(employee_url)
    employee = json.loads(employee_response.read())
    employee_name = employee["name"]

    # Count completed tasks
    completed_tasks = [todo for todo in todos if todo["completed"]]  
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos)

    # Display progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    """
       Retrieves employee ID from command line arguments  
       Calls display_employee_progress()
    """

    employee_id = int(sys.argv[1])
    display_employee_progress(employee_id)

