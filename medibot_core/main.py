import sys
from chatbot.nlp_processor import preprocess_input
from chatbot.greetings import check_greeting
from chatbot.medical_rules import apply_medical_rules
from chatbot.responses import get_medicine_test


def get_bot_response(user_input):
    """
    Chatbot pipeline:

    1. Greeting / chit-chat layer
    2. NLP processing
    3. Medical decision layer
    """

    greeting_response = check_greeting(user_input)
    if greeting_response:
        return greeting_response

    processed = preprocess_input(user_input)

    diseases = processed.get("diseases", [])
    symptoms = processed.get("matched", [])

    if diseases:
        return get_medicine_test(diseases[0])

    if symptoms:
        rule_response = apply_medical_rules(symptoms)
        if rule_response:
            return rule_response

        return get_medicine_test(symptoms[0])

    return "I couldn't understand your symptoms. Please describe them more clearly."


def run_cli():
    print("\n===================================")
    print("       MediBot AI  m  ")
    print("===================================\n")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ["exit", "quit", "stop"]:
            print("MediBot: Stay healthy! Goodbye 👋")
            sys.exit()

        response = get_bot_response(user_input)
        print("MediBot:", response)
        print()


if __name__ == "__main__":
    run_cli()