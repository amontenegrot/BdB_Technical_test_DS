import os

import pandas as pd


def create_global_dataframes(path: str) -> None:
    """
    Reads all CSV files in a given directory and creates a global DataFrame for each.

    Parameters:
    path (str): The directory path where the CSV files are located.
    """
    filepaths = [f for f in os.listdir(path) if f.endswith('.csv')]  # Get filenames

    # Generate dataframe names
    df_names = ['df_' + fp.rstrip('.csv') for fp in filepaths]

    # Read multiples CSV
    for i in range(len(df_names)):
        globals()[df_names[i]] = pd.read_csv(
            os.path.join(path, filepaths[i]),
            encoding='latin-1'
        )
