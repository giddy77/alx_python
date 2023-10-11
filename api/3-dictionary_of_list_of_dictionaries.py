
import json
import requests

def fetch_employee_todo_list(employee_id):
    # Fetch employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()

    # Check if the 'name' key exists in the employee data
    if 'name' not in employee_data:
        return None  # Employee not found

    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(todo_url)
    todo_data = response.json()

    # Create a list of tasks for the employee
    tasks = []
    for task in todo_data:
        task_data = {
            "username": employee_name,
            "task": task['title'],
            "completed": task['completed'],
        }
        tasks.append(task_data)

    return tasks

def export_todo_all_employees():
    all_employee_data = {}  # A dictionary to store all employees' data

    # Loop through employee IDs (assumes employees have sequential IDs)
    employee_id = 1
    while True:
        tasks = fetch_employee_todo_list(employee_id)
        if tasks is not None:
            all_employee_data[employee_id] = tasks
        else:
            break  # Stop when an employee is not found

        employee_id += 1

    # Create a JSON file for all employees
    json_file_name = 'todo_all_employees.json'

    # Write the data to the JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)

    print(f"Data for all employees exported to {json_file_name}")

if __name__ == '__main__':
    export_todo_all_employees()
