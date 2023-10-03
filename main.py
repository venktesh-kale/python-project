to_do_list = []


def display_list():
    if not to_do_list:
        print("your list is empty. ")
    else:
        print("to do list")
        for index, item in enumerate(to_do_list, 1):
            print(f"{index}. {item}")


def add_item():
    task = input("Enter the task you want to add: ")
    to_do_list.append(task)
    print(f"your {task} has been added. ")


def edit_item():
    display_list()
    if not to_do_list:
        return
    try:
        item_number = int(input("Enter the number of items you want to change: "))
        if 1 <= item_number <= len(to_do_list):
            new_task = input("Enter the new task: ")
            to_do_list[item_number - 1] = new_task
            print(f"task {item_number} has been updated ")
        else:
            print("invalid task number. ")
    except ValueError:
        print("Invalid input. please input a valid number.")


def delete_item():
    display_list()
    if not to_do_list:
        return
    try:
        item_number = int(input("Enter the number of task you want to delete: "))
        if 1 <= item_number <= len(to_do_list):
            deleted_task = to_do_list.pop(item_number - 1)
            print(f"{deleted_task} has been removed from your to do list.")
        else:
            print("invalid task number. ")
    except ValueError:
        print("Invalid input. please input a valid number.")


while True:
    print("\n options")
    print("1 Display to do list")
    print("2 Add task")
    print("3 Edit task")
    print("4 delete task")
    print("5 Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_list()
    elif choice == "2":
        add_item()
    elif choice == "3":
        edit_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        break
    else:
        print("invalid input, please enter a valid option.")


