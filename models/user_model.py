from models.database import connect_db

def get_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(user_id, name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (user_id, name) VALUES (?, ?)', (user_id, name))
    conn.commit()
    conn.close()

def update_interactions(user_id, interactions):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET interactions = ? WHERE user_id = ?', (interactions, user_id))
    conn.commit()
    conn.close()

def update_level(user_id, level):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET level = ? WHERE user_id = ?', (level, user_id))
    conn.commit()
    conn.close()
