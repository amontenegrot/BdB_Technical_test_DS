import pandas as pd

from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder


def label_encoder(var_encoder: str, encoder_name: str, dataframe: DataFrame) -> None:
    """
    Encodes a categorical variable in a DataFrame using LabelEncoder.

    Args:
        var_encoder (str): The name of the categorical variable to be encoded.
        encoder_name (str): The name of the column to store the encoded values.
        dataframe (DataFrame): The DataFrame containing the variable to be encoded.

    Returns:
        None
    """
    encoder_name = LabelEncoder()
    var_coded = var_encoder + '_ENC'
    dataframe[var_coded] = encoder_name.fit_transform(dataframe[var_encoder])
