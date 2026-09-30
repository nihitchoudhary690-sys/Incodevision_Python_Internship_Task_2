"""
Task 02: Console-Based To-Do List Application
IncodeVision Python Internship

Description:
A beginner-friendly, clean, and robust command-line To-Do List application.
Allows users to manage daily tasks by adding, viewing, completing, and deleting tasks
with persistent state during runtime.
"""


def display_menu():
    """Displays the main menu options to the user."""
    print("=" * 50)
    print("               TO-DO LIST APP               ")
    print("=" * 50)
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")
    print("-" * 50)


def add_task(tasks):
    """
    Prompts the user to enter a new task and adds it to the tasks list.

    Args:
        tasks (list): The list containing task dictionaries.
    """
    print("\n--- Add a New Task ---")
    task_title = input("Enter task description: ").strip()

    if not task_title:
        print("[!] Task description cannot be empty. Please try again.\n")
        return

    # Each task is stored as a dictionary with description and status
    new_task = {
        "title": task_title,
        "completed": False
    }
    tasks.append(new_task)
    print(f"[+] Task '{task_title}' added successfully!\n")


def view_tasks(tasks):
    """
    Displays all tasks with their index and current status (Pending / Completed).

    Args:
        tasks (list): The list containing task dictionaries.
    """
    print("\n--- All Tasks ---")
    if not tasks:
        print("Your to-do list is currently empty. Add a task to get started!\n")
        return

    print(f"{'#':<4} {'Status':<14} {'Task Description'}")
    print("-" * 50)
    for idx, task in enumerate(tasks, start=1):
        status = "[Completed]" if task["completed"] else "[Pending]"
        print(f"{idx:<4} {status:<14} {task['title']}")
    print("-" * 50 + "\n")


def mark_task_completed(tasks):
    """
    Marks a selected task as completed based on user-provided task number.

    Args:
        tasks (list): The list containing task dictionaries.
    """
    print("\n--- Mark Task as Completed ---")
    if not tasks:
        print("[!] No tasks available to mark as completed.\n")
        return

    view_tasks(tasks)
    user_input = input("Enter the task number to mark as completed (or 'c' to cancel): ").strip()

    if user_input.lower() == "c":
        print("[*] Action cancelled.\n")
        return

    try:
        task_num = int(user_input)
        if 1 <= task_num <= len(tasks):
            selected_task = tasks[task_num - 1]
            if selected_task["completed"]:
                print(f"[INFO] Task #{task_num} '{selected_task['title']}' is already marked as Completed.\n")
            else:
                selected_task["completed"] = True
                print(f"[+] Task #{task_num} '{selected_task['title']}' marked as Completed!\n")
        else:
            print(f"[!] Invalid task number. Please choose a number between 1 and {len(tasks)}.\n")
    except ValueError:
        print("[!] Invalid input: Please enter a valid task number.\n")


def delete_task(tasks):
    """
    Deletes a task from the list based on user-provided task number.

    Args:
        tasks (list): The list containing task dictionaries.
    """
    print("\n--- Delete a Task ---")
    if not tasks:
        print("[!] No tasks available to delete.\n")
        return

    view_tasks(tasks)
    user_input = input("Enter the task number to delete (or 'c' to cancel): ").strip()

    if user_input.lower() == "c":
        print("[*] Action cancelled.\n")
        return

    try:
        task_num = int(user_input)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"[+] Task #{task_num} '{removed_task['title']}' deleted successfully!\n")
        else:
            print(f"[!] Invalid task number. Please choose a number between 1 and {len(tasks)}.\n")
    except ValueError:
        print("[!] Invalid input: Please enter a valid task number.\n")


def main():
    """Main function controlling the application loop and user navigation."""
    # List to hold all task dictionaries
    tasks = []

    print("\nWelcome to the IncodeVision Console To-Do List Application!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nThank you for using the To-Do List App. Goodbye!\n")
            break
        else:
            print("\n[!] Invalid choice: Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
