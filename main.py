while True:
    user_action = input('Type add, show or display, edit, complete, or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo.capitalize())

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.capitalize()
                row = f"{index + 1}.{item}"
                print(row)
        case 'show' | 'display':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n').capitalize()
                row = f"{index + 1}.) {item}"
                print(row)
        case 'edit':
            number = int(input('Enter the number of todo to edit: '))
            number = number -1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        case 'complete':
            number = int(input('Enter the number of todo to complete: '))
            todos.pop(number -1)
        case 'exit':
            break
        case whatever_it_is:
            print('Hey! You entered an unknown command.')

print('Bye!')