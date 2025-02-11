def get_todos():
    with open('files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


while True:
    # Get user input and strip space chars from it
    user_action = input('Type add, show or display, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
            todo = user_action[4:]

            todos = get_todos()

            todos.append(todo.capitalize() + '\n')

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

    elif  user_action.startswith('show') or  user_action.startswith('display'):

        todos = get_todos()

        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos): # new_todos for the previous two
            item = item.strip('\n').capitalize()
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Expected the number of the todo instead of a name.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number  - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print("There's no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Hey! You entered an unknown command.')

print('Bye!')