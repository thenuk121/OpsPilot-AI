import sqlite3


DATABASE_PATH = "data/opspilot.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            minimum_stock INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()