import streamlit as st

# 1. STYLE: Individual colors for each button
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    /* Learn Quest - Pink */
    div[data-testid="stVerticalBlock"] > div:nth-child(2) button { background-color: #FFB7CE !important; }
    /* Day Flow - Yellow */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) button { background-color: #FFF44F !important; }
    /* Mind Anchor - Green */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) button { background-color: #B2FACD !important; }
    /* Book Bloom - Lavender */
    div[data-testid="stVerticalBlock"] > div:nth-child(5) button { background-color: #E6E6FA !important; }
    
    .stButton > button { width: 100%; height: 60px; font-weight: bold; color: #4B0082; border: none; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIC: Maintain the current module state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("<h1 style='text-align: center;'>ZENIRA</h1>", unsafe_allow_html=True)
    
    if st.button("LEARN QUEST"):
        st.session_state.page = 'Learn Quest'
        st.rerun()

    if st.button("DAY FLOW"):
        st.session_state.page = 'Day Flow'
        st.rerun()

    if st.button("MIND ANCHOR"):
        st.session_state.page = 'Mind Anchor'
        st.rerun()

    if st.button("BOOK BLOOM"):
        st.session_state.page = 'Book Bloom'
        st.rerun()

# --- MODULES: PASTE YOUR QUESTIONS HERE ---

elif st.session_state.page == 'Learn Quest':
    if st.button("⬅ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    
    st.header("📚 Learn Quest")
    # PASTE YOUR SUBJECT SELECTION CODE HERE
    goal = st.text_input("Enter your study goal:")
    if goal:
        # Put your logic for 'mathematics' etc. right here
        st.write(f"Quest activated for {goal}")

elif st.session_state.page == 'Day Flow':
    if st.button("⬅ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    
    st.header("🌊 Day Flow")
    # PASTE YOUR EARLY BIRD / NIGHT OWL QUESTIONS HERE
