import sqlite3
import os
from src.Task import Task
from src import path


class DBEngine:
    def __init__(self):
        self.path = os.path.join(path, "db", "work.db")
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.load_db()

    def load_db(self):
        self.data = [Task(*row) for row in self.cursor.execute("SELECT * FROM todo").fetchall()]

    def save_changes(self):
        self.cursor.execute("DELETE FROM todo")
        for task in self.data:
            self.cursor.execute("""INSERT INTO todo(name, description, status_id, imp) VALUES (?, ?, ?, ?)""",
                                task.to_row()[1:])
        self.connection.commit()
        self.load_db()

    def close(self):
        self.save_changes()
        self.connection.close()
