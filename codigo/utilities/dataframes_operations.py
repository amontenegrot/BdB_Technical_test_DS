import sqlite3
from typing import Dict

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
