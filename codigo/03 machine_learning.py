import os
import sqlite3

import pandas as pd
from pycaret.classification import *

# from sklearn.preprocessing import LabelEncoder
from features import label_encoder
from utilities import get_path, read_data_from_database


# Environment settings
PATH = get_path(2)
DATABASE_FOLDER = PATH + 'data/preprocessing/BANCO_BOGOTA.db'



# from typing import Optional
# from pathlib import Path
# from pandas import DataFrame
# from sklearn.preprocessing import LabelEncoder
# from pycaret.classification import *


# Environment settings
PATH = get_path()
DATABASE_FOLDER = PATH + 'data/preprocessing/BANCO_BOGOTA.db'

# Read data
df_train = read_data_from_database(DATABASE_FOLDER, 'prep_train_data')
df_test = read_data_from_database(DATABASE_FOLDER, 'prep_test_data')

# Label encoder
labels_to_encoders_name = {
    'Tipo_Trabajo':'Tipo_Trabajo_ENC',
    'Estado_Civil':'Estado_Civil_ENC',
    'Educacion':'Educacion_ENC',    
    'Contacto':'Contacto_ENC',
    'Mes':'Mes_ENC',
    'Dia':'Dia_ENC',
    'Resultado_Anterior':'Resultado_Anterior_ENC'
    }

for var_encoder, encoder_name in labels_to_encoders_name.items():
    label_encoder(var_encoder, encoder_name, df_train)
    label_encoder(var_encoder, encoder_name, df_test)



# Auto Machine Learning
df_new = df_train[[
    'Tipo_Trabajo_ENC', 'Estado_Civil_ENC',
    'mora', 'Vivienda', 'Consumo', 'Contacto_ENC',
    'Dias_Ultima_Camp', 'No_Contactos',
    'emp_var_rate', 'cons_price_idx', 'cons_conf_idx',
    'euribor3m', 'y'
    ]].copy()

data = df_new.sample(frac=0.8, random_state=0)
data_unseen = df_train.drop(data.index)

data.reset_index(inplace=True, drop=True)
data_unseen.reset_index(inplace=True, drop=True)
print(f'Datos para modelar: {data.shape}; y datos para predecir: {data_unseen.shape}')

model_setup = setup(data=data, target='y')

best_models = compare_models()

ada = create_model('ada')

tuned_ada = tune_model(ada)

unseen_predictions = predict_model(tuned_ada, data=data_unseen)

final_ada = finalize_model(tuned_ada)

# Save model
save_model(final_ada, PATH + 'data/salida/ADA_model_08-05-2024')

# Deploy
ada_model = load_model(PATH + 'data/salida/ADA_model_08-05-2024')

df_implement = predict_model(ada_model, data=df_test)
df_implement = df_implement.rename({
    'prediction_label':'y'
    }, axis=1)

# Load to DataBase
try:
    # Create a connection to the SQLite database
    conn = sqlite3.connect(os.path.join(PATH, 'data', 'preprocessing', 'BANCO_BOGOTA.db'))

    df_implement.to_sql(
    'Result_TechnicalTest_DS_AMT', conn, index=False, if_exists='replace'    
    )
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

del df_train, df_test, df_new, df_implement  # Delete variables to free memory
