import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Zenira", page_icon="🌸", layout="centered")

# 2. Aesthetic Customization (Pastel Colors)
st.markdown("""
    <style>
    /* Background Color (Lavender) */
    .stApp {
        background-color: #E0BBE4; 
    }
    
    /* Custom Button Styling */
    div.stButton > button:first-child {
        background-color: #FFB7CE; /* Baby Pink */
        color: #4B0082;
        border: 2px solid #FFF44F; /* Lemon Yellow Border */
        border-radius: 15px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #FFF44F; /* Lemon Yellow hover */
        border: 2px solid #B2F2BB; /* Pastel Green Border */
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #B2F2BB; /* Pastel Green */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.title("🌸 Zenira Menu")
page = st.sidebar.radio("Navigate to:", ["Home", "Learn Quest", "Day Flow", "Mind Anchor", "Book Bloom"])

# 4. Main Page Logic
if page == "Home":
    st.title("🌸 Welcome to Zenira")
    st.write("### Your aesthetic companion for focus and growth.")
    st.write("Select a module from the sidebar to begin your journey.")

elif page == "Day Flow":
    st.title("🌊 Day Flow")
    st.subheader("Discover Your Energy Pattern")
    
    # Implementing the categories we decided on: Early Bird, Night Owl, Day Spinner
    st.write("To build your perfect timetable, tell us about your rhythm:")
    
    q1 = st.selectbox("When do you feel most energetic?", 
                     ["Choose an option...", "Early Morning 🌅", "Late at Night 🦉", "Steady throughout the day 🌀"])
    
    if "Early Morning" in q1:
        st.success("You are an **Early Bird**! We'll schedule your hardest tasks for the AM.")
    elif "Late at Night" in q1:
        st.info("You are a **Night Owl**! Your peak focus time is in the evening.")
    elif "Steady" in q1:
        st.warning("You are a **Day Spinner**! A balanced, consistent routine works best for you.")

    # Audio placeholder for your .wav files
    st.write("---")
    st.write("🎵 **Ambience Player**")
    # Note: Ensure 'your_file.wav' is uploaded to the same GitHub folder
    # st.audio("your_file.wav") 

elif page == "Learn Quest":
    st.title("📚 Learn Quest")
    st.write("Your learning assistance module is ready for your notes!")
    # Add your study features here

elif page == "Mind Anchor":
    st.title("⚓ Mind Anchor")
    st.write("Take a deep breath. Focus on the present.")

elif page == "Book Bloom":
    st.title("🌻 Book Bloom")
    st.write("Track your reading and watch your knowledge grow.")import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Zenira", page_icon="🌸", layout="centered")

# 2. Aesthetic Customization (Pastel Colors)
st.markdown("""
    <style>
    /* Background Color (Lavender) */
    .stApp {
        background-color: #E0BBE4; 
    }
    
    /* Custom Button Styling */
    div.stButton > button:first-child {
        background-color: #FFB7CE; /* Baby Pink */
        color: #4B0082;
        border: 2px solid #FFF44F; /* Lemon Yellow Border */
        border-radius: 15px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #FFF44F; /* Lemon Yellow hover */
        border: 2px solid #B2F2BB; /* Pastel Green Border */
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #B2F2BB; /* Pastel Green */
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.title("🌸 Zenira Menu")
page = st.sidebar.radio("Navigate to:", ["Home", "Learn Quest", "Day Flow", "Mind Anchor", "Book Bloom"])

# 4. Main Page Logic
if page == "Home":
    st.title("🌸 Welcome to Zenira")
    st.write("### Your aesthetic companion for focus and growth.")
    st.write("Select a module from the sidebar to begin your journey.")

elif page == "Day Flow":
    st.title("🌊 Day Flow")
    st.subheader("Discover Your Energy Pattern")
    
    # Implementing the categories we decided on: Early Bird, Night Owl, Day Spinner
    st.write("To build your perfect timetable, tell us about your rhythm:")
    
    q1 = st.selectbox("When do you feel most energetic?", 
                     ["Choose an option...", "Early Morning 🌅", "Late at Night 🦉", "Steady throughout the day 🌀"])
    
    if "Early Morning" in q1:
        st.success("You are an **Early Bird**! We'll schedule your hardest tasks for the AM.")
    elif "Late at Night" in q1:
        st.info("You are a **Night Owl**! Your peak focus time is in the evening.")
    elif "Steady" in q1:
        st.warning("You are a **Day Spinner**! A balanced, consistent routine works best for you.")

    # Audio placeholder for your .wav files
    st.write("---")
    st.write("🎵 **Ambience Player**")
    # Note: Ensure 'your_file.wav' is uploaded to the same GitHub folder
    # st.audio("your_file.wav") 

elif page == "Learn Quest":
    st.title("📚 Learn Quest")
    st.write("Your learning assistance module is ready for your notes!")
    # Add your study features here

elif page == "Mind Anchor":
    st.title("⚓ Mind Anchor")
    st.write("Take a deep breath. Focus on the present.")

elif page == "Book Bloom":
    st.title("🌻 Book Bloom")
    st.write("Track your reading and watch your knowledge grow.")
