import sqlite3
from typing import Dict, Optional

import pandas as pd


def save_dataframe_to_sqlite(df: pd.DataFrame, table_name: str, conn: sqlite3.Connection) -> None:
    """
    Save a DataFrame to a specific table in an SQLite database.

    Parameters:
    df -- pandas DataFrame to save.
    table_name -- Name of the table in the SQLite database.
    conn -- Connection to the SQLite database.
    """
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
    except Exception as e:
        print(f"Error saving DataFrame to table {table_name}: {e}")
        raise
    finally:
        conn.commit()  # Commit changes
        conn.close()

def read_data_from_database(db_path: str, table_name: str) -> Optional[pd.DataFrame]:
    """
    Read data from a SQLite database table into a pandas DataFrame.

    Parameters:
    db_path (str): The path to the SQLite database.
    table_name (str): The name of the table in the database.

    Returns:
    Optional[pd.DataFrame]: The loaded DataFrame if successful, None otherwise.
    """
    try:
        conn = sqlite3.connect(db_path)
        consulta_sql = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(consulta_sql, conn)
        return df
    except sqlite3.Error as e:
        print(f"An error occurred while reading data from the database:\n{e}")
        return None  # Return None in case of error
    finally:
        if 'conn' in locals():
            conn.close()
            