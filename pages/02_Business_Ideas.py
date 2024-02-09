import streamlit as st
import pandas as pd

st.sidebar.title("Navigation")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"]::before {
            content: "ConsultART";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 30px;
            position: relative;
            top: 100px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center;'>Search for Key Market Ideas</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# INTRODUCTION


# READ DATA
def read_base():
    df_rest = pd.read_parquet('Data Engineering/Unification/df_restaurants.parquet')
    df_results = pd.read_parquet('Machine Learning/df_results.parquet')
    
    return df_rest, df_results

df_rest, df_results = read_base()
showoff = ['business_name','category','avg_rating','state','county','city','address']
def get_similar_businesses(business_id):
    # eleccion del top 5
    searched_id = business_id
    related = df_results[df_results['business_id'] == searched_id].related.tolist()[0]
    result = df_rest[df_rest['business_id'].isin(related)].drop(columns=['%_competition','longitude','latitude','cluster_rating','cluster_name','review_count','cluster','postal_code'])
    result = result[showoff]
    return result

user_input = st.text_input("Enter your restaurant ID here") 

st.write('You can use 0x80c2c84fc6975997:0x69176b0c7d86d5a7 as an example')

rename = {'business_name':'Restaurant','category':'Category','state':'State','avg_rating':'Rating','county':'County','city':'City','address':'Address'}

if user_input:
    st.write('Selected Restaurant:')
    searched = df_rest[df_rest.business_id == user_input]
    searched = searched[showoff]
    st.dataframe(searched.rename(columns=rename),hide_index=True,height=80)
    result = get_similar_businesses(user_input)
    st.write('Recommended restaurants to visit:')
    st.dataframe(result.rename(columns=rename),hide_index=True,height=220)