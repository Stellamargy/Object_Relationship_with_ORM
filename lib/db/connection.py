import sqlite3

def get_db_connection():
    """Create a database connection to the SQLite database."""
    conn = sqlite3.connect('article.db')
    conn.row_factory = sqlite3.Row  # Allows us to access columns by name
    return conn

