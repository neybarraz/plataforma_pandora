# core/auth/session.py

session = {}

def set_user(username):
    session["user"] = username

def get_user():
    return session.get("user")