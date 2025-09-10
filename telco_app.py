import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import joblib

# Load model and preprocessor
model = joblib.load("reg_log_model_churn.pkl")
scaler = joblib.load("scaler.pkl")
cols = joblib.load("features.pkl")  # List of features used in the model

# App title
st.title("📉 Telco Customer Churn Prediction")

# Sidebar form
st.sidebar.header("🧾 Informations client")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
tenure = st.sidebar.slider("Tenure (mois)", 0, 72, 12)
MonthlyCharges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 1500.0)
Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])

# Convert to DataFrame
input_dict = {
    'gender': gender,
    'SeniorCitizen': SeniorCitizen,
    'tenure': tenure,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges,
    'Contract': Contract,
    'InternetService': InternetService,
    'PaperlessBilling': PaperlessBilling
}
input_df = pd.DataFrame([input_dict])

num=['tenure', 'MonthlyCharges', 'TotalCharges']

# Preprocessing
input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=cols, fill_value=0)
input_scaled = input_encoded.copy()
input_scaled[num] = scaler.transform(input_encoded[num])

# Predict
proba = model.predict_proba(input_scaled)[0][1]
st.subheader("🎯 Result of prediction")
st.metric(label="Probability of churn", value=f"{proba*100:.2f} %")
if proba > 0.5:
    st.warning("⚠️ This client has a **high risk** of churn.")
else:
    st.success("✅ This client has a **low risk** of churn.")
