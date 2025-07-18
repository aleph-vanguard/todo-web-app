FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as temp_file:
        temp_todos = temp_file.readlines()
    return temp_todos

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as temp_file:
        temp_file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())