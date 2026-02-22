import sqlite3

# Connect to the database
conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()

# Function to initialize the database (create tables if they don't exist)
def initialize(): 
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS warnings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL, 
                guild_id INTEGER NOT NULL, 
                reason TEXT
            )
        ''')
        conn.commit()
    except sqlite3.OperationalError:
        print("Table warnings already exists...")

# Function to add a warning
def add_warning(user_id, guild_id, reason):
    cursor.execute('INSERT INTO warnings (user_id, guild_id, reason) VALUES (?, ?, ?)', (user_id, guild_id, reason))
    conn.commit()

# Function to get all warnings for a specific user
def get_warnings(user_id, guild_id):
    cursor.execute('SELECT reason FROM warnings WHERE user_id = ? AND guild_id = ?', (user_id, guild_id))
    return cursor.fetchall()

# Function to clear all warnings for a specific user
def clear_warnings(user_id, guild_id):
    cursor.execute('DELETE FROM warnings WHERE user_id = ? AND guild_id = ?', (user_id, guild_id))
    conn.commit()

# Function to close the database connection
def close_connection():
    conn.close()
