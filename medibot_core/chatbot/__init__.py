from chatbot.nlp_processor import preprocess_input
from chatbot.ml_model import predict_disease_proba
from chatbot.responses import get_medicine_test
from chatbot.greetings import check_greeting
from chatbot.medical_rules import apply_medical_rules
import datetime, csv, os

os.makedirs('logs', exist_ok=True)
if not os.path.exists('logs/queries.csv'):
    with open('logs/queries.csv','w',newline='',encoding='utf-8') as f:
        csv.writer(f).writerow(['Timestamp','User Input','Predicted Disease','Method','Probability','Recommended Medicine'])

def get_response(user_input):
    greeting = check_greeting(user_input)
    if greeting:
        return greeting

    matched_symptoms, suggestions = preprocess_input(user_input)
    
    if not matched_symptoms:
        return "I didn't detect any specific medical symptoms in your message. Could you please list the symptoms you are experiencing (e.g., 'I have a fever and headache')?"

    rule_diseases = apply_medical_rules(matched_symptoms)
    if rule_diseases:
        top_disease = rule_diseases[0]
        info_text = "Rule-based suggestion applied.\n"
        method = "Rule-based"
        probability = "High Confidence"
        info = get_medicine_test(top_disease)
        medicines = ', '.join([med['name'] for med in info['medicines']])
        tests = ', '.join(info['tests']) if info['tests'] else 'No tests required'

    else:
            disease_probs = predict_disease_proba(matched_symptoms, top_n=3)
            top_disease = disease_probs[0][0]
            info_text = "ML prediction applied based on your symptoms.\n"
            method = "ML"
            probability = f"{disease_probs[0][1]*100:.1f}%"
            info = get_medicine_test(top_disease)
            medicines = ', '.join([med['name'] for med in info['medicines']])
            tests = ', '.join(info['tests']) if info['tests'] else 'No tests required'

    precautions = "Please rest and follow doctor's advice."

    with open('logs/queries.csv', 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([
            datetime.datetime.now(),
            user_input,
            top_disease,
            method,
            probability,
            medicines
        ])

    response_final = f"**Predicted Disease:** {top_disease.title()}\n"
    response_final += f"**Confidence/Probability:** {probability}\n"
    response_final += f"**Precautions:** {precautions}\n"
    response_final += f"**Recommended Medicines:** {medicines}\n"
    response_final += f"**Suggested Tests:** {tests}\n"

    if suggestions:
        response_final += "\n**Note:** " + " ".join(suggestions) + "\n"

    disclaimer = "\n\n⚠️ *Disclaimer: I am an AI, not a doctor. This prediction is for informational purposes only. Please consult a healthcare professional for a real diagnosis.*"
    
    return response_final + disclaimer