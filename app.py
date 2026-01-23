import streamlit as st
from plagiarism import check_plagiarism

st.title("Plagiarism Checker")

text1 = st.text_area("Enter First Text")
text2 = st.text_area("Enter Second Text")

if st.button("Check Plagiarism"):
    if text1 and text2:
        result = check_plagiarism(text1, text2)
        st.success(f"Plagiarism Percentage: {result}%")

        if result > 70:
            st.error("High Plagiarism Detected")
        elif result > 40:
            st.warning("Moderate Similarity")
        else:
            st.info("Low or No Plagiarism")
    else:
        st.warning("Please enter both texts")
