import streamlit as st

# 1. SET THE AESTHETIC COLORS (Lavender Background)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6E6FA;
    }
    </style>
    """,
    unsafe_allow_stdio=True
)

# 2. Initialize Page State
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.image("https://img.icons8.com/color/96/cherry-blossom.png", width=50) # Aesthetic Logo
    st.title("Zenira")
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

# --- MODULES WITH YOUR LOGIC ---

elif st.session_state.page == 'Learn Quest':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    
    st.header("📚 Learn Quest")
    
    # FIX: Using a form so it doesn't reset until you press the button
    with st.form("learn_form"):
        goal = st.text_input("Enter your study goal:")
        submit = st.form_submit_button("Start Quest")
        
        if submit and goal:
            # THIS IS WHERE YOUR ORIGINAL LOGIC GOES
            st.success(f"Quest Activated for: {goal}")
            if "math" in goal.lower():
                st.write("✨ Your Math Journey: Focus on Calculus and Equations today.")
            else:
                st.write(f"✨ Custom plan generated for {goal}!")

elif st.session_state.page == 'Day Flow':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    st.header("🌊 Day Flow")
    # PASTE YOUR EARLY BIRD / NIGHT OWL QUESTIONS HERE

elif st.session_state.page == 'Mind Anchor':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    st.header("⚓ Mind Anchor")
    # PASTE YOUR MIND ANCHOR CODE HERE

elif st.session_state.page == 'Book Bloom':
    if st.button("⬅️ Back to Home"):
        st.session_state.page = 'Home'
        st.rerun()
    st.header("🌸 Book Bloom")
    # PASTE YOUR BOOK BLOOM CODE HERE
