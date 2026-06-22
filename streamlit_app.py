import uuid
import streamlit as st
from app.rag.chain import handle_user_query

st.set_page_config(
    page_title="Netflix Movie Chatbot",
    page_icon="🎬",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = ""

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.logged_in:

    st.title("🎬 Netflix Movie Chatbot")

    name = st.text_input(
        "Enter your name"
    )

    if st.button("Login"):

        if name.strip():

            st.session_state.logged_in = True
            st.session_state.user_id = name

            st.rerun()

else:

    st.title("🎬 Netflix Movie Chatbot")

    st.sidebar.header("User")

    st.sidebar.write(
        f"Logged in as: {st.session_state.user_id}"
    )

    if st.sidebar.button("New Chat"):

        st.session_state.messages = []

        st.session_state.conversation_id = str(
            uuid.uuid4()
        )

        st.rerun()

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user_id = ""
        st.session_state.messages = []

        st.rerun()

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask about movies..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        response = handle_user_query(
            query=prompt,
            user_id=st.session_state.user_id,
            conversation_id=st.session_state.conversation_id
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):

            st.markdown(response)