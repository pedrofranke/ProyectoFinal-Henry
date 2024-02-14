# Importaciones
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import random


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
#---------------------------------------------------------------------

def contar_nulos(df):
    """
    Cuenta la cantidad de valores nulos en cada columna del DataFrame.

    Args:
    df (pandas.DataFrame): El DataFrame para el cual se contará la cantidad de valores nulos.

    Returns:
    pandas.DataFrame: DataFrame que muestra la cantidad de valores nulos en cada columna.
    """
    return df.isna().sum().to_frame(name='cantidad_nulos')

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
                        .agg({'sentiment_analysis':'count'}))
        
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
  data = df.groupby('month').agg({'sentiment_analysis': 'count'}).reset_index()

  # Crear el gráfico de barras
  plt.figure(figsize=(6, 4))
  ax = sns.barplot(
      data=data,
      x='month',
      y='sentiment_analysis',
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

  # Filtrar el DataFrame para incluir solo los datos del año 2021
  df_2021 = df[df['year'] == 2021]

  # Definir la paleta de colores personalizada
  color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

  # Cuenta la cantidad de restaurantes únicos por estado.
  count_by_state = df_2021.groupby('state')['business_name'].nunique()

  # Crea el gráfico de tortas.
  plt.pie(count_by_state, labels=count_by_state.index, autopct='%.1f%%', colors= color_palette)

  # Muestra el gráfico.
  plt.show()
#--------------------------------------------------------------
def restaurantes_por_ciudad(dataframe):
    """
    Grafica la cantidad de restaurantes únicos por ciudad para cada estado.

    Args:
    dataframe (pandas.DataFrame): El DataFrame que contiene los datos de los restaurantes.
    """
    # Agrupar los nombres únicos de restaurantes por ciudad y estado
    restaurantes_por_ciudad = dataframe.groupby(['state', 'city'])['business_name'].nunique().reset_index()

    # Obtener la lista de estados
    estados = restaurantes_por_ciudad['state'].unique()

    # Definir paleta de colores
    color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

    # Crear subgráficos para cada estado
    fig, axs = plt.subplots(1, len(estados), figsize=(16, 6), sharey=True)

    # Generar gráfico de barras para cada estado
    for i, estado in enumerate(estados):
        datos_estado = restaurantes_por_ciudad[restaurantes_por_ciudad['state'] == estado]
        datos_estado = datos_estado.nlargest(10, 'business_name')  # Obtener las 10 primeras ciudades
        
        ax = axs[i] if len(estados) > 1 else axs  # Utilizar el mismo eje si solo hay un estado
        
        ax.bar(datos_estado['city'], datos_estado['business_name'], color=color_palette[i % len(color_palette)])
        ax.set_title(f'{estado}')
        ax.set_xlabel('Ciudad')
        ax.set_ylabel('Cantidad de Restaurantes')
        ax.tick_params(axis='x', rotation=90) #Modifica la rotación de titulos en eje x

    plt.tight_layout()  # Ajustar el espaciado entre los subgráficos
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
      - avg_rating: promedio de rating de los restaurantes en cada estado.
    '''
    grouped_df = df.groupby(['state'], as_index=False)

  # Calcula el promedio de rating para cada estado.
    avg_rating_by_state = grouped_df['avg_rating'].mean()

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
    df_resumen = pd.DataFrame(df[['year', 'sentiment_analysis']].groupby(['year'])['sentiment_analysis'].count())

    cant_resenias_total = df_resumen.sum().values[0]
    cant_dias_total = 365*6
    print(f'Cantidad de reseñas promedio por día: {cant_resenias_total/cant_dias_total:.0f}')

    #Definimos la paleta de colores
    color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

    #Creamos el gráfico de barras
    plt.figure(figsize=(10,4))
    sns.barplot(data=df_resumen,x=df_resumen.index,y='sentiment_analysis',palette=color_palette)
    plt.title('Cantidad de reseñas por año')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de reseñas')
    plt.show()

#--------------------------------------------------------------------------------------------

def calcular_moda_por_columna(df):
    '''
    Esta función toma un DataFrame con distintas columnas, calcula el valor Moda
    en cada una de ellas y devuelve otro DataFrame con los valores Moda de cada columna 
    del DataFrame original.

    Parameters:
      df(pandas.DataFrame): DataFrame que queremos analizar
    
    Returns:
      None.
    '''

    # Crear un DataFrame vacío para almacenar los valores moda por columna
    moda_por_columna = pd.DataFrame(columns=df.columns)
    
    # Iterar sobre cada columna del DataFrame original
    for columna in df.columns:
        # Calcular la moda de la columna actual
        moda = df[columna].mode()[0]
        
        # Agregar el valor moda al DataFrame de salida
        moda_por_columna[columna] = [moda]
    
    return moda_por_columna

#------------------------------------------
def competitividad_por_estado(df):
    '''
    Esta función toma un DataFrame que contiene datos sobre restaurantes.
    Devuelve un DataFrame con los promedios de competitividad de los restaurantes en cada estado.

    Parameters:
      df(pandas.DataFrame): El DataFrame que contiene los datos de los restaurantes.
    
    Returns:
      pandas.DataFrame: Un DataFrame que contiene:
      - state: Nombre del estado.
      - %_competence: promedio de competitividad de los restaurantes en cada estado.
    '''
    grouped_df = df.groupby(['state'], as_index=False)

  # Calcula el promedio de competitividad para cada estado.
    avg_competence_by_state = grouped_df['%_competence'].mean()

  # Crea un nuevo DataFrame con los resultados.
    df_result = avg_competence_by_state.reset_index().drop('index', axis=1) 

    return df_result

#----------------------------------------------------

def cant_restaurantes(dataframe):
    """
    Grafica la cantidad de restaurantes por estado y año.

    Args:
    dataframe (pandas.DataFrame): El DataFrame que contiene los datos de los restaurantes.
    """
    # Agrupar y contar la cantidad de restaurantes por estado y año.
    conteo_restaurantes = dataframe.groupby(['state', 'year'])['business_name'].nunique().unstack().fillna(0)

    # Calcular número de filas y columnas para los subgráficos
    num_graficos = len(conteo_restaurantes)
    num_filas = (num_graficos + 1) // 2  # Se suma 1 para asegurarse de que redondee hacia arriba
    num_columnas = 2

    # Definir paleta de colores
    color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

    # Crear subgráficos con la matriz especificada
    fig, axs = plt.subplots(num_filas, num_columnas, figsize=(12, 8))  # Aumentar el tamaño del gráfico

    # Crear un gráfico para cada estado
    for i, (estado, datos) in enumerate(conteo_restaurantes.iterrows()):
        fila = i // num_columnas
        columna = i % num_columnas
        ax = axs[fila, columna] if num_graficos > 1 else axs[columna]

        datos.plot(kind='line', ax=ax, color=color_palette, marker='o', linewidth=2)

        ax.set_title(f'Cantidad de Restaurantes en {estado}')
        ax.set_xlabel('Año')
        ax.set_ylabel('Cantidad de Restaurantes')

        # Añadir etiquetas de cantidad en cada punto
        for año, cantidad in datos.items():
            ax.annotate(f"{cantidad}",
                        xy=(año, cantidad),
                        xytext=(0, 5),  # Desplazamiento del texto
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=8)
        

    # Eliminar subgráficos vacíos
    for i in range(num_graficos, num_filas * num_columnas):
        fig.delaxes(axs.flatten()[i])

    plt.tight_layout()  # Ajustar el espaciado entre los subgráficos
    plt.show()

#----------------------------------------------------

def cantidad_categorias(dataframe):
    """
    Grafica las categorías más comunes por estado utilizando gráficos de torta con porcentajes.

    Args:
    dataframe (pandas.DataFrame): El DataFrame que contiene los datos de los restaurantes.
    """
    # Recuento de categorías por estado
    categorias_por_estado = dataframe.groupby('state')['category'].value_counts().reset_index(name='count')

    # Encontrar las 5 categorías más comunes por estado
    top_categorias_por_estado = categorias_por_estado.groupby('state').apply(lambda x: x.nlargest(5, 'count')).reset_index(drop=True)

    # Definir paleta de colores
    color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

    # Definir el color predeterminado para nuevas categorías
    nuevo_color = mcolors.to_hex((random.random(), random.random(), random.random()))

    # Definir las categorías y colores
    categorias = ['American', 'European', 'Central American', 'Asian', 'Family', 'No Detail', 'Cafe']

    colores_categorias = {categoria: color_palette[i] if i < len(color_palette) else nuevo_color for i, categoria in enumerate (categorias)}

    # Obtener la cantidad de filas necesarias para los subgráficos
    num_estados = len(top_categorias_por_estado['state'].unique())
    num_filas = (num_estados + 1) // 2  # Redondear hacia arriba

    # Crear subgráficos
    fig, axs = plt.subplots(num_filas, 2, figsize=(12, 4 * num_filas))
    fig.suptitle('Categorías más comunes por estado', fontsize=16)

    # Iterar sobre cada estado y generar su gráfico correspondiente
    for i, estado in enumerate(top_categorias_por_estado['state'].unique()):
        datos_estado = top_categorias_por_estado[top_categorias_por_estado['state'] == estado]
        
        # Configurar los datos para el gráfico de torta
        sizes = datos_estado['count']
        labels = datos_estado['category']
        colors = [colores_categorias[c] for c in labels]

        # Calcular los porcentajes de cada categoría
        total = sum(sizes)
        porcentajes = [100 * size / total for size in sizes]
        etiquetas = ['{0} - {1:1.1f}%'.format(label, porcentaje) for label, porcentaje in zip(labels, porcentajes)]

        # Generar el gráfico de torta
        ax = axs[i // 2, i % 2] if num_filas > 1 else axs[i]
        ax.pie(sizes, labels=etiquetas, colors=colors, autopct='', startangle=140)
        ax.set_title(estado)
        ax.axis('equal')  # Aspecto igual para asegurar que el gráfico de torta sea circular

    # Eliminar el espacio vacío del último subgráfico si es necesario
    if num_estados % 2 != 0:
        fig.delaxes(axs.flatten()[-1])

    plt.tight_layout()  # Ajustar el diseño de los subgráficos
    plt.show()

#------------------------------------------------------------

def categoria_por_condado(df, estado):
    '''
    Esta función recibe un DataFrame que contiene los datos de restaurantes por ciudad en un estado.

    Devuelve un gráfico de barras apiladas que muestra las distribución de categorias
    en las 5 ciudades más representativas del estado especificado.

    Parameters:
      df (pandas.DataFrame) : El DataFrame que contiene los datos de restaurantes.
      estado (str): El nombre del estado a analizar

    '''

    # Definir paleta de colores
    color_palette = ['#F89522', '#26AA91', '#4CB850', '#DF1F27', '#2D3E50']

    # Definir el color predeterminado para nuevas categorías
    nuevo_color = mcolors.to_hex((random.random(), random.random(), random.random()))

    # Definir las categorías y colores
    categorias = ['American', 'European', 'Central American', 'Cafe', 'Family', 'Asian']

    colores_categorias = {categoria: color_palette[i] if i < len(color_palette) else nuevo_color for i, categoria in enumerate (categorias)}
    
    #Filtramos el dataframe para obtener solo los datos del estado especificado
    df_estado = df[df['state'] == estado]

    #Obtenemos las 5 ciudades más representativas de dicho estado
    ciudades_representativas = df_estado['county'].value_counts().nlargest(5).index.tolist()

    #Filtramos el dataframe
    df_ciudades_representativas = df_estado[df_estado['county'].isin(ciudades_representativas)]

    #Calculamos la distribución de categorias por ciudad
    dist_categorias = df_ciudades_representativas.groupby(['county', 'category']).size().unstack(fill_value=0)

    #Calculamos las 5 categorias más representativas
    categ_importantes = df_ciudades_representativas.groupby('category').size().sort_values(ascending=False).nlargest(5).index.tolist()

    #Filtramos el df con las categorias más importantes
    dist_categorias = dist_categorias[categ_importantes]
    
    #Graficamos las categorias por ciudad

    dist_categorias.plot(kind='bar', stacked=True, figsize=(10, 6), color=colores_categorias)
    plt.title(f'5 categorias más populares en los 5 condados más populares de {estado}')
    plt.xlabel('Ciudad')
    plt.ylabel('Cantidad de restaurantes')
    plt.xticks(rotation=45)
    plt.legend(title='Categoria', loc='best')
    plt.tight_layout()
    plt.show()

#--------------------------------------------------

def promedio_rating_por_ciudad(df):
  """
  Esta función toma un DataFrame que contiene datos sobre restaurantes.
  Devuelve un DataFrame con el promedio de rating de los restaurantes en las 5 ciudades más representativas.

  Parameters:
    df (pandas.DataFrame): El DataFrame que contiene los datos de los restaurantes.

  Returns:
    pandas.DataFrame: Un DataFrame que contiene:
      - county: Nombre de la ciudad.
      - avg_rating: Promedio de rating de los restaurantes en cada ciudad.
  """

  # Agrupar los registros por ciudad y calcular el promedio de rating
  grouped_df = df.groupby('county')['avg_rating'].mean().sort_values(ascending=False)

  # Obtener las 7 ciudades más representativas
  ciudades_representativas = grouped_df.index.tolist()[:5]

  # Filtrar el DataFrame por las 7 ciudades más representativas
  df_ciudades_representativas = df[df['county'].isin(ciudades_representativas)]

  # Calcular el promedio de avg_rating para cada ciudad
  promedio_rating_por_ciudad = df_ciudades_representativas.groupby('county')['avg_rating'].mean().round(2)

  # Crear un nuevo DataFrame con los resultados
  df_resultado = promedio_rating_por_ciudad.reset_index()

  return df_resultado