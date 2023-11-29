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


def get_employee_name(employee_id):

  """
     Retrieves employee name from API
  """

  url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  response = urllib.request.urlopen(url)
  employee = json.loads(response.read())
  return employee["name"]


def display_employee_progress(employee_id):

  """
     Displays progress in specified format
  """

  todos = get_employee_todo_list(employee_id)
  employee_name = get_employee_name(employee_id)

  # rest of function

if __name__ == "__main__":

  """
     Calls main function
  """

  employee_id = int(sys.argv[1])
  display_employee_progress(employee_id)
