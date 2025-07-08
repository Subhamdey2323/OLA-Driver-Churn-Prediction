import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

# Load trained model
with open("ola_classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

# Title and Description
st.set_page_config(page_title="OLA Driver Churn Predictor", layout="centered")
st.title("🚖 OLA Driver Churn Prediction")
st.markdown("Use this tool to predict whether a driver is likely to churn based on business and personal details.")

# Default input template
default_data = {
    'Reportings': 5,
    'Driver_ID': 1,
    'Age': 34,
    'Gender': 0,
    'Education_Level': 1,
    'Grade': 2,
    'Total Business Value': 151600,
    'Income': 209224,
    'Joining Designation': 2,
    'Quarterly Rating': 1,
    'month': 2,
    'year': 2019,
    'Raise': 0,
    'Promotion': 0,
    'Cities': 25,
}

state = default_data.copy()

# -------- 👤 Personal Details --------
st.header("👤 Personal Information")
col1, col2 = st.columns(2)
with col1:
    state['Age'] = st.number_input("Driver Age", value=state['Age'], min_value=18, max_value=75)
with col2:
    gender_input = st.radio("Gender", ["Male", "Female"], index=state['Gender'], horizontal=True)
    state['Gender'] = 0 if gender_input == "Male" else 1

state['Cities'] = int(
    st.selectbox("City Code (from internal mapping)", list(range(1, 30)), index=state['Cities'] - 1)
)

# -------- 💼 Business Metrics --------
st.header("💼 Business Metrics")
col3, col4 = st.columns(2)
with col3:
    state['Total Business Value'] = st.number_input("Total Business Value (₹)", value=state['Total Business Value'])
with col4:
    state['Income'] = st.number_input("Annual Income (₹)", value=state['Income'])

# -------- 🏢 Employment Details --------
st.header("🏢 Employment History")
joining_date = st.date_input("Date of Joining", value=datetime(state['year'], state['month'], 1))
state['month'] = joining_date.month
state['year'] = joining_date.year

col5, col6, col7 = st.columns(3)
with col5:
    state['Grade'] = st.radio("Grade", [1, 2, 3, 4, 5], index=state['Grade'] - 1, horizontal=True)
with col6:
    state['Joining Designation'] = st.radio("Joining Designation", [1, 2, 3, 4, 5], index=state['Joining Designation'] - 1, horizontal=True)
with col7:
    state['Quarterly Rating'] = st.radio("Quarterly Rating", [1, 2, 3, 4, 5], index=state['Quarterly Rating'] - 1, horizontal=True)

state['Education_Level'] = st.radio("Education Level", ["No Degree", "UG", "PG"], index=state['Education_Level'], horizontal=True)
state['Education_Level'] = ["No Degree", "UG", "PG"].index(state['Education_Level'])

# -------- 🔧 Extra Inputs --------
st.header("🔧 Other Details")
col8, col9 = st.columns(2)
with col8:
    state['Promotion'] = st.radio("Was Promoted?", ["No", "Yes"], index=state['Promotion'], horizontal=True)
    state['Promotion'] = 0 if state['Promotion'] == "No" else 1
    state['Raise'] = st.radio("Received a Raise?", ["No", "Yes"], index=state['Raise'], horizontal=True)
    state['Raise'] = 0 if state['Raise'] == "No" else 1
with col9:
    state['Driver_ID'] = st.number_input("Driver ID (internal use)", value=state['Driver_ID'])
    state['Reportings'] = st.number_input("Number of Reportings", value=state['Reportings'])

# -------- 🚀 Prediction Button --------
if st.button("🚀 Predict Driver Churn"):
    input_df = pd.DataFrame([state])
    result = classifier.predict(input_df)
    prediction = "Churn" if result[0] == 1 else "No Churn"

    st.subheader("🧠 Prediction Result")
    if prediction == "Churn":
        st.error("⚠️ The driver is likely to **churn**.")
    else:
        st.success("✅ The driver is likely to **stay**.")

