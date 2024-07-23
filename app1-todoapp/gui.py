import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do item")
input_box = sg.InputText(tooltip="Type in a To-Do item", key="todo")
add_button = sg.Button(button_text="Add", tooltip="Add the To-Do item to the list")
edit_button = sg.Button(button_text="Edit", tooltip="Edit the To-Do item")
complete_button = sg.Button(button_text="Complete", tooltip="Complete the To-Do item")
exit_button = sg.Button(button_text="Exit", tooltip="Exit the program")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(55, 10))


# Define the window's contents
win = sg.Window(title="My To-Do App",
                layout=[[clock],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]],
                font=('Helvetica', 20))


while True:
    event, values = win.read(timeout=10)
    match event:
        case "Add":
            todo = values["todo"].strip()
            if not todo:
                sg.popup("Please enter something, don't leave it blank.")
            else:
                try:

                    todo = values["todo"] + "\n"
                    current_todos = functions.get_todos()
                    current_todos.append(todo)
                    functions.write_todos(current_todos)
                    print(f"Added {todo} to the list")
                    win["todos"].update(values=current_todos)
                    win["todo"].update(value="")
                except ValueError:
                    sg.popup("Invalid input. Please try again.")
                    continue

        case "Edit":
            try:
                selected_todo = values["todos"][0]
                new_todo = sg.popup_get_text("Enter a new todo item")

                current_todos = functions.get_todos()
                index = current_todos.index(selected_todo)
                if not new_todo:
                    sg.popup("Please enter something, don't leave it blank.")
                    continue
                else:
                    current_todos[index] = new_todo + "\n"
                functions.write_todos(current_todos)
                win["todos"].update(values=current_todos)
                win["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a todo item to edit.", title="Error", custom_text="ok", font=('Helvetica', 14))
                continue

        case "Complete":
            try:
                selected_todo = values["todos"][0]
                current_todos = functions.get_todos()
                current_todos.remove(selected_todo)
                functions.write_todos(current_todos)
                win["todos"].update(values=current_todos)
                win["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a todo item to complete.",
                         title="Error", custom_text="ok", font=('Helvetica', 14))
                continue
        case "Exit":
            break

        case 'todos':
            win['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
    win["clock"].update(value=time.strftime("%A, %b, %d, %Y, %H:%M:%S"))

print("Exiting program.")
win.close()
