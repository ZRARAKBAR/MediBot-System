import os
import json
import pandas as pd
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from difflib import get_close_matches

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SYMPTOM_CSV = os.path.join(BASE_DIR, "..", "data", "symptoms_100.csv")
ALIAS_JSON = os.path.join(BASE_DIR, "..", "data", "symptoms_alias.json")

symptoms_df = pd.read_csv(SYMPTOM_CSV)

with open(ALIAS_JSON, "r") as f:
    symptom_alias = json.load(f)

disease_names = set(symptoms_df["disease"].dropna().str.lower().str.strip())

all_symptoms = set()
multi_word_symptoms = set()

for col in symptoms_df.columns[1:]:
    for symptom in symptoms_df[col].dropna():
        s = str(symptom).lower().strip()
        all_symptoms.add(s)

        if " " in s:
            multi_word_symptoms.add(s)

stop_words = set(stopwords.words("english"))

ignore_words = {
    "nice", "good", "hello", "hi", "hey",
    "thanks", "thank", "okay", "yes", "no",
    "please", "ok"
}

def resolve_alias(token: str):
    """
    Converts synonyms into canonical symptom form
    """
    for canonical, aliases in symptom_alias.items():
        if token == canonical:
            return canonical
        if token in aliases:
            return canonical
    return None

def preprocess_input(user_input: str):
    """
    Returns structured NLP output:

    {
        "clean_text": str,
        "tokens": list,
        "matched": list,
        "suggestions": list,
        "diseases": list
    }
    """

    if not isinstance(user_input, str):
        return {
            "clean_text": "",
            "tokens": [],
            "matched": [],
            "diseases": [],
            "suggestions": []
        }

    text = user_input.lower().strip()

    matched = []
    suggestions = []
    detected_diseases = []

    for disease in disease_names:
        if disease in text:
            detected_diseases.append(disease)
            text = text.replace(disease, "")

    for symptom in multi_word_symptoms:
        if symptom in text:
            matched.append(symptom)
            text = text.replace(symptom, "")

    tokens = word_tokenize(text)

    tokens = [
        t for t in tokens
        if t not in stop_words
        and t not in string.punctuation
        and len(t) > 2
    ]

    for token in tokens:

        if token in ignore_words:
            continue

        if token in all_symptoms:
            matched.append(token)
            continue

        alias = resolve_alias(token)
        if alias:
            matched.append(alias)
            continue

        close = get_close_matches(token, all_symptoms, n=1, cutoff=0.82)

        if close:
            matched.append(close[0])
            suggestions.append(
                f"Did you mean '{close[0]}' instead of '{token}'?"
            )

    matched = list(dict.fromkeys(matched))
    detected_diseases = list(dict.fromkeys(detected_diseases))

    return {
        "clean_text": text,
        "tokens": tokens,
        "matched": matched,
        "diseases": detected_diseases,
        "suggestions": suggestions
    }