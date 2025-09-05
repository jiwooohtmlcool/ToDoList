tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("0. Quit")

    Ichoice = input("Choose an option: ")
    
    if Ichoice == "1":
        if not tasks:
            print("No task yet")
        else:
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")

    elif Ichoice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("task added")

    elif Ichoice == "3":
        if not tasks:
            print("No task to remove")
        else:
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number")

    elif Ichoice == "0":
        print("Goodye")
        break

    else:
        print("Invalid choice please try again")