from dotenv import load_dotenv
load_dotenv()


from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st
llm = ChatGroq(model="openai/gpt-oss-120b")

st.title("R🤖Bot - A Q&A Chatbot")
st.markdown("This is a simple Q&A chatbot built by 𝐇𝐚𝐦𝐳𝐚. Ask any question and get an answer!")

search = GoogleSerperAPIWrapper()



@st.cache_resource
def get_agent():
    agents = create_agent(
        model = llm,
        tools = [search.run],
        system_prompt = "you are a agent who can fetch data from google",
        checkpointer= MemorySaver()
    )
    return agents

agent = get_agent()

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
    
    res = agent.invoke({"messages":[{"role":"user","content":query}]},
                       {"configurable":{"thread_id":"1"}})
    result = res["messages"][-1].content
    st.session_state.messages.append({"role": "assistant", "content": result})
    st.chat_message("assistant").markdown(result)


