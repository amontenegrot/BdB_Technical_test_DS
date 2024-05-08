import os
import sqlite3

import pandas as pd

from sklearn.impute import KNNImputer
from utilities import get_path, read_data_from_database


# Environment settings
PATH = get_path()
DATABASE_FOLDER = PATH + 'data/preprocessing/BANCO_BOGOTA.db'

# Read data
df_train = read_data_from_database(DATABASE_FOLDER, 'clear_train_data')
df_test = read_data_from_database(DATABASE_FOLDER, 'clear_test_data')

# Simple imputation
cols_inputation = ['Estado_Civil', 'Tipo_Trabajo', 'Educacion']

for column in cols_inputation:
    df_train[column].fillna(df_train[column].mode()[0], inplace=True)
    df_test[column].fillna(df_test[column].mode()[0], inplace=True)

# KNN imputattion
cols_inputation = ['mora', 'Vivienda', 'Consumo']

for column in cols_inputation:
       number_neighbors = len(df_train[column].dropna().unique())
       imputer = KNNImputer(n_neighbors=number_neighbors, weights='uniform')
       imputer.fit(df_train[[column]])
       df_train[column] = imputer.transform(df_train[[column]]).ravel().round()
       df_test[column] = imputer.transform(df_test[[column]]).ravel().round()  # Replace in test data

# Load to DataBase
dataframes = {'prep_train_data': df_train, 'prep_test_data': df_test}

try:
    # Create a connection to the SQLite database
    conn = sqlite3.connect(os.path.join(PATH, 'data', 'preprocessing', 'BANCO_BOGOTA.db'))

    # Iterate over the DataFrames and their corresponding table names
    for table_name, df in dataframes.items():
        # Save the DataFrame to the SQLite database
        df.to_sql(table_name, conn, index=False, if_exists='replace')

    # Commit changes
    conn.commit()
    print('Data loaded successfully to the database.')
except Exception as e:
    print(f'An error occurred while loading {table_name} to the database: {str(e)}')
    if conn is not None:
        conn.rollback()
finally:
    # Close connection
    if conn is not None:
        conn.close()
        print('Database connection closed.')
