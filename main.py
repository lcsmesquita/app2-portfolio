import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2) # two columns, each one stored in a variable.

with col1:
    st.image("images\photo.png", width=500) # inserting an image in the first column

with col2:
    st.title("Lucas Mesquita") #  inserting a title in the column 2
    content = """ Hi, I am Lucas! I am a engeneering student currently at eighth semester
    in Faculdade Engenheiro Salvador Arena. I created this webpage aiming to develop my programmer
    skills. """
    st.info(content) # inserting some content on column 2 inside a filled box
    
content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me!
"""
st.write(content2)