import streamlit as st
import send_email

st.set_page_config(page_title="Contact Me", page_icon="🗣️")

st.header("Contact Me")

# with st.form(key="mail_form"):
#     sender = st.text_input("Write your email")
#     topic = st.text_input("Write the subject")
#     message = st.text_area("Write your message")
#     form_message = f"Subject: {topic}\r\n\r\nMessage: {message}\r\nEmail: {sender}"
#     button = st.form_submit_button("Submit")
#     if button:
#         if sender != "" and topic != "" and message != "":
#             send_email.email_send(form_message)
#             st.info("Your mail was sent.")
#         else:
#             st.error("Please, fill the form correctly.")

custom_css = """
<style>
    form {
        max-width: 400px;
        margin: auto;
        padding: 20px;
        background: #fff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: Arial, sans-serif;
    }

    label {
        font-weight: bold;
        display: block;
        margin-top: 10px;
    }

    input, textarea {
        width: 100%;
        padding: 10px;
        margin-top: 5px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 14px;
        resize: none;
    }

    button {
        width: 100%;
        padding: 10px;
        margin-top: 15px;
        background: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }

    button:hover {
        background: #0056b3;
    }
</style>
"""

form_html = """
<form action="https://formspree.io/f/mrbewnkp" method="POST">
    <label>Email:</label>
    <input type="email" name="email" required><br><br>

    <label>Subject:</label>
    <input type="text" name="subject" required><br><br>

    <label>Message:</label>
    <textarea name="message" rows="4" required></textarea><br><br>

    <button type="submit">Send</button>
</form>
"""

st.html(custom_css)
st.html(form_html)
