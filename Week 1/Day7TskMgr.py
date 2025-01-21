import os

#file to store tasks
FILE_NAME = "tasks.txt"

#load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" , ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

#save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} , {task['title']} , {task['status']}\n")
            
#add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default = 0)+1
    tasks[task_id] = {"title": title, "status": "pending"}
    print(f"Task '{title}' added successfully")

#view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}]. {task['title']} - {task['status']}")
            
#mark a task as done
def mark_done(tasks):
    task_id = int(input("Enter task id: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "done"
        print(f"Task '{tasks[task_id]['title']}' marked as done")
    else:
        print("Task not found")
        
#delete a task
def delete_task(tasks):
    task_id = int(input("Enter task id: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted")
    else:
        print("Task not found")
        
#task manager
def task_manager():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Thank you for using Task Manager")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    task_manager()