from flask import Blueprint, request, jsonify
from chatbot import ask_openai

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    print(data)

    if not data or "message" not in data:
        return jsonify({"error": "Message manquant"}), 400

    user_message = data["message"]
    response = ask_openai(user_message)
    return jsonify({"response": response})
