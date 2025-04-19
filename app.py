import streamlit as st
import joblib
import json
import numpy as np

# Load model and columns
model = joblib.load("bangalore_house_price_model.pkl")

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

# UI
st.title("🏡 Bangalore House Price Prediction")
st.markdown("Enter the details below to predict house price in Lakhs (INR)")

# Input fields
sqft = st.number_input("Total Square Feet", min_value=100, max_value=10000, value=1000)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, value=2)

# Location dropdown
location = st.selectbox("Location", sorted(data_columns[3:]))

# Predict button
if st.button("Predict Price"):
    input_data = np.zeros(len(data_columns))
    input_data[0] = sqft
    input_data[1] = bath
    input_data[2] = bhk
    loc_index = data_columns.index(location)
    input_data[loc_index] = 1

    prediction = model.predict([input_data])[0]
    st.success(f"💰 Estimated Price: ₹ {prediction:.2f} Lakhs")
