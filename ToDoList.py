ToDo_List = []

def view_task ():
    """Reads and diplays all tasks currently in the list."""

    print ("\n---Current To-Do List:---")
    if not ToDo_List:
        print ("Your To_Do List is empty.")
    else:
        for i, task in enumerate (ToDo_List):
            print (f"{i+1}.{task}")
    print ("--------------\n")

def add_task():
    new_task = input("Enter the new task.")
    ToDo_List.append(new_task)
    print (f"'{new_task}' added to the list.")

def complete_task ():
    view_task()

    if not ToDo_List:
        return
    
    try:
        task_num = int (input("Enter the number of the task to mark complete: "))
        task_index = task_num - 1

        if 0 <= task_index < len(ToDo_List):
            completed_task = ToDo_List[task_index]
            ToDo_List[task_index] = f"[DONE] {completed_task}"
            print (f"Task '{completed_task}' marked as complete !")
        else:
            print("Invalid Task Number. Please try Again.")

    except ValueError:
        print ("Invalid input. please enter a valid task number.  ")


def main_menu():
    while True:
        print("\n^^^ To-Do List MENU ^^^")
        print("1. view Tasks.")
        print("2. Add New Task.") 
        print("3. mark Task as Complete.")
        print("4. QUIT.")
        print("^_^ ^_^ ^_^ ^_^ ^_^ ^_^ ^_^")

        choice = input("enter your choice (1-4): ")

        if choice == '1':
            view_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            print ("Exiting To-Do List. ^_^!")
            break
        else:
            print ("Invalid choice !!! Enter 1,2,3 OR 4 only.")


if __name__ == "__main__":
    main_menu()