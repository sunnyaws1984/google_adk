import json
import os

SESSION_FILE = "session_data.json"

def save_session(app_name, user_id, session_id, state):
    data = {
        "app_name": app_name,
        "user_id": user_id,
        "session_id": session_id,
        "state": state,
    }
    with open(SESSION_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Session saved successfully!")

def load_session():
    if not os.path.exists(SESSION_FILE):
        return None
    with open(SESSION_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
