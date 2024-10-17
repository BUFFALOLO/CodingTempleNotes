task_list = []

def add_task(status="Incomplete"):
        task_name =  input("\nEnter the task you would like to add to your To-Do List: ")
        task_list.append({task_name, status})
        print(f"{task_name} has been added to the To-Do List.")

        while True:
            choice = input("\nWould you like to add another task? (yes/no): ").lower()
            if choice == 'yes':
                add_task()
                break
            elif choice == 'no':
                print("\nYou will be returned to the main menu")
                break
            else:
                print("\nYou have not made a valid entry - you will be returned to the main menu.")
                break

def view_tasks():
    if task_list:
        print("\nTo-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index} - {task}")
    else:
        print("\nThe To-Do List is Empty")

def mark_task_complete():
    pass

def delete_task():
    pass

def quit_application():
    pass

while True:
    try:
        print("\nWelcome to the To-Do List App!")
        print("\nMenu:")
        print("1. Add a Task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")

        menu_choice = int(input("\nEnter a number from the menu: "))

        if menu_choice == 1:
          add_task()
        elif menu_choice == 2:
          view_tasks()
        elif menu_choice == 3:
            pass
        elif menu_choice == 4:
            pass
        elif menu_choice == 5:
            pass
        else:
            print("\nPlease make a valid menu choice, enter a number from 1 to 5.")

    except ValueError:
        print("\nPlease make a valid menu choice, enter a number from 1 to 5.")
