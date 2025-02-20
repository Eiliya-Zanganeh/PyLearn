import sqlite3


class Database:
    def __init__(self):
        conct = sqlite3.connect("clock.db")
        cur = conct.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS clock (ID INTEGER PRIMARY KEY, clock text)")
        conct.commit()
        conct.close()

    def load_clocks(self):
        conct = sqlite3.connect("clock.db")
        cur = conct.cursor()
        cur.execute("SELECT * FROM clock")
        rows = cur.fetchall()
        conct.close()
        return rows

    def insert_clock(self, clock):
        conct = sqlite3.connect("clock.db")
        cur = conct.cursor()
        cur.execute("INSERT INTO clock VALUES (NULL, ?) ", (clock,))
        conct.commit()
        conct.close()

    def edit_clock(self, id, clock):
        conct = sqlite3.connect("clock.db")
        cur = conct.cursor()
        cur.execute("UPDATE clock SET clock = ? WHERE id=?", (clock, id,))
        conct.commit()
        conct.close()

    def delete_clock(self, id):
        conct = sqlite3.connect("clock.db")
        cur = conct.cursor()
        cur.execute("DELETE FROM clock WHERE id=?", (id,))
        conct.commit()
        conct.close()
