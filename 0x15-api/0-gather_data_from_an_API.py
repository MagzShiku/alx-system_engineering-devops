#!/usr/bin/python3

"""
    a Python script that, using this REST API, for a given employee ID
    (https://jsonplaceholder.typicode.com/)
    returns information about his/her TODO list progress.

    - You must use urllib or requests module
    - The script must accept an integer as a parameter, which is the
    employee ID
    - must display on the standard output the employee TODO list
    progress in this exact format
    - First line: Employee EMPLOYEE_NAME is done with
    tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS)
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS
    - Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

"""
import urllib.request
import json
import sys


def get_employee_todo_list(employee_id):
    """
        retrieves the TODO list for a given employee ID by
        appending the ID to the URL.
        reads and parses the response JSON
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    todos = json.loads(response.read())
    return todos


def display_employee_progress(employee_id):
    """
         function takes an employee ID as a parameter, calls the
         get_employee_todo_list function to retrieve the tasks,
         and then displays the employee's progress in the desired
         format. It uses string formatting to construct the output
         and a loop to iterate over the completed tasks and display
         their titles.
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
    print(f"Employee {employee_name} is done with\
        tasks({num_completed_tasks}/{total_num_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    """
        the main function: retrieves the employee ID from the comman
        line arguments and call the display_employee_progress
        function with the provided ID.
    """
    employee_id = int(sys.argv[1])
    display_employee_progress(employee_id)
