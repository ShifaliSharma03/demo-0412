import sqlite3

def vulnerable_login(username, password):
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()
  
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Attempting login for user: {username}")  # For teaching/demo only
    cur.execute(query)

    result = cur.fetchone()
    conn.close()
    return result
