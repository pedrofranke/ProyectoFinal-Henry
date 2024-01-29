import pandas as pd

def categorizar(df,columnain,columnaout,palabra): #agrega una nueva columna categorizando segun una columna
    def ejecutor(row):
        row[columnaout] = []
        if pd.notna(row[columnain]):  # Verificar si el valor no es NaN
            if palabra.lower() in row[columnain].lower():
                row[columnaout].append(palabra)
        return row
    df.apply(ejecutor,axis=1)
    return df

def tipo_datos(df): #verifica el tipo de datos y devuelve todos los tipos de datos por cada columna y nulos
    dic = {'Columna': [], 'Tipo_datos': [], '%_nulos': [], 'Nulos': [], 'Largo':[]}
    for column in df.columns: #itera sobre columnas
        tipos_de_datos = df[column].apply(lambda x: type(x).__name__).unique() #nos devuelve sobre la columna los tipos de datos sin repeticion
        isnap = df[column].isna().sum()/df[column].shape[0]*100 # calcula el porcentaje de nans 
        isna = df[column].isna().sum() #calcula la cantidad de nans
        dic['Columna'].append(column) # adjunta datos
        dic['Tipo_datos'].append(tipos_de_datos)
        dic['Cantidad de datos'].append(df[column].shape[0])
        dic['%_nulos'].append(isnap)
        dic['Nulos'].append(isna)
    
    datf = pd.DataFrame(dic) #genera dataframe para devolver

    return datf