# Importaciones
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns


def verificar_tipo_variable(df):
    '''
    Realiza un análisis de los tipos de datos y la presencia de valores nulos en un DataFrame.

    Esta función toma un DataFrame como entrada y devuelve un resumen que incluye información sobre
    los tipos de datos en cada columna.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene el resumen de cada columna, incluyendo:
        - 'nombre_campo': Nombre de cada columna.
        - 'tipo_datos': Tipos de datos únicos presentes en cada columna.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": []}

    for columna in df.columns:
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
    df_info = pd.DataFrame(mi_dict)
        
    return df_info

#-----------------------------------------------------------------------------------------------------

def reviews_mensuales(df):
    '''
    Crea gráficos de línea para la cantidad de reviews mensuales por año.

    Esta función toma un DataFrame que contiene datos de reviews, extrae los años únicos
    presentes en la columna 'year', y crea gráficos de línea para la cantidad de reviews por mes
    para cada año. Los gráficos se organizan en una cuadrícula de subgráficos de 2x3.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene los datos de reviews, con una columna 'year'.

    Returns:
        None
    '''
    # Definir la paleta de colores personalizada
    color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

    # Se obtiene una lista de años únicos
    años = df['year'].unique()

    # Se define el número de filas y columnas para la cuadrícula de subgráficos
    n_filas = 3
    n_columnas = 2

    # Se crea una figura con subgráficos en una cuadrícula de 2x3
    fig, axes = plt.subplots(n_filas, n_columnas, figsize=(14, 8))

    # Se itera a través de los años y crea un gráfico por año
    for i, year in enumerate(años):
        fila = i // n_columnas
        columna = i % n_columnas
        
        # Se filtran los datos para el año actual y agrupa por mes
        data_mensual = (df[df['year'] == year]
                        .groupby('month')
                        .agg({'restaurant_name':'count'}))
        
        # Se configura el subgráfico actual
        ax = axes[fila, columna]
        data_mensual.plot(ax=ax, kind='line', color=color_palette)
        ax.set_title('Año ' + str(year))  
        ax.set_xlabel('Mes')  
        ax.set_ylabel('Cantidad de Reviews')
        ax.legend_ = None
        
    # Se muestra y acomoda el gráfico
    plt.tight_layout()
    plt.show()

#------------------------------------------------------------------------------------------------

def cantidad_de_reviews_por_mes(df):
  """
  Crea un gráfico de barras que muestra la cantidad de reviews por mes.

  Esta función toma un DataFrame que contiene datos de reviews, agrupa los datos por mes
  y calcula la cantidad total de reviews por mes. Luego, crea un gráfico de barras que muestra
  la cantidad de reviews para cada mes.

  Parameters:
    df (pandas.DataFrame): El DataFrame que contiene los datos de reviews con una columna 'Mes'.

  Returns:
    None
  """

  # Definir la paleta de colores personalizada
  color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

  # Calcular la cantidad de reviews por mes
  data = df.groupby('month').agg({'restaurant_name': 'count'}).reset_index()

  # Crear el gráfico de barras
  plt.figure(figsize=(6, 4))
  ax = sns.barplot(
      data=data,
      x='month',
      y='restaurant_name',
      palette=color_palette,
  )
  ax.set_title('Cantidad de reviews por mes')
  ax.set_xlabel('Mes')
  ax.set_ylabel('Cantidad de reviews')

  # Imprimir resumen
  print(f'El mes con menor cantidad de reviews tiene {data.min()[1]} reviews')
  print(f'El mes con mayor cantidad de reviews tiene {data.max()[1]} reviews')

  # Mostrar el gráfico
  plt.show()

#---------------------------------------------------------------------------------------------

def restaurants_por_estado(df):
  """
  Esta función toma un DataFrame que contiene datos sobre restaurantes. 
  Cuenta la cantidad de restaurantes únicos por estado y crea un gráfico de tortas.

  Args:
    df(pandas.DataFrame): El DataFrame que contiene los datos de los restaurantes.

  Returns:
    El gráfico de tortas creado.
  """

  # Definir la paleta de colores personalizada
  color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

  # Cuenta la cantidad de restaurantes únicos por estado.
  count_by_state = df.groupby('state')['restaurant_name'].nunique()

  # Crea el gráfico de tortas.
  plt.pie(count_by_state, labels=count_by_state.index, autopct='%.1f%%', colors= color_palette)

  # Muestra el gráfico.
  plt.show()

#---------------------------------------------------------------------------------------------
def promedio_rating_reviews(df):
    '''
    Esta función toma un DataFrame que contiene datos sobre restaurantes.
    Devuelve un DataFrame con los promedios de rating de los restaurantes en cada estado.

    Parameters:
      df(pandas.DataFrame): El DataFrame que contiene los datos de los restaurantes.
    
    Returns:
      pandas.DataFrame: Un DataFrame que contiene:
      - state: Nombre del estado.
      - avg_rating_rest: promedio de rating de los restaurantes en cada estado.
    '''
    grouped_df = df.groupby(['state'], as_index=False)

  # Calcula el promedio de rating para cada estado.
    avg_rating_by_state = grouped_df['avg_rating_rest'].mean()

  # Crea un nuevo DataFrame con los resultados.
    df_result = avg_rating_by_state.reset_index().drop('index', axis=1) 

    return df_result

#-------------------------------------------------------------------------------------

def reviews_por_año(df):
    '''
    Esta función toma un DataFrame que contiene los datos de reseñas de usuarios en distintos restaurantes.
    Devuelve un gráfico de barras con la cantidad de reselas registradas por año.

    Parameters:
    df(pandas.DataFrame): el DataFrame que contiene los datos de reseñas.

    Returns:
    None.

    '''
    #Agrupa los datos por año.
    df_resumen = pd.DataFrame(df[['year', 'address']].groupby(['year'])['address'].count())

    cant_resenias_total = df_resumen.sum().values[0]
    cant_dias_total = 365*6
    print(f'Cantidad de reseñas promedio por día: {cant_resenias_total/cant_dias_total:.0f}')

    #Definimos la paleta de colores
    color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

    #Creamos el gráfico de barras
    plt.figure(figsize=(10,4))
    sns.barplot(data=df_resumen,x=df_resumen.index,y='address',palette=color_palette)
    plt.title('Cantidad de reseñas por año')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de reseñas [millones]')
    plt.show()

#--------------------------------------------------------------------------------------------

def precio_por_estado(df):
    # Agrupar los datos por estado y contar los valores únicos de price_numeric en cada grupo
    counts_by_state = df.groupby('state')['price_numeric'].value_counts().unstack(fill_value=0)

    # Configurar el estilo de Seaborn
    sns.set(style="whitegrid")

    # Crear una figura
    plt.figure(figsize=(20, 5))

    # Iterar sobre cada estado y crear un gráfico de barras
    for state in counts_by_state.index:
        counts = counts_by_state.loc[state]
        
        # Imprimir el total de registros para cada valor de price_numeric
        for price_numeric, total in counts.items():
            print(f"Total de registros para {state} y price_numeric {price_numeric}: {total}")
        
        plt.bar(counts.index, counts.values, label=state)

    # Configurar etiquetas y leyenda
    plt.title('Cantidad de registros por categoría de precio y estado')
    plt.xlabel('Categoría de precio')
    plt.ylabel('Cantidad de registros')
    plt.legend(title='Estado', loc='best')

    # Mostrar la figura
    plt.show()
  








