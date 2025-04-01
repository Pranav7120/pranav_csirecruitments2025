from flask import Flask, request, jsonify
import json
import random
from flask_cors import CORS
from fuzzywuzzy import process

app = Flask(__name__)
CORS(app)

# Load chatbot data
import os

# Get absolute path to the JSON file
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "model", "a.json")

with open(file_path, "r", encoding="utf-8") as file:
    chatbot_data = json.load(file)


# Extract patterns and responses into lists
patterns = []
responses = {}

for entry in chatbot_data:
    for key, value in entry.items():
        if key.startswith("patterns") and isinstance(value, str):
            patterns.append(value.lower())
            responses[value.lower()] = [entry[k] for k in entry if k.startswith("responses") and entry[k]]

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()
    
    # Find best match using fuzzy matching
    match, score = process.extractOne(user_input, patterns)
    
    if score > 60:  # Only pick if match is strong enough
        return random.choice(responses[match])
    
    return "I'm here to help. Can you tell me more?"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
