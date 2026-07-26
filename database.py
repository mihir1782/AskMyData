import sqlite3


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