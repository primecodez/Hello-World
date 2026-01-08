def todo_list():
    """Simple interactive to-do list in the terminal."""

    menu = (
        "1. Add a new task\n"
        "2. View all tasks\n"
        "3. Mark a task as completed\n"
        "4. Delete a task\n"
        "5. Exit"
    )

    tasks = []

    while True:
        print(menu)
        user_choice = input("Choose an option: ").strip()

        if user_choice == "1":
            task = input("Enter the task you want to add: ").strip()
            tasks.append(task)
            print(f'Task "{task}" added successfully.')

        elif user_choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("Your tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")

        elif user_choice == "3":
            if not tasks:
                print("No tasks to mark as completed.")
                continue
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if 0 < task_num <= len(tasks):
                completed_task = tasks.pop(task_num - 1)
                print(f'Task "{completed_task}" marked as completed and removed from the list.')
            else:
                print("Invalid task number.")

        elif user_choice == "4":
            if not tasks:
                print("No tasks to delete.")
                continue
            try:
                task_num1 = int(input("Enter the task number to delete: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if 0 < task_num1 <= len(tasks):
                deleted_task = tasks.pop(task_num1 - 1)
                print(f'Task "{deleted_task}" deleted successfully.')
            else:
                print("Invalid task number.")

        elif user_choice == "5":
            print("Exiting the to-do list application. Thanks for using it.Have a great day!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")



todo_list()