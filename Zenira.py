import streamlit as st

# 1. FIX THE COLOR (Lavender Background)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6E6FA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Initialize Page State
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# --- THE HOME PAGE ---
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

# --- THE MODULES (Logic Persistence Fixed) ---

elif st.session_state.page == 'Learn Quest':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    
    st.header("📚 Learn Quest")
    
    # This keeps your code running correctly
    goal = st.text_input("Enter your study goal (e.g., Mathematics):")
    if goal:
        st.success(f"Quest Started for: {goal}")
        # --- PASTE YOUR REMAINING MATH LOGIC HERE ---
        st.info("Now showing your custom study plan...")

elif st.session_state.page == 'Day Flow':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    st.header("🌊 Day Flow")
    # --- PASTE YOUR EARLY BIRD/NIGHT OWL QUESTIONS HERE ---

elif st.session_state.page == 'Mind Anchor':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    # --- PASTE YOUR MIND ANCHOR CODE HERE ---

elif st.session_state.page == 'Book Bloom':
    if st.button("⬅️ Back"):
        st.session_state.page = 'Home'
        st.rerun()
    # --- PASTE YOUR BOOK BLOOM CODE HERE ---
