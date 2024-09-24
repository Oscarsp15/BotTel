import sqlite3

def connect_db():
    conn = sqlite3.connect('user_levels.db')
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        level INTEGER NOT NULL DEFAULT 1,
        interactions INTEGER NOT NULL DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

# Ejecuta esta función al inicio del bot
create_tables()
