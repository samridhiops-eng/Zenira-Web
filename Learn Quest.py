import streamlit as st

st.markdown("<style>.stApp { background-color: #FFB7CE; }</style>", unsafe_allow_html=True) # Baby Pink
st.header("📚 Learn Quest")

# THIS IS YOUR CODE: It will now wait for your input properly
goal = st.text_input("Enter your study goal (e.g., Mathematics):")

if goal:
    # INSERT YOUR EXACT SUBJECT LOGIC HERE
    if "math" in goal.lower():
        st.write("### Mathematics Plan")
        st.write("1. Practice Algebra\n2. Review Geometry")
    else:
        st.success(f"Custom plan generated for: {goal}")
