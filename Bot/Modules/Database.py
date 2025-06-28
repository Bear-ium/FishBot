import sqlite3
from typing import Any, List, Tuple, Optional

class Database:
    def __init__(self, db_name: str = "Storage.db"):
        """
        Initializes and connects to a SQLite database file.

        @param db_name (str): The filename of the SQLite database
        
        @return None
        """
        self.db_name = db_name
        self.connection: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None
        self.connect()

    def connect(self):
        """
        Establishes a connection to the SQLite database.

        @return None
        """
        if self.connection:
            self.connection.close()

        self.connection = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def change_database(self, new_db_name: str):
        """
        Switches to a new SQLite database file.

        @param new_db_name (str): The new database file name
        
        @return None
        """
        self.db_name = new_db_name
        self.connect()

    def execute(self, query: str, params: Tuple[Any, ...] = ()) -> sqlite3.Cursor:
        """
        Executes a SQL query with optional parameters.

        @param query (str): The SQL query
        @param params (tuple): The query parameters
        
        @return sqlite3.Cursor: The result cursor
        """
        if self.connection is None or self.cursor is None:
            self.connect()

        # Pylance being a bit goofy!!
        conn = self.connection
        cur = self.cursor

        assert conn is not None
        assert cur is not None

        cur.execute(query, params)
        conn.commit()
        return cur

    def fetchall(self, query: str, params: Tuple[Any, ...] = ()) -> List[Tuple]:
        """
        Fetches all rows for a query.

        @param query (str): The SQL query
        @param params (tuple): The query parameters
        
        @return list[tuple]: The result rows
        """
        cur = self.execute(query, params)
        return cur.fetchall()

    def fetchone(self, query: str, params: Tuple[Any, ...] = ()) -> Optional[Tuple]:
        """
        Fetches a single row for a query.

        @param query (str): The SQL query
        @param params (tuple): The query parameters
        
        @return tuple | None: The result row or None
        """
        cur = self.execute(query, params)
        return cur.fetchone()

    def close(self):
        """
        Closes the database connection cleanly.

        @return None
        """
        if self.connection:
            self.connection.commit()
            self.connection.close()
            self.connection = None
            self.cursor = None
