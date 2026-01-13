import streamlit as st
import random
import time
from google import genai

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Let's start chatting! 👇"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            client = genai.Client()
            chat = client.chats.create(model="gemini-3-flash-preview")
            # Send all previous messages for context
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    chat.send_message_stream(msg["content"])  # context
            response = chat.send_message_stream(prompt)
            for chunk in response:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
                time.sleep(0.05)
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error: {e}"
            message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
