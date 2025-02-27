import streamlit as st
import send_email

st.set_page_config(page_title="Contact Me", page_icon="🗣️")

st.header("Contact Me")

with st.form(key="mail_form"):
    sender = st.text_input("Write your email")
    topic = st.text_input("Write the subject")
    message = st.text_area("Write your message")
    form_message = f"Subject: {topic}\r\n\r\nMessage: {message}\r\nEmail: {sender}"
    button = st.form_submit_button("Submit")
    if button:
        if sender != "" and topic != "" and message != "":
            send_email.email_send(form_message)
            st.info("Your mail was sent.")
        else:
            st.error("Please, fill the form correctly.")
