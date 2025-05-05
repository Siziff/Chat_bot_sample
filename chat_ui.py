import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Blaze Bar Chat", page_icon="🍻")
st.title("Chat with Blaze in the Bar")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Say something to Blaze...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    try:
        response = requests.post(API_URL, json={"message": user_input})
        response.raise_for_status()
        blaze_reply = response.json()["reply"]
    except Exception as e:
        blaze_reply = "Oops, Blaze ain't feelin' it right now... Try again later!"

    st.session_state.chat_history.append(("Blaze", blaze_reply))

for sender, msg in st.session_state.chat_history:
    if sender == "You":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg)
