prompt = 'Type add, show or display, edit, complete, or exit: '

todos = []

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo.capitalize())
        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.capitalize()
                row = f"{index + 1}.{item}"
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