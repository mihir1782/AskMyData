import sqlite3
import pandas as pd


def create_database(df):
    """
    Creates an in-memory SQLite database
    and stores the uploaded DataFrame as a table.
    """

    # Create a temporary SQLite database in memory
    connection = sqlite3.connect(":memory:")

    # Convert the DataFrame into a SQL table called "data"
    df.to_sql(
        "data",
        connection,
        if_exists="replace",
        index=False
    )

    return connection


def validate_sql(query):
    """
    Checks whether the generated SQL is safe to execute.
    Only read-only SELECT queries are allowed.
    """

    # Remove extra spaces and convert to uppercase
    # so checks are not affected by capitalization.
    cleaned_query = query.strip().upper()

    # The query must start with SELECT.
    if not cleaned_query.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")

    # Commands that could modify the database.
    forbidden_commands = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "REPLACE"
    ]

    # Reject the query if it contains any dangerous command.
    for command in forbidden_commands:
        if command in cleaned_query:
            raise ValueError(
                f"Unsafe SQL command detected: {command}"
            )

    return True

def execute_query(connection, query):
    """
    Validates and executes an SQL query
    and returns the result as a Pandas DataFrame.
    """

    # Make sure the generated SQL is safe.
    validate_sql(query)

    # Execute the SELECT query and convert
    # the returned rows directly into a DataFrame.
    result = pd.read_sql_query(query, connection)

    return result