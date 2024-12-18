import argparse
import os


def read_file(filename):
    #reads the todo list from the specified file
    if not os.path.exists(filename):
        return []
    
    with open(filename, 'r') as f:
        tasks = []
        for line in f:
            parts = line.strip().split('|')
            if len(parts) == 4:
                task_id, category, description, status = parts
                tasks.append({
                    'id': int(task_id),
                    'category': category,
                    'description': description,
                    'status': status
                })
        return tasks


def write_file(filename, tasks):
    #writes the todo list to the specified file
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['category']}|{task['description']}|{task['status']}\n")


def generate_id(todo_list):
    #generates ID for a new task
    return len(todo_list) + 1



def add_task(todo_list, category, description, status, filename):
    # adds a new task to the todo list
    id = generate_id(todo_list)
    task = {'id': id, 'category': category, 'description': description, 'status': status}
    todo_list.append(task)
    write_file(filename, todo_list)
    print(f"Task '{description}' added with ID {id}")


def update_task(todo_list, task_id, category, description, status, filename):
    # updates an existing task in the todo list
    for task in todo_list:
        if task['id'] == task_id:
            if category:
                task['category'] = category
            if description:
                task['description'] = description
            if status:
                task['status'] = status
                
            write_file(filename, todo_list)
            print(f"Task ID {task_id} updated.")
            return
    print(f"Task with ID {task_id} not found.")


def status(todo_list, task_id, status, filename):
    #changes the status of a task
    for task in todo_list:
        if task['id'] == task_id:
            task['status'] = status
            write_file(filename, todo_list)
            print(f"Task ID {task_id} status updated to '{status}'.")
            return
    print(f"Task with ID {task_id} not found.")


def list_tasks(todo_list):
    #lists all tasks in the todo list
    if not todo_list:
        print("No tasks found.")
        return
    for task in todo_list:
        print(f"ID: {task['id']} | Category: {task['category']} | Description: {task['description']} | Status: {task['status']}")


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool that allows you to create, change completion status, and edit items writen out in a TODO list."
        )
    
    parser.add_argument(
        '-l', '--listname', 
        type=str, 
        default='todo.txt', 
        help="Name of the TODO list file"
        )
    
    subparsers = parser.add_subparsers(
        dest='command', 
        required=True
        )

    # adds a task
    add_parser = subparsers.add_parser(
        'add', 
        help="Add a new task"
        )
    
    add_parser.add_argument(
        '-c', '--category', 
        type=str, 
        required=True, 
        help="Category of the task"
        )
    add_parser.add_argument(
        '-d', '--description',
        type=str, 
        required=True, 
        help="Description of the task"
        )
    add_parser.add_argument(
        '-s', '--status',
        type=str, 
        choices=['incomplete', 'in progress', 'complete'], 
        required=True, 
        help="Task status"
        )

    # list tasks
    subparsers.add_parser(
        'list', 
        help="List all tasks")

    # update a task
    update_parser = subparsers.add_parser(
        'update', 
        help="Update an existing task"
        )
    update_parser.add_argument(
        '--id', 
        type=int, 
        required=True, 
        help="ID of the task to update"
        )
    update_parser.add_argument(
        '-c', '--category',
        type=str, 
        help="New category for the task"
        )
    update_parser.add_argument(
        '-d', '--description', 
        type=str, 
        help="New description for the task"
        )
    update_parser.add_argument(
        '-s', '--status', 
        type=str, 
        choices=['incomplete', 'in progress', 'complete'], 
        help="New status for the task"
        )

    # change task status
    status_parser = subparsers.add_parser(
        'status', 
        help="Change the status of a task"
        )
    status_parser.add_argument(
        '--id', 
        type=int, 
        required=True, 
        help="ID of the task"
        )
    
    status_parser.add_argument(
        '--status', 
        type=str, 
        choices=['incomplete', 'in progress', 'complete'], 
        required=True, 
        help="New status for the task"
        )

    args = parser.parse_args()
    # load todo list from the specified file
    todo_list = read_file(args.listname)

    if args.command == 'add':
        add_task(todo_list, args.category, args.description, args.status, args.listname)
    elif args.command == 'list':
        list_tasks(todo_list)
    elif args.command == 'update':
        update_task(todo_list, args.id, args.category, args.description, args.status, args.listname)
    elif args.command == 'status':
        status(todo_list, args.id, args.status, args.listname)


if __name__ == '__main__':
    main()

