def get_todos(filepath='files/todos.txt'):
    """ Read a text and return the list
        of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='files/todos.txt'):
    """ Write the to-do items list
        in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

while True:
    user_action = input('Type add, show or display, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo.capitalize() + '\n')
        write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n').capitalize()
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print('Expected the number of the todo instead of a name.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
            print(f'Todo {todo_to_remove} was removed from the list.')
        except IndexError:
            print("There's no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Hey! You entered an unknown command.')

print('Bye!')