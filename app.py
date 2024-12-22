import random
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Réponses prédéfinies
responses = {
    "bonjour": "Bonjour ! Comment puis-je vous aider ?",
    "comment ça va": "Je vais bien, merci ! Et vous ?",
    "quelle est la capitale de la france": "La capitale de la France est Paris.",
    "au revoir": "Au revoir ! Passez une excellente journée."
}

# Réponse par défaut (peut répondre à tout)
default_responses = [
    "Je suis désolé, je n'ai pas la réponse exacte, mais je peux essayer de vous aider.",
    "Hmm, je ne suis pas sûr, mais c'est une question intéressante !",
    "Je ne connais pas la réponse exacte, mais vous pourriez me demander autrement.",
    "Pouvez-vous être plus précis ? Je vais essayer de vous répondre."
]

# Fonction pour répondre à l'utilisateur
def chatbot_response(user_input):
    user_input = user_input.lower().strip()  # Nettoie l'entrée utilisateur
    if user_input in responses:
        return responses[user_input]
    else:
        # Génère une réponse improvisée pour répondre à tout
        return (
            f"Vous avez demandé : '{user_input}'. "
            f"Malheureusement, je n'ai pas la réponse exacte pour cela, "
            f"mais je suis sûr qu'on peut approfondir si vous me donnez plus de détails."
        )

# Route principale
@app.route("/")
def index():
    return render_template("index.html")

# Route pour traiter les réponses
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot_response(user_input)
    return response

if __name__ == "__main__":
    # Utilise la variable PORT définie par Render ou 5000 par défaut
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
