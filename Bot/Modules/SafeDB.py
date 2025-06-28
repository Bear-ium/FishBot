import threading
from Modules.Database import Database

_local_thread = threading.local()

def getDB() -> Database:
    """Returns a local thread Database instance for safe access across different threads."""
    if not hasattr(_local_thread, "db"):
        _local_thread.db = Database()
    return _local_thread.db