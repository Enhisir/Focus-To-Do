import sqlite3
import os
from src.Task import Task
from src import path


class DBEngine:
    def __init__(self):
        self.path = os.path.join(path, "db", "work.db")
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.__data = []
        self.load_db()

    def get_data(self):
        return self.__data.copy()

    def update_data(self, data: list, mode="w"):
        if mode == "w":
            self.__data = data.copy()
        elif mode == "a":
            self.__data += data
        self.sort_data()
        self.save_data()

    def sort_data(self):
        self.__data.sort(key=lambda x: (x.status_id, -x.is_imp, x.name))

    def clear_data(self):
        self.__data = []
        self.save_data()

    def load_db(self):
        self.__data = [Task(*row) for row in self.cursor.execute("SELECT * FROM todo").fetchall()]

    def save_data(self):
        self.cursor.execute("DELETE FROM todo")
        for task in self.__data:
            self.cursor.execute("""INSERT INTO todo(name, description, status_id, imp, have_date, date) 
            VALUES (?, ?, ?, ?, ?, ?)""", task.to_row()[1:])
        self.connection.commit()
        self.load_db()

    def close(self):
        self.save_data()
        self.connection.close()
