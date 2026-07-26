import os

from dotenv import load_dotenv
from google import genai


# Load variables from the .env file
load_dotenv()

# Read our Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Create the Gemini client that our application
# will use to communicate with Google's Gemini API
client = genai.Client(api_key=api_key)


def generate_sql(question, df):
    """
    Converts the user's natural-language question
    into a SQLite SELECT query using Gemini.
    """

    # Create a description of the dataset's columns
    # so Gemini knows what data it is allowed to query.
    columns = []

    for column in df.columns:
        columns.append(
            f"{column}: {df[column].dtype}"
        )

    # Convert the list into one string.
    #
    # Example:
    # Product: object
    # Revenue: float64
    # Quantity: int64
    schema = "\n".join(columns)


    # Give Gemini the database structure,
    # user's question, and rules for generating SQL.
    prompt = f"""
You are an expert SQLite query generator.

There is one SQLite table named "data".

Its columns are:

{schema}

The user asked:

{question}

Generate a valid SQLite SELECT query that answers the question.

Rules:
1. Use only the table named data.
2. Use only columns provided in the schema.
3. Generate SQLite-compatible SQL.
4. Only generate a SELECT query.
5. Do not modify, delete, insert, or update data.
6. Return only the SQL query.
7. Do not include markdown code blocks.
"""


    # Send our prompt to Gemini.
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )


    # Gemini's response is an object containing metadata
    # and other information.
    #
    # .text extracts just the generated text.
    # .strip() removes unnecessary spaces/newlines
    # from the beginning and end.
    return response.text.strip()