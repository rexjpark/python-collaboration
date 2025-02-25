class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added successfully.')
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "[Completed]" if task['completed'] else "[Pending]"
                print(f"{idx}. {task['task']} {status}")
    
    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print(f"Task {task_index} marked as completed.")
        else:
            print("Invalid task index.")
    
    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            todo_list.view_tasks()
            task_index = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
