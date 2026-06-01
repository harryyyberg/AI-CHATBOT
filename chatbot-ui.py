from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

st.set_page_config(page_title="CHATBOT")
st.title("Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content='You are a helpful AI assistant')
    ]

for message in st.session_state.chat_history:
    if isinstance(message,HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    
    elif isinstance(message,AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

user_input = st.chat_input("Type your message ...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.chat_history.append(
        HumanMessage(content = user_input)
    )

    result = model.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(
        AIMessage(content = result.content)
    )

    with st.chat_message("assistant"):
        st.write(result.content)

if st.button("Clear Chat"):
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant")
    ]
    st.rerun()