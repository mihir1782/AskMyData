import streamlit as st
from file_handler import load_file

st.title("AI SQL RAG Chatbot")

st.write("Ask questions about your database using natural language.")

# Allow the user to upload CSV or Excel files
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

# This runs only after a file has been uploaded
if uploaded_file is not None:

    try:
        # Parse the uploaded file
        df = load_file(uploaded_file)

        st.success("File uploaded successfully!")

        # Basic information about the dataset
        st.write("### Dataset Information")

        # print(df.shape)
        # print(df.tail())

        st.write("Rows:", len(df))
        st.write("Columns:", df.shape[1])

        # Display the column names
        st.write("### Columns")
        st.write(df.columns.tolist())

        # Show the actual dataset
        st.write("### Data Preview")
        st.dataframe(df.head())

    except Exception as e:
        st.error(f"Error reading file: {e}")


question = st.text_input("Enter your question:")

if question:
    st.write("You asked:", question)