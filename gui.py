from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App', layout=[[label, add_button, edit_button], [input_box]])
window.read()
window.close()