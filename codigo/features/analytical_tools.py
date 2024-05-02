import pandas as pd
from sklearn.preprocessing import LabelEncoder


def label_encoder(var_encoder, encoder_name, dataframe):
    encoder_name = LabelEncoder()
    var_coded = var_encoder + '_ENC'
    dataframe[var_coded] = encoder_name.fit_transform(dataframe[var_encoder])
    