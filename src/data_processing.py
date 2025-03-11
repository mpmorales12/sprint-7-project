import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Limpia el dataset aplicando las siguientes transformaciones:
    1. Elimina filas duplicadas
    2. Convierte los tipos de datos a los tipos correctos.
        - columna model_year: de flotante a entero
        - columna date_posted: de object a date
        - columna is_4wd: de flotante a objeto
    3. Da tratamiento a los datos ausentes.
        - columna model_year: pone los datos ausentes en 0
        - columna cylinders y odometer: no hay modificación.
        - columna paint_color: modificarlo a 'custom'.
        - columna is_4wd: modifica los ausentes a 'No' y los valores en 1.0 a 'Yes'
    4. Extrae la marca del carro de la columna 'model'.

    :param df: DataFrame de Pandas con los datos de los vehículos.
    return: DataFrame limpio
    '''

    #Eliminar filas duplicadas
    df = df.drop_duplicates()

    # Modificar valores ausentes y tipo de datos columna date_posted
    df['model_year'] = df['model_year'].fillna(0).astype(int)
    df['model_year'] = df['model_year'].replace(0,'NaN')

    # Modificar tipo de datos de la columna date_posted
    df['date_posted'] = pd.to_datetime(df['date_posted'])

    # Modificar los valores ausentes columna paint_color
    df['paint_color'] = df['paint_color'].fillna('custom')

    #Modificar los valores ausentes de la columna is_4wd
    df['is_4wd'] = df['is_4wd'].astype('object').fillna('No')
    #Modificar todos los datos a categoricos 
    df['is_4wd'] = df['is_4wd'].replace(1.0,'Yes')

    #Crear columna de brand según columna model
    df['brand'] = df['model'].apply(lambda x: x.split()[0]).str.upper()

    return df