from flask import Flask
from routes.chatbot_route import chatbot_bp
from flask_cors import CORS  # Pour autoriser les requêtes depuis le frontend React

app = Flask(__name__)
CORS(app)  # autorise toutes les origines (pour dev)

# Enregistrement de la route du chatbot
app.register_blueprint(chatbot_bp)

if __name__ == "__main__":
    app.run(debug=True)
