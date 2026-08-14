import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ===== Page setup =====
st.set_page_config(page_title="Blinkit Delivery Time Predictor", page_icon="🛵", layout="centered")

st.title("🛵 Blinkit Delivery Time Predictor")
st.write("Dark store se customer tak delivery time predict karo, real-time factors ke saath.")

# ===== Load saved model =====
@st.cache_resource
def load_model():
    model = joblib.load("delivery_model.pkl")
    columns = joblib.load("model_columns.pkl")
    return model, columns

model, model_columns = load_model()

# ===== Sidebar inputs =====
st.sidebar.header("Order Details Daalo")

distance = st.sidebar.slider("Dark store se distance (km)", 0.5, 20.0, 5.0, 0.5)
prep_time = st.sidebar.slider("Picking/Packing time (min)", 1, 60, 15)
courier_exp = st.sidebar.slider("Delivery partner ka experience (years)", 0.0, 15.0, 3.0, 0.5)

weather = st.sidebar.selectbox("Weather", ["Clear", "Rainy", "Foggy", "Snowy", "Windy"])
traffic = st.sidebar.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.sidebar.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.sidebar.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])

predict_btn = st.sidebar.button("Predict Delivery Time", type="primary")

# ===== Build input row matching model's expected columns =====
def build_input_row():
    row = {col: 0 for col in model_columns}
    row['Distance_km'] = distance
    row['Preparation_Time_min'] = prep_time
    row['Courier_Experience_yrs'] = courier_exp
    row['Distance_Prep_Interaction'] = distance * prep_time

    # One-hot columns: only set to 1 if this category is NOT the dropped baseline
    weather_col = f"Weather_{weather}"
    if weather_col in row:
        row[weather_col] = 1

    traffic_col = f"Traffic_Level_{traffic}"
    if traffic_col in row:
        row[traffic_col] = 1

    time_col = f"Time_of_Day_{time_of_day}"
    if time_col in row:
        row[time_col] = 1

    vehicle_col = f"Vehicle_Type_{vehicle}"
    if vehicle_col in row:
        row[vehicle_col] = 1

    return pd.DataFrame([row])[model_columns]

# ===== Main panel: prediction =====
if predict_btn:
    input_df = build_input_row()
    prediction = model.predict(input_df)[0]

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Predicted Delivery Time", f"{prediction:.0f} min")
    with col2:
        sla_target = 30
        breach = prediction > sla_target
        st.metric("SLA Status (30 min promise)", "⚠️ Delay expected" if breach else "✅ On time")

    st.divider()

    # Feature importance visual (from trained model)
    st.subheader("Ye factors prediction ko sabse zyada affect kar rahe hain")
    importance_df = pd.DataFrame({
        'Feature': model_columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False).head(6)
    st.bar_chart(importance_df.set_index('Feature'))

    st.caption("Distance aur uska preparation time ke saath interaction is model mein sabse strong predictors hain.")
else:
    st.info("Sidebar mein order details bharo aur 'Predict Delivery Time' button dabao.")

st.divider()
st.caption("Model: Random Forest Regressor (tuned) | Trained on food delivery dataset, adapted for quick-commerce context")
