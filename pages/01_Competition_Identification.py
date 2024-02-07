import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

st.sidebar.title("Navigation")

st.markdown("<h1 style='text-align: center;'>Identify your Competition</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

def read_bases():
    df_rest = pd.read_parquet('Data Engineering/Unification/Final Unifications/df_restaurants.parquet')
    df_unificado = pd.read_parquet('Data Engineering/Unification/Final Unifications/df_reduct_unified.parquet')
    
    return df_rest, df_unificado

df_rest, df_unificado = read_bases()

def loc_recommend(user_preferences):
    #relacion de categorias
    mapper = {'Cafe':0, 'Family':2, 'American':3, 'European':7, 'Asian':8,
       'Central American':10, 'Vegetarian':6, 'Fastfood':4, 'No Detail':12,
       'South American':11, 'Night':5, 'African':9, 'Breakfast':1}
    
    # generacion de dataframes basicos
    df = df_unificado[(df_unificado.county == user_preferences['county']) & (df_unificado.state == user_preferences['state'])]
    content_features = df[['avg_rating','category']]
    user_preferences = pd.DataFrame(user_preferences,index=[0])
    categories = pd.DataFrame(columns=mapper.keys())

    # mapeo de los dataframes (puede hacerse antes de la funcion)
    def map_category(category):
        return 1 if category == key else 0
    for key in mapper.keys():
        categories[key] = user_preferences['category'].map(map_category)
    for key in mapper.keys():
        content_features[key] = content_features['category'].map(map_category)
    
    # bases finales
    content_features.drop(columns='category',inplace=True)
    user_preferences = pd.merge(user_preferences.drop(columns=['category','state','county']),categories,left_index=True,right_index=True)

    # Matrices de similitud
    similarity_scores = cosine_similarity(content_features, user_preferences).flatten()
    similarity_df = pd.DataFrame({
        'business_id': df['business_id'].values,
        'Cosine': similarity_scores
    })

    # eleccion del top 5
    indices = similarity_df.sort_values(by='Cosine', ascending=False)['business_id'].drop_duplicates().values[:5]

    # toma de datos de los ids seleccionados
    recommended_restaurants = df_rest[df_rest['business_id'].isin(indices)].drop_duplicates(subset='business_id').reset_index(drop=True)
    recommended_restaurants.drop(columns=['%_competition','longitude','latitude','cluster','cluster_rating','cluster_name','review_count'],inplace=True)
    
    return recommended_restaurants

user_preferences = {
    'category':'Family',
    'state': 'Florida',
    'county':'Pinellas County',
    'avg_rating': 4.8}

st.dataframe(loc_recommend(user_preferences))
