from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Please enter a message"}), 400

    if len(user_message) > 500:
        return jsonify({"error": "Message is too long"}), 400

    bot_reply = get_response(user_message)

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
    
    