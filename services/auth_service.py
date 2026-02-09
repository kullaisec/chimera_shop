from db.database import get_user

def login(user_id):
    user = get_user(user_id)
    if user:
        return {"token": f"token-{user[0]}"}
    return {"error": "invalid"}, 401
