import threading
from Modules.Database import Database

_thread_local: threading.local = threading.local()

def getDB() -> Database:
    """
    Returns a thread-local Database instance.

    Ensures that each thread gets its own connection-safe Database wrapper.

    @return Database: A thread-local SQLite database object
    """
    if not hasattr(_thread_local, "db"):
        _thread_local.db = Database()
    return _thread_local.db