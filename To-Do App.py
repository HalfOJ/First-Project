
tasks = []
while True:
    choice = 0

    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")
    
    choice = int(input("Enter choice"))
    if choice == 1:
        tasks.append(str(input("Enter task")))
    elif choice == 2:
        print(tasks)
    elif choice == 3:
        break
    else:
        choice = int(intput("Enter a valid number"))




