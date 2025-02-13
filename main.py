def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

while True:
    user_action = input('Type add, show or display, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos('files/todos.txt')
        todos.append(todo.capitalize() + '\n')
        write_todos('files/todos.txt', todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = get_todos('files/todos.txt')
        for index, item in enumerate(todos):
            item = item.strip('\n').capitalize()
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos('files/todos.txt')
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            write_todos('files/todos.txt', todos)
        except ValueError:
            print('Expected the number of the todo instead of a name.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos('files/todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos('files/todos.txt', todos)
            print(f'Todo {todo_to_remove} was removed from the list.')
        except IndexError:
            print("There's no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Hey! You entered an unknown command.')

print('Bye!')