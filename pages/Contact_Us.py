import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"): #component that contains other components
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    submit_Button = st.form_submit_button()
    if submit_Button:
        send_email(message)
        st.info("Your email was sent successfully")