import os

from dotenv import load_dotenv
# google-genai = a Python package made by Google 
# SDK (Software Development Kit) = basically a library/toolkit Google gives programmers so Python code can easily communicate with Gemini.
from google import genai


# It reads .env and loads its values into the program's environment variables.
load_dotenv()

# Read our Gemini API key from .env
# uses Python's built-in os module to retrieve that environment variable.
# Environment variables are named values available in the environment where your program/process is running.
api_key = os.getenv("GEMINI_API_KEY")

# Create the Gemini client that our application
# will use to communicate with Google's Gemini API
# creates a client object. Think of client as our connection/interface for talking to Google's Gemini API.
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
    # Using this client, send my prompt to the Gemini API and ask this particular Gemini model to generate a response.
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

def generate_answer(question, result):
    """
    Uses Gemini to convert the SQL result into
    a simple natural-language answer.
    """

    # Convert the result DataFrame into text
    # so it can be included in the prompt.
    result_text = result.to_string(index=False)

    prompt = f"""
                You are a data analysis assistant.

                The user asked:

                {question}

                The SQL query returned this result:

                {result_text}

                Answer the user's question using only the provided result.

                Rules:
                1. Give a clear and concise answer.
                2. Do not mention SQL unless necessary.
                3. Do not make up information that is not in the result.
                4. Include important numbers from the result.
                5. If there are multiple rows, briefly explain the important comparison or trend.
            """

    # Send the question + SQL result to Gemini.
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    # Return only Gemini's generated answer.
    return response.text.strip()