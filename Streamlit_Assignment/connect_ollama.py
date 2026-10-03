import streamlit as st
from langchain_ollama import ChatOllama

st.set_page_config(
    page_title="Abhi's AI Chatbot",
    page_icon="🤖"
)

llm = ChatOllama(
    model="gemma3:4b"
)

st.title("Abhi's AI Chatbot")