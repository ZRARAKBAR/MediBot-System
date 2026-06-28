import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DISEASE_PATH = os.path.join(BASE_DIR, "..", "data", "disease_info_100.csv")
MEDICINE_PATH = os.path.join(BASE_DIR, "..", "data", "medicine_book.csv")

disease_info = pd.read_csv(DISEASE_PATH)
medicine_book = pd.read_csv(MEDICINE_PATH)

disease_info["disease"] = disease_info["disease"].astype(str).str.lower().str.strip()
medicine_book["disease"] = medicine_book["disease"].astype(str).str.lower().str.strip()

DISEASE_LOOKUP = {
    row["disease"]: row for _, row in disease_info.iterrows()
}

MEDICINE_GROUPED = medicine_book.groupby("disease")

avoid_dict = {
    "flu": ["Cold drinks", "Smoking", "Stress"],
    "cold": ["Cold foods", "Smoking"],
    "malaria": ["Alcohol", "Fatty foods"],
    "migraine": ["Chocolate", "Cheese", "Stress"],
    "chickenpox": ["Scratching blisters", "Crowded places"],
    "dengue": ["NSAIDs like ibuprofen", "Dehydration"],
    "diabetes": ["Sugary foods", "Excess carbs"],
    "asthma": ["Smoking", "Dust", "Cold air"],
    "typhoid": ["Street food", "Unhygienic water"],
    "hepatitis": ["Alcohol", "Fatty food"],
    "pneumonia": ["Smoking", "Polluted air"]
}

def get_medicine_test(disease_name: str, api_data=None):
    """
    Medical response engine:
    - supports API mode
    - supports local dataset mode
    - returns structured JSON response
    """

    if not disease_name or not isinstance(disease_name, str):
        return {
            "status": "error",
            "message": "Invalid disease input",
            "tests": [],
            "medicines": [],
            "avoid": []
        }

    disease = disease_name.lower().strip()

    if api_data:
        return {
            "status": "api",
            "disease": disease,
            "tests": api_data.get("tests", []),
            "medicines": [
                {
                    "name": m.get("name", ""),
                    "dosage": m.get("dosage", ""),
                    "precautions": m.get("precautions", "")
                }
                for m in api_data.get("medicines", [])
            ],
            "avoid": avoid_dict.get(disease, [])
        }

    row = DISEASE_LOOKUP.get(disease)

    if row is not None:
        tests_raw = row.get("recommended_tests", "")

        if isinstance(tests_raw, str):
            tests = [t.strip() for t in tests_raw.split(",") if t.strip()]
        else:
            tests = []
    else:
        tests = []

    medicines = []

    if disease in MEDICINE_GROUPED.groups:
        group = MEDICINE_GROUPED.get_group(disease)

        medicines = [
            {
                "name": r.get("medicine_name", ""),
                "dosage": r.get("dosage", ""),
                "precautions": r.get("precautions", "")
            }
            for _, r in group.iterrows()
        ]

    return {
        "status": "local",
        "disease": disease,
        "tests": tests,
        "medicines": medicines,
        "avoid": avoid_dict.get(disease, [])
    }