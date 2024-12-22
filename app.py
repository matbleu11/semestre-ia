import random
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Réponses prédéfinies
greetings = ["salut", "bonjour", "hello", "bonsoir"]
responses = {
    "bonjour": "Bonjour ! Comment puis-je vous aider ?",
    "salut": "Salut ! Comment ça va ?",
    "comment ça va": "Je vais bien, merci ! Et vous ?",
    "quelle est la capitale de la france": "La capitale de la France est Paris.",
    "au revoir": "Au revoir ! Passez une excellente journée."
}

# Réponse par défaut pour les questions non reconnues
default_responses = [
    "C'est une question intéressante, mais je ne connais pas la réponse exacte.",
    "Hmm, je ne suis pas sûr de comprendre, mais essayons d'en discuter.",
    "Pouvez-vous me donner plus de détails ? Je vais essayer de vous aider.",
    "Je ne sais pas exactement, mais je peux chercher si vous reformulez."
]

# Fonction pour déterminer si une phrase est une question
def is_question(user_input):
    return user_input.endswith("?") or "quel" in user_input or "quoi" in user_input

# Fonction pour répondre à l'utilisateur
def chatbot_response(user_input):
    user_input = user_input.lower().strip()  # Nettoie l'entrée utilisateur
    
    # Vérifie les salutations
    if user_input in greetings:
        return random.choice([
            "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
            "Salut ! Ravi de vous voir. Une question ?",
            "Hello ! Que puis-je faire pour vous ?"
        ])
    
    # Vérifie les réponses prédéfinies
    if user_input in responses:
        return responses[user_input]
    
    # Si c'est une question
    if is_question(user_input):
        return random.choice(default_responses)
    
    # Réponse par défaut pour les phrases non reconnues
    return (
        f"Vous avez dit : '{user_input}'. Je ne suis pas sûr de comprendre, mais je suis là pour discuter si besoin."
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
