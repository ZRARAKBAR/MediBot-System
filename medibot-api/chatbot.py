import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_response(user_message):

     
    client = Groq(api_key = os.getenv("GROQ_API_KEY"))
     
     
    user_lower = user_message.lower()
    is_developer = "zrar akbar" in user_lower or "muhammad zrar akbar" in user_lower

    system_prompt = (
    "You are MediBot, a professional medical awareness AI and you deveolper is Muhammad Zrar Akbar. "
    "LANGUAGE RULES: "
    "1. firstly you have examine the input is in english or not If the user input is in English, you MUST strictly reply in English.otherwise  user input is in Roman Urdu, you MUST reply in Pakistani-style Roman Urdu of that input only ."
    "3. Language Detection: If the input is a simple greeting (like 'hi', 'hello', 'hey') or a name introduction, "
    "default to English unless the user specifically uses Urdu words in their greeting (e.g., 'Assalam-o-Alaikum'). "
    "4. Style: Use natural Pakistani Roman Urdu (e.g., 'shukriya', 'ap', 'kya haal hai'). NEVER use Hindi words "
    "(e.g., 'dhanyawad', 'kripya').  "
    "5. Disclaimer: ONLY include the sentence 'I am an AI, not a doctor. Please consult a physician for a formal diagnosis.' "
    "if the user asks about specific health symptoms, diseases, or medical advice. Do not add it to simple greetings."
)
    
 

     
    if is_developer:
        system_prompt += (
            " NOTE: The user is Zrar, the Developer and Boss of MediBot. "
            "Treat him with special respect, acknowledge his role as the creator, "
            "and be ready to assist him with any technical or administrative inquiries regarding the bot."
        )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"DEBUG ERROR: {e}")
        return "I am currently undergoing maintenance. Please try again later."