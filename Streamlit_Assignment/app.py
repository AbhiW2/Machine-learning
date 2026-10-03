import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


st.set_page_config(
    page_title="Abhi's AI Chatbot",
    page_icon="🤖"
)

llm = ChatOllama(
    model="gemma3:4b",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful and friendly AI tutor.

Answer the users question in simple english language.
Give a clear explanation.
Give an example when useful.

User Question:
{question}
""")

chain = prompt | llm

st.title("Abhi's AI Chatbot")
st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])
user_question = st.chat_input("Ask me anything!")

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.write(user_question)

    response = chain.invoke({
        "question": user_question
    })


    response_text = response.content


    st.session_state.messages.append({
        "role": "assistant",
        "content": response_text
    })

    with st.chat_message("assistant"):
        st.write(response_text)