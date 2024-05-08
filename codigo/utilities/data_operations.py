from pandas import DataFrame


def replace_value(df: DataFrame, column: str, old_value: str, new_value: str) -> DataFrame:
    """
    Replace a specific value in a DataFrame column with a new value.

    Args:
        df (DataFrame): The DataFrame containing the column to be modified.
        column (str): The name of the column to be modified.
        old_value (str): The value to be replaced.
        new_value (str): The new value to replace the old value.

    Returns:
        DataFrame: The modified DataFrame with the specified value replaced.
    """
    df[column] = df[column].str.replace(old_value, new_value, regex=False)
    return df
