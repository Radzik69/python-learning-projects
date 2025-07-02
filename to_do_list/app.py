import json

all_tasks = {}

def append_json_tasks():
    global all_tasks
    try:
        with open("tasks_json_data.json", "r") as file:
            json_file = file.read()
            all_tasks = json.loads(json_file)
    except Exception as e:
        print(f"Error: {e}")

def append_current_tasks_to_json():
    with open("tasks_json_data.json", "w") as file:
        json.dump(all_tasks, file, indent=4)


def show_tasks_menu():
    print("Welcome to Tasks List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Mark task as done")
    print("6. Exit program")

def select_action_from_menu():
    show_tasks_menu()
    selected_action = input("Select action: ")

    match selected_action:
        case "1":
            view_tasks()
        case "2":
            add_task()
        case "3":
            delete_task()
        case "4":
            edit_task()
        case "5":
            complete_task()
        case "6":
            append_current_tasks_to_json()
            return
        case _:
            print("Invalid input")

def view_tasks():
    print(all_tasks)
    select_action_from_menu()

def add_task():
    this_task = {}
    task_data = input("Write a task: ")
    this_task["task"] = task_data
    this_task["done"] = False
    all_tasks[len(all_tasks)+1] = this_task
    select_action_from_menu()

def delete_task():
    try:
        task_number_to_delete = int(input("Enter task number to delete: "))
    except Exception as e:
        print(f"Error: {e}")
    all_tasks.pop(task_number_to_delete)
    select_action_from_menu()

def edit_task():
    try:
        task_number_to_edit = int(input("Enter task number to edit: "))
    except Exception as e:
        print(f"Error: {e}")
    edited_data = input("Enter edited task: ")
    all_tasks[task_number_to_edit].update({"task": edited_data})
    select_action_from_menu()

def complete_task():
    try:
        task_number_to_complete = int(input("Enter task number to complete: "))
    except Exception as e:
        print(f"Error: {e}")
    all_tasks[task_number_to_complete].update({"done": True})
    select_action_from_menu()

append_json_tasks()
select_action_from_menu()

