# 🚑 Predictive Triage Assistant

A machine learning web application that predicts emergency triage priority levels (1 = most critical, 4 = least urgent) based on patient data collected at hospital intake.

This project uses XGBoost for modeling and Streamlit for the frontend to help hospitals or healthcare facilities triage patients more effectively.

---

## 🔍 What It Does

* Takes in patient features such as age, gender, symptoms, and vital signs
* Predicts triage level instantly (1 to 4)
* Helps prioritize critical patients in real time
* Fully interactive frontend using Streamlit

---

## 📊 Demo

👉 **Live App**: [triage-assistant-app.streamlit.app](https://triage-assistant-app.streamlit.app/)

---

## 📁 Folder Structure

```
triage-assistant-app/
├── app/
│   └── app.py
├── model/
│   └── triage_model.json
├── data/
│   └── ED_triage.csv (optional, for training)
├── notebooks/
│   └── triage_model_dev.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* XGBoost
* Scikit-learn
* Streamlit
* Pandas & NumPy

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/SJ-ShahJeet/triage-assistant-app.git
cd triage-assistant-app

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/app.py
```

---

## 📦 Dependencies

Make sure your `requirements.txt` contains:

```txt
streamlit
xgboost
scikit-learn
pandas
numpy
joblib
```

---

## 🙌 Author

**Jeet Shah**
[LinkedIn](https://www.linkedin.com/in/jeetshah2087) | [GitHub](https://github.com/SJ-ShahJeet)

Feel free to fork, star, or contribute! ⭐
