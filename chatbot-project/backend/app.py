import os

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
from flask_cors import CORS

CORS(app)


# Use your Groq API Key here
GROQ_API_KEY = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "model": "llama3-8b-8192"  # or another model if you'd like
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "Sorry, the chatbot failed to respond."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
