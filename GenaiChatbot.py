from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(page_title="GenAI Chatbot with Groq", page_icon="🤖", layout="centered")
st.title("🤖 GenAI Chatbot with Groq")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

llm= ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1,   
)


user_promt = st.chat_input("Ask me anything...")


if user_promt:
     st.chat_message("user").markdown(user_promt)
     st.session_state.chat_history.append({"role": "user", "content": user_promt})

     response = llm.invoke(
          input =[{"role":"system","content":"You are a helpful assistant."},*st.session_state.chat_history]
          )
     assistant_message = response.content
     st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

     with st.chat_message("assistant"):
            st.markdown(assistant_message)

