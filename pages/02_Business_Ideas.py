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
with st.expander('Understanding Your Audience', expanded=True):
    # Preguntas y respuestas sobre la temática
    st.subheader("What is Our Target Audience? 🎯")
    st.write("Understanding your target audience is essential for effective marketing strategies. Our model helps you identify and analyze the characteristics of your audience.")

    st.subheader("How Do We Create Brand Identity? 🌟")
    st.write("Building a strong brand identity is crucial for connecting with your audience and standing out in the market. Our model provides insights and recommendations for brand development.")

    st.subheader("How Can Design Orient Us? 🎨")
    st.write("Design plays a significant role in shaping perceptions and attracting customers. Our model offers guidance on design principles and aesthetics to enhance brand appeal.")

    st.subheader("Are There Essential Attributes? 💡")
    st.write("Certain attributes are more impactful than others in influencing consumer behavior. Our model helps you identify and prioritize the key attributes for your brand.")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Llamado a la acción
    st.subheader("Ready to Connect with Your Audience?")
    st.write("Discover insights and strategies to build a strong brand and engage your target audience!")

# READ DATA
def read_base():
    df_rest = pd.read_parquet('Data Engineering/Unification/df_restaurants.parquet')
    df_results = pd.read_parquet('Machine Learning/df_results.parquet')
    
    return df_rest, df_results

df_rest, df_results = read_base()

def get_similar_businesses(business_id):
    # eleccion del top 5
    searched_id = business_id
    related = df_results[df_results['business_id'] == searched_id].related.tolist()[0]
    result = df_rest[df_rest['business_id'].isin(related)].drop(columns=['%_competition','longitude','latitude','cluster_rating','cluster_name','review_count'])
    return result

if st.button("Explore the Model"):

    user_input = st.text_input("Enter your text here")  

    if user_input:
        rename = {'business_name':'Restaurant','category':'Category','avg_rating':'Rating','county':'County','city':'City','address':'Address'}
        result = get_similar_businesses(user_input)

        st.dataframe(result.rename(columns=rename).drop(columns='business_id'),hide_index=True,height=220)
