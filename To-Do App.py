import json
import os
from colorama import init, Fore, Style
from datetime import datetime

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
        print(color+f"{index}: [{status}] {task['title']} - {task['priority']}")
        if (task['Overdue'] == True):
            print("Due Date: " + task['due_date'] + Fore.RED + " - OVERDUE")
        else:
            print("Due Date: " + task['due_date'])
    print()
    print()

              

def checkOverDue(task):

    try:
        overdue = isOverDue(task['due_date'])
        if overdue & task['done'] == False:
            return True
        else:
            return False
    except ValueError:
        print("Invalid Date")


def isOverDue(date):
    try:
        today = datetime.today().date()
        task_date = datetime.strptime(date, "%Y-%m-%d").date()
        if task_date < today:
            return True
        else:
            return False
    except ValueError:
        print("Invalid Date")


def addTask(tasks):
    title = input("\nEnter task\n").strip()
    print()
    dueDate = input("\nEnter due date (YYYY-MM-DD) : ").strip()
    print()

    try:
        datetime.strptime(dueDate,"%Y-%m-%d")
    except ValueError:
        print("\nInvalid Date Format. Use (YYYY-MM-DD)")
        return
    
    overdue = isOverDue(dueDate)
    
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

            tasks.append({"title": title, 
                          "done": False, 
                          "priority": priority, 
                          "due_date": dueDate, 
                          "Overdue": overdue
                          })
            save(tasks)
            print("\n Successfully added task\n")
        else:
            print("\nTask cannot be empty\n")
        sortTask(tasks)
    except ValueError:
        print("\nError: Enter valid input")



def markTask(tasks) :

    if tasks:
        viewTask(tasks)

        try:
            num = int(input("\nEnter a task to mark as done\n"))
            if (1 <= num <= len(tasks)):
                tasks[num-1]["done"] = True
                if tasks[num-1]["Overdue"]:
                    tasks[num-1]["Overdue"] = False
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

    priorityOrder = {
        "High": 0,
        "Medium": 1,
        "Low": 2
    }

    tasks.sort(key=lambda task: priorityOrder[task["priority"]])
    """
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
    save(tasks)
    """

def editTask(tasks):
    if not tasks:
        print("\nNo Tasks to Edit\n")
        return
    viewTask(tasks)
    try:
        choice = int(input("Choose task to edit\n"))
        if 0 < choice <= len(tasks):
            prioNum = 0
            while not (0 < prioNum < 5):
                print("What priority?")
                print("1. High")
                print("2. Medium")
                print("3. Low")
                print("4. Cancel")
                prioNum = int(input("\nChoose new priority\n"))

                if prioNum == 1:
                    tasks[choice - 1]['priority'] = "High"
                    print("Task Priority Changed to High")
                elif prioNum == 2:
                    tasks[choice - 1]['priority'] = "Medium"
                    print("Task Priority Changed to Medium")
                elif prioNum == 3:
                    tasks[choice - 1]['priority'] = "Low"
                    print("Task Priority Change to Low")
                elif prioNum == 4:
                    print("\nTask Not Edited\n")
                else:
                    print("\nEnter a valid input")
            save(tasks)

                
                    
    except ValueError:
        print("\nInvalid Task Number\n")




def main() :
    tasks = load_tasks()

    while True:
        try:
            choice = 0
            print("=== TO-DO APP ===")
            print("1. View Tasks")
            print("2. Add a Task")
            print("3. Mark Task as Done")
            print("4. Delete Task")
            print("5. Edit Task")
            print("6. Sort Task")
            print("7. Quit")
            
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
                editTask(tasks)
            elif choice == 6:
                sortTask(tasks)
            elif choice == 7:
                save(tasks)
                print("To-Do App Exited")
                break
            else:
                print("\nChoose a valid number\n")
        except ValueError:
            print("\nInvalid Input\n")

if __name__ == "__main__":
    main()


