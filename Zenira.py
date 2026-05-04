import streamlit as st

# YOUR COLORS: Lavender, Baby Pink, Lemon Yellow, Pastel Green
st.set_page_config(page_title="Zenira", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #E6E6FA; } /* Lavender Background */
    h1 { text-align: center; color: #333; font-size: 60px; }
    .stButton>button { width: 100%; height: 70px; font-size: 20px; font-weight: bold; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("ZENIRA")
st.write("### Welcome to your aesthetic productivity hub.")
st.info("Use the sidebar on the left to start your journey!")
