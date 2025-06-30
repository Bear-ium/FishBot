import os
import sqlite3

DB_NAME = "Storage.db"

SQL_COMMANDS = [
    """
    CREATE TABLE IF NOT EXISTS catches (
        fishId INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        fish_name TEXT NOT NULL,
        weight NUMERIC NOT NULL,
        value INTEGER NOT NULL,
        variant TEXT NOT NULL,
        timestamp INTEGER NOT NULL,
        isFav BOOLEAN NOT NULL
    );
    """,
    # Add more tables as needed
]

def main():
    if not os.path.isfile(DB_NAME):
        print(f"{DB_NAME} not found in current directory.")
        return

    print(f"Found {DB_NAME}, running SQL...")

    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        for command in SQL_COMMANDS:
            cursor.execute(command)
        conn.commit()
        print("All tables created (if they didn't already exist).")
    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
