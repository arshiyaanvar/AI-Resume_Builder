import streamlit as st
from app import generate_bullets

# Page config
st.set_page_config(page_title="AI Resume Builder", page_icon="📄")

# Title
st.title("📄 AI Resume Builder")
st.write("Generate professional resume bullet points using AI")

# Inputs
role = st.text_input("Enter Job Role")
level = st.selectbox("Select Experience Level", ["Fresher", "Experienced"])

# Button
if st.button("Generate Resume Points"):
    if role:
        with st.spinner("Generating..."):
            result = generate_bullets(role, level)

        st.subheader("✨ Generated Resume Points")

        for line in result.split("\n"):
            if line.strip():
                clean_line = line.strip().lstrip("0123456789. ")
                st.write(f"• {clean_line}")
    else:
        st.warning("Please enter a job role")