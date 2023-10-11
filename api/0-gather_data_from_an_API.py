import requests
import sys

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

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list_progress(employee_id)
