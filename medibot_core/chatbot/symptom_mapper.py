SYMPTOM_MAP = {
    "fever": "s_21",
    "cough": "s_10",
    "headache": "s_98",
    "fatigue": "s_156"
}

def encode_symptoms(symptoms):
    return [
        {"id": SYMPTOM_MAP[s], "choice_id": "present"}
        for s in symptoms if s in SYMPTOM_MAP
    ]