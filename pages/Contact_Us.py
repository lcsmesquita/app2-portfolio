import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"): #component that contains other components
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    submit_Button = st.form_submit_button()