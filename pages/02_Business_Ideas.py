'''import streamlit as st
import pickle
import gzip
import joblib
import pandas as pd

st.sidebar.title("Navigation")

st.markdown("<h1 style='text-align: center;'>Identify your Competition</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

def read_base():
    with open('raw_to_inner.pkl', 'rb') as f:
        raw_to_inner = pickle.load(f)

    with open('inner_to_raw.pkl', 'rb') as f:
        inner_to_raw = pickle.load(f)
    
    with gzip.open('modelo_knn.gz', 'rb') as f:
        knn = joblib.load(f)

    df_rest = pd.read_parquet('Data Engineering/Unification/Final Unifications/df_restaurants.parquet')
    
    return raw_to_inner, inner_to_raw, knn, df_rest

raw_to_inner, inner_to_raw, knn, df_rest = read_base()

def get_similar_businesses(business_id,cluster):
    # eleccion del top 5
    business_inner_id = raw_to_inner[business_id]
    business_similarities = knn.get_neighbors(business_inner_id, k=1000)
    
    # toma de datos de los ids seleccionados
    similar_businesses_ids = [inner_to_raw[inner_id] for inner_id in business_similarities]
    similar_businesses = df_rest[df_rest['business_id'].isin(similar_businesses_ids) & (df_rest['cluster'] == cluster)].head(5)
    similar_businesses.drop(columns=['%_competition','longitude','latitude','cluster','cluster_rating','cluster_name','review_count'],inplace=True)

    return similar_businesses

business_id = '0x88c2fd4b6db6ca95:0x5b414c5c84a4c5e0'  # business_id deseado
cluster = df_rest[df_rest['business_id'] == business_id]['cluster'].values[0]
top_recommendations = get_similar_businesses(business_id,cluster)

st.dataframe(top_recommendations)
'''