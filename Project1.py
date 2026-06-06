tasks = []

while True:
    print("\nTask Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, or 3.")
