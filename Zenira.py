import streamlit as st

# 1. Page Config for that Aesthetic Feel
st.set_page_config(page_title="Zenira", page_icon="🌸")

# 2. Keep the user on the right page (The Logic Fix)
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# --- THE HOME PAGE ---
if st.session_state.page == 'Home':
    st.title("🌸 Zenira")
    st.write("Welcome to your aesthetic productivity hub.")
    st.write("### Your Journey Starts Here")
    
    # These buttons appear on the main page now
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

# --- THE MODULES (Paste your specific logic below) ---

elif st.session_state.page == 'Learn Quest':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    
    st.subheader("📚 Learn Quest")
    # YOUR ORIGINAL LOGO/TEXT CODE GOES HERE
    goal = st.text_input("Enter your study goal:")
    if goal:
        # This will now STAY on the screen because of session_state
        st.success(f"Logic Triggered for: {goal}")
        # PASTE YOUR CALCULATIONS/STUDY PLAN LOGIC HERE

elif st.session_state.page == 'Day Flow':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    st.subheader("🌊 Day Flow")
    # PASTE YOUR EARLY BIRD / NIGHT OWL QUESTIONS HERE

elif st.session_state.page == 'Mind Anchor':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    # PASTE YOUR MIND ANCHOR CODE HERE

elif st.session_state.page == 'Book Bloom':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    # PASTE YOUR BOOK BLOOM CODE HERE
