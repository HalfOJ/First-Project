import json
import os
from colorama import init, Fore, Style
init(autoreset=True)

file_name = "realTaskList.json"


def load_tasks():

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    else:
        return []

def save(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)



def viewTask(tasks):
    if not tasks:
        print("\nNo tasks yet\n")
        return
    print("\nYour To-Do List\n")
    for index, task in enumerate(tasks, start= 1):
        status = "✓" if task["done"] else " "
        if task['priority'] == "High":
            color = Fore.RED
        elif task['priority'] == "Medium":
            color = Fore.YELLOW
        elif task['priority'] == "Low":
            color = Fore.GREEN
        print(color+f"{index}: [{status}] {task['title']}")
    print()
    print()

              

def addTask(tasks):
    title = input("\nEnter task\n").strip()
    print()
    
    try:
        prioTitle = 0
        priority = ""
        while priority == "":
            print("What priority?")
            print("1. High")
            print("2. Medium")
            print("3. Low")

            prioTitle = int(input("\nEnter Priority\n"))

            if prioTitle == 1:
                priority = "High"
            elif prioTitle == 2:
                priority = "Medium"
            elif prioTitle == 3:
                priority = "Low"
            else:
                print("\nError: Enter a valid input\n")

        if title:
            tasks.append({"title": title, "done": False, "priority": priority})
            save(tasks)
            print("\n Successfully added task\n")
        else:
            print("\nTask cannot be empty\n")
        sortTask(tasks)
    except ValueError:
        print("\nError: Enter valid input")



def markTask(tasks) :
    viewTask(tasks)

    try:
        num = int(input("\nEnter a task to mark as done\n"))
        if (1 <= num <= len(tasks)):
            tasks[num-1]["done"] = True
            save(tasks)
            print("\n Task marked done\n")
        else:
            print("\nPlease enter a valid task number\n")
    except ValueError:
        print("\nInput is invalid\n")

def delTask(tasks):
    viewTask(tasks)

    if tasks:
        try:
            num = int(input("\nEnter a number task to delete\n"))
            if (0 < num <= len(tasks)) :
                tasks.pop(num - 1)
                save(tasks)
                print("\nTask Deleted\n")
            else:
                print("\nPlease enter a valid number\n")
        except ValueError:
            print("\nInput is invalid\n")

def sortTask(tasks):
    low = []
    med = []
    high = []
    for task in tasks:
        prio = task['priority']
        if prio == "Low":
            low.append(task)
        elif prio == "Medium":
            med.append(task)
        elif prio == "High":
            high.append(task)
    
    rTask = []
    for task in high:
        rTask.append(task)
    for task in med:
        rTask.append(task)
    for task in low:
        rTask.append(task)
    tasks[:] = rTask

def main() :
    tasks = load_tasks()

    while True:
        try:
            choice = 0
            print("=== TO-DO APP ===")
            print("1. View Tasks")
            print("2. Add a task")
            print("3. Mark task as done")
            print("4. Delete task")
            print("5. Quit")
            
            choice = int(input("\nEnter choice\n"))
            if choice == 1:
                viewTask(tasks)
            elif choice == 2:
                addTask(tasks)
            elif choice == 3:
                markTask(tasks)
            elif choice == 4:
                delTask(tasks)
            elif choice == 5:
                save(tasks)
                break
            else:
                print("\nChoose a valid number\n")
        except ValueError:
            print("\nInvalid Input\n")

if __name__ == "__main__":
    main()


