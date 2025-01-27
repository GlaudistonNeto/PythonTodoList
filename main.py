prompt = 'Type add, show or display, edit or exit: '

todos = []

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo.capitalize())
        case 'show' | 'display':
            for item in todos:
                item = item.capitalize()
                print(item)
        case 'edit':
            number = int(input('Enter the number of todo to edit: '))
            number = number -1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        case 'exit':
            break
        case whatever_it_is:
            print('Hey! You entered an unknown command.')

print('Bye!')