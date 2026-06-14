tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                status = "✓" if tasks[i]["done"] else " "
                print(f"{i + 1}. [{status}] {tasks[i]['task']}")

    elif choice == "2":
        new_task = input("Enter the new task: ")
        tasks.append({"task": new_task, "done": False})
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            task_no = int(input("Enter task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["done"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Deleted task: {removed['task']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")