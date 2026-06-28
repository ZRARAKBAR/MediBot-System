import os
import joblib
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier

# ---------- Project Paths ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DATA_DIR = os.path.join(PROJECT_DIR, "data")
MODEL_DIR = os.path.join(PROJECT_DIR, "models")

SYMPTOM_FILE = os.path.join(DATA_DIR, "symptoms_100.csv")
MODEL_FILE = os.path.join(MODEL_DIR, "disease_model.pkl")
MLB_FILE = os.path.join(MODEL_DIR, "mlb.pkl")

# Train model (or load if already trained)
os.makedirs(MODEL_DIR, exist_ok=True)

if not os.path.exists(MODEL_FILE):
    symptoms_df = pd.read_csv(SYMPTOM_FILE)

    diseases = symptoms_df["disease"].values
    symptom_list = symptoms_df.iloc[:, 1:].apply(lambda x: list(x.dropna()), axis=1)

    mlb = MultiLabelBinarizer()
    X = mlb.fit_transform(symptom_list)

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, diseases)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(mlb, MLB_FILE)
    
# ---------- Load Model Once ----------
model_loaded = joblib.load(MODEL_FILE)
mlb_loaded = joblib.load(MLB_FILE)

# Functions
def predict_disease(user_symptoms):

    if not user_symptoms:
        return None
    

    flat_symptoms = []
    for sym in user_symptoms:
        if isinstance(sym, list):
            flat_symptoms.extend(sym)
        else:
            flat_symptoms.append(sym)

    flat_symptoms = [
        str(sym).strip().lower()
        for sym in flat_symptoms
        if str(sym).strip()
    ]

    user_vector = mlb_loaded.transform([flat_symptoms])
    prediction = model_loaded.predict(user_vector)

    return prediction[0]

def predict_disease_proba(user_symptoms, top_n=3):
    if not user_symptoms:
        return []
    flat_symptoms = []
    for sym in user_symptoms:
        if isinstance(sym, list):
            flat_symptoms.extend(sym)
        else:
            flat_symptoms.append(sym)

    flat_symptoms = [
        str(sym).strip().lower()
        for sym in flat_symptoms
        if str(sym).strip()
    ]

    user_vector = mlb_loaded.transform([flat_symptoms])
    probs = model_loaded.predict_proba(user_vector)[0]
    classes = model_loaded.classes_

    disease_probs = sorted(zip(classes, probs), key=lambda x: x[1], reverse=True)
    return disease_probs[:top_n]

   
   
 

         