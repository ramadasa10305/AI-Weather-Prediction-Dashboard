import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("weather_prediction_model.pkl")

st.title(" Rain Prediction")

st.write("Enter today's weather information to predict whether it will rain tomorrow.")

st.markdown("---")

# =====================================
# TEMPERATURE
# =====================================

with st.expander("🌡 Temperature Details", expanded=True):

    col1,col2=st.columns(2)

    with col1:
        MinTemp=st.number_input("Minimum Temperature",value=15.0)

        MaxTemp=st.number_input("Maximum Temperature",value=28.0)

    with col2:
        Temp9am=st.number_input("Temperature at 9 AM",value=20.0)

        Temp3pm=st.number_input("Temperature at 3 PM",value=25.0)

# =====================================
# HUMIDITY
# =====================================

with st.expander("💧 Humidity", expanded=True):

    col1,col2=st.columns(2)

    with col1:
        Humidity9am=st.slider("Humidity 9 AM",0,100,50)

    with col2:
        Humidity3pm=st.slider("Humidity 3 PM",0,100,50)

# =====================================
# PRESSURE
# =====================================

with st.expander("🌍 Pressure", expanded=False):

    col1,col2=st.columns(2)

    with col1:
        Pressure9am=st.number_input("Pressure 9 AM",value=1013.0)

    with col2:
        Pressure3pm=st.number_input("Pressure 3 PM",value=1013.0)

# =====================================
# WIND
# =====================================

with st.expander("🌬 Wind Information", expanded=False):

    col1,col2=st.columns(2)

    with col1:

        WindGustSpeed=st.number_input("Wind Gust Speed",value=20)

        WindSpeed9am=st.number_input("Wind Speed 9 AM",value=15)

    with col2:

        WindSpeed3pm=st.number_input("Wind Speed 3 PM",value=20)

        WindGustDir=st.number_input("Wind Gust Direction (Encoded)",value=0)

        WindDir9am=st.number_input("Wind Direction 9 AM (Encoded)",value=0)

        WindDir3pm=st.number_input("Wind Direction 3 PM (Encoded)",value=0)

# =====================================
# RAIN
# =====================================

with st.expander("🌧 Rain Information", expanded=True):

    Rainfall=st.number_input("Rainfall (mm)",value=0.0)

    RainToday=st.selectbox(
        "Rain Today",
        [0,1],
        format_func=lambda x:"No" if x==0 else "Yes"
    )
#============================================
#LOCATION
#============================================
location_dict = {
    "Adelaide": 0,
    "Albany": 1,
    "Albury": 2,
    "Alice Springs": 3,
    "Badgerys Creek": 4,
    "Ballarat": 5,
    "Bendigo": 6,
    "Brisbane": 7,
    "Cairns": 8,
    "Canberra": 9,
    "Cobar": 10,
    "Coffs Harbour": 11,
    "Dartmoor": 12,
    "Darwin": 13,
    "Gold Coast": 14,
    "Hobart": 15,
    "Katherine": 16,
    "Launceston": 17,
    "Melbourne": 18,
    "Melbourne Airport": 19,
    "Mildura": 20,
    "Moree": 21,
    "Mount Gambier": 22,
    "Mount Ginini": 23,
    "Newcastle": 24,
    "Nhil": 25,
    "Norah Head": 26,
    "Norfolk Island": 27,
    "Nuriootpa": 28,
    "Pearce RAAF": 29,
    "Penrith": 30,
    "Perth": 31,
    "Perth Airport": 32,
    "Portland": 33,
    "Richmond": 34,
    "Sale": 35,
    "Salmon Gums": 36,
    "Sydney": 37,
    "Sydney Airport": 38,
    "Townsville": 39,
    "Tuggeranong": 40,
    "Uluru": 41,
    "Wagga Wagga": 42,
    "Walpole": 43,
    "Watsonia": 44,
    "Williamtown": 45,
    "Witchcliffe": 46,
    "Wollongong": 47,
    "Woomera": 48
}

selected_location = st.selectbox(
    "📍 Select Location",
    list(location_dict.keys())
)

Location = location_dict[selected_location]

st.markdown("---")

# =====================================
# PREDICTION
# =====================================

if st.button("🌦 Predict Rain Tomorrow",use_container_width=True):

    input_data=pd.DataFrame({

        "Location":[Location],
        "MinTemp":[MinTemp],
        "MaxTemp":[MaxTemp],
        "Rainfall":[Rainfall],
        "WindGustDir":[WindGustDir],
        "WindGustSpeed":[WindGustSpeed],
        "WindDir9am":[WindDir9am],
        "WindDir3pm":[WindDir3pm],
        "WindSpeed9am":[WindSpeed9am],
        "WindSpeed3pm":[WindSpeed3pm],
        "Humidity9am":[Humidity9am],
        "Humidity3pm":[Humidity3pm],
        "Pressure9am":[Pressure9am],
        "Pressure3pm":[Pressure3pm],
        "Temp9am":[Temp9am],
        "Temp3pm":[Temp3pm],
        "RainToday":[RainToday]

    })

    prediction=model.predict(input_data)[0]

    probability=model.predict_proba(input_data)[0]

    confidence=max(probability)*100

    st.markdown("---")

    if prediction==1:

        st.error("## 🌧 Rain Expected Tomorrow")

    else:

        st.success("## ☀ No Rain Expected Tomorrow")

    st.metric("Prediction Confidence",f"{confidence:.2f}%")