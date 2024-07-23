import streamlit as st
from send_email import send_email

st.header("🤖Contact Us")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email")
    topicSelection = st.selectbox("Reason for contacting", ["Job Inquiries", "Project Proposal", "I have a suggestion", "Other"])
    raw_message = st.text_area("Your message")
    user_message = f"""\
Subject: New message from {user_email} regarding {topicSelection}

{user_email} is contacting regarding {topicSelection}:

{raw_message}
"""
    submit_button = st.form_submit_button(label="Submit")
    st.info("This will not work at the moment as the email credentials are not set up.")
    if submit_button:
        send_email(user_message)
        st.success("Your message has been sent! 🚀")