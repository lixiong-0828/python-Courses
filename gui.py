import FreeSimpleGUI as gui
from module.functions import get_contents as get,write_to_file as write

gui_lable = gui.Text("Enter  add XXX(or new), del XXX(or delete), show, edit XXX, exit.")
gui_input = gui.InputText(tooltip="Input Item" , key = 'user_inpit' )
gui_add = gui.Button("Add")
gui_edit = gui.Button("Edit")
gui_delete = gui.Button("Delete")
gui_listbox = gui.Listbox(values=get() , key='list_items' ,enable_events= True , size=(50,20))

gui_layout=[[gui_lable],
            [gui_input,gui_add],
            [gui_listbox,gui_edit],
            [gui_delete]]

win = gui.Window('My Python Window',layout=gui_layout,  size=(800,600) )
while True:
    event,value = win.read()
    print(event)
    print(value)

    match event:
        case 'Add':
            # print('IN add case')
            items = get()
            input_iten = value['user_inpit']

            if(input_iten.count('\n') <1):
                items.append(f"{input_iten}\n" )
            else:
                items.append(f"{input_iten}")

            write(items )

            new_items = get()
            win['list_items'].update(new_items)

        case 'Edit':
            print("edit")
            if len(value['list_items']) > 0:
                items = get()
                input_iten = value['user_inpit']
                select_item = value['list_items'][0]
                new_item = value['user_inpit']
                print(f"select_item  :{select_item}" )
                items = get()

                index = items.index(select_item)
                print(f"index :{index}")
                if(new_item.count('\n') <1):
                    items[index] = f"{new_item}\n"
                else:
                    items[index] = f"{new_item}"
                write(items)

                new_items = get()
                win['list_items'].update(new_items)
            else:
                print("no items selected.")
        case 'Delete':
            print("Delete")
            select_item = value['list_items'][0]
            items = get()
            index = items.index(select_item)

            items.pop(index)
            write(items)
            new_items = get()
            win['list_items'].update(new_items)

        case 'list_items':
            print("list_items")
            select_item = value['list_items'][0]
            win["user_inpit"].update(select_item)
        case gui.WINDOW_CLOSED:
            break

win.close()
