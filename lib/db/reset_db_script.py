import os
from .connection import get_db_connection, get_db_cursor

def reset_db(reset_db):
    """Reset the database by dropping all tables ."""
    conn = get_db_connection()
    cursor = get_db_cursor()
    try:
        directory = os.path.dirname(__file__)
        sql_file_path = os.path.join(directory, reset_db)
        print("MySQL file path:", sql_file_path)
        with open(sql_file_path, 'r') as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()
    finally:
        cursor.close()
        conn.close()

reset_db('reset_db.sql')