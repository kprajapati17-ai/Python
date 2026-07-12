# app.py
# Main runner for the simplified Easy Learn Academy Chatbot Flask Web Application.

from flask import Flask, render_template, request, jsonify
import chatbot

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the single-page interface index.html.
    """
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """
    Endpoint for the web client to POST query messages.
    Receives JSON: {"message": "..."}
    Returns JSON: {"response": "..."}
    """
    # 1. Get JSON data sent from Javascript fetch call
    data = request.get_json()
    user_message = data.get("message", "")
    
    # 2. Get response from the simple matching engine
    bot_response = chatbot.get_response(user_message)
    
    # 3. Return response back as JSON
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    print("==========================================================")
    print("           EASY LEARN ACADEMY CHATBOT SERVER             ")
    print("==========================================================")
    print(" Running at: http://127.0.0.1:5000 in your browser ")
    print("==========================================================\n")
    
    # Start Flask local server on port 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
