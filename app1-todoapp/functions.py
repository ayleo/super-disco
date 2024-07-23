FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_args)


if __name__ == "__main__":
    print("hello")
    print("hello from functions")
