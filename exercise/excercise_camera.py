import streamlit as st
from PIL import Image
from streamlit import expander

with st.expander("strat camera:"):
    #start camera
    camera_img = st.camera_input("Camera")

if camera_img:
    #Create a pillow image instance
    img = Image.open(camera_img)

    #Convert the pillow image to grayscale
    gray_img = img.convert('L')

    # Render the origin image on web
    st.image(img)

    #Render the grayscale image on web
    st.image(gray_img)