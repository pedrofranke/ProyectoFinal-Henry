import pandas as pd
import jsonlines

def analizar_datos(df):
    


    resumen_dict = {"Nombre": [], "Tipos de Datos Únicos": [], "% de Valores No Nulos": [], "% de Valores Nulos": [], "Cantidad de Valores Nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        resumen_dict["Nombre"].append(columna)
        resumen_dict["Tipos de Datos Únicos"].append(df[columna].apply(type).unique())
        resumen_dict["% de Valores No Nulos"].append(round(porcentaje_no_nulos, 2))
        resumen_dict["% de Valores Nulos"].append(round(100 - porcentaje_no_nulos, 2))
        resumen_dict["Cantidad de Valores Nulos"].append(df[columna].isnull().sum())

    resumen_dataframe = pd.DataFrame(resumen_dict)
        
    return resumen_dataframe

def cantidad_porcentaje(dataframe, columna):
    
    cantidad = dataframe.shape[0]
    cantidad_columna = dataframe[columna].value_counts(dropna=False)
    porcentaje_columna = round((cantidad_columna / cantidad) * 100, 2)
    
    print(f'Los valores de {columna}:\n{cantidad_columna.to_string(header=False)}')
    print(f'\nEl porcentaje que representa cada valor:\n{porcentaje_columna.to_string(header=False)}')

def AbrirJsonYelp(file_path):

    json_objects = []

    with jsonlines.open(file_path) as reader:
     for line in reader:
          json_objects.append(line)

    df = pd.DataFrame(json_objects)
    return df

def duplicates(DataFrame):

    if DataFrame.empty:
        print(f"El DataFrame {DataFrame} no tiene duplicados")
        return {}

    duplicates = DataFrame[DataFrame.duplicated(keep=False)]
    
    return duplicates

def nulls(DataFrame,column):

    null = DataFrame[DataFrame[column].isna()]
    null = pd.DataFrame(null)
    if null.empty:
        print(f'The column "{column}" does not have nulls')

    return null

def empty_values(DataFrame,column):

    emptys = [x for x in DataFrame[column] if x == '' or x is None]

    if not emptys:
        print(f'The column "{column}" does not have empty values')
        return None
    
    return pd.DataFrame(emptys)