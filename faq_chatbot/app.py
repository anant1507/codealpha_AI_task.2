from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    data = request.get_json()  # Correctly handling JSON input
    user_text = data.get("msg")
    print("Received message from user:", user_text)  # Debugging log

    response = get_response(user_text)
    print("Generated response:", response)  # Debugging log

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
