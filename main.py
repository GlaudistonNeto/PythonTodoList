# from modules.functions import get_todos, write_todos "not necessary functions. before get_todos and write_todos", but requires __init__.py inside modules directory
from modules import functions

while True:
    user_action = input('Type add, show or display, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo.capitalize() + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n').capitalize()
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print('Expected the number of the todo instead of a name.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            print(f'Todo {todo_to_remove} was removed from the list.')
        except IndexError:
            print("There's no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Hey! You entered an unknown command.')

print('Bye!')