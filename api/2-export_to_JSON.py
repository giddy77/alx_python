#this is the export to json module
import requests
import sys
import json

#this is the export to json module
def get_employee_todo_list_progress(employee_id):
    # Fetch employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()

    if 'name' not in employee_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(todo_url)
    todo_data = response.json()

    # Calculate the progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    # Create a data structure for JSON export
    export_data = {
        "USER_ID": [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todo_data]
    }

    # Create a JSON file for the employee
    json_file_name = f'{employee_id}.json'

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    # Write the data to the JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(export_data, json_file, indent=4)

    print(f"Data exported to {json_file_name}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list_progress(employee_id)
