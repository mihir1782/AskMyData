import pandas as pd


def load_file(uploaded_file):
    """
    Reads an uploaded CSV or Excel file
    and returns it as a Pandas DataFrame.
    """

    # Get the file extension
    file_name = uploaded_file.name.lower()

    # CSV file
    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    # Excel file
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file type.")

    return df