import streamlit as st
from module.functions import get_contents as get,write_to_file as write

def write_to_file():
    print("Writing to file...")
    # print(st.session_state['input_item'])
    items.append(st.session_state['input_item'] + '\n')
    write(items)

def delete_from_file():
    # print("Deleting file...")
    for key in st.session_state.keys():
        if st.session_state[key] == True:
            items.remove(key)
    write(items)

items = get()

st.title("Python Web App")
st.subheader("my web app"  )
st.write("bellow items from output_file")

for item in items:
    st.checkbox(item,  key=item )

st.text_input(label="",placeholder="input new item",key="input_item" )
# st.text_area(label="",placeholder="input new item" ,key="input_items",on_change = write_to_file)

st.button(label="write_to_file",on_click=write_to_file)
st.button(label="delete_from_file",on_click=delete_from_file)

# print(st.session_state['input_items'])
# print(st.session_state['input_items'])
st.session_state