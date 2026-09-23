from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent
import streamlit as st

db = SQLDatabase.from_uri("sqlite:///my_tasks.db")
db.run(
    """create table if not exists tasks(
        id INTEGER primary key autoincrement,
        title varchar(50) not null,
        description text ,
        status text check(status in ("pending","in progress","completed")) default 'pending',
        created_at timestamp default current_timestamp
    );
    """
)

llm = ChatGroq(model = "openai/gpt-oss-120b")



sqltool = SQLDatabaseToolkit(db=db,llm = llm)
tools = sqltool.get_tools()

system_prompt = """
You are a task management assistant that interacts with a SQL database containing a 'tasks' table.

TASK RULES:
1. Limit SELECT queries to 10 results max with ORDER BY created_at DESC
2. After CREATE/UPDATE/DELETE, confirm with SELECT query
3. If the user requests a list of tasks, present the output in a structured table format to ensure a clean and organized display in the browser

CRUD OPERATIONS:
    CREATE: INSERT INTO tasks(title, description, status)
    READ: SELECT * FROM tasks WHERE ... LIMIT 10
    UPDATE: UPDATE tasks SET status=? WHERE id=? OR title=?
    DELETE: DELETE FROM tasks WHERE id=? OR title=?

Table schema: id, title, description, status(pending/in_progress/completed), created_at.
"""

@st.cache_resource
def get_agent():
   agent = create_agent(
    model = llm, 
    tools = tools,
    checkpointer= MemorySaver(),
    system_prompt= system_prompt
   )
   return agent 
 
 
agent = get_agent()

st.title("TaskB🤖t-Manage your Tasks")

if "messages" not in st.session_state:
  st.session_state.messages = []
  
  
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

prompt = st.chat_input("Ask me to manage your tasks...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    
    with st.chat_message("ai"):
        with st.spinner("Processing.."):
    
          res = agent.invoke(
          {"messages":[{"role":"user","content":prompt}]},
          {"configurable":{"thread_id":"1"}}
          )
    
          result = res["messages"][-1].content 
          st.markdown(result)
          st.session_state.messages.append({"role":"ai","content":result})
    
    