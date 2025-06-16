import streamlit as st
import numpy as np
import xgboost as xgb

model = xgb.XGBClassifier()
model.load_model("model/triage_model.json")


st.set_page_config(page_title="Triage Assistant", layout="centered")

st.title("🚑 Predictive Triage Assistant")
st.write("Enter patient information to predict emergency triage level (1 = most critical, 4 = least urgent).")

# Collect inputs
age = st.slider("Age", 0, 120, 30)
gender = st.radio("Gender", ["Male", "Female"])
admission_hour = st.slider("Admission Hour", 0, 23, 12)
admission_weekday = st.selectbox("Admission Weekday", list(range(0, 7)))
need_fast_execute = st.radio("Need Fast Execution?", [0, 1])

pain_grade = st.slider("Pain Grade (0–10)", 0, 10, 5)
mental_distress = st.slider("Mental Distress (0–10)", 0, 10, 3)
material_distress = st.slider("Material Distress (0–10)", 0, 10, 3)
critical_status = st.slider("Critical Status (0–10)", 0, 10, 5)
stupor_status = st.slider("Stupor Status (0–10)", 0, 10, 5)

avpu = st.selectbox("AVPU Scale", ["A", "V", "P", "U", "Unknown"])

# Convert inputs to numeric
gender_val = 1 if gender == "Male" else 0
avpu_map = {"A": 0, "V": 1, "P": 2, "U": 3, "Unknown": 4}
avpu_val = avpu_map[avpu]

input_data = np.array([[age, gender_val, admission_hour, admission_weekday,
                        need_fast_execute, pain_grade, mental_distress,
                        material_distress, critical_status, stupor_status, avpu_val]])

# Prediction
if st.button("Predict Triage Level"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Triage Level: **{int(prediction)+1}**")
