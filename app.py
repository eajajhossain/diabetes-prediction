import streamlit as st
import numpy as np
import pickle


@st.cache_resource
def load_model():
    with open("lightgbm_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()


st.set_page_config(page_title="Diabetes Prediction", layout="centered")
st.title("🩺 Diabetes Prediction ")
st.write("Enter patient details to predict diabetes risk")


pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)


if st.button("Predict"):
    input_data = np.array([[ 
        pregnancies,
        glucose,
        blood_pressure,
        insulin,
        bmi,
        dpf,
        age
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of Diabetes ({probability:.2%})")
    else:
        st.success(f"✅ Low risk of Diabetes ({probability:.2%})")
