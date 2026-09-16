from dotenv import load_dotenv
load_dotenv()


from langchain_groq import ChatGroq
import streamlit as st
llm = ChatGroq(model="openai/gpt-oss-120b")

st.title("R🤖Bot - A Q&A Chatbot")
st.markdown("This is a simple Q&A chatbot built by 𝐇𝐚𝐦𝐳𝐚. Ask any question and get an answer!")

query = st.chat_input("Ask a question...")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    
    res = llm.invoke(query)
    st.session_state.messages.append({"role": "assistant", "content": res.content})
    st.chat_message("assistant").markdown(res.content)


