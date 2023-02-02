FILEPATH = "todolist.txt"


def get_todolist(filepath=FILEPATH):
    """Read a text file and return a list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todolist_local = file_local.readlines()
    return todolist_local


def write_todolist(todolist_arg, filepath=FILEPATH):
    """Write a to-do list item in a text file"""
    with open(filepath, "w") as file:
        file.writelines(todolist_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todolist())
