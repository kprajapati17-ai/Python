# app.py
# Main runner for the Easy Learn Academy Chatbot Flask Web Application.

import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import chatbot

# Initialize Flask app
app = Flask(__name__)

# Ensure chat logs directory exists
LOGS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chat_logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Active session store
SESSIONS = {}

def save_session_log(session_id):
    """
    Writes the timestamped chat session log file to the chat_logs folder.
    """
    if session_id not in SESSIONS:
        return
        
    session = SESSIONS[session_id]
    if session.get("saved"):
        return
        
    session["saved"] = True
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"chat_log_{session['start_time'].replace(':', '-').replace(' ', '_')}_{session_id[:8]}.txt"
    filepath = os.path.join(LOGS_DIR, filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("============================================================\n")
            f.write("EASYLEARN ACADEMY - CHAT SESSION LOG\n")
            f.write("============================================================\n")
            f.write(f"Session ID : {session_id}\n")
            f.write(f"Full Name  : {session.get('fullname', 'N/A')}\n")
            f.write(f"Email      : {session.get('email', 'N/A')}\n")
            f.write(f"Mobile     : {session.get('mobile', 'N/A')}\n")
            f.write(f"Start Time : {session.get('start_time')}\n")
            f.write(f"End Time   : {end_time}\n")
            f.write("============================================================\n\n")
            f.write("CONVERSATION HISTORY:\n")
            for msg in session.get("messages", []):
                f.write(f"[{msg['timestamp']}] [{msg['sender']}]: {msg['text']}\n")
            f.write("\n============================================================\n")
    except Exception as e:
        print(f"Error saving chat log for session {session_id}: {e}")

@app.route("/")
def index():
    """
    Renders the interactive chatbot interface index.html.
    """
    return render_template("index.html")

@app.route("/api/start", methods=["POST"])
def api_start():
    """
    Registers a new student session with name, email, and mobile.
    Receives JSON: {"fullname": "...", "email": "...", "mobile": "..."}
    Returns JSON: {"session_id": "...", "status": "success"}
    """
    data = request.get_json(silent=True) or {}
    fullname = str(data.get("fullname", "")).strip()
    email = str(data.get("email", "")).strip()
    mobile = str(data.get("mobile", "")).strip()
    
    session_id = uuid.uuid4().hex
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    SESSIONS[session_id] = {
        "session_id": session_id,
        "fullname": fullname,
        "email": email,
        "mobile": mobile,
        "start_time": now_str,
        "messages": [
            {"sender": "Bot", "text": "Hello! I am your EasyLearn Academy assistant.", "timestamp": now_str},
            {"sender": "Bot", "text": "Type 'bye' or click 'End Session' to finish the session.", "timestamp": now_str}
        ],
        "saved": False
    }
    
    return jsonify({
        "session_id": session_id,
        "status": "success",
        "message": "Session started successfully."
    })

@app.route("/api/message", methods=["POST"])
def api_message():
    """
    Processes chat queries for an active session.
    Receives JSON: {"session_id": "...", "message": "..."}
    Returns JSON: {"response": "...", "session_ended": bool}
    """
    data = request.get_json(silent=True) or {}
    session_id = str(data.get("session_id", ""))
    user_message = str(data.get("message", "")).strip()
    
    if not user_message:
        return jsonify({"response": "Please ask a question so I can assist you!", "session_ended": False})
        
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Retrieve or create fallback session
    if session_id not in SESSIONS:
        session_id = uuid.uuid4().hex
        SESSIONS[session_id] = {
            "session_id": session_id,
            "fullname": "Guest",
            "email": "N/A",
            "mobile": "N/A",
            "start_time": now_str,
            "messages": [],
            "saved": False
        }
        
    session = SESSIONS[session_id]
    session["messages"].append({"sender": "User", "text": user_message, "timestamp": now_str})
    
    # Get response from priority search engine
    bot_response = chatbot.get_response(user_message)
    session["messages"].append({"sender": "Bot", "text": bot_response, "timestamp": now_str})
    
    # Check for exit command
    exit_commands = ["bye", "exit", "goodbye", "quit"]
    session_ended = any(cmd in user_message.lower().split() for cmd in exit_commands)
    
    if session_ended:
        save_session_log(session_id)
        
    return jsonify({
        "response": bot_response,
        "session_ended": session_ended
    })

@app.route("/api/exit", methods=["POST"])
def api_exit():
    """
    Ends the current session and writes the conversation log file.
    Receives JSON: {"session_id": "..."}
    Returns JSON: {"status": "success", "message": "Session ended."}
    """
    data = request.get_json(silent=True) or {}
    session_id = str(data.get("session_id", ""))
    
    if session_id in SESSIONS:
        save_session_log(session_id)
        
    return jsonify({
        "status": "success",
        "message": "Session ended successfully."
    })

@app.route("/ask", methods=["POST"])
def ask():
    """
    Legacy POST endpoint for single-query requests.
    Receives JSON: {"message": "..."}
    Returns JSON: {"response": "..."}
    """
    data = request.get_json(silent=True) or {}
    user_message = str(data.get("message", "")).strip()
    
    if not user_message:
        return jsonify({"response": "Please ask a question so I can assist you!"})
        
    bot_response = chatbot.get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 5000))
    debug_mode = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")

    print("==========================================================")
    print("           EASY LEARN ACADEMY CHATBOT SERVER             ")
    print("==========================================================")
    print(f" Running at: http://{host}:{port} in your browser ")
    print("==========================================================\n")
    
    app.run(host=host, port=port, debug=debug_mode)


