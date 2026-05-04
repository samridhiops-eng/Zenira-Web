import streamlit as st

# 1. Page Configuration & Theme
st.set_page_config(page_title="Zenira", page_icon="🌸", layout="centered")

# 2. Aesthetic Customization (Lavender, Baby Pink, Lemon Yellow)
st.markdown("""
    <style>
    /* Background Color (Lavender) */
    .stApp {
        background-color: #E6E6FA;
    }
    
    /* Custom Button Styling */
    div.stButton > button:first-child {
        background-color: #FFB7CE; /* Baby Pink */
        color: #4B0082; /* Deep Indigo Text */
        border: 2px solid #FFF44F; /* Lemon Yellow Border */
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }

    /* Hover effect: Lemon Yellow */
    div.stButton > button:first-child:hover {
        background-color: #FFF44F;
        border: 2px solid #FFB7CE;
        color: #000000;
    }
    </style>
    """, unsafe_allow_type=True)

# 3. Audio Implementation (Startup Sound)
# This will attempt to autoplay startup.wav from your GitHub folder
st.audio("startup.wav", format="audio/wav", autoplay=True)

# 4. Main App Interface
st.title("🌸 Zenira")
st.write("Welcome to your aesthetic productivity hub.")

# Sidebar Navigation for Modules
menu = ["Home", "Learn Quest", "Day Flow", "Mind Anchor", "Book Bloom"]
choice = st.sidebar.selectbox("Navigate Modules", menu)

if choice == "Home":
    st.subheader("Your Journey Starts Here")
    st.write("Select a module from the sidebar to begin.")

elif choice == "Day Flow":
    st.subheader("🌊 Day Flow: Routine Manager")
    st.write("Discover your energy pattern.")
    
    pattern = st.radio(
        "Which describes you best?",
        ["Early Bird (Morning Energy)", "Night Owl (Late Night Energy)", "Day Spinner (Mid-day Energy)"]
    )
    
    if st.button("Save My Pattern"):
        st.success(f"Routine updated! You are officially a {pattern}.")

elif choice == "Learn Quest":
    st.subheader("📚 Learn Quest")
    st.info("Focus mode activated. What are we studying today?")
    st.text_input("Enter your study goal:")

elif choice == "Mind Anchor":
    st.subheader("⚓ Mind Anchor")
    st.write("Take a deep breath. Focus on the lavender background.")
    if st.button("Start Meditation Timer"):
        st.write("Timer started... Stay calm.")

elif choice == "Book Bloom":
    st.subheader("📖 Book Bloom")
    st.write("Track your reading and watch your knowledge grow.")
    st.number_input("Pages read today:", min_value=0)

# Final footer to prevent syntax sticking
st.write("---")
