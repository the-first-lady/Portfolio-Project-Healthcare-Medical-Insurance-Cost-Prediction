# main.py
import streamlit as st
import joblib
import pandas as pd

# =========================
# 1. Load pipeline (GBR Optuna)
# =========================
pipeline = joblib.load("models/gbr_optuna_pipeline.pkl")

# =========================
# 2. UI Input
# =========================
st.title("Medical Insurance Cost Prediction")
st.write("Masukkan data pasien untuk memprediksi biaya medis:")

age = st.number_input("Age", min_value=0, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# =========================
# 3. Prediksi
# =========================
if st.button("Predict"):
    # Buat dataframe input
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    # Prediksi dengan pipeline GBR Optuna
    prediction = pipeline.predict(input_data)[0]
    st.success(f"Predicted Medical Cost: ${prediction:,.2f}")
