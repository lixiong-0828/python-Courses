from unittest import case

import FreeSimpleGUI as gui
from module.zip import make_zip

gui_lable_01 = gui.Text("Enter feet")
gui_lable_02 = gui.Text("Enter yard")
gui_lable_03 = gui.Text(key='output', text_color='green')
gui_lable_04 = gui.Text(key='output', text_color='red')

gui_input_01 = gui.InputText(tooltip="Enter feet")
gui_input_02 = gui.InputText(tooltip="Enter yard")

gui_button_01 = gui.FilesBrowse("Choose_files",key="files")
gui_button_02 = gui.FolderBrowse("dest_folder",key="dest_folder")
gui_button_03 = gui.Button("Compress")

gui_layout = ([gui_lable_01, gui_input_01, gui_button_01],
                [gui_lable_02, gui_input_02, gui_button_02],
              [gui_button_03,gui_lable_03])

win = gui.Window('My Python Window',layout = gui_layout)

while True:
    event,values = win.read()
    print(event,values)
    files = values["files"].split(";")
    folder = values["dest_folder"]
    # zip_name = "compress_01.zip"

    match event:
        case 'Compress':
            print("Compress")
            make_zip(files,folder)
            win['output'].update("Compress completed!")
        case gui.WIN_CLOSED :
            break

win.close()