from flask import Flask, render_template, request

app = Flask(__name__)

# Chatbot : Dictionnaire de réponses
responses = {
    "bonjour": "Bonjour ! Comment puis-je vous aider ?",
    "comment ça va": "Je vais bien, merci ! Et vous ?",
    "quelle est la capitale de la france": "La capitale de la France est Paris.",
    "au revoir": "Au revoir ! Passez une excellente journée."
}

# Fonction pour obtenir une réponse du chatbot
def chatbot_response(user_input):
    return responses.get(user_input.lower(), "Désolé, je ne comprends pas cette question.")

# Route principale
@app.route("/")
def index():
    return render_template("index.html")

# Route pour gérer les réponses
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot_response(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
