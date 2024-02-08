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
st.image("Images/Logo-NOBKG.png", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.title("Introduction")

# Introducción
st.markdown("""
We are a consultancy specialized in business feasibility, and we present our artificial intelligence system, where you can find businesses of your interest to understand the competition and get ideas!
""")

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# COMPETITION MODEL
with st.expander('Identify your Competition',expanded=True):
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

    st.link_button("Explore the Competition model", './Competition_Identification')

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

    st.link_button("Explore the Research model", './Business_Ideas')