import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

st.sidebar.title("Navigation")

st.markdown("<h1 style='text-align: center;'>Identify your Competition</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

def read_bases():
    columns = ['business_id', 'business_name', 'category', 'avg_rating', 'address',
       'state', 'city', 'county','%_competition','cluster_name','cluster_rating','review_count']
    df = pd.read_parquet('Data Engineering/Unification/df_restaurants.parquet',columns=columns)
    return df

df_rest = read_bases()

def loc_recommend(user_preferences):
    #relacion de categorias
    mapper = {'Cafe':0, 'Family':2, 'American':3, 'European':7, 'Asian':8,
       'Central American':10, 'Vegetarian':6, 'Fastfood':4, 'No Detail':12,
       'South American':11, 'Night':5, 'African':9, 'Breakfast':1}
    
    # generacion de dataframes basicos
    if len(county) == 0:
        df = df_rest[df_rest.state == state]
    else:
        df = df_rest[(df_rest.county.isin(county)) & (df_rest.state == state)]

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
    user_preferences = pd.merge(user_preferences.drop(columns=['category']),categories,left_index=True,right_index=True)

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
    recommended_restaurants.drop(columns=['%_competition','cluster_rating','cluster_name','review_count'],inplace=True)
    
    return recommended_restaurants

categories = df_rest.category.unique()
type = st.selectbox("Choose a restaurant type", categories)

states = df_rest.state.unique()
state = st.selectbox("Choose a restaurant type", states)

counties = df_rest[df_rest.state == state].county.unique()
county = st.multiselect('Choose counties:', counties)

numero = st.number_input("Provide an average rating:", min_value=1.0, max_value=5.0, step=0.1,value=4.8)

user_preferences = {
    'category':type,
    'avg_rating': numero}

st.dataframe(loc_recommend(user_preferences))
