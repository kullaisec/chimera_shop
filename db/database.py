import sqlite3

def get_user(username):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    sql = f"SELECT id, role FROM users WHERE username = '{username}'"
    cur.execute(sql)
    return cur.fetchone()
