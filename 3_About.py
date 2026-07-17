import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("---")

st.header("🎯 Project Objective")

st.write("""
The objective of this project is to predict whether it will rain tomorrow
using Machine Learning techniques based on historical weather data.

This dashboard demonstrates data preprocessing,
model training, evaluation, and deployment using Streamlit.
""")

st.markdown("---")

st.header("📂 Dataset")

st.write("""
**Dataset Name:** WeatherAUS

The dataset contains historical weather observations collected from multiple weather stations.

Target Variable:

**RainTomorrow**
""")

st.markdown("---")

st.header("🤖 Machine Learning Models")

st.write("""
Three Machine Learning algorithms were trained and compared:

• Logistic Regression

• Decision Tree

• Random Forest

Random Forest achieved the highest accuracy and was selected for deployment.
""")

st.markdown("---")

st.header("📊 Model Performance")

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Logistic Regression","83.60%")

with col2:
    st.metric("Decision Tree","77.95%")

with col3:
    st.metric("Random Forest","85.11%")

st.markdown("---")

st.header("🛠 Technologies Used")

st.write("""
- Python

- Pandas

- NumPy

- Matplotlib

- Seaborn

- Scikit-Learn

- Joblib

- Streamlit
""")



st.markdown("---")

st.header("🚀 Future Improvements")

st.write("""
• Live weather API integration

• Real-time prediction

• Interactive location selection

• Better visualization

• Mobile-friendly dashboard
""")

st.markdown("---")

st.success("✅ AI Weather Prediction Dashboard developed using Machine Learning and Streamlit.")