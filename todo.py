# Create an empty list to store tasks
todo_list = []

while True:
    # Display menu options
    print("\nTo-Do List:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")

    # Get user choice
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task to add: ")
        todo_list.append(task)
        print("Task added to the list!")

    elif choice == "2":
        if len(todo_list) == 0:
            print("The to-do list is empty.")
        else:
            print("Current tasks:")
            for index, task in enumerate(todo_list):
                print(f"{index + 1}. {task}")
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            if 0 <= task_index < len(todo_list):
                removed_task = todo_list.pop(task_index)
                print(f"'{removed_task}' removed from the list.")
            else:
                print("Invalid index. No task removed.")

    elif choice == "3":
        if len(todo_list) == 0:
            print("The to-do list is empty.")
        else:
            print("Current tasks:")
            for index, task in enumerate(todo_list):
                print(f"{index + 1}. {task}")

    elif choice == "4":
        print("Exiting the to-do list program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

