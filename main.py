import streamlit as st
import pandas   # Going to use it for reading csv file, we could do it 
# using the with open method, but it would be a lot of work.
#test
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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) #setting collumns and scale of columns.

df = pandas.read_csv("data.csv", sep=';') #sep default is ","

with col3:
    for index, row in df[:10].iterrows(): #iterrows iter about rows in pairs.
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
    


with col4:
    for index, row in df[10:].iterrows(): #the [10:] slicer means that i'll only have in this
        # column, the rows that start in index 10, and go beyond.
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"]) #adding the image adress
        # it's important to note that, i did not have to use the backslash.