class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("List of Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task '{old_task}' updated to '{new_task}' successfully.")
        else:
            print(f"Task '{old_task}' not found in the TodoList")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task index. Task not deleted.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            self.completed_tasks.append(completed_task)
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task index. Task not marked as completed.")

    def view_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks in the list.")
        else:
            print("List of Completed Tasks:")
            for i, task in enumerate(self.completed_tasks, 1):
                print(f"{i}. {task}")

    def clear_tasks(self):
        self.tasks = []
        self.completed_tasks = []
        print("All tasks and completed tasks cleared.")

def main():
    todo_list = TodoList()
    menu_options = {
        '1': todo_list.add_task,
        '2': todo_list.view_tasks,
        '3': todo_list.delete_task,
        '4': todo_list.update_task,
        '5': todo_list.mark_completed,
        '6': todo_list.view_completed_tasks,
        '7': todo_list.clear_tasks,
        '8': exit
    }

    while True:
        print("\n******** To-Do-List Application ********")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Mark Task as Completed")
        print("6. View Completed Tasks")
        print("7. Clear All Tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice in menu_options:
            if choice in ('2', '6'):
                menu_options[choice]()
            elif choice in ('3', '5'):
                task_index = int(input("Enter the task index: "))
                menu_options[choice](task_index)
            elif choice == '4':
                old_task = input("Enter the task to update: ")
                new_task = input("Enter the new task: ")
                todo_list.update_task(old_task, new_task)
            elif choice == '7':
                confirmation = input("Are you sure you want to clear all tasks? (y/n): ")
                if confirmation.lower() == 'y':
                    menu_options[choice]()
            elif choice == '8':
                print("Thanks for using this Application!")
                break
            else:
                task = input("Enter the task: ")
                menu_options[choice](task)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
