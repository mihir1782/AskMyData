import streamlit as st

st.title("AI SQL RAG Chatbot")

st.write("Ask questions about your database using natural language.")

question = st.text_input("Enter your question:")

if question:
    st.write("You asked:", question)