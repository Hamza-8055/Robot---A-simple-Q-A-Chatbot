# 🤖 GenAI Chatbot using LangChain, Streamlit & Groq

A simple and interactive **Generative AI chatbot** built with **Python, LangChain, Streamlit, and Groq LLMs**. This project demonstrates how to integrate a Large Language Model (LLM) into a web application and manage conversational interactions using LangChain and Streamlit session state.

---

## 📌 Overview

This project is designed to provide hands-on experience with the fundamentals of **Generative AI application development**.

The application uses **Groq's high-speed LLM inference** to generate responses, while **LangChain** is used to structure the interaction between the application and the language model. **Streamlit** provides a simple and interactive chat-based user interface.

The project also maintains the conversation history during the user's session, allowing the chatbot to respond based on previous messages.

---

## ✨ Features

* 🤖 AI-powered conversational chatbot
* ⚡ Fast response generation using Groq LLM
* 🔗 LangChain integration
* 💬 Interactive Streamlit chat interface
* 🧠 Conversation history management
* 🔄 Session-based message persistence
* 📝 Prompt-based interaction with the LLM
* 🔐 Secure API key management using `.env`
* 🐍 Built entirely with Python

---

## 🛠️ Technologies Used

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| **Python**        | Core programming language       |
| **LangChain**     | LLM application framework       |
| **Groq**          | Fast LLM inference              |
| **Streamlit**     | Web-based user interface        |
| **python-dotenv** | Environment variable management |

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
Conversation / Session State
  │
  ▼
LangChain
  │
  ▼
Groq LLM
  │
  ▼
Generated Response
  │
  ▼
Streamlit UI
```

---

## 📂 Project Structure

```text
GenAI-Project/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .env                    # API keys and environment variables
├── .gitignore              # Files excluded from Git
└── README.md               # Project documentation
```

> **Note:** File names may vary depending on your implementation.

---

## ⚙️ How It Works

### 1. User Input

The user enters a message through the Streamlit chat interface.

### 2. Session State

Streamlit's session state is used to store the conversation history during the current session.

This allows the application to maintain previous messages instead of displaying only the latest interaction.

### 3. LangChain

LangChain manages the interaction between the application and the LLM.

It can be used to construct prompts, manage messages, and connect different components of an LLM application.

### 4. Groq LLM

The user's prompt and relevant conversation history are sent to the selected Groq-hosted language model.

The model processes the input and generates a response.

### 5. Response Display

The generated response is returned to the Streamlit application and displayed in the chat interface.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.9+
* pip
* Git
* A Groq API key

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone  https://github.com/Hamza-8055/Robot---A-simple-Q-A-Chatbot.git
```

Navigate into the project directory:

```bash
cd YOUR_REPOSITORY
```

---

### 2. Create a Virtual Environment

```bash
python -m venv env
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\env\Scripts\Activate.ps1
```

**Windows CMD:**

```cmd
env\Scripts\activate
```

**Linux / macOS:**

```bash
source env/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual Groq API key.

### ⚠️ Important

**Never upload your `.env` file or API keys to GitHub.**

Add the following to your `.gitignore`:

```text
.env
env/
__pycache__/
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

If it doesn't open automatically, Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

---

## 💬 Example Interaction

```text
User:
What is Generative AI?

AI:
Generative AI refers to artificial intelligence systems
that can generate new content such as text, images, code,
audio, and other forms of data based on learned patterns.
```

The chatbot can continue the conversation while maintaining the messages stored in the current Streamlit session.

---

## 🧠 Concepts Learned

This project helped explore several important Generative AI concepts:

* Large Language Models (LLMs)
* Prompt Engineering
* Tokenization
* Chat-based LLM interaction
* LangChain fundamentals
* Message handling
* Conversation history
* Streamlit Session State
* API integration
* Environment variables
* LLM application architecture

---

## 🔮 Future Improvements

The project can be extended with more advanced GenAI capabilities:

* 📚 Retrieval-Augmented Generation (RAG)
* 📄 PDF/document question answering
* 🗄️ Vector databases
* 🔍 Semantic search
* 🤖 AI agents
* 🛠️ Tool calling
* 🌐 Web search integration
* 💾 Persistent conversation history
* 👤 User authentication
* 🎙️ Voice-based interaction
* 🧩 Structured outputs
* 📊 LLM evaluation and monitoring

---

## 🎯 Learning Objective

The goal of this project is to understand how **LLMs can be integrated into real-world applications** rather than using them only through standalone chat interfaces.

It provides a foundation for building more advanced applications involving:

```text
LLM
 ↓
LangChain
 ↓
Prompt Engineering
 ↓
RAG
 ↓
Vector Database
 ↓
AI Agents
 ↓
Tool Calling
 ↓
Production GenAI Applications
```

---

## 👨‍💻 Author

**Abu Hamza**

Computer Science & Engineering Student

Interested in:

* Java & Spring Boot
* Python
* Backend Development
* Generative AI
* LangChain
* RAG
* AI Agents
* Cloud & DevOps

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub!
