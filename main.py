prompt = 'Type add, show or display, or exit: '

todos = []

while True:
    user_action = input(prompt)
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo.capitalize())
        case 'show' | 'display':
            for item in todos:
                item = item.capitalize()
                print(item)
        case 'exit':
            break
        case whatever_it_is:
            print('Hey! You entered an unknown command.')