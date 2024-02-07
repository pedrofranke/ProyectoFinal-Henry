import streamlit as st

st.set_page_config(page_title="Business Recommendation Model")
st.sidebar.title("Navigation")

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

st.markdown("<h1 style='text-align: center;'>Business Intelligence Consulting</h1>", unsafe_allow_html=True)
st.image("../Images/Logo-Horizontal.png", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.title("Introduction")

# Introducción
st.markdown("""
We are a consultancy specialized in business feasibility, and we present our artificial intelligence system, where you can find businesses of your interest to understand the competition and get ideas!
""")

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# Sección de dos columnas
col1, col2 = st.columns(2)

# Sección 1: Business Ideas
with col2:
    st.markdown("<h2 style='text-align: center;'>Business Ideas</h2>", unsafe_allow_html=True)
    st.markdown("The objective of this section is to recommend restaurants similar to your restaurant idea but on other locations, so that you can visit them and obtain business and design ideas.")
    st.link_button("Go to Business Idea Recommendations", './Business_Ideas')

# Sección 2: Competition
with col1:
    st.markdown("<h2 style='text-align: center;'>Competition</h2>", unsafe_allow_html=True)
    st.markdown("""

    The objective of this section is to recommend restaurants that are direct competitors according to the location and type of restaurant chosen, 
    so that the client can visit them and deepen their knowledge of the market.
    """)
    st.link_button("Go to Competition identification", './Competition_Identification')

