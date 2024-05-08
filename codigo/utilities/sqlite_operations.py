import sqlite3
from typing import Optional

import pandas as pd


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
            