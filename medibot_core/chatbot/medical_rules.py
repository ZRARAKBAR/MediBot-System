from difflib import get_close_matches

MEDICAL_RULES = {
    "migraine": {
        "required": ["headache"],
        "forbidden": ["sneezing", "runny nose", "cough", "mucus"]
    },
    "cold": {
        "required": ["sneezing", "runny nose", "cough"],
        "forbidden": []
    },
    "flu": {
        "required": ["fever", "body pain", "chills", "fatigue"],
        "forbidden": []
    },
    "stomach infection": {
        "required": ["abdominal pain", "diarrhea", "nausea", "vomiting"],
        "forbidden": []
    },
    "pneumonia": {
        "required": ["cough", "fever", "chest pain", "difficulty breathing"],
        "forbidden": []
    }
}

def apply_medical_rules(symptoms, match_threshold=0.7):
    """
    Filters diseases based on strict medical rules with partial matching.
    
    Args:
        symptoms (list): Preprocessed user symptoms.
        match_threshold (float): Threshold for considering required symptoms as matched.
        
    Returns:
        List of matched diseases, ranked by proportion of required symptoms matched.
    """
    matched_diseases = []

    for disease, rules in MEDICAL_RULES.items():
        required = rules.get("required", [])
        forbidden = rules.get("forbidden", [])

        if any(symptom.lower() in [f.lower() for f in forbidden] for symptom in symptoms):
            continue

        matched_required = 0
        for req_symptom in required:
            close = get_close_matches(req_symptom.lower(), [s.lower() for s in symptoms], n=1, cutoff=match_threshold)
            if close:
                matched_required += 1

        if matched_required / max(len(required),1) >= match_threshold:
            matched_diseases.append((disease, matched_required / len(required)))

    matched_diseases.sort(key=lambda x: x[1], reverse=True)

    return [d[0] for d in matched_diseases]
