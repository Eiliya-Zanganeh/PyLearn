import sqlite3


class Database:
    def __init__(self):
        conct = sqlite3.connect("todo_list.db")
        cur = conct.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS tasks (ID INTEGER PRIMARY KEY, title text, description text, is_done BOOLEAN DEFAULT FALSE, priority BOOLEAN DEFAULT FALSE, time text)")
        conct.commit()
        conct.close()

    def load_tasks(self):
        conct = sqlite3.connect("todo_list.db")
        cur = conct.cursor()
        cur.execute("SELECT * FROM tasks ORDER BY is_done, priority DESC")
        rows = cur.fetchall()
        conct.close()
        return rows

    def insert_task(self, title, description, time):
        conct = sqlite3.connect("todo_list.db")
        cur = conct.cursor()
        cur.execute("INSERT INTO tasks VALUES (NULL, ?, ?, 0, 0, ?) ", (title, description, time))
        conct.commit()
        conct.close()

    def edit_task_done(self, id):
        conct = sqlite3.connect("todo_list.db")
        cur = conct.cursor()
        cur.execute("UPDATE tasks SET is_done = NOT is_done WHERE id=?", (id,))
        conct.commit()
        conct.close()

    def edit_task_priority(self, id):
        conct = sqlite3.connect("todo_list.db")
        cur = conct.cursor()
        cur.execute("UPDATE tasks SET priority = NOT priority WHERE id=?", (id,))
        conct.commit()
        conct.close()

    def delete_task(self, id):
        conct = sqlite3.connect("todo_list.db")
        cur = conct.cursor()
        cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        conct.commit()
        conct.close()

    def show_description(self, id):
        conct = sqlite3.connect("todo_list.db")
        cur = conct.cursor()
        cur.execute("SELECT * FROM tasks WHERE id=?", (id,))
        rows = cur.fetchall()
        conct.close()
        return rows
