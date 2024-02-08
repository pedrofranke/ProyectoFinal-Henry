import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

st.sidebar.title("Navigation")

st.markdown("<h1 style='text-align: center;'>Identify your Competition</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Introducción
st.header('Why is it important?')
with st.expander('Algo',expanded=True):
    st.subheader("Who Are Our Competitors? 🔍")
    st.write("Understanding who your competitors are is crucial for success in the restaurant industry. Our machine learning model helps you identify and analyze your competitors.")

    st.subheader("What Defines the Local Market? 🏙️")
    st.write("Every restaurant operates within a unique local market. Our model considers various factors to help you understand the dynamics of your specific market.")

    st.subheader("How Developed is the Market? 📈")
    st.write("Assessing the level of development in your market can provide valuable insights for strategic decision-making. Our model evaluates market maturity and competitiveness.")

    st.subheader("What Sets Us Apart? 🚀")
    st.write("While knowing your competitors is essential, it's equally important to understand your unique value proposition. Our model helps you identify your strengths and points of differentiation.")

    st.markdown("<hr>", unsafe_allow_html=True)
    # Call to Action
    st.subheader("Ready to Get Started?")
    st.write("Discover your competition and gain insights to drive your restaurant's success!")



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
    recommended_restaurants.drop(columns=['%_competition','cluster_rating','cluster_name','review_count','state'],inplace=True)
    showoff = ['business_name','category','avg_rating','county','city','address','business_id']
    recommended_restaurants = recommended_restaurants[showoff]
    return recommended_restaurants

# Button to Proceed to the Model
if st.button("Explore the Model"):
    # Aquí colocarías el código para ejecutar tu modelo de machine learning

    categories = df_rest.category.unique()
    type = st.selectbox("Choose a restaurant type", categories,index=3)

    states = df_rest.state.unique()
    state = st.selectbox("Choose a restaurant type", states)

    counties = df_rest[df_rest.state == state].county.unique()
    county = st.multiselect('Choose desired counties:', counties)

    numero = st.number_input("Provide an average rating:", min_value=1.0, max_value=5.0, step=0.1,value=4.8)

    user_preferences = {
        'category':type,
        'avg_rating': numero}

    rename = {'business_name':'Restaurant','category':'Category','avg_rating':'Rating','county':'County','city':'City','address':'Address'}
    result = loc_recommend(user_preferences)

    st.dataframe(result.rename(columns=rename).drop(columns='business_id'),hide_index=True)

    business_names = result.business_name

    selected_name = st.selectbox("Choose business to explore", business_names)
    copytext = result[result.business_name == selected_name].business_id.values[0]

    st.write('Reference Business ID:')
    Path = f'''{copytext}'''
    st.code(Path, language="python")

    st.link_button("Go to Business Idea Recommendations", './Business_Ideas')
