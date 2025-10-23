import FreeSimpleGUI as gui

gui_lable_01 = gui.Text("Enter feet")
gui_lable_02 = gui.Text("Enter yard")

gui_input_01 = gui.InputText(tooltip="Enter feet")
gui_input_02 = gui.InputText(tooltip="Enter yard")

gui_button_01 = gui.Button("Add Feet")
gui_button_02 = gui.Button("Add Yard")

gui_layout = ([gui_lable_01, gui_input_01, gui_button_01],
                        [gui_lable_02, gui_input_02, gui_button_02])

win = gui.Window('My Python Window',layout=gui_layout,)
win.read()
win.close()