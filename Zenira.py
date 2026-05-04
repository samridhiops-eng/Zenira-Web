import streamlit as st

# 1. FIXED AESTHETIC STYLING
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6E6FA; /* Lavender Background */
    }
    .stButton>button {
        background-color: #FFB7CE; /* Baby Pink Buttons */
        color: #000000;
        border: 2px solid #FFF44F; /* Lemon Yellow Border */
        border-radius: 12px;
    }
    input {
        background-color: #F0FFF0 !important; /* Pastel Green Input */
        border: 1px solid #FFF44F !cite: 3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. SESSION STATE (Ensures your code doesn't reset)
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.title("🌸 Zenira")
    st.write("Welcome to your aesthetic productivity hub.")
    st.write("### Your Journey Starts Here")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📚 Learn Quest"):
            st.session_state.page = 'Learn Quest'
            st.rerun()
        if st.button("⚓ Mind Anchor"):
            st.session_state.page = 'Mind Anchor'
            st.rerun()
    with col2:
        if st.button("🌊 Day Flow"):
            st.session_state.page = 'Day Flow'
            st.rerun()
        if st.button("🌸 Book Bloom"):
            st.session_state.page = 'Book Bloom'
            st.rerun()

# --- MODULES (Running YOUR Exact Code) ---

elif st.session_state.page == 'Learn Quest':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    
    st.header("📚 Learn Quest")
    # This input will now trigger your specific subject logic
    goal = st.text_input("Enter your study goal:") 

    if goal:
        # INSERT YOUR SUBJECT LOGIC HERE (e.g., if goal == 'mathematics': ...)
        # It will only show what you have coded for that subject.
        pass

elif st.session_state.page == 'Day Flow':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    st.header("🌊 Day Flow")
    # INSERT YOUR EARLY BIRD / NIGHT OWL QUESTIONS HERE

elif st.session_state.page == 'Mind Anchor':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    # INSERT YOUR MIND ANCHOR CODE HERE

elif st.session_state.page == 'Book Bloom':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    # INSERT YOUR BOOK BLOOM CODE HERE
