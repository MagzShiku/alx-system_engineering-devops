#!/usr/bin/python3

"""
   Python script that uses REST API (https://jsonplaceholder.typicode.com/) 
   to return TODO list progress for a given employee ID

   Requirements:
   - Use urllib module
   - Accept integer parameter (employee ID)
   - Display progress in specified format
"""


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


def display_progress(employee_id):
  todos = get_employee_todos(employee_id)
  name = get_employee_name(employee_id)

  completed = 0
  total = len(todos)

  for todo in todos:
    if todo["completed"]:
      completed += 1
      print(f"\t{todo['title']}")

  print(f"Employee {name} is done with tasks({completed}/{total}):")


if __name__ == "__main__":
  employee_id = int(sys.argv[1])
  display_progress(employee_id)
