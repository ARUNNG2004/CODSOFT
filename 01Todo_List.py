class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            remove = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {remove}")
        else:
            print("Invalid task number")

def main():
    todo_list = ToDoList()

    while True:
        print("""
        To-Do List Application
        1. Add task
        2. View tasks
        3. Delete task
        4. Exit
        """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == 2:
            todo_list.view_tasks()
        elif choice == 3:
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid input .Please try again.")

if __name__ == "__main__":
    main()
