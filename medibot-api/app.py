import os
import logging
from flask import Flask, redirect, render_template, request, jsonify
from chatbot import get_response
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__, template_folder="templates", static_folder="static")

# --- Page Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/chat')
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

# --- Unified Chat API Route ---
@app.route("/get", methods=["POST"])
def chatbot_response():
    # Supports both JSON and Form data for maximum compatibility
    if request.is_json:
        user_text = request.json.get("message")
    else:
        user_text = request.form.get("msg")
    
    if not user_text:
        return jsonify({"response": "I didn't receive a message."})

    try:
        response = get_response(user_text)
        logging.info(f"User: {user_text} | Bot Success")
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"response": "I'm having trouble connecting right now."})

if __name__ == "__main__":
     
    # Remove debug=True for deployment
    app.run()