from modules import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt, 'w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do", key='label')
input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button(
    image_source="imgs/add.png",
    key="Add", size=10,
    mouseover_colors="LightBlue2",
    tooltip="Add a new to-do")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button(
    image_source="imgs/edit.png",
    key="Edit", size=10,
    mouseover_colors="LightBlue2",
    tooltip="Edit a to-do")
complete_button = sg.Button(
    image_source="imgs/complete.png",
    key="Complete", size=10,
    mouseover_colors="LightBlue2",
    tooltip="Complete a to-do")
exit_button = sg.Button(
    image_source="imgs/exit.png",
    key="Exit", size=10,
    mouseover_colors="LightBlue2",
    tooltip="Exit the app")

layout = [
    [clock],
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
]

window = sg.Window('My To-Do App', layout=layout, font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))


    match event:
        case "Add":
            try:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todo'].update(value="")
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()