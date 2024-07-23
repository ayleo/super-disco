import functions
import time

now = time.strftime("%A, %b, %d, %Y, %H:%M:%S")
print("Current time is", now)


while True:
    user_action = input("What would you like to do? (add, view, edit, complete or exit) ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todo_list = functions.get_todos()

        todo_list.append(todo + "\n")

        functions.write_todos(todo_list)

    elif user_action.startswith("view"):
        todo_list = functions.get_todos()

        for i, item in enumerate(todo_list):
            item = item.title().strip('\n')
            listItems = f"{i + 1}. {item}"
            print(listItems)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todo_list = functions.get_todos()

            new_todo = input("Enter a new todo item: ")
            todo_list[number] = new_todo + "\n"

            functions.write_todos(todo_list)
        except ValueError:
            print("Invalid input. Please try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            listNumber = int(user_action[9:])

            todo_list = functions.get_todos()
            
            index = listNumber - 1
            todo_to_complete = todo_list[listNumber - 1].strip("\n")
            todo_list.pop(index)

            functions.write_todos(todo_list)

            userMessage = f"Item {todo_to_complete} has been completed."
            print(userMessage)
        except IndexError:
            print("Invalid input. Out of range. Please try again.")
            continue
    elif user_action.startswith("exit"):
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please try again.")
        
        