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

def get_schema(df):
    """
    Returns user-friendly information about the DataFrame columns.
    """

    schema = []

    for column in df.columns:
        dtype = df[column].dtype

        if pd.api.types.is_integer_dtype(dtype):
            data_type = "Integer"

        elif pd.api.types.is_float_dtype(dtype):
            data_type = "Float"

        elif pd.api.types.is_bool_dtype(dtype):
            data_type = "Boolean"

        elif pd.api.types.is_datetime64_any_dtype(dtype):
            data_type = "Date/Time"

        else:
            data_type = "Text"

        schema.append({
            "Column": column,
            "Type": data_type
        })

    return pd.DataFrame(schema)