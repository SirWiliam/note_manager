import sqlite3


def setup_database():

    connection = sqlite3.connect('notes.db')

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        title TEXT,
        content TEXT,
        status TEXT,
        created_date TEXT,
        issue_date TEXT)
        """
    );

    connection.commit()

    connection.close()


setup_database()