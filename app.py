import streamlit as st
from models import get_recommendations

st.title("🔍 ML Model Chooser")
st.write("Answer a few quick questions and get ML model suggestions!")

# --- User Inputs ---
problem_type = st.selectbox("What type of problem are you solving?", 
                            ["Classification", "Regression", "Clustering", "Recommendation"])

accuracy_needed = st.radio("Do you need high accuracy?", ["Yes", "No"])
explainability = st.radio("Is explainability important?", ["Yes", "No"])
data_size = st.radio("What is the size of your dataset?", ["Small", "Medium", "Large"])

# --- Result ---
if st.button("Suggest Model"):
    models = get_recommendations(problem_type, accuracy_needed, explainability, data_size)
    st.subheader("📌 Suggested Models:")
    for m in models:
        st.markdown(f"- **{m['model']}**: {m['reason']}")
