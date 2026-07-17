import streamlit as st
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Rain Prediction",
    page_icon="🌦",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp{
    background-color:#F4F8FB;
}

h1{
    color:#1E3A8A;
    text-align:center;
}

h2,h3{
    color:#2563EB;
}

.card{
    background:white;
    padding:18px;
    border-radius:12px;
    border:1px solid #DDE7F5;
    text-align:center;
    box-shadow:2px 2px 8px rgba(0,0,0,0.08);
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# TITLE
# ============================================================

st.title("🌦 AI Weather Prediction Dashboard")

st.subheader("Rain Forecast Module")

today = datetime.now()

st.caption(
    f" 📅 {today.strftime('%d %B %Y')} |  Model: 🤖 Random Forest |  Accuracy: 85.11%"
)

st.write("""
Welcome to the **AI Weather Prediction Dashboard**.

This project focuses on predicting whether it will rain tomorrow
using historical weather parameters and Machine Learning.

The dashboard compares multiple machine learning models and deploys
the best-performing Random Forest model to forecast rain.
""")

st.caption(
    " Trained on the WeatherAUS dataset containing weather observations from 49 locations across Australia."
)

st.info("👈 Use the navigation menu on the left to explore the Prediction, Analysis and About pages.")
st.markdown("---")

# ============================================================
# PROJECT OVERVIEW CARDS
# ============================================================

st.subheader("Project Overview")

c1,c2,c3,c4=st.columns(4)

with c1:

    st.markdown("""
    <div class="card">
    <h4>Accuracy</h4>
    <h2 style="color:#16A34A;">85.11%</h2>
    </div>
    """,unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">
    <h4>Algorithm</h4>
    <h2 style="color:#2563EB;">Random Forest</h2>
    </div>
    """,unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="card">
    <h4>Features</h4>
    <h2 style="color:#F59E0B;">17</h2>
    </div>
    """,unsafe_allow_html=True)

with c4:

    st.markdown("""
    <div class="card">
    <h4>Dataset</h4>
    <h2 style="color:#8B5CF6;">Australian Weather</h2>
    </div>
    """,unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# WORKFLOW
# ============================================================

st.subheader("⚙️ Project Workflow")

st.info("""

📂 Data Collection

⬇️

🧹 Data Cleaning & Preprocessing

⬇️

🏷️ Feature Encoding

⬇️

🤖 Model Training

⬇️

📊 Model Comparison

⬇️

🌦️ Weather Prediction

""")

st.markdown("---")

# ============================================================
# DASHBOARD PAGES
# ============================================================

st.subheader("📑 Dashboard Navigation")

col1,col2,col3=st.columns(3)

with col1:

    st.success("Prediction")

    st.write("""
    Predict whether it will rain tomorrow
    by entering today's weather conditions.
    """)

with col2:

    st.info("Analysis")

    st.write("""
    Compare machine learning models,
    feature importance and weather statistics.
    """)

with col3:

    st.warning("ℹAbout")

    st.write("""
    Learn about the project,
    dataset, technologies and future scope.
    """)

st.markdown("---")

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

Developed using ❤️ Python | Streamlit | Scikit-Learn | Pandas

</div>
""",unsafe_allow_html=True)