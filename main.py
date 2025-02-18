from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Helpbot! Send a POST request to /helpbot with {'message': 'your question'}"

@app.route("/helpbot", methods=["POST"])
def helpbot():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    return jsonify({"reply": f"You said: {user_message}"})

if __name__ == "__main__":
    app.run(debug=True)
