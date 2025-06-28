import sqlite3
from typing import Any, List, Tuple, Optional

class Database:
    def __init__(self, db_name: str = "Storage.db"):
        self.db_name = db_name
        self.connection = Optional[sqlite3.Connection] = None
        self.cursor = Optional[sqlite3.Cursor] = None
        self.connect()
    
    def connect(self):
        """Establish a connection to the database."""
        if self.connection:
            self.connection.close()
        
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = sqlite3.connection.cursor()
    
    def change_database(self, new_db_name: str):
        """Switch to a different SQLite based Database file."""
        self.db_name = new_db_name
        self.connect()
        
    def execute(self, query: str, params: Tuple[Any, ...] = ()) -> sqlite3.Cursor:
        """Execute a query and return the Cursor."""
        if not self.connection:
            self.connect
        
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self, query: str, params: Tuple[Any, ...] = ()) -> List[Tuple]:
        """Fetch all results from a query."""
        cur = self.execute(query, params)
        return cur.fetchall()

    def fetchone(self, query: str, params: Tuple[Any, ...] = ()) -> Optional[Tuple]:
        """Fetch one result from a query."""
        cur = self.execute(query, params)
        return cur.fetchone()
    
    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.commit()
            self.connection.close()
            self.connection = None
            self.cursor = None