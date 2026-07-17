import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analysis", page_icon="📊", layout="wide")

st.title("📊 Weather Prediction Analysis Dashboard")

st.write("This page compares machine learning models and visualizes important weather data.")

st.markdown("---")

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("Encoded_WeatherAUS.csv")

# ==========================
# Dataset Summary
# ==========================

st.subheader("📂 Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Rows", df.shape[0])

with c2:
    st.metric("Columns", df.shape[1])

with c3:
    st.metric("Features Used", "17")

with c4:
    st.metric("Best Accuracy", "85.11%")

st.markdown("---")

# ==========================
# Model Comparison
# ==========================

st.subheader("🏆 Machine Learning Model Comparison")

comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy (%)": [
        83.60,
        77.95,
        85.11
    ],
    "Result": [
        "Good",
        "Average",
        "Best"
    ]
})

st.dataframe(comparison, use_container_width=True)

st.markdown("---")

# ==========================
# Accuracy Graph
# ==========================

st.subheader("📈 Accuracy Comparison")

fig, ax = plt.subplots(figsize=(7,4))

colors = ["#3B82F6","#F59E0B","#10B981"]

ax.bar(
    comparison["Model"],
    comparison["Accuracy (%)"],
    color=colors,
    edgecolor="black"
)

ax.set_ylabel("Accuracy (%)")
ax.set_ylim(70,90)
ax.grid(axis="y", alpha=0.3)

st.pyplot(fig)

st.markdown("---")

# ==========================
# Feature Importance
# ==========================

st.subheader("⭐ Top Feature Importance")

importance = pd.DataFrame({

"Feature":[
"Humidity3pm",
"Pressure3pm",
"Humidity9am",
"Pressure9am",
"WindGustSpeed",
"Rainfall",
"Temp3pm",
"MinTemp",
"MaxTemp",
"Temp9am"
],

"Importance":[
0.195949,
0.070793,
0.067603,
0.064684,
0.061602,
0.059927,
0.059029,
0.057881,
0.056594,
0.053639
]

})

importance = importance.sort_values(
    by="Importance",
    ascending=True
)

fig2, ax2 = plt.subplots(figsize=(8,5))

ax2.barh(
    importance["Feature"],
    importance["Importance"],
    color="#2563EB",
    edgecolor="black"
)

ax2.set_xlabel("Importance Score")
ax2.grid(alpha=0.3)

st.pyplot(fig2)

st.markdown("---")

# ==========================
# TWO CHARTS
# ==========================

col1,col2 = st.columns(2)

with col1:

    st.subheader("🌧 Rain Tomorrow Distribution")

    fig3,ax3 = plt.subplots(figsize=(5,5))

    colors=["#60A5FA","#34D399"]

    df["RainTomorrow"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        colors=colors,
        explode=(0.03,0.08),
        shadow=True,
        ax=ax3
    )

    ax3.set_ylabel("")

    st.pyplot(fig3)

with col2:

    st.subheader("🌡 Max Temperature Distribution")

    fig4,ax4 = plt.subplots(figsize=(6,5))

    ax4.hist(
        df["MaxTemp"],
        bins=20,
        color="#F97316",
        edgecolor="black"
    )

    ax4.grid(alpha=0.3)

    ax4.set_xlabel("Maximum Temperature")

    st.pyplot(fig4)

st.markdown("---")

# ==========================
# TWO MORE CHARTS
# ==========================

col3,col4 = st.columns(2)

with col3:

    st.subheader("💧 Humidity at 3 PM")

    fig5,ax5 = plt.subplots(figsize=(6,5))

    ax5.hist(
        df["Humidity3pm"],
        bins=20,
        color="#10B981",
        edgecolor="black"
    )

    ax5.grid(alpha=0.3)

    ax5.set_xlabel("Humidity")

    st.pyplot(fig5)

with col4:

    st.subheader("🌧 Rainfall Distribution")

    fig6,ax6 = plt.subplots(figsize=(6,5))

    ax6.hist(
        df["Rainfall"],
        bins=20,
        color="#8B5CF6",
        edgecolor="black"
    )

    ax6.grid(alpha=0.3)

    ax6.set_xlabel("Rainfall")

    st.pyplot(fig6)

st.markdown("---")

# ==========================
# Final Conclusion
# ==========================

st.success("""
### ✅ Conclusion

• Three machine learning models were trained and compared.

• Logistic Regression Accuracy : **83.60%**

• Decision Tree Accuracy : **77.95%**

• Random Forest Accuracy : **85.11%**

Random Forest achieved the highest accuracy and was selected for deployment in the dashboard.
""")