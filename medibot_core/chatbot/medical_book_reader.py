import re

# Load medical book into memory
def load_medical_book(file_path="data/medical_book.txt"):
    medical_data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                disease, info = line.split(":", 1)
                disease = disease.strip().lower()
                info = info.strip()
                # Extract structured info
                duration = ""
                precautions = ""
                symptoms = []
                parts = info.split(".")
                for part in parts:
                    part = part.strip()
                    if part.lower().startswith("duration"):
                        duration = part.split(":",1)[1].strip() if ":" in part else ""
                    elif part.lower().startswith("precautions"):
                        precautions = part.split(":",1)[1].strip() if ":" in part else ""
                    elif part:
                        symptoms.extend([s.strip() for s in part.split(",")])
                medical_data[disease] = {
                    "symptoms": symptoms,
                    "duration": duration,
                    "precautions": precautions
                }
    except FileNotFoundError:
        print("Medical book not found. Please add data/medical_book.txt")
    return medical_data

# Find disease by keyword/pattern
def find_disease_from_text(user_input, medical_data, threshold=0.3):
    """
    Returns disease info if at least threshold proportion of symptoms match.
    """
    user_input_lower = user_input.lower()
    best_match = None
    best_score = 0
    for disease, info in medical_data.items():
        matched = [s for s in info['symptoms'] if s.lower() in user_input_lower]
        if not matched:
            continue
        score = len(matched)/max(len(info['symptoms']),1)
        if score > best_score:
            best_score = score
            best_match = (disease, info, matched)
    if best_match and best_score >= threshold:
        disease, info, matched = best_match
        info_text = f"Symptoms matched: {', '.join(matched)}\n"
        if info['duration']:
            info_text += f"Duration: {info['duration']}\n"
        if info['precautions']:
            info_text += f"Precautions: {info['precautions']}\n"
        return disease, info_text
    return None, None
