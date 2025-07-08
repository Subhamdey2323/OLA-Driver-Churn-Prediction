# 🚖 OLA Driver Churn Prediction

A machine learning web application to predict whether a driver working for OLA is likely to **churn (leave)** the organization based on their personal, professional, and performance-related attributes.

Built using:
- 🧠 Scikit-learn (or XGBoost for modeling)
- 📊 Pandas for data processing
- 🎨 Streamlit for the user interface

---

## 📌 Project Objective

Employee churn is a major concern in fleet and ride-sharing companies like OLA. This project aims to **predict driver churn** using historical data and provide a simple, interactive web interface where HR managers or analysts can enter driver details and get immediate predictions.

---

## 🚀 Features

- Predicts churn based on input driver details.
- Interactive UI using **Streamlit**.
- Takes into account multiple factors:
  - Age, Gender, Education
  - Business metrics (Income, Business Value)
  - Ratings, Designation, Promotions
  - Join date & number of cities worked in

---

## 🧠 ML Model

- Preprocessed data with necessary encoding and feature engineering.
- Trained using `XGBoostClassifier` (or similar) for better performance on imbalanced datasets.
- Model and preprocessor are saved using `pickle`.

---
