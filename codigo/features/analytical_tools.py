import pandas as pd
from sklearn import preprocessing


def label_encoder(var_encoder, encoder_name, dataframe):
    encoder_name = preprocessing.LabelEncoder()
    var_coded = var_encoder + '_ENC'
    dataframe[var_coded] = encoder_name.fit_transform(dataframe[var_encoder])