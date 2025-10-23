import FreeSimpleGUI as gui
from module.functions import get_contents as get,write_to_file as write

gui_lable = gui.Text("Enter  add XXX(or new), del XXX(or delete), show, edit XXX, exit.")
gui_input = gui.InputText(tooltip="Input Item")
gui_button = gui.Button("Add")

gui_layout=[[gui_lable],
            [gui_input,gui_button]]

win = gui.Window('My Python Window',layout=gui_layout,size=(800,600))
win.read()



win.close()