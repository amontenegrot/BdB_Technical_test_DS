import os
import sqlite3

import pandas as pd

from utilities import get_path


def replace_value(df, column, old_value, new_value):
    df[column] = df[column].str.replace(old_value, new_value, regex=False)
    return df


# Environment settings
PATH = get_path()
DATA_PATH = PATH + 'data/insumo/'

# Read data
df_train = pd.read_csv(
    DATA_PATH + 'train.csv', dtype={'nr_employed': str, 'Campana': str},
    na_values=['unknown']
    )
df_test = pd.read_csv(
    DATA_PATH + 'test.csv', dtype={'nr_employed': str, 'Campana':str},
    na_values=['unknown']
    )

# Represent in lowercase only if column is categorical
cols_cat = [
    'Tipo_Trabajo', 'Estado_Civil', 'Educacion', 'mora',
    'Vivienda', 'Consumo', 'Contacto', 'Mes', 'Dia',
    'Campana', 'Resultado_Anterior', 'nr_employed'
]

for column in df_train.columns:
    if column in cols_cat:
        df_train[column] = df_train[column].str.lower()
        df_test[column] = df_test[column].str.lower()

# Manual label encoding
encode = {
    'si': 1, 'no': 0, 
    999: -1,
    'mon': 'lun', 'tue': 'mar', 'wed': 'mié', 'thu': 'jue', 'fri': 'vie',
    'jan': 'ene', 'feb': 'feb', 'mar': 'mar', 'apr': 'abr', 'may': 'may', 'jun': 'jun', 
    'jul': 'jul', 'aug': 'ago', 'sep': 'sep', 'oct': 'oct', 'nov': 'nov', 'dec': 'dic'
    }
df_train = df_train.replace(encode).infer_objects(copy=False)
df_test = df_test.replace(encode).infer_objects(copy=False)

# Define the values to be replaced in a dictionary
replace_dict = {
    'Estado_Civil': [('single', 'soltero'), ('divorced', 'divorciado')]
}

# Iterate over the columns and apply the function
for column, replacements in replace_dict.items():
    for old_value, new_value in replacements:
        df_train = replace_value(df_train, column, old_value, new_value)
        df_test = replace_value(df_test, column, old_value, new_value)

# Load to DataBase
# Assume df_train and df_test are your existing DataFrames
dataframes = {'clear_train_data': df_train, 'clear_test_data': df_test}

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
    print(f'An error occurred while loading data to the database: {str(e)}')
    if conn is not None:
        conn.rollback()
finally:
    # Close connection
    if conn is not None:
        conn.close()
        print('Database connection closed.')
