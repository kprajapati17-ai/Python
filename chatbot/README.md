# Easy Learn Academy AI Chatbot 🎓🌐

A simplified, offline, Flask-based IT student chatbot assistant. This application runs entirely on your local machine using standard Python and requires **no internet**, **no database setup**, and **no external APIs**.

Designed to be simple and beginner-friendly for college project vivas.

---

## 📂 Project Directory Structure

```text
EasyLearnChatbot/
│
├── app.py                 # Main Flask server (exposes page and ask routes)
├── chatbot.py             # Simple keyword matching search logic
├── knowledge_base.py      # Local dictionary of topics, keywords, and answers
├── preprocessing.py       # Basic string cleaning helper
├── requirements.txt       # Dependencies list (contains only 'Flask')
│
└── templates/
    └── index.html         # Web page containing the Chat interface
```

---

## 🚀 How to Install and Run

### Step 1: Install Flask
Open your terminal or command prompt in this directory, and install Flask:
```bash
pip install -r requirements.txt
```

### Step 2: Start the Web App
Run the Flask server:
```bash
python app.py
```

### Step 3: Open in Browser
Open your browser and navigate to:
```text
http://127.0.0.1:5000
```
Type your questions inside the input bar and press Enter or click the Send button!

---

## 🧠 Simple Matching Logic Explained

1. **Text Preprocessing** (`preprocessing.py`):
   - Converts the question to lowercase (so `"Hi"` and `"hi"` are matching).
   - Removes punctuation characters (like `?`, `!`, `,`).
2. **Keyword Matching** (`chatbot.py`):
   - Splits the clean question sentence into a list of single words.
   - Loops through each category in `knowledge_base.py`.
   - If any keyword associated with a category is found inside the user's question words, the chatbot immediately returns the official answer.
   - Example: typing `"hi"` matches the keyword `"hi"` in `"greetings"` and returns `"hi how are you have nice day aam ok"`.
3. **Fallback**:
   - If no keyword matches, the bot returns: `"Sorry, I don't have information about that yet."`
