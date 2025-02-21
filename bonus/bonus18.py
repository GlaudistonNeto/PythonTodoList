import FreeSimpleGUI as fsg
from zip_extractor import extract_archive

fsg.theme('Black')

label1 = fsg.Text("Select archive:")
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse("Choose", key="archive")

label2 = fsg.Text("Select dest. dir.:")
input2 = fsg.Input()
choose_button2 = fsg.FileBrowse("Choose", key="folder")

extract_button = fsg.Button("Extract")
output_label = fsg.Text(key="output", text_color="green")

window = fsg.Window("Archive Extractor",
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [extract_button, output_label]])

while True:
    event, values = window.read()

    match event:
        case fsg.WIN_CLOSED:
            break

        case "Extract":
            archivepath = values["archive"]
            dest_dir = values["folder"]

            if archivepath and dest_dir:
                try:
                    extract_archive(archivepath, dest_dir)
                    window["output"].update(value="Extraction Completed!", text_color="green")
                except FileNotFoundError:
                    window["output"].update(value="Error: Archive file not found.", text_color="red")
                except PermissionError:
                    window["output"].update(value="Error: Permission denied.", text_color="red")
                except Exception as e:
                    window["output"].update(value=f"Error: {e}", text_color="red")
            else:
                window["output"].update(value="Please select both archive and destination directory.",
                                        text_color="red")

window.close()