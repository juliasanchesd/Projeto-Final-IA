from flask import Flask, request, jsonify, render_template
from agent import find_jobs

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Digite uma mensagem para começarmos"})

    reply = find_jobs(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
