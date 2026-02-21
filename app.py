import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("?? Vehicle Fuel Efficiency Predictor")

st.write("Enter vehicle parameters to predict Fuel Efficiency (MPG)")

# User Inputs
cylinders = st.number_input("Number of Cylinders", min_value=2, max_value=12, value=4)
displacement = st.number_input("Engine Displacement")
horsepower = st.number_input("Horsepower")
weight = st.number_input("Vehicle Weight")
acceleration = st.number_input("Acceleration")

# Predict Button
if st.button("Predict Fuel Efficiency"):
    input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Fuel Efficiency: {prediction[0]:.2f} MPG")