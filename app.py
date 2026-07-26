import streamlit as st
from file_handler import load_file, get_schema
from database import create_database

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
        connection = create_database(df)
        test_query = "SELECT * FROM data LIMIT 5"

        result = connection.execute(test_query).fetchall()

        st.write("### SQLite Test")
        st.write(result)

        schema = get_schema(df)

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

        # display schema
        st.write("### Dataset Schema")

        schema = get_schema(df)
        st.dataframe(schema, hide_index=True, use_container_width=True)

        # Show the actual dataset
        st.write("### Data Preview")
        st.dataframe(df.head())

    except Exception as e:
        st.error(f"Error reading file: {e}")


question = st.text_input("Enter your question:")

if question:
    st.write("You asked:", question)