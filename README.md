# diabetes-prediction
Built an end-to-end machine learning application that predicts the likelihood of diabetes based on patient health metrics. The model was trained using a LightGBM classifier and deployed as an interactive Streamlit web app for real-time inference.


# 🩺 Diabetes Prediction Web App

A machine learning–powered web application for predicting the likelihood of diabetes based on patient health metrics.  
The model is trained using **LightGBM** and deployed using **Streamlit** for an interactive user interface.

---

## 🚀 Live Demo
(Deploy on Streamlit Cloud and paste link here)

---

## 📌 Features
- Predicts diabetes risk using clinical input parameters
- Clean and interactive Streamlit UI
- Probability-based output for better decision interpretation
- Lightweight and fast inference using LightGBM

---

## 🧠 Machine Learning Model
- Algorithm: LightGBM Classifier
- Task: Binary Classification (Diabetes: Yes / No)
- Trained on medical diagnostic data
- Outputs both prediction and probability score

---

## 📊 Input Parameters
- Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

> ⚠️ Input feature order strictly matches the training pipeline to ensure correct predictions.

---

## 🛠 Tech Stack
- Python
- LightGBM
- Scikit-learn
- NumPy
- Streamlit

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/diabetes-prediction-streamlit-app.git
cd diabetes-prediction-streamlit-app
pip install -r requirements.txt
streamlit run app.py
