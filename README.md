<<<<<<< HEAD
# AskMyData 


### AI-Powered Natural Language to SQL Chatbot

AskMyData is an AI-powered application that lets users query CSV or Excel datasets using plain English instead of SQL. Simply upload a dataset, ask a question, and receive the query results along with an AI-generated explanation.

Built with **Python, Streamlit, Pandas, SQLite, and Google Gemini**, the project demonstrates how Large Language Models (LLMs) can simplify data exploration for users without SQL knowledge.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend application logic |
| Streamlit | Interactive web interface |
| Pandas | Data loading and preprocessing |
| SQLite | Temporary relational database |
| Google Gemini 2.5 Flash | Natural Language → SQL generation and result explanation |
| SQL | Data querying |
| python-dotenv | Secure API key management |

---

## Features

- Upload CSV or Excel datasets
- Automatically extract dataset schema
- Convert natural language into SQL queries
- Execute SQL safely on a temporary SQLite database
- Generate AI-powered explanations of query results
- User-friendly Streamlit interface
- Modular project architecture
- Secure API key management using `.env`

---

## Project Overview

Many valuable datasets are stored in spreadsheets, but querying them usually requires SQL knowledge. AskMyData removes this barrier by allowing users to ask questions in natural language. The application converts the question into SQL using Gemini, executes it on a temporary SQLite database, and returns both the results and an easy-to-understand explanation.

Example questions:

- Which product generated the highest revenue?
- Show the top 10 customers.
- What is the average salary in each department?

---

## Problem Statement

Analyzing structured data often requires SQL, making it difficult for non-technical users to explore their own datasets. This project addresses that challenge by allowing users to interact with data using plain English while automatically handling SQL generation, execution, and result explanation behind the scenes.

---

## Version 1 Scope

Version 1 focuses on building a complete end-to-end Natural Language to SQL pipeline.

Current capabilities:

- Single dataset upload
- Automatic schema extraction
- Temporary SQLite database creation
- AI-generated SQL generation
- SQL validation and execution
- AI-generated result explanations
- Interactive Streamlit interface

Planned improvements include Retrieval-Augmented Generation (RAG), conversational memory, data visualizations, multi-table support, and cloud deployment.

---

## System Architecture

```text
                           +----------------------+
                           |      User            |
                           +----------+-----------+
                                      |
                                      | Upload CSV / Excel
                                      ▼
                           +----------------------+
                           |      Pandas          |
                           |  Load & Parse File   |
                           +----------+-----------+
                                      |
                                      | Extract Schema
                                      ▼
                           +----------------------+
                           |      SQLite          |
                           | Temporary Database   |
                           +----------+-----------+
                                      ▲
                                      |
                     Execute SQL       |
                                      |
+----------------------+              |
| Natural Language     |              |
| User Question        |              |
+----------+-----------+              |
           |                          |
           ▼                          |
+----------------------+              |
| Google Gemini 2.5    |--------------+
| Generate SQL Query   |
+----------+-----------+
           |
           | Validate SQL
           ▼
+----------------------+
|  Safe SQL Query      |
+----------+-----------+
           |
           ▼
+----------------------+
| Query Results        |
+----------+-----------+
           |
           ▼
+----------------------+
| Google Gemini 2.5    |
| Explain Results      |
+----------+-----------+
           |
           ▼
+----------------------+
| Streamlit Interface  |
+----------------------+
```

### Workflow

1. Upload a CSV or Excel file.
2. Load the dataset using Pandas.
3. Create a temporary SQLite database.
4. Extract the database schema.
5. User enters a question in plain English.
6. Gemini converts the question into an SQL query.
7. The generated SQL is validated for safety.
8. SQLite executes the query.
9. Results are displayed in Streamlit.
10. Gemini generates a natural language explanation of the results.

---
## Future Improvements

### Version 2

- Support multiple tables and relationships
- Retrieval-Augmented Generation (RAG)
- Better prompt engineering for improved SQL generation
- Interactive charts and visualizations
- Query history and saved sessions

### Version 3

- PostgreSQL/MySQL support
- User authentication
- Docker containerization
- AWS deployment
- Multi-user support
- Dashboard with analytics
=======
>>>>>>> 8cf14f5 (V2 - React app + Fast API Endpoints)
