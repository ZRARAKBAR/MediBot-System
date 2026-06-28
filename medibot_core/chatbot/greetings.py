import random
import re

GREETING_PATTERNS = {
    "hello", "hi", "hey", "good morning",
    "good evening", "good afternoon"
}

THANKS_PATTERNS = {
    "thanks", "thank you", "thx", "thankyou"
}

CHIT_CHAT_PATTERNS = {
    "how are you", "how do you do", "am good what about you"
}

GREETING_RESPONSES = [
    "Hello! I am MediBot AI. How can I help you today?",
    "Thanks for being here! Describe your symptoms.",
    "I can help identify possible diseases and suggest medicines.",
    "Good day! How are you feeling today?"
]

THANKS_RESPONSES = [
    "You're welcome! Take care.",
    "No problem! I'm here to help.",
    "Glad I could assist you."
]

CHIT_CHAT_RESPONSES = [
    "I'm fine and ready to help you!",
    "All good here. Tell me your symptoms.",
    "I'm here to assist you medically."
]

OWNERS = {"zrar"}

OWNER_RESPONSE = (
    "G maalik hukam!! Apko kiaa hogyaa? "
    "Apni care karein aur symptoms bataiye."
)

UNKNOWN_NAME_RESPONSE = (
    "Please describe your symptoms so I can help you medically."
)

def contains_pattern(text, patterns):
    return any(p in text for p in patterns)

def check_greeting(sentence: str):
    """
    Intent detection layer:
    - greeting
    - thanks
    - chit-chat
    - self-introduction
    """

    if not isinstance(sentence, str):
        return None

    text = sentence.lower().strip()

    match = re.search(
        r"\b(i am|i'm|my name is)\s+([a-zA-Z]+)",
        text
    )

    if match:
        name = match.group(2).lower()

        if name in OWNERS:
            return OWNER_RESPONSE

        return UNKNOWN_NAME_RESPONSE

    if contains_pattern(text, GREETING_PATTERNS):
        return random.choice(GREETING_RESPONSES)

    if contains_pattern(text, THANKS_PATTERNS):
        return random.choice(THANKS_RESPONSES)

    if contains_pattern(text, CHIT_CHAT_PATTERNS):
        return random.choice(CHIT_CHAT_RESPONSES)

    return None